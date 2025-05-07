from django.db import models

class Lista(models.Model):
    name       = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name

class Etiqueta(models.Model):
    name  = models.CharField(max_length=50)
    color = models.CharField(max_length=7, default='#ffffff')
    def __str__(self): return self.name

class Tarea(models.Model):
    PRIORITY_CHOICES = [('low','Baja'),('medium','Media'),('high','Alta')]
    lista      = models.ForeignKey(Lista, on_delete=models.CASCADE, related_name='tasks')
    title      = models.CharField(max_length=200)
    description= models.TextField(blank=True)
    due_date   = models.DateField(null=True, blank=True)
    priority   = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='medium')
    completed  = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    etiquetas  = models.ManyToManyField(Etiqueta, through='TareaEtiqueta', related_name='tasks')
    def __str__(self): return self.title

class TareaEtiqueta(models.Model):
    tarea    = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('tarea','etiqueta')
