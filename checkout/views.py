from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'You have no items in your bag.')
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JAhPDGzNWLkO7k0ZCCtSnz9AZ6SklbskBAyJm6I91LOyRawQiAwaB1c4mjX4lHDguVESbK990tHfQAk6XWSHB8600Y9nVAKKL',
        'client_secret': 'sk_test_jwzDYqzvH9KtbzrzfH0YKcw',
    }

    return render(request, template, context)