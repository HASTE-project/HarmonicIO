import pytest

from harmonicIO.stream_connector.stream_connector import StreamConnector


def test_instantiate_client():
    # Ensure that we can instantiate the stream connector:
    connector = StreamConnector('127.0.0.1',1234)