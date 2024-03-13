from django.conf import settings
from django.db import models
from django.utils import timezone

pa_autoconfigure_django.py --python=3.8 https://github.com/SalvaGarciaOlmedo/https://github.com/SalvaGarciaOlmedo/RecuDjangoGirls.git


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title