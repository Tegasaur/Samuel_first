from django.shortcuts import render
from app1.models import accesscodes,creditcard
from app1 import forms
# Create your views here.
def index(request):
    return render(request,'app1/index.html')


def access(request):
    try:
        model=accesscodes.objects.order_by('id')[0]
        if request.GET.get('sub') == 'Click':
            var1=[model]
        else:
            var1=[]
    except:
        var1=[]
    try:
        var1= var1[0].CodeNumber

    except:
        var1="no codes"
    dict={'model':var1}
    print(var1)
    try:
        model.delete()
    except:
        pass
    return render(request,'app1/purchase.html',context=dict)
