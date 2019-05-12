from django import forms
from .models import Review, Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
#
# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ('message')
#
