from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .models import Book
# Create your views here.
from django.urls import reverse_lazy

class Home(TemplateView):
    template_name = 'home.html'

def uplode(request):
    context = {}
    if request.method == 'POST' and 'filename' in request.FILES:
        doc = request.FILES #returns a dict-like object
        doc_name = doc['filename']
        fs = FileSystemStorage()
        name = fs.save(doc_name.name,doc_name)
        context['url'] = fs.url(name)
        # print(url)

        # print(doc_name.name)
    return render(request, 'uplode.html',context)

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', context={'books': books})

def delete_book(request, pk):
    if request.method == "POST":
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')

def uplode_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'uplode_book.html', context={'form':form})


class BookListView(ListView):
    model = Book
    template_name = 'class_book_list.html'
    context_object_name = 'books'

class UplodeBookView(CreateView):
    model = Book
    form_class = BookForm
    # fields = {'title', 'author', 'pdf', 'cover'}
    success_url = reverse_lazy('class_book_list')
    template_name = 'uplode_book.html'








    #     fs = FileSystemStorage()
        # name = fs.save(uploded_file.name, uploded_file)
    #     context['url'] = fs.url(name)
    # return render(request, 'uplode.html')

# def book_list(request):
#     book = Book.object.all()

