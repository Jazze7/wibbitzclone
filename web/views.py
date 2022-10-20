import json
from multiprocessing import context

from urllib import response
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from more_itertools import first
from web.admin import ContactAdmin

from web.models import Contact, Creator, Subscribe, Feature, Videoblog, Testimonial, Product, Blog
from web.forms import ContactForm


# Create your views here.


def index(request):
    creator = Creator.objects.all()
    latest_creator = Creator.objects.all()[:4]
    feature = Feature.objects.all()
    videoblog = Videoblog.objects.all()
    testimonial = Testimonial.objects.filter(isfeatured=True)[:2]
    product = Product.objects.all()
    blog = Blog.objects.all()
    form = ContactForm()
    context = {
        "creators": creator,
        "features": feature,
        "videoblogs": videoblog,
        "testimonials": testimonial,
        "products": product,
        "blogs": blog,
        "form": form,
        "latest_creators":latest_creator,
    }
    return render(request, "index.html", context=context)


def subscribe(request):
    email = request.POST.get('email')

    if email:
        if not Subscribe.objects.filter(email=email).exists():
            Subscribe.objects.create(
                email=email
            )

            response_data = {
                "status": "success",
                "title": "Well done",
                "message": "You have been Subscribed successfully"
            }
        else:
            response_data = {
                "status": "error",
                "title": "Already Subscribed",
                "message": "You are already a Member. No need to register again.",
            }
    else:
        response_data = {
            "status": "warning",
            "title": "Oops!",
            "message": "Please fill the field",
        }

    # return redirect(reverse("web:index"))
    return HttpResponse(json.dumps(response_data), content_type="application/javascript")


def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        response_data = {
            "status": "success",
            "title": "Well done",
            "message": "You have been Subscribed successfully"
        }
    else:
        response_data = {
            "status": "error",
            "title": "Already Subscribed",
            "message": "You are already a Member. No need to register again.",
        }

    # return redirect(reverse("web:index"))
    return HttpResponse(json.dumps(response_data), content_type="application/javascript")
