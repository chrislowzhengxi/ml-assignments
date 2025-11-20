[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/2a5U16fo)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21752828)
## Internet Privacy

The goal of this assignment is to understand how your web activity can
be tracked using your DNS queries. To do so, you will visit a website of
your choice and log all DNS queries made by your browser. Try to pick a
popular website (nytimes, facebook, reddit, etc) that you have not
visited in a while. Please answer the following questions in your
write-up. For simplicity, assume that all caches are empty and you are
browsing on the UChicago network. 

### Tasks

1. Capture the DNS queries made by your browser when loading this
website. You can do this either with a tool like wireshark. Please
include your results in the form of a pcap that contains *only* the DNS
queries (you can filter for DNS queries in Wireshark). Based on your
data:

-   Who (i.e., what companies) can see that you\'ve visited the website
    based on unencrypted DNS queries? 

-   Beyond DNS queries, name all other entities that know you\'ve
    visited the website. Present your findings by grouping your domain
    names into companies (e.g., the company \"Google\" has many domain
    names). Explain how these companies may have visited the website.

-   What different types of concerns might you have about the above
    companies knowing this information (concerns may differ by
    company!).

2. Now [enable encrypted DNS in your browser](https://developers.cloudflare.com/1.1.1.1/encrypted-dns/dns-over-https/encrypted-dns-browsers)
and repeat the above exercise.

-   Who can see that you\'ve visited the website based on encrypted DNS
    queries?
-   Comment on the privacy tradeoffs with encrypted DNS. Some companies
    from part 1 can *still *see your browsing activity, and other
    companies might not be able to, yet some *new* companies may have
    now gained some visibility into your browsing.

Hint: If you\'d like, install [Warp,](https://1.1.1.1/)
a DNS tool from Cloudflare. It may be more
comprehensible than the Wireshark output. 
# internet-privacy
