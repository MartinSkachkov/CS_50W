from django.db import models
import uuid

def unique_upload_to(instance, filename):
    # Keep the directory structure and add a unique identifier
    upload_directory = 'resumes/pdfs/'
    ext = filename.split('.')[-1]
    unique_filename = f"{uuid.uuid4().hex}.{ext}"
    return f'{upload_directory}{unique_filename}'

# Create database table called Form.
class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)
    resume = models.FileField(upload_to=unique_upload_to)

    # __str__ method in a class is a special method that is used to define the "informal" or
    # nicely printable string representation of an instance of that class (p=Person() print(p))

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"