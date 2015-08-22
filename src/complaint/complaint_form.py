from django import forms

from .models import complaint

class ComplaintForm(complaint_form.ModelForm):
	class Meta:
		model = complaint
		fields = ['name', 'complaint_type', 'complaint_desc','address','cit','email']


		