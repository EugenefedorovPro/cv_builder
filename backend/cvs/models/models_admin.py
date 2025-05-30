import ipdb
from django.contrib import admin
from .models import Header
from django.db.models import QuerySet


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        ipdb.set_trace()
        qs: QuerySet[Header] = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user = request.user)

    def has_change_permission(self, request, obj = None):
        if request.user.is_superuser:
            return True
        if obj is not None:
            return obj.user == request.user
        return True

    def has_delete_permission(self, request, obj = None):
        if request.user.is_superuser:
            return True
        if obj is not None:
            return obj.user == request.user
        return True

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()