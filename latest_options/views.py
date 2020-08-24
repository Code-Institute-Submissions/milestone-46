from django.shortcuts import render

from .models import Latest_option


def latest_options(request):
    """ This view returns the Latest Options page """

    latest_options = Latest_option.objects.all()

    context = {
        'latest_options': latest_options,
    }

    return render(request, 'latest_options/latest_options.html', context)
