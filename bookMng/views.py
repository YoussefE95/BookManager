from django.shortcuts import render
from django.http import HttpResponse
from .models import MainMenu
from .forms import BookForm
from django.http import HttpResponseRedirect
from .models import Book
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
    return render(request, 
                'bookMng/index.html',
                {
                    'item_list': MainMenu.objects.all()
                })


@login_required(login_url=reverse_lazy('login'))
def all_books(request):
    books = Book.objects.all()

    for b in books:
        b.pic_path = b.picture.url[14:]

    return render(request,
            'bookMng/all_books.html',
            {
                'item_list': MainMenu.objects.all(),
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
                'item_list': MainMenu.objects.all(),
                'books': books,
            })


@login_required(login_url=reverse_lazy('login'))
def post_book(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
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
                    'item_list': MainMenu.objects.all(),
                    'submitted': submitted
                })


@login_required(login_url=reverse_lazy('login'))
def about_us(request):
    return render(request, 'bookMng/about_us.html')


@login_required(login_url=reverse_lazy('login'))
def book_details(request, book_id):
    book = Book.objects.get(id=book_id)

    book.pic_path = book.picture.url[14:]
    return render(request,
            'bookMng/book_details.html',
            {
                'item_list': MainMenu.objects.all(),
                'book': book,
            })


@login_required(login_url=reverse_lazy('login'))
def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()

    return render(request,
            'bookMng/book_delete.html',
            {
                'item_list': MainMenu.objects.all(),
            })