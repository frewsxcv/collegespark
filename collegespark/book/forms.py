from django import forms

CHOICES = (('1', 'New',), ('2', 'Used',))


class BookInfoForm(forms.Form):
    school_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter a School Name'}), required=True)
    dpt_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter a Department Name'}), required=True)
    class_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter a Class Name'}), required=True)
    book_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter a Book Name'}), required=True)
    author = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter an author Name'}), required=True)
    ISBN = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter an ISBN'}), required=True)
    price = forms.DecimalField(required=True)
    description = forms.CharField(widget=forms.Textarea(), required=True)
    condition = forms.ChoiceField(widget=forms.Select, choices=CHOICES,
                                  required=True)
    image = forms.ImageField(required=False)

    def clean(self):
        return self.cleaned_data
