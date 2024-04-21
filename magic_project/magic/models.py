from django.db import models


class Card(models.Model):
    title = models.CharField(max_length=200)
    oracle_text = models.TextField(null=True)
    flavor_text = models.TextField(null=True)
    mana_cost = models.TextField(null=True)
    colors = models.TextField(null=True)
    set = models.ForeignKey('Set', on_delete=models.PROTECT)
    tags = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return f'Карта: {self.title}'

    class Meta:
        app_label = 'magic'


class Set(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Collection(models.Model):
    card = models.ForeignKey('Card', on_delete=models.PROTECT)
    user_id = models.IntegerField()

    def __str__(self):
        return f'Коллекция пользователя: {self.user_id}'
