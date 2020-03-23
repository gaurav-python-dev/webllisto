from django import forms
from.models import Product, Category
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'category', 'description', 'image', 'tags')
    def __init__(self,*args,**kwargs):
        super(ProductForm,self).__init__(*args,**kwargs)
        self.fields['category'].empty_label = 'Select'
        self.fields['category'].required = True

#CategoryForm
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=('name',)

# Registration form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]