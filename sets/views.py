from django.shortcuts import redirect, render

from .forms import SetForm, CardForm
from .models import Set, Flashcard
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    sets = Set.objects.all()
    return render(request, "home.html", {'sets': sets})


@login_required
def set_create(request):
    context = {}
    form = SetForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("/sets")

    context['form'] = form
    return render(request, 'set_create.html', context)


@login_required
def flashcard_list(request, flashcard_id):
    if request.method == 'POST':
        flashcard = Flashcard()

        flashcard.front = request.POST.get('front')
        flashcard.back = request.POST.get('back')
        flashcard.set = Set.objects.get(id=flashcard_id)

        flashcard.save()

    context = {
        'set': Set.objects.prefetch_related('flashcard_set').get(id=flashcard_id)
    }

    return render(request, 'flashcard_list.html', context)


@login_required
def flashcard_delete(request, flashcard_id):
    card = Flashcard.objects.get(id=flashcard_id)
    set_id = card.set.id
    flash = Flashcard.objects.filter(id=flashcard_id)

    if request.method == "POST":
        flash.delete()
        return redirect("/sets")

    return render(request, "set_delete.html")


@login_required
def learn(request, learn_id):
    context = {
        'set': Set.objects.prefetch_related('flashcard_set').get(id=learn_id)
    }
    return render(request, 'learn.html', context)
