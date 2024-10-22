"""
Page and slide form generation for main site page with htmlgenerator.

The PageForm is required for the user to fill in data about each section of the custom one-page site. 
Each section after the form is confirmed will be automatically generated and displayed on the site.

The SlideForm is required for the user to fill in data about each slide of the slider, which might be
presented in user custom section.
"""

# library import
from django import forms
from .models import Page, Slide
from django.forms import TextInput, Textarea, ClearableFileInput, NumberInput, CheckboxInput
from django.forms import modelformset_factory

# HTML Generator page form
class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = [
            'background_color', 'background_image', 'title', 'subtitle',
            'column_number', 'column_content_1_image', 'column_content_1_text',
            'column_content_2_image', 'column_content_2_text', 'effect',
            'column_content_3_image', 'column_content_3_text', 'dark_mode'
        ]

        widgets = {
            "background_color": TextInput(attrs={
                'class': 'form-control',
                'type': 'color',
            }),
            "background_image": ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
            }),
            "subtitle": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subtitle',
            }),
            "column_number": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Column Count (1-3)',
            }),
            "column_content_1_image": ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            "column_content_1_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Column 1 Text',
                'rows': 3,
            }),
            "column_content_2_image": ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            "column_content_2_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Column 2 Text',
                'rows': 3,
            }),
            "column_content_3_image": ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            "column_content_3_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Column 3 Text',
                'rows': 3,
            }),
            "dark_mode": CheckboxInput(attrs={
                'class': "form-check-input",
            }),
            "effect": CheckboxInput(attrs={
                'class': "form-check-input",
            }),
        }

    # Modification of original fields
    background_color = forms.CharField(
        required=False,  # Change form field to optional
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'color'  # Input type color
        })
    )
    column_number = forms.IntegerField(
        required=False,  # Change form field to optional
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Column Count (1-3)',  # Placeholder for column number in a page
        })
    )


# Page slider each slide form
class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = ['paragraph', 'image']
        widgets = {
            "image": ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            "paragraph": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Slider Image Text',
                'rows': 2,
            }),
        }
# Slide form set creation for filling slides data for slider
SlideFormSet = modelformset_factory(Slide, form=SlideForm, extra=3)
