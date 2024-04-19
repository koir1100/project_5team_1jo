from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'email']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    'class': 'input form-control mb-3',
                    'placeholder': '%s' % name,
                }
            )
    