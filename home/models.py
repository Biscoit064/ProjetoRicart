from django.db import models

# Create your models here.
class Task(models.Model):
    Status= (('doing', 'Pendente'), ('done', 'Concluída'))

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    state = models.CharField(max_length=20, choices=Status)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo