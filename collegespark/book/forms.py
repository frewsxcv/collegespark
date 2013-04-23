from django import forms
from collegespark.book.models import Book


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

    def __init__(self, *args, **kwargs):
        self.seller = kwargs.pop('user', None)
        self.school_name = kwargs.pop('school_name', None)
        self.book = None
        self.ip = kwargs.pop('ip', None)
        super(BookInfoForm, self).__init__(*args, **kwargs)

    def clean(self):
        return self.cleaned_data

    def save(self):

        dpt_name = self.cleaned_data['dpt_name']
        class_name = self.cleaned_data['class_name']
        book_name = self.cleaned_data['book_name']
        author = self.cleaned_data['author']
        ISBN  = self.cleaned_data['ISBN']
        price = self.cleaned_data['price']
        description = self.cleaned_data['description']
        condition = self.cleaned_data['condition']
        image = self.cleaned_data['image']

        if image:
            print "image"
        else:
            print "no image"

        self.book = Book(seller=self.seller, school_name=self.school_name,
                         isSold=False, views=0, dpt_name=dpt_name,
                         class_name=class_name, book_name=book_name,
                         author=author, ISBN=ISBN, price=price,
                         description=description, condition=condition,
                         image=image)

        self.book.save()
