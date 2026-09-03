from django.urls import path

from pages import views

app_name = 'pages'


urlpatterns = [
    path('', 
         views.index, 
         name='index'
    ),

    path(
        'mensagens/',
        views.mensagens,
        name='mensagens',
    ),

      path(
            'lista/',
            views.lista,
            name='lista',
        ),

]