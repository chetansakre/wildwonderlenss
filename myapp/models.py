from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.utils.html import mark_safe



# Create your models here.
class Categories(models.Model):
    # icon = models.CharField(max_length=200,null=True)
    name = models.CharField(max_length=200,null=True)

    # animal = models.ForeignKey(Animal,  on_delete=models.CASCADE)
    # bird = models.ForeignKey(Bird,  on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Visitor(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    ip_address = models.CharField(max_length=50, null=True)
    session_id = models.CharField(max_length=50, null=True)

    def __str__(self):
        if self.created_at:
            return f"Visitor {self.pk} - Created at: {self.created_at}"
        else:
            return f"Visitor {self.pk} - No creation timestamp available"


class SubCategories(models.Model):
    # icon = models.CharField(max_length=200,null=True)
    name = models.CharField(max_length=200,null=True)

    # animal = models.ForeignKey(Animal,  on_delete=models.CASCADE)
    # bird = models.ForeignKey(Bird,  on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Size(models.Model):
    height = models.CharField( max_length=50,null=True)
    width = models.CharField( max_length=50,null=True)

    def __str__(self):
        return str(self.height) + " * " + str(self.width)


class Color(models.Model):
    name = models.CharField(max_length=50,null = True)


    def __str__(self):
        return self.name

class Photoframe(models.Model):
    STATUS = (
        ('PUBLISH','PUBLISH'),
        ('DRAFT', 'DRAFT'),
    )
    name = models.CharField( max_length=100, unique=True)
    image =  models.ImageField(upload_to="Media/img", null=True)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    status = models.CharField(choices=STATUS,max_length=100,null=True)
    price = models.IntegerField(null=True,default=0)
    # discount = models.IntegerField(null=True)
    description = models.TextField()

    # Frame_size = models.ForeignKey(Size,  on_delete=models.CASCADE,null =True)
    # color = models.ForeignKey(Color,  on_delete=models.CASCADE,null =True)

    created_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE,null = True)
    subcategory = models.ForeignKey(SubCategories,on_delete=models.CASCADE,null = True,blank = True)
    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.image.url))
    image_tag.short_description = 'Image'




    def __str__(self):
        return self.name
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("course_details", kwargs= {'slug':self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Photoframe.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Photoframe)




class Image(models.Model):
    photoframe = models.ForeignKey(Photoframe, related_name='images', on_delete=models.CASCADE,null = True)
    image = models.ImageField(upload_to="Media/img", null=True)
    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.image.url))
    image_tag.short_description = 'Image'

class Review(models.Model):
    product = models.ForeignKey(Photoframe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null = True)  # ForeignKey to User model
    rating = models.DecimalField(max_digits=2, decimal_places=1)  # Assuming you're storing ratings like 4.5, 3.5, etc.
    content = models.TextField()
    name = models.CharField( max_length=100)
    email = models.EmailField(max_length=254)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ContactUs(models.Model):
    # name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Wishlist(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE,null = True)
    photoframe = models.ForeignKey(Photoframe, on_delete=models.CASCADE)

    def __str__(self):
        return self.photoframe.name

class FrameDetail(models.Model):
    photoframe = models.ForeignKey(Photoframe, on_delete=models.CASCADE,null =True)
    size = models.CharField(max_length=50)
    color = models.CharField( max_length=50)

    def __str__(self):
        return self.size + "-" + self.color

class Order(models.Model):
    firstname = models.CharField( max_length=100)
    lastname = models.CharField( max_length=100)
    country = models.CharField( max_length=100)
    streetadd = models.CharField( max_length=100)
    city = models.CharField( max_length=100 )
    postcode = models.CharField( max_length=100)
    phoneno = models.CharField( max_length=100)
    email = models.CharField( max_length=100)
    order_id = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.CharField( max_length=50)


    def __str__(self):
        return str(self.order_id)


class CartItem(models.Model):
    order = models.ForeignKey(Order,  on_delete=models.CASCADE,null = True)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image =  models.ImageField(upload_to="Media/img")

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.image.url))
    image_tag.short_description = 'Image'
    def __str__(self):
        return self.user.username + "-" + self.product_name

class Newsletter(models.Model):
    email = models.EmailField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class PhotoTour(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phoneno = models.CharField(max_length=200)
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name +"-"+self.email


