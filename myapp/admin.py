from django.contrib import admin
from myapp.models import *

# Register your models here.
class Image_Tabularinline(admin.TabularInline):
    model = Image

class Cart_Tabularinline(admin.TabularInline):
    model = CartItem
    extra = 0
    fields = [  'image_tag','product_name','quantity','size','price','color',]
    readonly_fields = ['image_tag']

    def image_tag(self, obj):
        if obj.image:
            return mark_safe('<img src="%s" width="100px" height="100px" />' % obj.image.url)
        else:
            return 'No Image'

    image_tag.short_description = 'Image'
class Photoframe_admin(admin.ModelAdmin):
    inlines = (Image_Tabularinline,)
    list_display = ["name","price","category", "image_tag"]
    search_fields = ("name",)
    list_filter = ("category", )

class Review_admin(admin.ModelAdmin):
    # inlines = (Image_Tabularinline,)
    list_display = ["product","user","rating","email","date"]
    search_fields = ("product__name",)
    list_filter = ("rating",)
class Wishlist_admin(admin.ModelAdmin):
    # inlines = (Image_Tabularinline,)
    list_display = ["user","photoframe"]
    # search_fields = ("product__name",)
    # list_filter = ("rating",)

class Image_admin(admin.ModelAdmin):
    # inlines = (Image_Tabularinline,)
    list_display = ["photoframe","image_tag"]
    # search_fields = ("product__name",)
    # list_filter = ("rating",)

class Contact_admin(admin.ModelAdmin):
    # inlines = (Image_Tabularinline,)
    list_display = ["email","subject"]
    # search_fields = ("product__name",)
    # list_filter = ("rating",)
class CartItem_admin(admin.ModelAdmin):
    # inlines = (Image_Tabularinline,)
    list_display = ["user","product_name" ,'order', "image_tag"]
    search_fields = ("product_name",)
    list_filter = ("product_name",)

class Order_admin(admin.ModelAdmin):
    inlines = [Cart_Tabularinline]
    list_display = ["customer","email" , "date","order_id" , "country"]
    search_fields = ("customer__username",)
    # list_filter = ("product_name",)
class FrameDetail_admin(admin.ModelAdmin):
    list_display = ["photoframe","size" , "color"]
    search_fields = ("photoframe__name",)
    list_filter = ("photoframe",)

class newsletter_admin(admin.ModelAdmin):
    list_display = ["email" , "created_at"]

    list_filter = ("created_at",)


class PhotoTour_admin(admin.ModelAdmin):
    list_display = ["name","email","created_at"]
    list_filter =  ("created_at",)


admin.site.register(Photoframe,Photoframe_admin)
admin.site.register(Size)
admin.site.register(Categories)
admin.site.register(Image,Image_admin)
admin.site.register(Review,Review_admin)
admin.site.register(ContactUs,Contact_admin)
admin.site.register(Color)
admin.site.register(SubCategories)
admin.site.register(Wishlist,Wishlist_admin)
admin.site.register(FrameDetail,FrameDetail_admin)
admin.site.register(Order,Order_admin)
admin.site.register(CartItem,CartItem_admin)
admin.site.register(Newsletter,newsletter_admin)
admin.site.register(PhotoTour,PhotoTour_admin)
admin.site.register(Visitor)





