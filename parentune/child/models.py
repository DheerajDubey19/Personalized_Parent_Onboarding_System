from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from parent.models import Parent


# This model represents a child, linked to a parent, with fields for name, age, and gender,
# including validation to ensure age falls within a specified range and providing options for gender.
class Child(models.Model):
    Gender_Choice = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    gender = models.CharField(max_length=10, choices=Gender_Choice)

    def _str_(self):
        return self.name