import pytest
from apps.core.exceptions import custom_exception_handler
from rest_framework.exceptions import NotFound


class TestExceptionHandler:
    def test_handler_returns_none_for_none_response(self):
        # وقتی exception ناشناخته باشه
        result = custom_exception_handler(Exception("test"), {})
        assert result is None
