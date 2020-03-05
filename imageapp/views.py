from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import profile

# Create your views here.
def home(request):
    all_upload = profile.objects.all()
    return render(request,'home.html',{'uploads':all_upload})
def normalupload(request):
    if request.method =='POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        url = fs.url(filename)
        new_profile = profile(
            name = request.POST['name'],
            age = request.POST['age'],
            image = url
        )
        new_profile.save()
        return redirect('/home/')
    else:
        return redirect('/home/')