from django.db import models
from django.contrib.auth.models import User


class company_model(models.Model):
    company_name = models.TextField()
    symbol = models.CharField(max_length=200)
    scripcode = models.IntegerField()

    def __str__(self):
        return self.company_name


class watchlist_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(company_model, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s watchlist: {self.company.company_name}"
