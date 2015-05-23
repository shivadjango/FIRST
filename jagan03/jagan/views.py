from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext



def about(request):
    context = RequestContext(request)

    return render_to_response('jagan/test16.html',context)
# Create your views here.

def timeline(request):
    context = RequestContext(request)

    return render_to_response('jagan/timeline.html',context)

def handler404(request):
    return render(request, "404.html")

