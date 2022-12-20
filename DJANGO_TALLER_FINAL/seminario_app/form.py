from django import forms
from seminario_app.models import Inscritos
import datetime
from django.core.validators import RegexValidator


##### Validacion campo Telefono solo ingresos de numeros #####
fono_regex =RegexValidator(
        regex=r'^\d+$',
        message="Solo puede ingresar Numeros" 
    )

class formParticipante(forms.ModelForm):
    #Validacion formulario
    telefono = forms.CharField(
    min_length=8, 
    max_length=8, 
    validators=[fono_regex],
    widget=forms.TextInput(attrs={'placeholder': '92388192'}),
    )

    class Meta:
        model = Inscritos
        fields = '__all__' 
        widgets = {
        "fechaInscripcion": forms.DateInput(attrs={'type': 'date'}),
        "nombre": forms.TextInput(attrs={'placeholder': 'Viejito Pascuero'}),
        "horaInscripcion" : forms.TextInput(attrs={'placeholder': '14:30'})
        } 

    # Validacion de fechas
    def clean_fechaInscripcion(self):
        fecha = self.cleaned_data['fechaInscripcion'] 
        if fecha > datetime.date.today():
            raise forms.ValidationError("La fecha no puede ser mayor a la de hoy")
        return fecha



