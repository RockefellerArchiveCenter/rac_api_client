from unittest.mock import patch

import requests

from rac_api_client import Client


def test_client_init():
    client = Client()
    assert client.base_url == "https://api.rockarch.org"
    assert client.page_size == 50
    assert isinstance(client.session, requests.Session)
    assert client.session.headers["Accept"] == 'application/json'
    assert client.session.headers["User-Agent"] == 'rac-api-client/0.1'


@patch('requests.Session.get')
def test_get(mock_get):
    mock_json = {"title": "foobar"}
    mock_text = "foobar"
    mock_get.return_value.json.return_value = mock_json

    client = Client()
    assert client.get("collections/1234") == mock_json
    mock_get.assert_called_with(
        'https://api.rockarch.org/collections/1234', params={})

    mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError()
    mock_get.return_value.text = mock_text
    assert client.get(
        "collections/1234",
        params={
            "query": "yellow fever"}) == mock_text
    mock_get.assert_called_with(
        'https://api.rockarch.org/collections/1234',
        params={
            "query": "yellow fever"})


@patch('requests.Session.get')
def test_get_paged(mock_get):
    collection_list = [{"title": "foo"}, {"title": "bar"}, {"title": "baz"}]
    mock_get.return_value.json.side_effect = [
        {"results": collection_list, "next": "collections"}, {"results": [], "next": None}]

    client = Client()
    assert list(
        client.get_paged(
            "collections", params={
                "query": "yellow fever"})) == collection_list
    mock_get.assert_called_with(
        "https://api.rockarch.org/collections",
        params={"query": "yellow fever", 'limit': 50, 'offset': 50})
