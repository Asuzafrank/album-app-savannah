from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import DetailView
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm,ProfileUpdateForm,UserUpdateform
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
         form = UserRegisterForm(request.POST)
         if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!. login now!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})
    
@login_required
def profile(request):
    if request.method == 'POST':
        
        u_form=UserUpdateform(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account has been updated successfully.')
            return redirect('profile')
    else:
        u_form=UserUpdateform(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)

    context={"u_form":u_form, "p_form":p_form}
    return render(request, 'users/profile.html',context)

class UserDetailView(DetailView):
    model = User
    template_name = 'users/show_profile.html'
    context_object_name = 'user'
