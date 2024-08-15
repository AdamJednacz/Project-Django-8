from django import forms

from .models import Wydzial, Kierunek, Student

class WydzialForm(forms.ModelForm):
    class Meta:
        model = Wydzial
        fields = '__all__'


class KierunekForm(forms.ModelForm):
    class Meta:
        model = Kierunek
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'