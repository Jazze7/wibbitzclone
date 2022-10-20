from django.contrib import admin
from web.models import Subscribe, Creator, Feature, Videoblog, Testimonial, MarketingFeature, Product, Blog, Contact

# Register your models here.


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ["id", "email"]


admin.site.register(Subscribe, SubscribeAdmin)


class CreatorAdmin(admin.ModelAdmin):
    list_display = ["id", "image"]


admin.site.register(Creator, CreatorAdmin)


class FeatureAdmin(admin.ModelAdmin):
    list_display = ["id", "image", "icon",
                    "icon_background", "title", "description"]


admin.site.register(Feature, FeatureAdmin)


class VideoblogAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "logo"]


admin.site.register(Videoblog, VideoblogAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]


admin.site.register(Testimonial, TestimonialAdmin)


class MarketingFeatureAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description"]


admin.site.register(MarketingFeature, MarketingFeatureAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description"]


admin.site.register(Product, ProductAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description"]


admin.site.register(Blog, BlogAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name"]


admin.site.register(Contact, ContactAdmin)
