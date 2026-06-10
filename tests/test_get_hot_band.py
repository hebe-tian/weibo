import pytest
from get_hot_band import check_response, get_hot_band_allmsg, get_hot_band_list


class TestCheckResponse:
    "Test the check_response function"

    def test_check_response_with_valid_response(self, valid_response):
        result = check_response(valid_response)
        assert result == True

    def test_check_response_error_with_ok(self, response_error_with_ok):
        result = check_response(response_error_with_ok)
        assert result == False

    def test_check_response_without_ok(self, response_error_without_ok):
        result = check_response(response_error_without_ok)
        assert result == False

    def test_check_response_without_realtime(self, response_error_without_realtime):
        result = check_response(response_error_without_realtime)
        assert result == False


    def test_check_response_error_without_dict(self, response_error_type):
        result = check_response(response_error_type)
        assert result == False

class TestGetHotBandAllmsg:
    "Test the get_hot_band_allmsg function"
    def test_get_hot_band_allmsg_with_valid_response(self, valid_response):
        result = get_hot_band_allmsg(valid_response)
        assert result[0].get("note") == "热搜话题1"
        assert result[0].get("label_name") == "热"
        assert result[0].get("num") == 1234567
        assert result[0].get("allmsg") == "allmsgbody"

    def test_get_hot_band_allmsg_without_ealtime(self, response_error_without_realtime):
        result = get_hot_band_allmsg(response_error_without_realtime)
        assert result == None

    def test_get_hot_band_allmsg_without_dict(self, response_error_type):
        result = get_hot_band_allmsg(response_error_type)
        assert result == None

    def test_get_hot_band_allmsg_with_empty_realtime(self, response_error_with_empty_realtime):
        result = get_hot_band_allmsg(response_error_with_empty_realtime)
        assert result == []

class TestGetHotBandList:
    "Test the get_hot_band_list function"
    def test_get_hot_band_list_with_valid_response(self, bandlist_valid_msg):
        result = get_hot_band_list(bandlist_valid_msg)
        assert result[0].get("note") == "热搜话题1"
        assert result[0].get("tag") == "热"
        assert result[0].get("num") == 1234567
        assert result[0].get("allmsg") == None

    def test_get_hot_band_list_without_msg(self, bandlist_msg_without_msg):
        result = get_hot_band_list(bandlist_msg_without_msg)
        assert result == None

    def test_get_hot_band_list_with_empty_list(self, bandlist_msg_with_empty_list):
        result = get_hot_band_list(bandlist_msg_with_empty_list)
        assert result == []

    def test_get_hot_band_list_with_error_type(self, bandlist_msg_with_error_type):
        result = get_hot_band_list(bandlist_msg_with_error_type)
        assert result == None
