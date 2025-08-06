from django.shortcuts import render, get_object_or_404
from administrator.models import Brand, Product, Distributor, Carousel


# Create your views here.
def home(request):
    brand_carousels = Carousel.objects.all()  # Fetch all Brand objects
    products = Product.objects.all()  # Fetch all Product objects

    context = {
        "brand_carousels": brand_carousels,  # Pass the queryset directly
        "products": products,  # Pass the queryset directly
    }
    return render(request, "client/home.html", context)


def about_us(request):
    return render(request, "client/about_us.html")


def our_brands(request):
    brands = Brand.objects.all()  # Fetch all Brand objects from the database
    context = {"brands": brands}  # Pass the brands queryset to the template
    return render(request, "client/our_brands.html", context)


def brand_details(request):
    brand_id = request.GET.get("brand_id")
    brand = None
    products = []
    if brand_id:
        brand = get_object_or_404(Brand, id=brand_id)
        products = brand.products.all()  # Access related products

    context = {"brand": brand, "products": products}
    return render(request, "client/brand_details.html", context)


def our_channel(request):
    distributors = Distributor.objects.all()  # Fetch all Distributor objects
    context = {"distributors": distributors}
    return render(request, "client/our_channel.html", context)


def connect_us(request):
    return render(request, "client/connect_us.html")
