from django.db import models

class Employeedetails (models.Model):
    emp_id = models.PositiveIntegerField()
    emp_name = models.CharField(max_length=50)
    emp_email = models.EmailField(max_length=50)
    emp_designation = models.CharField(max_length=50)

    def __str__(self):
        return self.emp_name