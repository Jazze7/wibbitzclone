from email.mime import image
from random import choices
from turtle import title
from unicodedata import name
from django.db import models


COMPANY_SIZE = (
    ("1", "1-10"),
    ("2", "11-50"),
    ("3", "50-100"),
    ("4", "100-200"),
)
INDUSTRY_SIZE = (
    ("1", "Industry"),
    ("2", "Agriculture"),
    ("3", "Banking & Finance"),
    ("4", "Business Services & Software"),
)
JOB = (
    ("1", "Software Engineer"),
    ("2", "Database Engineer"),
    ("3", "Business Analytics"),
    ("4", "Developer"),
)
COUNTRY = (
    ("1", "India"),
    ("2", "USA"),
    ("3", "UK"),
    ("4", "UAE"),
)
# Create your models here.


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Creator(models.Model):
    image = models.FileField(upload_to="document/")

    def __str__(self):
        return str(self.id)


class Feature(models.Model):
    image = models.ImageField(upload_to="feature/")
    icon = models.FileField(upload_to="document/")
    icon_background = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    testimonial_description = models.TextField()
    testimonial_author = models.CharField(max_length=255)
    author_designation = models.CharField(max_length=255)
    testimonial_logo = models.FileField(upload_to="document/")

    def __str__(self):
        return self.title


class Videoblog(models.Model):
    image = models.ImageField(upload_to="videoblog/")
    title = models.CharField(max_length=255)
    logo = models.FileField(upload_to="document/")

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    image = models.ImageField(upload_to="testimonial/")
    logo = models.FileField(upload_to="document/", blank=True, null=True)
    description = models.TextField()
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    isfeatured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class MarketingFeature(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to="document/")
    description = models.TextField()

    def __str__(self):
        return self.title


class Product(models.Model):
    logo = models.FileField(upload_to="document/")
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="product/")

    def __str__(self):
        return self.title


class Blog(models.Model):
    content = (
        ("Blog post", "Blog post"),
        ("Webinar", "Webinar"),
        ("Report", "Report"),
    )
    image = models.ImageField(upload_to="blog/")
    title = models.CharField(
        max_length=255, choices=content, default="Webinar")
    description = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    company = models.CharField(max_length=255)
    company_size = models.CharField(max_length=255, choices=COMPANY_SIZE)
    industry = models.CharField(max_length=255, choices=INDUSTRY_SIZE)
    job = models.CharField(max_length=255, choices=JOB)
    country = models.CharField(max_length=255, choices=COUNTRY)
    user_agreement = models.BooleanField(default=False)

    class Meta:
        db_table = "web_data"
        ordering = ["-id"]

    def __str__(self):
        return self.first_name
