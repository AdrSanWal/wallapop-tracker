from django.db import models

from multiselectfield import MultiSelectField

from user.models import User


class Filters(models.Model):
    CONDITION_CHOICES = [
        ('n', 'new'),
        ('a', 'as_good_as_new'),
        ('g', 'good'),
        ('f', 'fair'),
        ('h', 'has_given_it_all'),
    ]
    user = models.ManyToManyField(User, related_name='rel_user')
    keywords = models.CharField(max_length=30)
    min_sale_price = models.IntegerField()
    max_sale_price = models.IntegerField()
    condition = MultiSelectField(choices=CONDITION_CHOICES)
