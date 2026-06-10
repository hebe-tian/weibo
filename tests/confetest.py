import pytest

@pytest.fixture
def valid_response():
    """
    A valid response for testing.
    """
    return {
        "ok": 1,
        "data": {
            "realtime": [
                {
                    "note": "热搜话题1",
                    "label_name": "热",
                    "num": 1234567
                },
                {
                    "note": "热搜话题2",
                    "label_name": "新",
                    "num": 987654
                },
                {
                    "note": "热搜话题3",
                    "label_name": "",
                    "num": 456789
                }
            ]
        }
    }


@pytest.fixture
def response_error_with_ok():
    """
    A response with an error with ok.
    """
    {
        "ok": 0,
        "data": {
            "realtime": [
                {
                    "note": "热搜话题1",
                    "label_name": "热",
                    "num": 1234567
                },
                {
                    "note": "热搜话题2",
                    "label_name": "新",
                    "num": 987654
                },
                {
                    "note": "热搜话题3",
                    "label_name": "",
                    "num": 456789
                }
            ]
        }
    }

@pytest.fixture
def response_error_without_ok():
    """
    A response with an error without ok.
    """
    return {
        "data": {
            "realtime": [
                {
                    "note": "热搜话题1",
                    "label_name": "热",
                    "num": 1234567
                },
                {
                    "note": "热搜话题2",
                    "label_name": "新",
                    "num": 987654
                },
                {
                    "note": "热搜话题3",
                    "label_name": "",
                    "num": 456789
                }
            ]
        }
    }

@pytest.fixture
def response_error_without_realtime():
    """
    A response without realtime.
    """
    {
        "ok": 0,
        "data": {
            "without realtime": [
                {
                    "note": "热搜话题1",
                    "label_name": "热",
                    "num": 1234567
                },
                {
                    "note": "热搜话题2",
                    "label_name": "新",
                    "num": 987654
                },
                {
                    "note": "热搜话题3",
                    "label_name": "",
                    "num": 456789
                }
            ]
        }
    }

@pytest.fixture
def response_error_with_empty_realtime():
    """
    A response with an error with empty realtime.
    """
    {
        "ok": 0,
        "data": {
            "realtime": [
            ]
        }
    }

@pytest.fixture
def response_error_without_msg():
    """
    A response with an error without necessary msg.
    """
    {
        "ok": 0,
        "data": {
            "realtime": [
                {
                    "label_name": "热",
                    "num": 1234567
                },
                {
                    "note": "热搜话题2",
                    "num": 987654
                },
                {
                    "note": "热搜话题3",
                    "label_name": "",
                }
            ]
        }
    }
