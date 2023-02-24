from django.shortcuts import render
from django.core.cache import cache

from .models import Author, Book, Tag
import time

from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_control




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


# Mesure le temps d'exécution d'une requête donnée
def measure_query_time(query):
    start_time = time.time()
    results = list(query)
    end_time = time.time()
    query_time = end_time - start_time
    return results, query_time




@cache_control(private=True, max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def view_test_without_and_with(request):
    
    # clear cache
    cache.clear()
    
    books, without_optimize_time = measure_query_time(Book.objects.all())
    books, with_select_optimize_time = measure_query_time(Book.objects.all().select_related('author'))
    books, with_prefect_optimize_time = measure_query_time(Book.objects.all().prefetch_related('tags'))
    books, with_prefect_and_related_time = measure_query_time(Book.objects.all().select_related('author').prefetch_related('tags'))

 
    
    context = {
        'without_optimize_time': without_optimize_time,
        'with_select_optimize_time': with_select_optimize_time,
        'with_prefetch_optimize_time': with_prefect_optimize_time,
        'with_perfect_and_related_time': with_prefect_and_related_time
    }


    return render(request, 'optimization.html', context)


