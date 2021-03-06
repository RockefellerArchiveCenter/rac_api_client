# rac_api_client
A client to interact with the Rockefeller Archive Center's Collections API.

[![Build Status](https://app.travis-ci.com/RockefellerArchiveCenter/rac_api_client.svg?branch=base)](https://app.travis-ci.com/RockefellerArchiveCenter/rac_api_client)

## Dependencies

*   [Python 3.6 or higher](https://www.python.org/)

## Getting Started

`pip install rac_api_client`

## Usage

In order to use the client in your Python script, you first need to import it and create an instance.

```
from rac_api_client import Client
client = Client()
```

This client contains two methods to facilitate working with the RAC's Collections API.
- `get` sends a GET request for a single object. The URI for that object should be passed as the first argument.

```
client.get("/collections/WY7fpswEV3oLhyjiArpHES")
```

- `get_paged` returns all results for paged content, for example a list of collections or search results.

```
client.get_paged("/collections")
```

For both of these methods, parameters can optionally be passed as a dictionary.

```
client.get_paged("/objects", params={"online": True, "start_date__gte": "1950"})
client.get("/search", params={"query": "yellow fever"})
```

## Development
This repository contains a configuration file for git [pre-commit](https://pre-commit.com/) hooks which help ensure that code is linted before it is checked into version control. It is strongly recommended that you install these hooks locally by installing pre-commit and running `pre-commit install`.

## License
This code is released under the MIT License. See `LICENSE.md` for more information.
