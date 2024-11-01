from django.db import models

class Department(models.Model):
    name = models.CharField("학과", max_length=20)
    memo = models.CharField("메모", max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "학과"
        verbose_name_plural = "학과"
        tablename = "departments"