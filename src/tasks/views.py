from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Lista, Tarea, Etiqueta
from .serializers import ListaSerializer, TareaSerializer, EtiquetaSerializer

# —————————————
# API REST con DRF
# —————————————
class ListaViewSet(viewsets.ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer

class EtiquetaViewSet(viewsets.ModelViewSet):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    # Añadimos 'lista' para poder filtrar tareas por lista también
    filterset_fields = ['lista', 'due_date', 'priority', 'completed']

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        tarea = self.get_object()
        tarea.completed = True
        tarea.save()
        return Response({'status': 'completada'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def assign_labels(self, request, pk=None):
        tarea = self.get_object()
        label_ids = request.data.get('labels', [])
        etiquetas = Etiqueta.objects.filter(id__in=label_ids)
        tarea.etiquetas.set(etiquetas)
        return Response(TareaSerializer(tarea).data, status=status.HTTP_200_OK)


# —————————————
# VISTAS FRONTEND con Django
# —————————————
def list_list(request):
    """
    Renderiza la página con todas las listas;
    el JS hará fetch a /api/lists/ para poblarla.
    """
    return render(request, 'tasks/list_list.html')

def list_detail(request, pk):
    """
    Renderiza la página de detalle de una lista (pk);
    el JS hará fetch a /api/tasks/?lista=pk para mostrar sus tareas.
    """
    return render(request, 'tasks/list_detail.html', {'list_id': pk})

def label_list(request):
    """Página que lista y gestiona etiquetas (JS fetch /api/labels/)."""
    return render(request, 'tasks/label_list.html')

def label_detail(request, pk):
    """Detalle de etiqueta (opcional: puede servir para editar/borrar)."""
    return render(request, 'tasks/label_detail.html', {'label_id': pk})