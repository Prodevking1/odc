from django.forms import ModelForm
from .models import Todo


class TaskForm(ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'
