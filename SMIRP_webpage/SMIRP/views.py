from django.shortcuts import render
from django.http import HttpResponse
from .forms import PredictionForm


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PredictionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            model = form.cleaned_data['model']
            sequence = form.cleaned_data['sequence']

            return render(request, 'SMIRP/index.html', {
                'form': form
            })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PredictionForm()
    return render(request, 'SMIRP/index.html', {'form': form})