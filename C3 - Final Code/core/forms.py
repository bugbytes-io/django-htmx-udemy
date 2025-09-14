from django import forms
from core.models import Book


class BookForm(forms.Form):
    name = forms.CharField(
        max_length=128,
        widget=forms.TextInput(attrs={'class': 'input input-primary'})
    )

    genre = forms.ChoiceField(
        choices=Book.GenreChoices.choices,
        widget=forms.Select(attrs={'class': 'select select-primary'})
    )

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 5 or len(name) > 50:
            raise forms.ValidationError(
                "Book name must be between 5 and 50 characters long."
            )
        return name


    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        # check the database to see if the user already has the book in their list
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        genre = cleaned_data.get('genre')

        if name and genre and self.user:
            # check if the book exists
            if self.user.books.filter(name=name, genre=genre).exists():
                raise forms.ValidationError(f"You already have '{name}' in your book list!")
            
        return cleaned_data