from django.forms import CharField, EmailField, Form, PasswordInput, ValidationError, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail

from django.conf import settings
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Layout, Fieldset, Field,
    ButtonHolder, Submit, HTML, Div, MultiField)


class SignUpForm(UserCreationForm):

    first_name = CharField(
                max_length=30, required=False,
                label = "First name:",
                widget=TextInput(attrs={'autocomplete': 'off'})
            )

    last_name = CharField(
                max_length=30, required=False,
                label = "Last name:",
                widget=TextInput(attrs={'autocomplete': 'off'})
            )

    email = EmailField(max_length=254,
                label = "Email address:",
                widget=TextInput(attrs={'autocomplete': 'off'})
            )

    password1 = CharField(
                    label = "Password:",
                    widget=PasswordInput(attrs={
                        'autocomplete': 'off',
                        'placeholder': 'Password',
                    })
                )

    password2 = CharField(
                    label = "Confirm password:",
                    widget=PasswordInput(attrs={
                        'autocomplete': 'off',
                        'placeholder': 'Confirm New Password',
                    })
                )


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )
        # exclude = ['username',]


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


        self.helper.layout = Layout(

            Field('first_name',
                autocomplete='off',
                css_class="search-form-label"
                ),

            Field('last_name',
                autocomplete='off',
                css_class="search-form-label",
                ),

            Field('email',
                autocomplete='off',
                css_class="search-form-label",
                ),
            Field('password1',
                autocomplete='off',
                css_class="search-form-label",
                ),
            Field('password2',
                autocomplete='off',
                css_class="search-form-label",
                ),


            HTML(""" """),


            Submit('submit', 'Sign up', css_class='upload-btn')
        )


        self.helper.form_method = 'POST'


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            message = "Passwords did not match"
            raise(ValidationError(message))

        return(password2)


    def clean(self):

        """ Create username from first/lastnames
        """

        self.first_name = self.cleaned_data.get('first_name')
        self.last_name = self.cleaned_data.get('last_name')

        print(self.cleaned_data)

        self.username = "%s.%s" %(str(self.first_name), str(self.last_name))
        # print('USERNAME: %s') %(self.username)


    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)

        # automatically set to email address to create a unique identifier
        user.username = self.username

        if commit:
            user.is_active = False
            user.save()


        return(user)













''
