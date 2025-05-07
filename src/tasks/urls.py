# src/tasks/urls.py
from rest_framework.routers import DefaultRouter
from .views import ListaViewSet, TareaViewSet, EtiquetaViewSet

router = DefaultRouter()
router.register(r'lists',  ListaViewSet, basename='list')
router.register(r'tasks',  TareaViewSet, basename='task')
router.register(r'labels', EtiquetaViewSet, basename='label')

urlpatterns = router.urls
