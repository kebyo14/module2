from django.db import models

class ProductMini(models.Model):
    name = models.CharField(max_length=255)
    sing = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class HeaderNav(models.Model):
    name = models.CharField(max_length=255, default=True)
    text = models.CharField(max_length=255)
    img = models.CharField(max_length=500,  default=True)

    def __str__(self):
        return self.name

class IMG(models.Model):
    img = models.CharField(max_length=255, default=True)

    def __str__(self):
        return self.img
    


class HeaderInfo(models.Model):
    text = models.CharField(max_length=500)
    img = models.CharField(max_length=255, default=True)

    def __str__(self):
        return self.text
    

class Section(models.Model):
    name = models.CharField(max_length=500, default=True)
    text = models.CharField(max_length=5000, default=True)
    btn = models.CharField(max_length=500, default=True)
    img = models.CharField(max_length=255, default=True)
    

    def __str__(self):
        return self.name