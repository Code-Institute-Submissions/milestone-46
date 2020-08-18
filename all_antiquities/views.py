from django.shortcuts import render
from .models import Antiquity


def all_antiquities(request):
    """ Shows all antiquities and includes sorting and searching. """

    antiquities = Antiquity.objects.all()

    context = {
        'antiquities': antiquities,
    }

    return render(request, 'all_antiquities/all_antiquities.html', context)
