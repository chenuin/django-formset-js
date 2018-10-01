from django.shortcuts import render
from django import forms
from .models import Member
from django.forms import modelformset_factory
from djangoformsetjs.utils import formset_media_js
from django.contrib import messages

# Create your views here.
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
    class Media:
        js = formset_media_js

MyFormSet = modelformset_factory(Member, form=MemberForm, can_delete = True)

def index(request):
    if request.method == 'POST':
        formset = MyFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Profile details updated.')
    data = Member.objects.all()
    return render(request, 'index.html', {'formset': MyFormSet, 'data': data})
