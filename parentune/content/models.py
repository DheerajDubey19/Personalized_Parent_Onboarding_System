from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from child.models import Child
from parent.models import Parent


# This model represents different types of content (blogs and vlogs) aimed at specific age groups,
# genders, and parent types, including validation to ensure logical age ranges and fields for metadata
# such as title, synopsis, URL, and last updated timestamp.

class Content(models.Model):
    Content_Type=[
        ('blog','Blog'),
        ('vlog','Vlog'),
    ]
    title = models.CharField(max_length=50)
    synopsis = models.TextField(null=True)
    content_type = models.CharField(max_length=10,choices=Content_Type, blank=True,null=True)
    min_age = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    max_age = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    gender = models.CharField(max_length=10, choices=Child.Gender_Choice, blank=True, null=True)
    parent_type = models.CharField(max_length=20, choices=Parent.Parent_Type, blank=True, null=True)
    url = models.URLField()
    updatedOn = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return self.title

    def clean(self):
        if self.min_age > self.max_age:
            raise ValidationError({'max_age': 'Max age must be greater than or equal to min age.'})