from django import forms
from webapp.models import Product, Review
from django.forms import ValidationError



def max_length_validator(string):
    if len(string) > 20:
        raise ValidationError('The max number of characters is 20')
    return string


def min_length_validator(string):
    if len(string) < 4:
        raise ValidationError('The minimum number of characters is 8')
    return


class ProductForm(forms.ModelForm):

    name = forms.CharField(validators=(min_length_validator, max_length_validator))

    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'image')


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('text', 'rating')