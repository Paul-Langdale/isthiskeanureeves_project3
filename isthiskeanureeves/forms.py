from django import forms
from django.contrib.auth.models import User
from isthiskeanureeves.models import Category, UserProfile, Page


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    img = forms.CharField(max_length=64, unique=True)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

    # Hopefully this gives us two inputs for name and picture
    # (we can put more in later, keeping it simple for now)

#class DropCat(forms.Form):
  #  categories_list = forms.ChoiceField(choices=[for c in categories])

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('name', 'picture', 'category')
