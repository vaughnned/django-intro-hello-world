from django.http import HttpResponse

def home_view(request, *args, **kwargs):
  return HttpResponse("<h1>Hello World</h1>")