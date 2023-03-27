import datetime

from django.forms import ModelForm, CharField, TextInput, DateField, DateInput, Select, ModelMultipleChoiceField, SelectMultiple
from .models import Author, Quote, Tag


class AuthorForm(ModelForm):
    fullname = CharField(widget=TextInput(attrs={"class": "form-control"}))
    born_date = DateField(initial=datetime.date.today, widget=DateInput(attrs={"class": "form-control", "type": "date"}))
    born_location = CharField(widget=TextInput(attrs={"class": "form-control"}))
    description = CharField(widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Author
        fields = "__all__"


class QuoteForm(ModelForm):
    tags = ModelMultipleChoiceField(widget=SelectMultiple(attrs={"class": "form-control"}), queryset=Tag.objects.all())
    author = Select(attrs={"class": "form-control"}, choices=Author.objects.all())
    quote = CharField(widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Quote
        fields = "__all__"