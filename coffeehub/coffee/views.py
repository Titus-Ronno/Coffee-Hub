from django.contrib.auth.decorators import login_required
from django.template import loader
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import JsonResponse
from.models import Coffee, Card, Reply, Gallery, TrainingSession, Event
from .forms import ReplyForm
from django.contrib import messages
from .forms import TrainingSessionForm
from django.core.mail import send_mail
from datetime import date
# Create your views here.

def check_authentication(request):
    # Implement your authentication logic here
    authenticated = request.user.is_authenticated
    return JsonResponse({'authenticated': authenticated})

@login_required
def cart(request):
    CoffeeStore = Coffee.objects.all()
    template = loader.get_template('cart.html')
    context = {
        'CoffeeStore' : CoffeeStore,
    }
    return HttpResponse(template.render(context, request))
def landing_page(request):
    template = loader.get_template('landing_page.html')
    return HttpResponse(template.render())
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def card_view(request):
    cards = Card.objects.all()
    template = loader.get_template('card.html')
    context = {
        'cards' : cards,
    }
    return HttpResponse(template.render(context, request))

def submit_reply(request):
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            form.save()            
            return render(request, 'submit-reply.html', {'form': form})  # Redirect to a success page or back to the form
    else:
        form = ReplyForm()
    return render(request, 'submit-reply.html', {'form': form})

def image_view(request):
    images = Gallery.objects.all()
    template = loader.get_template('gallery.html')
    context = {
        'images': images
    }
    return HttpResponse(template.render(context, request))

def rewards(request):
    return render(request, 'rewards.html')

def events(request):
    today = date.today()
    events = Event.objects.filter(date__gte=today)
    return render(request, 'events.html', {'events':events })

def about(request):
    return render(request, 'about.html')


#def schedule_training(request):
    #if request.method == 'POST' and request.is_ajax():
        #coffee_id = request.POST.get('coffee_id')
        # Logic to schedule training for the coffee with the given ID
        # Replace this with your actual logic to schedule training
        # For demonstration, let's just return a success response
        #return JsonResponse({'status': 'success', 'coffee_id': coffee_id})
   # else:
        # Handle invalid requests or methods
       # return JsonResponse({'status': 'error', 'message': 'Invalid request'})

# views.py


def schedule_training(request):
    if request.method == 'POST':
        form = TrainingSessionForm(request.POST)
        if form.is_valid():
            training_session = form.save(commit=False)
            training_session.user = request.user
            training_session.save()

            # Send notification to the user
            send_training_notification(training_session)

            messages.success(request, 'Training session scheduled successfully!')
            return redirect('schedule_success')
    else:
        form = TrainingSessionForm()
    return render(request, 'schedule_training.html', {'form': form})

def send_training_notification(training_session):
    # Example: Send email notification to the user
    subject = 'Training Session Scheduled'
    message = f"Your training session on {training_session.date} has been scheduled successfully."
    recipient = training_session.user.email
    send_mail(subject, message, 'coffeehub@gmail.com', [recipient])

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

