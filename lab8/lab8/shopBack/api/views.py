from django.http import JsonResponse,HttpRequest
from django.shortcuts import get_object_or_404
from django.views import View
from .models import Category, Product

def home(request):
    return JsonResponse({"message": "Welcome to my API!"})

class ProductListView(View):
    def get(self, request):
        products = list(Product.objects.values("id", "name", "price", "description", "count", "is_active", "category__name"))
        return JsonResponse(products, safe=False, json_dumps_params={"indent": 2})

class ProductDetailView(View):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        return JsonResponse({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "count": product.count,
            "is_active": product.is_active,
            "category": product.category.name if product.category else None
        }, json_dumps_params={"indent": 2})

class CategoryListView(View):
    def get(self, request):
        categories = list(Category.objects.values("id", "name"))
        return JsonResponse(categories, safe=False, json_dumps_params={"indent": 2})

class CategoryDetailView(View):
    def get(self, request, id):
        category = get_object_or_404(Category, id=id)
        return JsonResponse({
            "id": category.id,
            "name": category.name
        }, json_dumps_params={"indent": 2})

class CategoryProductsView(View):
    def get(self, request, id):
        category = get_object_or_404(Category, id=id)
        products = list(category.products.values("id", "name", "price", "description", "count", "is_active"))
        return JsonResponse(products, safe=False, json_dumps_params={"indent": 2})
