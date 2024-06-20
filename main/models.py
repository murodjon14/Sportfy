from django.db import models

class Qoshiqchi(models.Model):
    ism = models.CharField(max_length=255)
    t_sana = models.DateField(blank=True, null=True)
    davlat = models.CharField(max_length=255, blank=True, null=True)

class Albom(models.Model):
    nom = models.CharField(max_length=255)
    sana = models.DateField(blank=True, null=True)
    rasm = models.ImageField(upload_to='albomlar/')
qoshiqchi = models.ForeignKey(Qoshiqchi, on_delete=models.CASCADE)

class Qoshiq(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=50)
    davomilik = models.DurationField(blank=True, null=True)
    fayl = models.FileField(upload_to='qoshiqlar/', blank=True, null=True)
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE)

class QoshiqchiAlbomlari(models.Model):
    qoshiqchi = models.ForeignKey(Qoshiqchi, on_delete=models.CASCADE)
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE)

class AlbomlarniQoashiqlari(models.Model):
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE)
    qoshiq = models.ForeignKey(Qoshiq, on_delete=models.CASCADE)