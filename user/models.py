from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key = True)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    is_enable = models.BooleanField(default=True)
    is_confrimed =models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    public_address = models.CharField(max_length=100)
    private_key = models.CharField(max_length=100)
    public_key = models.CharField(max_length=100)
    asset=models.DecimalField(max_digits=6, decimal_places=2,default=0)
    profit=models.DecimalField(max_digits=6, decimal_places=2,default=0)
    def __str__(self):
        return f'user({self.id},{self.username},{self.email},{self.is_enable},{self.is_confrimed},{self.create_time},{self.public_address},{self.asset},{self.profit})'

