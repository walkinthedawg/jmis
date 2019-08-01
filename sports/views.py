from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Sport
from .forms import SportForm

# Create your views here.
def index(request):
    """ A view to display the index page """
    return render(request, 'index.html')
    
def about(request):
    """ A view to display the index page """
    return render(request, 'about.html')
    
def sports(request):
    """
    Create a view that will return a list
    of Sports and render them to the 'sports.html' template
    """
    sports = Sport.objects.order_by('name')
    return render(request, "sports.html", {'sports': sports})

def get_sports(request):
    """
    Create a view that will return a list
    of Sports and render them to the 'sports.html' template
    """
    sports = Sport.objects.order_by('name')
    return render(request, "sports.html", {'sports': sports})


def sport_detail(request, pk):
    """
    Create a view that returns a single
    Sport object based on the sport ID (pk) and
    render it to the 'sportdetail.html' template.
    Or return a 404 error if the sport is
    not found
    """
    sport = get_object_or_404(Sport, pk=pk)
    sport.views += 1
    sport.save()
    return render(request, "sportdetail.html", {'sport': sport})


def create_or_edit_sport(request, pk=None):
    """
    Create a view that allows us to create
    or edit a sport depending if the Sport ID
    is null or not
    """
    sport = get_object_or_404(Sport, pk=pk) if pk else None
    if request.method == "POST":
        form = SportForm(request.POST, request.FILES, instance=sport)
        if form.is_valid():
            sport = form.save()
            return redirect(sport_detail, sport.pk)
    else:
        form = SportForm(instance=sport)
    return render(request, 'sportform.html', {'form': form})
    
    