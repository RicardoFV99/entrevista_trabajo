from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('lista-usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('lista-logs/', views.lista_logs, name='lista_logs'),
    path('lista-publicaciones/<int:id>', views.lista_publicaciones, name='lista_publicaciones'),
    path('lista-albumes/<int:id>', views.lista_albumes, name='lista_albumes'),
    path('album/ver_fotos/<int:id>', views.ver_fotos, name='ver_fotos'),
]