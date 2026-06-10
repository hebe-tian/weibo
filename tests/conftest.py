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
                    "num": 1234567,
                    "allmsg": "allmsgbody"
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
    return {
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
    return {
        "ok": 1,
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
    return {
        "ok": 1,
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
    return {
        "ok": 1,
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

@pytest.fixture
def response_error_type():
    '''
    A response data not dict type.
    '''
    return """{
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
    }"""


@pytest.fixture
def bandlist_valid_msg():
    '''
    A valid message for bandlist.
    '''
    return [
        {
            "note": "热搜话题1",
            "allmsg": "allmsgbody",
            "label_name": "热",
            "num": 1234567
        },
        {
            "note": "热搜话题2",
            "label_name": "",
            "num": 987654
        }
    ]

@pytest.fixture
def bandlist_msg_without_msg():
    '''
    A message for bandlist without without necessary msg.
    '''
    return [
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

@pytest.fixture
def bandlist_msg_with_empty_list():
    '''
    A valid message for bandlist without necessary msg.
    '''
    return []

@pytest.fixture
def bandlist_msg_with_error_type():
    '''
    A message for bandlist with empty list.
    '''
    return '''[
        {
            "note": "热搜话题1",
            "allmsg": "allmsgbody",
            "label_name": "热",
            "num": 1234567
        },
        {
            "note": "热搜话题2",
            "label_name": "",
            "num": 987654
        }
    ]'''
