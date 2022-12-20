from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from seminario_app.form import formParticipante
from .models import Inscritos, Institucion

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from . serializers import ParticipanteSerializer, InstitucionSerializer

from rest_framework.views import APIView
from django.http import Http404

from django.contrib import messages

# Create your views here.

####### Pagina de inicio ########
def index(request):
    return render(request, 'Paginas/index.html')

def carta(request):
    return render(request, 'Paginas/carta.html')

######## CRUD #########
def agregar_participante(request):
    data = {'form': formParticipante}
    if request.method == 'POST':
        formulario = formParticipante(data=request.POST)
        if formulario.is_valid():  
            formulario.save()
            return redirect('/lista-participante')
        data['form'] = formulario
    return render(request, 'CRUD/agregar_participante.html', data)

def lista_participante(request):
    participante = Inscritos.objects.all()
    data = {'participante' : participante}
    return render(request ,'CRUD/lista_participante.html', data)

def editar_participante(request, id):
    participante = get_object_or_404(Inscritos, id = id)
    data = {'form': formParticipante(instance = participante)}
    if request.method == 'POST':
        formulario = formParticipante(data=request.POST, instance = participante)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡Modificado correctamente!")
            return redirect('/lista-participante')         
        data["form"] = formulario
    return render(request, 'CRUD/agregar_participante.html', data)

def eliminar_participante(request, id):
    participante = get_object_or_404(Inscritos, id = id)
    participante.delete()
    return redirect('/lista-participante')


######### API #########
def participanteLista(request):
    participante = Inscritos.objects.all()
    data = {'participante': list(participante.values(
        'id',
        'nombre',
        'telefono',
        'institucion',
        'fechaInscripcion',
        'horaInscripcion',
        'estado',
        'observacion'
        ))}
    return JsonResponse(data)



@api_view(['GET'])
def participanteDetalle(request, pk):
    try: 
        participante = Inscritos.objects.get(id = pk)
    except Inscritos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serial = ParticipanteSerializer(participante)
        return Response(serial.data)


########## FBV ###########
@api_view (['GET', 'POST'])
def institucionLista(request):
    if request.method == 'GET':
        institucion = Institucion.objects.all()
        serial = InstitucionSerializer(institucion, many=True)
        return Response(serial.data)

    if request.method == 'POST':
        serial = InstitucionSerializer.objects.all()
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def institucionDetalle(request, pk):
    try: 
        institucion = Institucion.objects.get(id = pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serial = InstitucionSerializer(institucion)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = InstitucionSerializer(institucion, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        institucion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   


########## CBV ###########
class InscritosLista(APIView):
    def get(self, request):
        inscritos = Inscritos.objects.all()
        serial = ParticipanteSerializer(inscritos, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = ParticipanteSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class InscritosDetalle(APIView):
    def get_object(self, pk):
        try:
            return Inscritos.objects.get(id = pk)
        except Inscritos.DoesNotExist:
            return Http404

    def get(self, request, pk):
        inscritos = self.get_object(pk)
        serial = ParticipanteSerializer(inscritos)
        return Response(serial.data)
    
    def put(self, request, pk):
        inscritos = self.get_object(pk)
        serial = ParticipanteSerializer(inscritos, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        inscritos = self.get_object(pk)
        inscritos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   






    