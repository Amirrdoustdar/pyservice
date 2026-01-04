import pytest
from django.contrib.auth.models import User
from services import ServiceResult, BaseService, CRUDService


class TestServiceResult:
    def test_success_result(self):
        result = ServiceResult(success=True, data="test")
        assert result.success
        assert result.data == "test"
        assert bool(result) is True

    def test_failure_result(self):
        result = ServiceResult(success=False, error="error")
        assert not result.success
        assert result.error == "error"
        assert bool(result) is False


class UserService(CRUDService):
    model_class = User


@pytest.mark.django_db
class TestCRUDService:
    def test_create(self):
        service = UserService()
        result = service.create({'username': 'test', 'password': 'pass123'})
        assert result.success
        assert result.data.username == 'test'

    def test_get_by_id(self):
        user = User.objects.create(username='findme')
        service = UserService()
        result = service.get_by_id(user.id)
        assert result.success
        assert result.data.username == 'findme'

    def test_get_by_id_not_found(self):
        service = UserService()
        result = service.get_by_id(9999)
        assert not result.success
        assert 'Not found' in result.error

    def test_update(self):
        user = User.objects.create(username='old')
        service = UserService()
        result = service.update(user.id, {'username': 'new'})
        assert result.success
        assert result.data.username == 'new'

    def test_update_not_found(self):
        service = UserService()
        result = service.update(9999, {'username': 'x'})
        assert not result.success

    def test_delete(self):
        user = User.objects.create(username='delete_me')
        service = UserService()
        result = service.delete(user.id)
        assert result.success
        assert not User.objects.filter(id=user.id).exists()

    def test_delete_not_found(self):
        service = UserService()
        result = service.delete(9999)
        assert not result.success
