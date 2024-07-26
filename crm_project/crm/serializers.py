from rest_framework import serializers
from .models import Empresa, Contacto, EjecutivoCuenta, Cliente, Lead, OportunidadVenta, Proyecto, Tarea

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'

class EjecutivoCuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EjecutivoCuenta
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

class OportunidadVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OportunidadVenta
        fields = '__all__'

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'
