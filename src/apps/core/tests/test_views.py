from apps.core.exceptions import custom_exception_handler


class TestExceptionHandler:
    def test_handler_returns_none_for_none_response(self):
        result = custom_exception_handler(Exception("test"), {})
        assert result is None
