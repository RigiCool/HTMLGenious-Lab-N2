# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PageForm, SlideForm, SlideFormSet
from .models import Page, Slide

def index(request):
    error = ''
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)  # Add request.FILES here to handle file uploads
        formset = SlideFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            page = form.save()  # Save the page instance

            # Save the slides
            slides = formset.save(commit=False)  # Don't save yet
            for slide in slides:
                slide.page = page  # Associate each slide with the page
                slide.save()  # Now save the slide
            return redirect('index') # Page return with 'GET' method
        else:
            error = 'Form is not valid.'

    pages = Page.objects.all() # Retrieving All Pages
    form = PageForm() # PageForm creation
    formset = SlideFormSet(queryset=Slide.objects.none()) #SlideForm set creation

    # Data combination 
    data = {
        'pages': pages,
        'form': form,
        'formset': formset,
        'error': error
    }
    return render(request, 'main/index.html', data)

def delete_page(request, page_id):
    page = get_object_or_404(Page, id=page_id)  # Find page by ID
    page.delete()  # Delete page
    return redirect('index')  # Page return with 'GET' method