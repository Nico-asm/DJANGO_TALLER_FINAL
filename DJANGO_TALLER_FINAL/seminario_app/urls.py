from django.urls import path
from . import views 

urlpatterns = [
    ## CRUD ##
    path('', views.index, name='inicio'),
    path('carta/', views.carta, name='carta'),
    path('agregar-participante/', views.agregar_participante, name='agregar_participante'),
    path('lista-participante/', views.lista_participante, name='lista_participante'),
    path('editar-participante/<int:id>', views.editar_participante, name='editar_participante'),
    path('eliminar-participante/<int:id>', views.eliminar_participante, name='eliminar_participante'),

    ## API ##
    path('participante/', views.participanteLista, name='participante'),
    path('participante/<int:pk>', views.participanteDetalle),

    ## FBV ##
    path('institucion/', views.institucionLista, name='institucion'),
    path('institucion/<int:pk>', views.institucionDetalle),

    ## CBV ##
    path('inscritos/', views.InscritosLista.as_view(), name='inscritos'),
    path('inscritos/<int:pk>', views.InscritosDetalle.as_view()),

]
