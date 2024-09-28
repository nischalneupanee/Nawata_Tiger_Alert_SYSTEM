from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from handling_model.models import detected_database

def index_page(request):
    return render(request,'index.html')


def map_page(request):
    return render(request,'map.html')

def about_page(request):
    return render(request,'about.html')
def login_view(request):
    if request.method =="POST":
        contact=request.POST.get('contact')
        password=request.POST.get('password')
        print(contact,password)
        user=authenticate(request,Contact_no=contact,password=password)
        if user is not None:
            login(request,user)
            return redirect('accounts:dashboard')
        else:
            print("something is wrong")






    return render(request,'accounts/login.html')


def logged_in_dashboard(request):
    return render(request,'accounts/logged_dashboard.html')

def register_view(request):
    if request.method=="POST":
        print("CAME HEREEEEEEEEEEEEEEEEEEee")
        name=request.POST.get('name')
        contact=request.POST.get('contactNo')
        occupation=request.POST.get('occupation')
        identity_proof=request.FILES.get('identity')
        reason_for_access=request.POST.get('reason')
        password=request.POST.get('password')

        print(name,contact,occupation,identity_proof,reason_for_access)

        CustomUser.objects.create_user(Name=name,Contact_no=contact,password=password, occupation=occupation,identity=identity_proof,Reason_for_membership=reason_for_access)
        return HttpResponse("submitted successfully")






    return render(request,
                  'accounts/Register_form.html')


def verification_page(request):

    users=CustomUser.objects.all()

    return render(request, 'accounts/user_verification.html',{"members":users})


from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import CustomUser


def verify_user(request, id):
    # Use get_object_or_404 to handle user not found
    user = get_object_or_404(CustomUser, id=id)

    # Verify if the user is already verified
    if user.verified:
        return HttpResponse("User is already verified.")

    # Verify the user
    user.verified = True
    user.save()

    return HttpResponse("User verified successfully!")

