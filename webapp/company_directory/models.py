from django.db import models


class State(models.Model):
    code = models.CharField(max_length=2, unique=True, default='')
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class Company(models.Model):
    """A model for venture capitalist companies"""
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.ForeignKey(State)
    zip = models.CharField(max_length=5)
    founded = models.PositiveSmallIntegerField()
    capital = models.IntegerField()
    date_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def capital_as_string(self):
        if self.capital <= 999:
            return str(self.capital) + ' Million'
        elif self.capital <= 999999:
            return str(self.capital / 1000) + ' Billion'
        else:
            return str(self.capital) + '1 Trillion+'

    class Meta:
        verbose_name_plural = "companies"

    def __unicode__(self):
        return self.name
