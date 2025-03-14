from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriptionForm
from .models import Subscriber, Newsletter

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for subscribing!')
            return redirect('home')  # Replace 'home' with your desired redirect URL
    else:
        form = SubscriptionForm()
    return render(request, 'newsletter/subscribe.html', {'form': form})

def newsletter_list(request):
    newsletters = Newsletter.objects.all().order_by('-created_on')
    return render(request, 'newsletter/newsletter_list.html', {'newsletters': newsletters})