from django.forms import ModelForm
from .models import Book,Transaction


class ItemForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        exclude =["id"]


