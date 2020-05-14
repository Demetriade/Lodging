from django.db import models
from django.contrib.auth.models import User

        
class Lodge(models.Model):
    address = models.CharField(max_length= 100)
    postal_code = models.CharField(max_length=6)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_lodge_pic.jpg', upload_to='lodgment_pics')
    total_nb = models.IntegerField()
    lodged_nb = models.IntegerField()
    information = models.TextField()

    def __str__(self):
        return self.address