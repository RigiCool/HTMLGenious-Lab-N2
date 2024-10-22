"""
Page and slide model generation for website user data definition and saving in a unified format.

The Page model is contain common section information of the user custom one page website. 
This information will be saved and processed for web page generation by user request.

The Slide model is contain additional information of the sections. Contain data for each slider slide,
which might be added to the section by user request.
"""

# library import
from django.db import models

# Page model creation
class Page(models.Model):
    background_color = models.CharField('Background Color',max_length=7, help_text="Background color in HEX format (e.g., #FFFFFF)")
    background_image = models.ImageField('Background Image',upload_to='backgrounds/', blank=True, null=True)

    title = models.CharField('Title', max_length = 50)
    subtitle = models.CharField('Subtitle', max_length = 50)

    column_number = models.IntegerField(null=True, blank=True)

    column_content_1_image = models.ImageField(upload_to='backgrounds/', blank=True, null=True)
    column_content_1_text = models.TextField(blank=True, null=True)

    column_content_2_image = models.ImageField(upload_to='backgrounds/', blank=True, null=True)
    column_content_2_text = models.TextField(blank=True, null=True)

    column_content_3_image = models.ImageField(upload_to='backgrounds/', blank=True, null=True)
    column_content_3_text = models.TextField(blank=True, null=True)

    dark_mode = models.BooleanField(default=False)  # Enabling website dark mode

    effect = models.BooleanField(default=False)  # Enabling 3D effect for each column image

    def __str__(self):
        return self.title

class Slide(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='slides')
    image = models.ImageField(upload_to='slides/', blank=True, null=True)
    paragraph = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Slide for {self.page.title}"
