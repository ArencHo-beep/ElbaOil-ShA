from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.http import JsonResponse

def category_autocomplete(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        query = request.GET.get('term', '')
        categories = Category.objects.filter(name__icontains=query)
        results = [category.name for category in categories]
        return JsonResponse(results, safe=False)


def home_view(request):
    all_categories = Category.objects.all()
    ctx = {
        'categories': all_categories
    }
    return render(request, "index.html", ctx)

def product_list_view(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def contact_view(request):
    return render(request, "contact.html")

def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    print(products)
    return render(request, 'category_detail.html', {'category': category, 'products': products})

def search_view(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')

    products = Product.objects.all()
    if query:
        products = products.filter(name__icontains=query)

    if category_id:
        products = products.filter(category__id=category_id)

    categories = Category.objects.all()
    return render(request, 'search_results.html', {
        'query': query,
        'results': products,
        'categories': categories,
        'selected_category': category_id
    })

def search_suggestions(request):
    query = request.GET.get('term', '')
    results = []
    if query:
        matches = Product.objects.filter(name__icontains=query)[:5]
        results = [{'label': p.name, 'id': p.id} for p in matches]
    return JsonResponse(results, safe=False)

