from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Student, Evaluation
class EvaluatorRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EvaluationForm(forms.ModelForm):
    student = forms.ModelChoiceField(
        queryset=Student.objects.all(),
        label="Select Student (Matric Number)"
    )

    class Meta:
        model = Evaluation
        fields = [
            'student',
            'introduction',
            'problem_statement',
            'objectives',
            'methodology',
            'architecture',
            'significance',
            'related_works',
            'design_analysis',
            'implementation'
        ]
        widgets = {
            'introduction': forms.NumberInput(attrs={'min': 0, 'max': 5}),
            'problem_statement': forms.NumberInput(attrs={'min': 0, 'max': 5}),
            'objectives': forms.NumberInput(attrs={'min': 0, 'max': 5}),
            'methodology': forms.NumberInput(attrs={'min': 0, 'max': 5}),
            'architecture': forms.NumberInput(attrs={'min': 0, 'max': 5}),
            'significance': forms.NumberInput(attrs={'min': 0, 'max': 5}),
            'related_works': forms.NumberInput(attrs={'min': 0, 'max': 5}),
            'design_analysis': forms.NumberInput(attrs={'min': 0, 'max': 5}),
            'implementation': forms.NumberInput(attrs={'min': 0, 'max': 10}),
        }
