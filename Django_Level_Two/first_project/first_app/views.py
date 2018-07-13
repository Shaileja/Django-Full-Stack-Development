from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
from django.views.decorators.cache import cache_page
# Create your views here.

# Our original index view function
# Corresponds to original_index.html (rename it to index.html to use it!)

# def index(request):
#     my_dict = {'insert_me':"Now I am coming from first_app/index.html!"}
#     # Make sure this is pointing to the correct index
#     return render(request,'first_app/index.html',context=my_dict)

@cache_page(60 * 5)
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    webpage_list=Webpage.objects.order_by('url')
    date_dict = {"access_records":webpages_list,"webpage":webpage_list}
    return render(request,'first_app/index.html',date_dict)
