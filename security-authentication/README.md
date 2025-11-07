[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Im-1WOrm)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21495965)



# Twitter API Access Control Demo

**Name:** Chris Low  
**CNET ID:** chrislowzhengxi  
**Date:** November 2025  

---

## Overview

This project shows how a third-party application can connect to the Twitter (X) API and get data using the app’s access credentials.  
The goal was to understand how API access control works in practice and to see how authentication and rate limits affect what a client can do.


## How Twitter Handles Access Control

Twitter uses **OAuth 2.0** to control which apps can access its data.  
When you register an app on the [X Developer Portal](https://developer.x.com/), Twitter gives you a few credentials:

- **API Key** and **API Secret** – identify your app.  
- **Bearer Token** – used for app-only authentication (for reading public data).  
- **Access Token** and **Access Token Secret** – used when an app acts on behalf of a signed-in user (for posting or editing tweets).

Every request to the API must include an **Authorization header**:
`Authorization: Bearer <token>`. If the header or token is missing or invalid, the API returns `401 Unauthorized`.

Twitter also limits how many requests an app can make in a short period. For the free tier, most read endpoints allow around 15 requests every 15 minutes. When the limit is reached, the server returns a `429 Too Many Requests` error. This form of **rate limiting** is part of access control because it keeps one client from overusing the service (and possibly preventing attacks). 

**Simple flow diagram**
```
[Developer App] --> (API key + secret)
        ↓
 [Auth Server] --> issues Bearer Token
        ↓
 [Client Application] --> sends request with Authorization header
        ↓
 [Twitter API] --> validates token and returns JSON data
```



## Description of My App

The app (`twitter_app.py`) uses my Bearer Token to connect to the Twitter API.  
It has two main parts:

1. **User lookup:** Calls `/2/users/by/username/{username}` to get a user’s id, name, and handle.

2. **Recent tweets:** Uses `/2/users/{id}/tweets` to fetch the latest five tweets for that user.

The script prints both JSON responses in a readable format and summarizes each tweet’s text and timestamp.  
It also handles common HTTP errors, including rate-limit messages (HTTP 429). In which case, the following outputs: 
```
== Looking up user by username: @theunhingedlens
HTTP 429 error at https://api.x.com/2/users/by/username/theunhingedlens?user.fields=created_at%2Cpublic_metrics
Response:
{"title":"Too Many Requests","detail":"Too Many Requests","type":"about:blank","status":429}
```

Here is the core part that handles authentication:

```python
req.add_header("Authorization", f"Bearer {get_bearer_token()}")
```

This shows that access is only granted when the request includes a valid token.



## Proof That the App Works

I ran the program with my account handle:

```bash
$ export X_BEARER_TOKEN="my_bearer_token"
$ python3 twitter_app.py theunhingedlens
```

The output returned the correct user id and profile information, followed by a list of recent tweets.

A full copy of the output is saved under
[`proof/twitter_run.txt`](proof/twitter_run.txt)

While testing, I also received an HTTP 429 error (“Too Many Requests”) after running the script several times in a row.
That error confirmed that Twitter’s rate limiting is active and forms part of the access control process.


## Code

The full code is in [`twitter_app.py`](twitter_app.py).
It only uses the Python standard library (`urllib`), so no extra packages are needed.



## Conclusion and References

This short project made it clear how APIs protect both their data and infrastructure. Even a simple read-only request needs a registered app and a valid token, and the system quickly blocks repeated calls. It’s an easy but practical way to see OAuth 2.0 and rate limiting working together.


* [Twitter API v2 Documentation](https://developer.x.com/en/docs)
* [OAuth 2.0 Overview](https://oauth.net/2/)


