from django.db import models


class Games(models.Model):
    side = models.CharField(max_length=100)
    time_res = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.side}, time = {self.time_res}"

    @staticmethod
    def stat_game():
        games = Games.objects.all().order_by('-id')[:5]
        res = {'orel': 0, 'reshka': 0}
        for elem in games:
            count = res.get(elem.side)
            res[elem.side] = count + 1
        return res


class Author(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField(max_length=1500)
    birthday = models.DateField(blank=False)

    def fullname(self):
        return f'{self.name} {self.lastname}'
