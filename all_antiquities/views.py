from django.shortcuts import render, redirect, reverse, get_object_or_404


from .models import Antiquity, Category, Period


def all_antiquities(request):
    """ A view for all antiquities, includes sorting and searching. """

    antiquities = Antiquity.objects.all()
    categories = Category.objects.all()
    periods = Period.objects.all()

    context = {
        'antiquities': antiquities,
        'categories': categories,
        'periods': periods,
    }

    return render(request, 'all_antiquities/all_antiquities.html', context)


def single_antiquity(request, antiquity_id):
    """ A view to show details for a single antiquity. """

    antiquity = get_object_or_404(Antiquity, pk=antiquity_id)
    categories = Category.objects.all()
    periods = Period.objects.all()

    context = {
        'antiquity': antiquity,
        'categories': categories,
        'periods': periods,
    }

    return render(request, 'all_antiquities/single_antiquity.html', context)
