import requests
from django.shortcuts import render
from .models import CustomArticle

def homepage(request):
    # Your NewsAPI key and endpoint
    api_key = 'd1864738d85844b18033e0ad7d818ff5'  # replace with your actual API key
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'

    # Fetch news from the API
    response = requests.get(url)
    print(response.json())  # This will show the JSON response in your console

    api_articles = response.json().get('articles', []) if response.status_code == 200 else []

    # Fetch custom articles from the database
    custom_articles = CustomArticle.objects.all()

    # Combine API news and custom articles
    context = {
        'api_articles': api_articles,
        'custom_articles': custom_articles,
    }
    return render(request, 'news/homepage.html', context)
