from django.shortcuts import render

# Create your views here.

from .forms import PasteForm
from .models import Paste
from .brain import hash_gen_engine

def create_paste(request):
    form = PasteForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            stuff = form.cleaned_data
            slug = hash_gen_engine()
            new_paste = Paste(title=stuff['title'], author=stuff['author'],
                                content=stuff['content'], language=stuff['language'], slug=slug)
            new_paste.save()
            return render(request, 'paste_service/paste_created.html', {"paste": new_paste, "slug": slug})
    return render(request, 'paste_service/create_paste.html', {"form": form})