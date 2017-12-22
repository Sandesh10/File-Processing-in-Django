from django.db import models
from django.forms import ModelForm

# Create your models here.

class Document(models.Model):
    docfile = models.FileField(upload_to='documents')

#FileUpload form class
class UploadForm(ModelForm):
    class Meta:
        model = Document
        fields =('docfile',)
	
