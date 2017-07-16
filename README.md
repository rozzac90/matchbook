# matchbook
Python wrapper for Matchbook API.

[Matchbook Documentation](https://developers.matchbook.com/v1.0/reference)

# Installation

```
$ python install matchbook
```

# Usage

```python
>>> from matchbook.apiclient import APIClient
>>> api = APIClient('username', 'password')
>>> sport_ids = api.reference_data.get_sports()
>>> tennis_events = api.market_data.get_events(sport_ids=[9]) 
```
