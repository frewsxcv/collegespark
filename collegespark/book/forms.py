from django import forms

CHOICES = (('1', 'Used',), ('2', 'New',))


class BookInfoForm(forms.Form):
    dpt_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input-dpt',
               'placeholder': 'Enter a Department Name'}), required=True)
    class_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input-class',
               'placeholder': 'Enter a Class Name'}), required=True)
    book_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input-book',
               'placeholder': 'Enter a Book Name'}), required=True)
    author = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input-author',
               'placeholder': 'Enter an author Name'}), required=False)
    ISBN = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input-ISBN',
               'placeholder': 'Enter an ISBN'}), required=False)
    price = forms.DecimalField(decimal_places=2, required=True)
    description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'input-description',
               'placeholder': 'Enter description of the book'}), required=True)
    condition = forms.ChoiceField(widget=forms.Select, choices=CHOICES,
                                  required=True)
    image = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'input-image'}), required=False)

    def clean(self):
        return self.cleaned_data
