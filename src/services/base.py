from dataclasses import dataclass
from typing import TypeVar, Generic, Optional
from django.db import transaction

T = TypeVar('T')

@dataclass
class ServiceResult(Generic[T]):
    success: bool
    data: Optional[T] = None
    error: Optional[str] = None

    def __bool__(self):
        return self.success

class BaseService:
    pass

class CRUDService(BaseService, Generic[T]):
    model_class = None

    def get_queryset(self):
        return self.model_class.objects.all()

    def get_by_id(self, pk):
        try:
            return ServiceResult(success=True, data=self.get_queryset().get(pk=pk))
        except self.model_class.DoesNotExist:
            return ServiceResult(success=False, error="Not found")

    @transaction.atomic
    def create(self, data):
        try:
            obj = self.model_class.objects.create(**data)
            return ServiceResult(success=True, data=obj)
        except Exception as e:
            return ServiceResult(success=False, error=str(e))

    @transaction.atomic
    def update(self, pk, data):
        try:
            obj = self.get_queryset().get(pk=pk)
            for k, v in data.items():
                setattr(obj, k, v)
            obj.save()
            return ServiceResult(success=True, data=obj)
        except self.model_class.DoesNotExist:
            return ServiceResult(success=False, error="Not found")

    @transaction.atomic
    def delete(self, pk):
        try:
            self.get_queryset().get(pk=pk).delete()
            return ServiceResult(success=True, data=True)
        except self.model_class.DoesNotExist:
            return ServiceResult(success=False, error="Not found")
