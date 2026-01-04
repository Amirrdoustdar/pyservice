import pytest
from rest_framework import status


@pytest.mark.django_db
class TestHealth:
    def test_health(self, client):
        r = client.get('/api/v1/health/')
        assert r.status_code == status.HTTP_200_OK
        assert r.json()['status'] == 'healthy'
        assert 'uptime_seconds' in r.json()

    def test_live(self, client):
        r = client.get('/api/v1/health/live/')
        assert r.status_code == status.HTTP_200_OK
        assert r.json()['status'] == 'alive'

    def test_ready(self, client):
        r = client.get('/api/v1/health/ready/')
        assert r.status_code == status.HTTP_200_OK
        assert r.json()['status'] == 'ready'


@pytest.mark.django_db
class TestHealthService:
    def test_health_service_check(self):
        from apps.health.services import health_service
        result = health_service.check()
        assert result.success
        assert result.data.status == 'healthy'

    def test_health_service_uptime(self):
        from apps.health.services import health_service
        result = health_service.check()
        assert result.data.uptime >= 0
