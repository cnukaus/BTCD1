### Feature hierarchy:


[feature_source].[feature_set].[feature_name]

examples:

"[gitcoin.co](http://gitcoin.co/)"."user_sybil"."sybil_likelihood"

"[api.github.com](http://api.github.com/)"."reputation"."followers"

"manual_googlesheets"."joe"."favouriteicons_count"


### Selection criteria:


1. Coverage: data fields  covering a significant amount of users are prefered

sparse features require more preparation effort to be useful, it is possible to include, maybe sometimes consider to derive/pca/merge sparse ones

2. Battle-tested: Used in previous GR rounds

3. Subject Matter Experts

4. Industry anti-spam resources (curated list, blacklist, IP addresses)

5. based on data source list (asked for it from dao members)

### V0.1 feature proposal

[api.github.com]
- Number of repos
- Number of repos where fork=false
- Followers
- Followed
- watchers

   derived or row level
- total issues (summary from all repos)
- highest open_issues_count of rep
- total forks (summary from all repos)
- highest forks of rep
- total stars (summary from all repos)
- highest stars of rep
- language, size, created_at, pushed_at date of each repo


 Data source
-  Is the user followed by an authenticated github account - and history
- Most number of folders created across all repos
- Most number of files created across all reposts
- Number of different programming languages used across all repos

[gitcoin.co][behaviour]

Registration, Date/Time

Last Activity, Date/Time

kudos collected, int

quest started, int

Quest finished, int

donation row level data (Address, grant, quantity, token, time)

hackathon started count, int

bounty started count, int

bounty finished count,int

IP Address row level/summary data (IP, date or first/last date range)

browsing row level data (type of url, date)

changed_default_preference, boolean

count of activities in each GR round

 data source TBD

[gitcoin.co][attributes]

email domain (Inherit from Github), string
Feedback row level/summary
Built avatar, boolean
job status, string
Location, string


other potential:

[gov.gitcoin.co]

Some data rules already on  [https://www.daostewards.xyz/](https://www.daostewards.xyz/))
[Discord activity raw data]

[user][self_defined_rules]



### Ref
[GR10 antifraud report blockscience] (https://medium.com/block-science/evaluating-the-anti-fraud-results-for-gitcoin-round-10-cec9277ce5b2)
