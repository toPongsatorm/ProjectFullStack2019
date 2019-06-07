from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Book,Transaction
from .form import ItemForm
# Create your views here.



def list_item(request):
    context = dict()
    context['Book'] = Book.objects.all().order_by('Book')
    return render(request,'listitem.html',context)






@login_required
def auth_page(request):
    return render(request, 'auth_page.html')

def home(request):
    context = dict()

    if request.user.is_authenticated:
        context['greeting'] = 'Welcome Back {}'.format(request.user)
    else:
        context['greeting'] = 'Welcome Anonymous'

    return render(request, 'home.html', context)

@login_required
def logoutView(request):
    logout(request)
    return redirect('home')

def sent(request,pks):
        if request.method =='POST':
                try:
                    book = Book.objects.get(pk=pks)
                    status = int(request.POST['amount'])
                    book.status -1
                    book.save()
                    Transaction.objects.create(
                            book=book,
                            status=status,                
                    )
                    return redirect('list_item')
                except Exception as e:
                        print(e)
                        return e
        else:
                book =Book.objects.get(pk=pks)
                context = {'book':book}
                return render(request,'sent.html',context)