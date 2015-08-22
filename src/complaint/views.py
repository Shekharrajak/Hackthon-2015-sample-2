from django.shortcuts import render,render_to_response,RequestContext,HttpResponseRedirect
# Create your views here.
#from django.contrib import message
from .complaint_form import ComplaintForm
def complaint(request):
	form = ComplaintForm(request.POST or None)

	if form.is_valid():
		save_it =form.save(commit=False)
		save_it.save()
		#messages.success(request,'complaint Submitted !')
		return HttpResponseRedirect('/Complaint_registered/')
	return render_to_response("complaint.html",
								locals(),
								context_instance=RequestContext(request))

def Complaint_registered(request):
	
	return render_to_response("Submitted.html",
								locals(),
								context_instance=RequestContext(request))
