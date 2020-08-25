from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty!")
        return redirect(reverse('all_antiquities'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HDWiQG4FS2lVNP2ZjAZuL3La3a4zsL9VwsrPPprns3YiMqaYQ5sV3tUWfhveQvE2p4jLaIYP39EZEoKxPQ3bxdU00Nqx8yy28',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
