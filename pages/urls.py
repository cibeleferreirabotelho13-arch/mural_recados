from django.urls import path

from pages import views

app_name = 'pages'


urlpatterns = [

    path(
        '',
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

    path(
        'cadastro/',
        views.cadastro_view,
        name='cadastro',
    ),

    path(
        'login/',
        views.login_view,
        name='login',
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout',
    ),

    path(
        'meus-recados/',
        views.meus_recados,
        name='meus_recados',
    ),

   
    path(
        'recado/<int:id>/',
        views.detalhes_recado,
        name='detalhes_recado',
    ),

    path(
        'recado/<int:id>/editar/',
        views.editar_recado,
        name='editar_recado',
    ),

  
    path(
        'recado/<int:id>/excluir/',
        views.excluir_recado,
        name='excluir_recado',
    ),
]
