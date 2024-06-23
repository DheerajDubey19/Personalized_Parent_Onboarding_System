from django.db import models
from django.core.validators import MinLengthValidator

# This model represents a parent with fields for email, names of both parents, type of parent (first-time or experienced),
# contact information with validation, and an optional address.
class Parent(models.Model):
    Parent_Type = [
        ('first_time', 'First Time Parent'),
        ('experienced', 'Experienced Parent'),
    ]
    email = models.EmailField(unique=True)
    parent1_name = models.CharField(max_length=50)
    parent2_name = models.CharField(max_length=50)
    parent_type = models.CharField(max_length=20, choices=Parent_Type)
    contact = models.CharField(validators=[MinLengthValidator(4)], max_length=10, blank=False)
    address = models.CharField(max_length=255, null=True)

    def _str_(self):
        return self.email