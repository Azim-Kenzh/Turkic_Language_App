from rest_framework.permissions import BasePermission

from app.models import Category


class PaymentPermission(BasePermission):

    def has_permission(self, request, view):
        category_id = request.query_params.get('category')
        category = Category.objects.filter(id=category_id).first()
        if category and category.is_free:
            return True
        return request.user.is_premium()

    def has_object_permission(self, request, view, obj):
        return obj.category.is_free
