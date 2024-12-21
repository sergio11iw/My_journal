from django.shortcuts import render
from django.http import HttpResponse
from .models import Note




def main(request):
    notes = Note.objects.all()
    return render(request, 'main.html', {'notes': notes})

def about(request):
    return HttpResponse('<h2>Вторая страница</h2>')

# def produkts(request):
#     produkts = Produkt.objects.all()
#     produkts = Produkt.objects.filter(price__gt=100) # фильтр больше 100
#     produkts = Produkt.objects.filter(price__lt=100)  # фильтр меньше 100
#     produkts = Produkt.objects.filter(name="Апельсин")
#     # produkts = [{'id': 1, 'name': 'banana', 'price': 100},
#     #             {'id': 2, 'name': 'apple', 'price': 200}
#     #             ]
#     return render(request, 'produkts.html', {'produkts': produkts})
