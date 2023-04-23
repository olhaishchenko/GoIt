import os

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import AuthorForm, QuoteForm
from .models import Author, Quote, Tag


# Create your views here.
def main(request):
    return render(request, 'app_my_site/index.html', context={"title": "AUTHOR_QUOTE", "quotes": Quote.objects.all(), "tags": Tag.objects.all()})


@login_required
def upload_author(request):
    if request.method == "POST":
        author = AuthorForm(request.POST)
        if author.is_valid():
            author.save()
            return redirect(to='app_my_site:root')
        else:
            return render(request, 'app_my_site/upload_author.html', context={"title": "AUTHOR_QUOTE", "form": author})

    return render(request, 'app_my_site/upload_author.html', context={"title": "AUTHOR_QUOTE", "form": AuthorForm()})


def upload_quote(request):
    if request.method == "POST":
        quote = QuoteForm(request.POST)
        if quote.is_valid():
            quote.save()
            return redirect(to='app_my_site:root')
        else:
            return render(request, 'app_my_site/upload_quote.html', context={"title": "AUTHOR_QUOTE", "form": quote})

    return render(request, 'app_my_site/upload_quote.html', context={"title": "AUTHOR_QUOTE", "form": QuoteForm()})


def authors_descr(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'app_my_site/authors_descr.html', context={"title": "AUTHOR_DESCRIPTION", "author": author})
