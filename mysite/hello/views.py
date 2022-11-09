# Create your views here.
from django.http import HttpResponse

def helloworld(request):
    response = """<html><body><p>Hello world DJ4E in HTML</p>
    <p>This sample code is available at
    <a href="https://github.com/ciprianfc/django_learning">
    https://github.com/ciprianfc/django_learning</a></p>
    </body></html>"""

    return HttpResponse(response)