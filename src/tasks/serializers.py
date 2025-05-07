from rest_framework import serializers
from .models import Lista, Tarea, Etiqueta

class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = ['id','name','color']

class TareaSerializer(serializers.ModelSerializer):
    etiquetas = EtiquetaSerializer(many=True, read_only=True)
    class Meta:
        model = Tarea
        fields = ['id','lista','title','description',
                  'due_date','priority','completed',
                  'created_at','etiquetas']

class ListaSerializer(serializers.ModelSerializer):
    tasks = TareaSerializer(many=True, read_only=True)
    class Meta:
        model = Lista
        fields = ['id','name','created_at','tasks']
