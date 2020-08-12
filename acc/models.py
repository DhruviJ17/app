from django.db import models

class Entry(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'entries'


class Task(models.Model):
    title = models.CharField(max_length=200, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
