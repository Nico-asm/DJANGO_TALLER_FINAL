from rest_framework import serializers
from .models import Inscritos, Institucion

############## Participante ###############
class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscritos
        fields = '__all__'


############### Institucion ###############
class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'