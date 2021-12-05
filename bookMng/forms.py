from django import forms
from django.forms import ModelForm
from .models import Book
from .models import Comment
from .models import Message
from .models import Rate


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
            'b_id',
            'content'
        ]


class RateForm(ModelForm):
    class Meta:
        model = Rate
        fields = [
            'rate',
        ]


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = [
            'name',
            'content'
        ]