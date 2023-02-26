from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    dien_thoai = models.CharField(max_length=20)
    dia_chi = models.TextField()

    def __str__(self):
        return f'{self.user.username} and {self.dien_thoai}'

    class Meta:
        db_table = u'customers'