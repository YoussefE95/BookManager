from django import forms
from django.forms import ModelForm
from .models import Book
from .models import Comment
from .models import Message


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'web',
            'price',
            'picture',
        ]


class SearchForm(forms.Form):
    query = forms.CharField(label='query', max_length=100)

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'name',
            'email',
            'comment',
        ]

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = [
            'name',
            'message',
        ]