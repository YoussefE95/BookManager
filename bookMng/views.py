from django.shortcuts import render
from django.http import HttpResponse
from .models import MainMenu
from .forms import BookForm
from .forms import SearchForm
from .forms import CommentForm
from .forms import MessageForm
from django.http import HttpResponseRedirect
from .models import Book
from .models import Comment
from .models import Message
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


def index(request):
    return render(request, 'bookMng/index.html')


@login_required(login_url=reverse_lazy('login'))
def all_books(request):
    books = Book.objects.all()

    for b in books:
        b.pic_path = b.picture.url[14:]

    return render(request,
            'bookMng/all_books.html',
            {
                'books': books,
            })


@login_required(login_url=reverse_lazy('login'))
def my_books(request):
    books = Book.objects.filter(username=request.user)

    for b in books:
        b.pic_path = b.picture.url[14:]

    return render(request,
            'bookMng/my_books.html',
            {
                'books': books,
            })


@login_required(login_url=reverse_lazy('login'))
def post_book(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/post_book?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,
                'bookMng/post_book.html',
                {
                    'form': form,
                    'submitted': submitted
                })


@login_required(login_url=reverse_lazy('login'))
def search_books(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            books = Book.objects.filter(name__contains=query)

            for b in books:
                b.pic_path = b.picture.url[14:]

            return render(request,
                'bookMng/search_books.html',
                {
                    'books': books,
                    'query': query
                })

    return render(request, 'bookMng/search_books.html')


def about_us(request):
    return render(request, 'bookMng/about_us.html')


@login_required(login_url=reverse_lazy('login'))
def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    book.pic_path = book.picture.url[14:]
    comments = Comment.objects.all()
    submitted = False
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)

        if form.is_valid():
            # form.save()
            comment = form.save(commit=False)
            try:
                comment.username = request.user
            except Exception:
                pass
            comment.save()
            return HttpResponseRedirect(f"/book_details/{book_id}")
    else:
        form = CommentForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
            'bookMng/book_details.html',
            {
                'form': form,
                'item_list': MainMenu.objects.all(),
                'submitted': submitted,
                'book': book,
                'comments': comments,


            })


@login_required(login_url=reverse_lazy('login'))
def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()

    return render(request, 'bookMng/book_delete.html')


def message(request):
    messages = Message.objects.all()
    submitted = False
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)

        if form.is_valid():
            # form.save()
            message = form.save(commit=False)
            try:
                message.username = request.user
            except Exception:
                pass
            message.save()
            return HttpResponseRedirect('/messagebox?submitted=True')
    else:
        form = MessageForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,'bookMng/messagebox.html',
                  {

                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted,
                      'messages': messages,
                  })
