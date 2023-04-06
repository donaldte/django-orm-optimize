# Performance de select_related et prefetch_related
Ce projet est un exemple de l'utilisation des méthodes select_related et prefetch_related pour améliorer les performances de votre application Django.

Il comprend trois modèles Author, Book et Tag, où Book est lié à Author via une clé étrangère et à Tag via une relation ManyToMany.

## Installation

Cloner le dépôt :

```

 git clone https://github.com/donaldte/django-orm-optimize.git

```

## Accéder au dossier :

```
cd django-orm-optimize

```

## Installer les dépendances :

```
pip install -r requirements.txt

```

## Exécuter  migrations :

```
python manage.py migrate

```

## Demarer le serveur

```
python manage.py runserver
```

## Generer les donnees:

```
127.0.0.1:8000/generate

```

## Voir le performances:

```
127.0.0.1:8000/performance

```
