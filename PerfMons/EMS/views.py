from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django import forms

# Create your views here.

class EmsCollectorForm(forms.Form):
    collector = forms.CharField(label="Collector", required=False)

#class EmsDatesForm(forms.Form):
    fromdate = forms.CharField(label="From", required=False)
    todate = forms.CharField(label="To", required=False)

#class EmsCheckBoxesForm(forms.Form):
    critical = forms.BooleanField(label = "Critica", required=False, initial=True)
    error = forms.BooleanField(label = "Error", required=False, initial=True)
    warning = forms.BooleanField(label = "Warning", required=False, initial=True)
    info = forms.BooleanField(label = "Info", required=False, initial=True)
    

def index(request):
    if request.method =="POST":
        collform = EmsCollectorForm(request.POST)
 #       datesform = EmsDatesForm(request.POST)
 #       cbform = EmsCheckBoxesForm(request.POST)
        if collform.is_valid():
            Coll = collform.cleaned_data["collector"]
            From = collform.cleaned_data["fromdate"]
            To = collform.cleaned_data["todate"]
            ShowCritical = collform.cleaned_data["critical"]
            ShowError = collform.cleaned_data["error"]
            ShowWarning = collform.cleaned_data["warning"]
            Showinfo = collform.cleaned_data["info"]
            


 #       if datesform.is_valid():
 #           EmsDatesForm.cleaned_data
 #       if cbform.is_valid:
 #           EmsCheckBoxesForm.cleaned_data

 #       collector = request.POST["collector"]
 #       From = request.POST["fromdate"]
 #       To = request.POST["todate"]
#
#        ShowError = request.POST["error"]
#        ShowWarning = request.POST["warning"]
#        ShowInfo = request.POST["info"]
#  


 #       return HttpResponseRedirect("")
        pass
    if request.method=="GET":
#        return render(request, "ems/index.html", {
#            "Collector": collector,
#            "From": fromdate,
#            "To": todate
#        })

 #       return render(request, "ems/index.html") 
        return render(request, "ems/index.html",{
#            "formCollector":EmsCollectorForm(),
#            "formDates":EmsDatesForm(),
#            "formCheckBoxes":EmsCheckBoxesForm()     
            "formCollector":EmsCollectorForm()
        })

