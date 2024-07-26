from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpresaViewSet, ContactoViewSet, EjecutivoCuentaViewSet, ClienteViewSet, LeadViewSet, OportunidadVentaViewSet, ProyectoViewSet, TareaViewSet

router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'contactos', ContactoViewSet)
router.register(r'ejecutivos', EjecutivoCuentaViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'leads', LeadViewSet)
router.register(r'oportunidades', OportunidadVentaViewSet)
router.register(r'proyectos', ProyectoViewSet)
router.register(r'tareas', TareaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
