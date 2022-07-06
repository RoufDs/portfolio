import email
from django.contrib import messages
from django.core import paginator
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from category.models import Category
from my_web.models import My_website
from django.core.paginator import Paginator
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'index.html')

def resume(request):
    return render(request, 'resume.html')

def portfolio(request):
    category = Category.objects.all()
    my_list = My_website.objects.all().order_by("-pk")

    paginator = Paginator(my_list, 4)
    page_num = request.GET.get('page')
    my_web = paginator.get_page(page_num)
    vars = {
        'categories': category,
        'my_web': my_web
    }

    if request.method == 'POST':
        subject = request.POST.get('subject')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        msg = '''        
            Hello, My name is {} {}
            I want to contact: {}

            From: {}
            '''.format(firstname, lastname, message, email)

        send_mail(subject, msg, '', ['four.3687zero@gmail.com'])
        messages.success(request, "อีเมลถูกส่งแล้ว")
        
        return redirect('/portfolio')

    return render(request, 'port.html', vars)

def my_search(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        res = None
        my_input = request.POST.get("my_input")
        # print(my_input)
        qs = My_website.objects.filter(name__contains=my_input)
        # print(qs)
        if len(my_input) > 0 and len(qs) > 0:
            data = []
            for pos in qs:
                item = {
                    "url": pos.url,
                    "name": pos.name,
                    "image": pos.image.url,
                    "create": pos.create,
                }
                data.append(item)
            res = data
        else:
            res = "No websites found ..."
        return JsonResponse({"data": res})
    return JsonResponse({})