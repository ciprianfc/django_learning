from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from form.forms import BasicForm, CatForm
from form.models import Cat
import html

# Create your views here.
def example(request):
    form = BasicForm()
    return HttpResponse(form.as_table())

# Call ass dumpdata ('GET', request.GET)
def dumpdata(place, data):
    retval = ""
    if len(data) > 0:
        retval += f'<p>Incoming {place} data:<br/>\n'
        for key, value in data.items():
            retval += f'{html.escape(key)} = {html.escape(value)}</br>\n'
        retval += '</p>\n'
    
    return retval

class DumpPostView(View): #reusable bit...
    def post(self, request):
        dump = dumpdata('POST', request.POST)
        cntx = {'title' : 'request.POST', 'dump': dump}
        return render(request, 'form/dump.html', cntx)

class SimpleCreate(DumpPostView):
    def get(self, request):
        form = BasicForm()
        cntx = {'form' : form}
        return render(request,'form/form.html', cntx)

class SimpleUpdate(DumpPostView):
    def get(self, request):
        old_data = {
            'title' : 'Skoda',
            'mileage' : 42,
            'purchase_date' : '2019-08-14'
        }
        form = BasicForm(old_data)
        cntx = {'form' : form}
        return render(request,'form/form.html', cntx)

class Validate(DumpPostView):
    def get(self, request):
        old_data = {
            'title' : 'Skoda',
            'mileage' : 42,
            'purchase_date' : '2019-08-14'
        }
        form = BasicForm(initial=old_data)
        cntx = {'form' : form}
        return render(request,'form/form.html', cntx)
    
    def post(self, request):
        form = BasicForm(request.POST)
        if not form.is_valid():
            cntx = {'form' : form}
            return render(request, 'form/form.html', cntx)
        x = reverse('form:success')
        return redirect(x)

def success(request):
    return HttpResponse('Thank you!!!')

class CatCreate(View):
    def get(self, request):
        form = CatForm()
        cntx = {'form' :form}
        return render(request, 'form/form.html',cntx)
    
    def post(self,request):
        form = CatForm(request.POST)
        if not form.is_valid():
            cntx = {'form' : form}
            return render(request, 'form/form.html', cntx)
        
        #save form and get a model object
        newcat = form.save()
        x = reverse('form:main') + '#' + str(newcat.id)
        return redirect(x)

class CatUpdate(View):
    def get(self, request, pk):
        oldcat = get_object_or_404(Cat,pk = pk)
        form = CatForm(instance=oldcat)
        cntx = {'form' : form}
        return render(request, 'form/form.html', cntx)
    
    def post(self,request, pk):
        oldcat = get_object_or_404(Cat, pk = pk)
        form = CatForm(request.POST, instance=oldcat)
        if not form.is_valid() :
            cntx = {'form' : form}
            return render(request,'form/form.html',cntx)
        
        editcat= form.save()
        x = reverse('form:main')
        return redirect(x)

# References

# https://stackoverflow.com/questions/383944/what-is-a-python-equivalent-of-phps-var-dump