from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UserFeedbackForm
from django.core.mail import send_mail


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):

    #Instance=request.user = fills users data into update form fields
    #request.POST = Specifies that the data from form is going to be sent to database
    #u_form.save() = Saves data in the database
    #request.FILES = file data from request(profile picture request)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            # to avoid post-get-redirect pattern 
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }

    return render(request, 'users/profile.html', context=context)

@login_required
def contact(request):

    if request.method == 'POST':
        form = UserFeedbackForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            comments = form.cleaned_data.get('comments')

            #send email

            send_mail(
                username, #subject
                comments, #message
                email, # from email
                ['aschonn.trinity@gmail.com'], # To email
            )

            messages.success(request, f'Your Message Has Been Sent! Look Forward To Talking To You Soon, {username.up}')
            return redirect('contact')
    else:
        form = UserFeedbackForm(instance=request.user)
    return render(request, 'users/contact.html', {'form': form})

