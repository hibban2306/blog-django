from django.shortcuts import render,redirect

# Create your views here.
from .models import RegBrg

def hapus(req, id):
    dt = RegBrg.objects.get(id=id)
    dt.delete()
    return redirect('/market/')