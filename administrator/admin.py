from django.contrib import admin
from django.utils.html import format_html
from .models import Distributor, Brand, Product, Carousel


@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "contact_person",
        "phone_number",
        "email",
        "address",
        "display_coverage_areas",
        "display_image_thumbnail",
    )
    search_fields = (
        "name",
        "contact_person",
        "email",
        "address",
        "coverage_areas",
    )
    list_filter = ()
    list_display_links = (
        "name",
        "contact_person",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "contact_person",
                    "phone_number",
                    "email",
                    "address",
                )
            },
        ),
        (
            "Additional Information",
            {
                "fields": (
                    "coverage_areas",
                    "image",
                ),
                "description": "Enter coverage areas as a comma-separated list. Upload an image if available.",
            },
        ),
    )

    def display_coverage_areas(self, obj):
        if obj.coverage_areas:
            return obj.coverage_areas.replace(",", ", ")
        return "N/A"

    display_coverage_areas.short_description = "Coverage Areas"

    def display_image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 5px;" />',
                obj.image.url,
            )
        return "No Image"

    display_image_thumbnail.short_description = "Image"

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
        "establish_date",
        "display_description_snippet",
        "display_image_thumbnail",
    )
    search_fields = (
        "name",
        "country",
        "description",
    )
    list_filter = (
        "country",
        "establish_date",
    )
    list_display_links = ("name",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "country",
                    "establish_date",
                    "description",
                )
            },
        ),
        (
            "Additional Information",
            {
                "fields": ("image",),
                "description": "Upload the brand's logo or a representative image.",
            },
        ),
    )

    def display_image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 5px;" />',
                obj.image.url,
            )
        return "No Image"

    display_image_thumbnail.short_description = "Image"

    def display_description_snippet(self, obj):
        if obj.description:
            return (
                (obj.description[:75] + "...")
                if len(obj.description) > 75
                else obj.description
            )
        return "N/A"

    display_description_snippet.short_description = "Description"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "brand",
        "self_life",
        "display_available_sizes",
        "display_packaging",
        "display_description_snippet",
        "display_image_thumbnail",
    )
    search_fields = (
        "name",
        "description",
        "self_life",
        "available_sizes",
        "packaging",
        "brand__name",
    )
    list_filter = (
        "brand",
    )
    list_display_links = (
        "name",
        "brand",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "brand",
                    "description",
                    "self_life",
                )
            },
        ),
        (
            "Additional Information",
            {
                "fields": (
                    "available_sizes",
                    "packaging",
                    "image",
                ),
                "description": "Enter sizes and packaging as comma-separated lists. Upload a product image.",
            },
        ),
    )
    raw_id_fields = (
        "brand",
    )

    def display_image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 5px;" />',
                obj.image.url,
            )
        return "No Image"

    display_image_thumbnail.short_description = "Image"

    def display_description_snippet(self, obj):
        if obj.description:
            return (
                (obj.description[:75] + "...")
                if len(obj.description) > 75
                else obj.description
            )
        return "N/A"

    display_description_snippet.short_description = "Description"

    def display_available_sizes(self, obj):
        if obj.available_sizes:
            return obj.available_sizes.replace(",", ", ")
        return "N/A"

    display_available_sizes.short_description = "Available Sizes"

    def display_packaging(self, obj):
        if obj.packaging:
            return obj.packaging.replace(",", ", ")
        return "N/A"

    display_packaging.short_description = "Packaging"


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ("name", "description_short", "image_thumbnail")
    list_display_links = ("name",)
    search_fields = ("name", "description")
    fieldsets = (
        (None, {"fields": ("name", "description")}),
        (
            "Additional Information",
            {
                "fields": ("image",),
                "description": "Upload the image for this carousel item.",
            },
        ),
    )

    def description_short(self, obj):
        if obj.description:
            return (
                obj.description[:75] + "..."
                if len(obj.description) > 75
                else obj.description
            )
        return "-"

    description_short.short_description = "Description"

    def image_thumbnail(self, obj):
        if obj.image and hasattr(obj.image, "url"):
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: contain;" />',
                obj.image.url,
            )
        return "No Image"

    image_thumbnail.short_description = "Thumbnail"