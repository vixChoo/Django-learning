from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

STATUS = (
    ('P', 'Pending'),
    ('C', 'Confirm')
)
MEAL = (
    ('B', 'Pending'),
    ('L', 'Confirm'),
    ('D', 'Dinner')
)

# Create your models here.
class Booking(models.Model) :
    status = models.CharField(choices=STATUS,default='P',max_length=1)
    meal_type = models.CharField(choices=MEAL,max_length=1)
    people = models.PositiveIntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})