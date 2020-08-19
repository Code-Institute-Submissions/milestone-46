from django.shortcuts import render


def latest_options(request):
    """ This view returns the Latest Options page """

    return render(request, 'latest_options/latest_options.html')
