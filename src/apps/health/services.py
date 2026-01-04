import time
from dataclasses import dataclass
from django.db import connection
from services import BaseService, ServiceResult


@dataclass
class Health:
    status: str
    uptime: float

    def to_dict(self):
        return {"status": self.status, "uptime_seconds": round(self.uptime, 2)}


class HealthService(BaseService):
    _start = time.time()

    def check(self):
        try:
            with connection.cursor() as c:
                c.execute("SELECT 1")
            status = "healthy"
        except Exception:
            status = "unhealthy"
        return ServiceResult(
            success=True, data=Health(status, time.time() - self._start)
        )


health_service = HealthService()
