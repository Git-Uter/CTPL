from django.db import models


class Distributor(models.Model):
    name = models.CharField(
        max_length=255,
        help_text="Enter the full name of the distribution hub (e.g., Eastern Distribution Hub).",
    )
    contact_person = models.CharField(
        max_length=255,
        help_text="Enter the name of the primary contact person for this distributor (e.g., Ramesh Rai).",
    )
    phone_number = models.CharField(
        max_length=20,
        help_text="Enter the contact phone number, including the country code if applicable (e.g., 9848567890).",
    )
    email = models.EmailField(
        help_text="Enter the official contact email address for the distributor (e.g., eastern@nepalcorpffmcg.com).",
    )
    address = models.CharField(
        max_length=255,
        help_text="Enter the full physical address of the distribution hub (e.g., Biratnagar, Province 1).",
    )
    image = models.ImageField(
        upload_to="distributor_images/",
        help_text="Upload a representative image for the distributor, such as their office or a logo.",
    )
    coverage_areas = models.CharField(
        max_length=500,  
        help_text="Enter a comma-separated list of all geographical areas covered by this distributor (e.g., Sunsari, Morang, Jhapa).",
    )

    def __str__(self):
        return self.name

    def get_coverage_areas_list(self):
        if self.coverage_areas:
            return [area.strip() for area in self.coverage_areas.split(",")]
        return []


class Brand(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        help_text="Enter the unique name of the brand (e.g., PureVital Foods).",
    )
    image = models.ImageField(
        upload_to="brand_images/",
        help_text="Upload the official logo or a representative image of the brand.",
    )
    country = models.CharField(
        max_length=100,
        help_text="Enter the country of origin or the main country of operation for the brand (e.g., India).",
    )
    description = models.TextField(
        help_text="Provide a detailed description of the brand, its values, and its product focus (e.g., Premium organic and natural food products sourced from the best farms globally.)."
    )
    establish_date = models.DateField(
        help_text="Enter the date the brand was officially established (e.g., 2005-01-01)."
    )

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name="products",
        help_text="Select the brand this product belongs to from the list.",
    )
    name = models.CharField(
        max_length=255,
        help_text="Enter the specific name of the product (e.g., Coca-Cola Classic).",
    )
    image = models.ImageField(
        upload_to="product_images/",
        help_text="Upload a clear image of the product itself.",
    )
    description = models.TextField(
        help_text="Provide a detailed description of the product, including its key features and benefits."
    )
    self_life = models.CharField(
        max_length=50,
        help_text="Specify the shelf life of the product (e.g., 12 Months).",
    )
    available_sizes = models.CharField(
        max_length=500,
        help_text="Enter a comma-separated list of all available sizes or variants for this product (e.g., 250ml Can, 330ml Bottle).",
    )
    packaging = models.CharField(
        max_length=500,
        help_text="Enter a comma-separated list of packaging details for the product (e.g., 24 cans per case, 12 bottles per case).",
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["name"]

    def __str__(self):
        return f"{self.brand.name} - {self.name}"

    def get_available_sizes_list(self):
        if self.available_sizes:
            return [size.strip() for size in self.available_sizes.split(",")]
        return []

    def get_packaging_list(self):
        if self.packaging:
            return [pack.strip() for pack in self.packaging.split(",")]
        return []


class Carousel(models.Model):
    image = models.ImageField(
        upload_to="carousel_images/",
        help_text="Upload the image for this carousel slide.",
    )
    name = models.CharField(
        max_length=100, help_text="Enter a short title or name for this carousel item."
    )
    description = models.TextField(
        help_text="Provide a brief description or call-to-action text for the carousel slide."
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Carousel Item"
        verbose_name_plural = "Carousel Items"
        ordering = ["name"]
