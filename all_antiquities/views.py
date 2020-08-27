from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Antiquity, Category, Period
from .forms import AntiquityForm


def all_antiquities(request):
    """ A view for all antiquities, includes sorting and searching. """

    antiquities = Antiquity.objects.all()
    categories = Category.objects.all()
    periods = Period.objects.all()
    query = None
    # categories = None
    sort = None
    direction = None
    # import pdb; pdb.set_trace()

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                antiquities = antiquities.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            antiquities = antiquities.order_by(sortkey)

        if 'category' in request.GET:
            get_categories = request.GET['category'].split(',')
            antiquities = antiquities.filter(category__name__in=get_categories)
            categories = Category.objects.filter(name__in=get_categories)

        if 'period' in request.GET:
            get_periods = request.GET['period'].split(',')
            print(periods)
            antiquities = [antiquity for antiquity in antiquities if antiquity.period == get_periods[0]]
            periods = Period.objects.filter(name__in=get_periods)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter your search parameters.")
                return redirect(reverse('all_antiquities'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(period__icontains=query) | Q(culture__icontains=query)
            antiquities = antiquities.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'antiquities': antiquities,
        'categories': categories,
        'periods': periods,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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


def add_antiquity(request):
    """ Add an Antiquity to the site """
    if request.method == 'POST':
        form = AntiquityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You successfully added the antiquity to site.')
            return redirect(reverse('add_antiquity'))
        else:
            messages.error(request, 'Failed to add antiquity. Please ensure the form is valid.')
    else:
        form = AntiquityForm()
        
    template = 'all_antiquities/add_antiquity.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
