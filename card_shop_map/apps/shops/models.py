from django.db import models


class CardGame(models.Model):
    name = models.CharField(max_length=127)
    publisher = models.CharField(max_length=127)
    link = models.CharField(max_length=127)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Shop(models.Model):
    name = models.CharField(max_length=127)
    postcode = models.CharField(max_length=7, null=False)
    address = models.CharField(max_length=127)
    phone_number = models.CharField(max_length=15)
    photo_link = models.CharField(max_length=255, null=True)

    games = models.ManyToManyField(CardGame)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BusinessHours(models.Model):
    DAYS = [
        ("1", "Monday"),
        ("2", "Tuesday"),
        ("3", "Wednesday"),
        ("4", "Thursday"),
        ("5", "Friday"),
        ("6", "Saturday"),
        ("7", "Sunday"),
        ("8", "holidays"),
    ]
    day = models.CharField(choices=DAYS, max_length=1)
    shop = models.ForeignKey("Shop", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
