from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import CustomerProfileMultiForm, FreelancerProfileMultiForm


User = get_user_model()


class FreelancerSignUp(CreateView):
    form_class = FreelancerProfileMultiForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html' 

    def form_valid(self, form):

        user = form['user'].save(commit=False)
        user.role = 'freelancer'
        user.save()
        profile = form['profile'].save(commit=False)
        profile.user = user
        profile.save()

        return redirect(self.success_url)


class CustomerSignUp(CreateView):
    form_class = CustomerProfileMultiForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html' 

    def form_valid(self, form):

        user = form['user'].save(commit=False)
        user.role = 'customer'
        user.save()
        profile = form['profile'].save(commit=False)
        profile.user = user
        profile.save()

        return redirect(self.success_url)


@login_required
def my_profile(request):
    template = 'users/profile_card.html'
    return render(request, template)


@login_required
def users_profile(request, username):
    template = 'users/profile_card.html'
    user = get_object_or_404(User, username=username)

    context = {
        'user' : user,
    }
    return render(request, template, context)
