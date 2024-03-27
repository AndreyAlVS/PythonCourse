from django.db import models


class Games(models.Model):
    side = models.CharField(max_length=100)
    time_res = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.side}, time = {self.time_res}"
