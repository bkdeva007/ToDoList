from django import forms
from .models import List
#from .forms import ListForm
from django.contrib import messages

class ListForm(forms.ModelForm):
	class Meta:
		model=List
		fields=["item","completed"]