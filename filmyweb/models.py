from django.db import models

class Film(models.Model):
    tytul= models.CharField(max_length=60,  blank= False ,unique=True)
    rok = models.PositiveSmallIntegerField(default=2000)
    opis = models.TextField(default="")
    premiera = models.DateField(null=True, blank=True)
    imdb_rating=models.DecimalField(max_digits= 4, decimal_places= 2, null=True, blank=True)
    plakat= models.ImageField(upload_to="plakaty", null=True, blank= True)

    def __str__(self):
        return self.tytul + '(' + str(self.rok) + ')'

    def tytul_z_rokiem(self):
        return "{} ({})".format(self.tytul, self.rok)