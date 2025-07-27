from django import forms
from .models import Book

# Form to add/edit books
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']

# Form with custom validation
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if "@" in name:
            raise forms.ValidationError("Name should not contain @ symbol.")
        return name