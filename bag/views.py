from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from all_antiquities.models import Antiquity


def view_bag(request):
    """ This view returns the Cart contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add the specified product to the shopping Cart"""

    antiquity = get_object_or_404(Antiquity, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated quantity of donations to {antiquity.name} (Total: {bag[item_id]})')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {antiquity.name} to your cart')

    request.session['bag'] = bag
    return redirect(redirect_url)



def adjust_bag(request, item_id):
    """Adjust the quantity of the specified item in the Cart"""

    antiquity = get_object_or_404(Antiquity, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated quantity of donations to {antiquity.name} (Total: {bag[item_id]})')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {antiquity.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))



def remove_from_bag(request, item_id):
    """Remove an item from the shopping Cart"""

    try:
        antiquity = get_object_or_404(Antiquity, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {antiquity.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
