from rest_framework import viewsets
from .models import Empresa, Contacto, EjecutivoCuenta, Cliente, Lead, OportunidadVenta, Proyecto, Tarea
from .serializers import EmpresaSerializer, ContactoSerializer, EjecutivoCuentaSerializer, ClienteSerializer, LeadSerializer, OportunidadVentaSerializer, ProyectoSerializer, TareaSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

class EjecutivoCuentaViewSet(viewsets.ModelViewSet):
    queryset = EjecutivoCuenta.objects.all()
    serializer_class = EjecutivoCuentaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class OportunidadVentaViewSet(viewsets.ModelViewSet):
    queryset = OportunidadVenta.objects.all()
    serializer_class = OportunidadVentaSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
