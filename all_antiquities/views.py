from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Antiquity, Category, Period


def all_antiquities(request):
    """ A view for all antiquities, includes sorting and searching. """

    antiquities = Antiquity.objects.all()
    categories = Category.objects.all()
    periods = Period.objects.all()
    query = None
    # categories = None

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category']
            print(antiquities
            antiquities = antiquities.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter your search parameters.")
                return redirect(reverse('all_antiquities'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(period__icontains=query) | Q(culture__icontains=query)
            antiquities = antiquities.filter(queries)

    context = {
        'antiquities': antiquities,
        'categories': categories,
        'periods': periods,
        'search_term': query,
        'current_categories': categories,
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
