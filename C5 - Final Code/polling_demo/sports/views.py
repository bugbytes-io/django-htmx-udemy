from django.shortcuts import render
from sports.models import Fixture
import time

# Create your views here.
def fixtures(request):
    fixtures = Fixture.objects.all()
    context = {'fixtures': fixtures}
    if request.htmx:
        time.sleep(2)
        return render(request, 'sports/fixtures.html#fixture-block', context)
    return render(request, 'sports/fixtures.html', context)