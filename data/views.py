from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Document,UploadForm
from .forms import DocumentForm
import ntpath
import os
import pandas as pd
import numpy as np

def home(request):
    if request.method=="POST":
        form = UploadForm(request.POST, request.FILES)
        ##print(request.FILES.get('docfile'))
        if form.is_valid():  
            form.save()
            path = os.getcwd()+os.sep+'media'+os.sep+'documents'+os.sep+str(request.FILES.get('docfile'))
            f = open(path)
            return HttpResponseRedirect(reverse('fileupload'))  
    else:
        form=UploadForm()

    docs=Document.objects.all()
    
    files = list()
    for file in docs:
        p = dict()
        p['name'] = ntpath.basename(file.__dict__['docfile'])
        files.append(p)
    return render(request,'home.html',{'form':form,'docfiles':files})
