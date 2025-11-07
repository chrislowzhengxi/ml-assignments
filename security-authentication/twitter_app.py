#!/usr/bin/env python3
"""
With the Bearer Token set in the environment, this script demonstrates two Twitter API v2:
1) GET /2/users/by/username/{username}  -> prints user id, name, username
2) GET /2/users/{id}/tweets             -> prints recent tweets for that user
"""

import os
import sys
import json
import time
from typing import Dict, Any, Optional
import urllib.parse
import urllib.request

API_BASE = "https://api.x.com/2"

def get_bearer_token() -> str:
    """
    Read the bearer token from the environment.
    """
    token = os.getenv("X_BEARER_TOKEN")
    if not token:
        print("Error: X_BEARER_TOKEN is not set. Try:\n  export X_BEARER_TOKEN=\"YOUR_BEARER_TOKEN\"")
        sys.exit(1)
    return token

def http_get(url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    HTTP GET Request helper. 
    Gemini prompt: Please help me write a Python function that performs an HTTP
    GET request to a given URL with optional query parameters, includes an 
    Authorization header with a bearer token, and returns the JSON response as a
    dictionary. The function should handle HTTP and network errors gracefully by
    printing error messages and exiting the program.
    """
    if params:
        safe_params = {}
        for k, v in params.items():
            if isinstance(v, (list, dict)):
                safe_params[k] = json.dumps(v)
            else:
                safe_params[k] = str(v)
        url = f"{url}?{urllib.parse.urlencode(safe_params)}"

    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {get_bearer_token()}")
    req.add_header("User-Agent", "twitter-read-demo/1.0")

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            charset = resp.headers.get_content_charset() or "utf-8"
            body = resp.read().decode(charset, errors="replace")
            return json.loads(body)
    except urllib.error.HTTPError as e:
        msg = e.read().decode("utf-8", errors="replace")
        print(f"HTTP {e.code} error at {url}\nResponse:\n{msg}")
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Network error: {e.reason}")
        sys.exit(1)

def get_user_by_username(username: str) -> Dict[str, Any]:
    """
    Calls GET /2/users/by/username/{username}
    Returns the JSON response as a dict.
    """
    url = f"{API_BASE}/users/by/username/{username}"
    # You can request extra fields if you like:
    params = {"user.fields": "created_at,public_metrics"}
    return http_get(url, params)

def get_recent_tweets(user_id: str, max_results: int = 5) -> Dict[str, Any]:
    """
    Calls GET /2/users/{id}/tweets
    Returns the JSON response as a dict.
    """
    url = f"{API_BASE}/users/{user_id}/tweets"
    params = {
        "max_results": max_results,             
        "tweet.fields": "created_at,public_metrics,lang",
    }
    return http_get(url, params)

def pretty(obj: Any) -> str:
    """
    Pretty-print JSON for screenshots and proof.
    """
    return json.dumps(obj, indent=2, ensure_ascii=False)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 twitter_app.py <username>\nExample: python3 twitter_app.py theunhingedlens")
        sys.exit(1)

    username = sys.argv[1].lstrip("@")

    print(f"\n== Looking up user by username: @{username}")
    user_json = get_user_by_username(username)
    print(pretty(user_json))

    # Pull out the user id for the next call
    try:
        user_id = user_json["data"]["id"]
        display_name = user_json["data"]["name"]
        handle = user_json["data"]["username"]
        print(f"\nFound user id: {user_id}  ({display_name} / @{handle})")
    except KeyError:
        print("Could not find 'data.id' in the response. Check your token and username.")
        sys.exit(1)

    time.sleep(1.0)

    print(f"\n== Fetching recent tweets for user id: {user_id}")
    tweets_json = get_recent_tweets(user_id, max_results=5)
    print(pretty(tweets_json))

    print("\n== Summary (tweet id • created_at • first 80 chars):")
    for t in tweets_json.get("data", []):
        tid = t.get("id", "")
        created = t.get("created_at", "")
        text_first80 = (t.get("text", "") or "").replace("\n", " ")[:80]
        print(f"- {tid} • {created} • {text_first80}")

if __name__ == "__main__":
    main()
