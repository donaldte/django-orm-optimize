from django.shortcuts import render
from django.core.cache import cache

from .models import Author, Book, Tag
import time

from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_control

from django.conf import settings


from faker import Faker
from .models import Author, Book, Tag

def generate_random_data(request):
    fake = Faker()

    # Générer des données pour le modèle Author
    for i in range(100):
        name = fake.name()
        author = Author(name=name)
        author.save()

    # Générer des données pour le modèle Tag
    for i in range(100):
        name = fake.word()
        tag = Tag(name=name)
        tag.save()

    # Générer des données pour le modèle Book
    for i in range(200):
        title = fake.sentence(nb_words=3, variable_nb_words=True)
        author = Author.objects.order_by('?').first()
        tags = Tag.objects.order_by('?')[:fake.random_int(min=1, max=5)]
        book = Book(title=title, author=author)
        book.save()
        book.tags.set(tags)

    return render(request, 'random_data.html')


# Mesure le temps d'exécution  requête donnée
def measure_query_time(query, sub_querry_1=None, sub_querry_2=None):
    
    start_time = time.time()
    
    books = query
    if sub_querry_1=='YES': authorS = [book.author for book in books]
    if sub_querry_2=='YES': tags = [book.tags.all() for book in books ]
    
    end_time = time.time()
    
    query_time = end_time - start_time
    
    return  query_time



@cache_control(private=True, max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def view_test_without_and_with(request):
    
    # clear cache
    cache.clear()
    
    without_optimize_time = measure_query_time(query=Book.objects.all(), sub_querry_1='YES', sub_querry_2='YES')
    with_select_optimize_time = measure_query_time(query=Book.objects.all().select_related('author'), sub_querry_2='YES')
    with_prefect_optimize_time = measure_query_time(query=Book.objects.all().prefetch_related('tags'), sub_querry_1='YES')
    with_prefect_and_related_time = measure_query_time(query=Book.objects.all().select_related('author').prefetch_related('tags'))

 
    
    context = {
        'without_optimize_time': without_optimize_time,
        'with_select_optimize_time': with_select_optimize_time,
        'with_prefetch_optimize_time': with_prefect_optimize_time,
        'with_perfect_and_related_time': with_prefect_and_related_time
    }


    return render(request, 'optimization.html', context)


def mainpage(request, *args, **kwargs):

    api_key = settings.API_KEY_PAYMENT
    context = {
        'api_key': api_key
    }
    return render(request, 'main.html', context)