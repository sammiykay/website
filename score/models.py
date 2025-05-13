from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    matric_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    project_topic = models.CharField(max_length=255)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.matric_number} - {self.full_name}"


class Evaluation(models.Model):
    evaluator = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    introduction = models.PositiveIntegerField()
    problem_statement = models.PositiveIntegerField()
    objectives = models.PositiveIntegerField()
    methodology = models.PositiveIntegerField()
    architecture = models.PositiveIntegerField()
    significance = models.PositiveIntegerField()
    related_works = models.PositiveIntegerField()
    design_analysis = models.PositiveIntegerField()
    implementation = models.PositiveIntegerField()

    total_score = models.PositiveIntegerField(editable=False)

    class Meta:
        unique_together = ('evaluator', 'student')

    def save(self, *args, **kwargs):
        self.total_score = (
            self.introduction +
            self.problem_statement +
            self.objectives +
            self.methodology +
            self.architecture +
            self.significance +
            self.related_works +
            self.design_analysis +
            self.implementation
        )
        super().save(*args, **kwargs)
