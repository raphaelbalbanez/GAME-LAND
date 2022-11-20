import pytest


def test_example(client):
    resp = client.get("GAMELAND/anunciar/")
    assert resp.status_code == 200