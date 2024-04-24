from django import forms

from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('type', 'name', 'description', 'price', 'image',)
        widgets = {
            'type': forms.Select(attrs={
            }),
            'name': forms.TextInput(attrs={
            }),
            'description': forms.Textarea(attrs={
            }),
            'price': forms.TextInput(attrs={
            }),
            'image': forms.FileInput(attrs={
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={

            }),
            'description': forms.TextInput(attrs={

            }),
            'price': forms.TextInput(attrs={

            }),
            'image': forms.FileInput(attrs={

            })
        }

class FilterForm(forms.Form):
    class Meta:
        model = Item
        fields = ('type', 'name', 'description', 'price', 'image',)