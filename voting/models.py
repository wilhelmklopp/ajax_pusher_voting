from django.db import models


class Voting(models.Model):
    auto_id = models.AutoField(primary_key=True)
    total_votes = models.BigIntegerField()
    score = models.BigIntegerField()
