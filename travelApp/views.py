from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import UserRegisterForm,UserLoginForm
from .models import UserRegisterInfo


# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Create and save new contact entry
        Contact.objects.create(name=name, email=email, phone=phone, message=message)

        return render(request,'success_contact.html')

    return render(request, 'contact.html')

def services(request):
    return render(request,'services.html')

def booking(request):
    return render(request,'booking.html')

def user_login(request):
    return render(request,'user_login.html')        

def success_contact(request):
    return render(request,'success_contact.html')

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_contact')  # if error check this
    else:
        form = UserRegisterForm()

    return render(request, 'user_register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            nrc_number = form.cleaned_data['nrc_number']
            
            # Check if user exists in the database
            try:
                user = UserRegisterInfo.objects.get(username=username, nrc_number=nrc_number)
                return render(request, 'home.html', {'user': user})  # Render success page if user is found
            except UserRegisterInfo.DoesNotExist:
                return redirect('user_register')  # Redirect to registration page if user is not found
    else:
        form = UserLoginForm()

    return render(request, 'user_login.html', {'form': form})

