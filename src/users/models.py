from django.db import models
from django.contrib.auth.models import User, Group

class Profile(models.Model):
    user = models.ForeignKey(User, related_name='profiles',on_delete=models.CASCADE)
    groups = models.ManyToManyField(
        Group,
        verbose_name="nomes dos perfis do usuário",
    )
    def __str__(self):
        return self.user.username
