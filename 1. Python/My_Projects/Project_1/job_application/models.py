from django.db import models

# Create database table called Form.
class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)
    resume = models.FileField(upload_to='resumes/pdfs/')

    # __str__ method in a class is a special method that is used to define the "informal" or
    # nicely printable string representation of an instance of that class (p=Person() print(p))

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"