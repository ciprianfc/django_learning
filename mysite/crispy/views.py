from pyexpat.errors import messages
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from crispy.froms import BasicForm
from django.urls import reverse
from django.contrib import messages

# Create your views here.


class MyView(View):
    template_name = None  # we will overrite in urls.py

    def get(self, request):
        old_data = {
            'title': 'Scotet',
            'mileage': 52000,
            'purchase_Date': '2018-08-14'
        }

        form = BasicForm(initial=old_data)
        cntx = {'form': form}
        return render(request, self.template_name, cntx)

    def post(self, request):
        form = BasicForm(request.POST)

        if not form.is_valid():
            cntx = {'form':form}
            return render(request, self.template_name, cntx)

        messages.add_message(request, messages.SUCCESS, 'Data saved.')
        return redirect(reverse('crispy:main'))