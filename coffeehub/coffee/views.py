from django.template import loader
from django.http import HttpResponse
from.models import Coffee
# Create your views here.

def home(request):
    CoffeeStore = Coffee.objects.all()
    template = loader.get_template('home.html')
    context = {
        'CoffeeStore' : CoffeeStore,
    }
    return HttpResponse(template.render(context, request))