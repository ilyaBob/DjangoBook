from django import forms

from ..Infrastructure.models import Book, Category, Author, Reader


class BookForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
    )

    class Meta:
        model = Book
        fields = (
            'title',
            'description',
            'age',
            'time',
            'category',
        )


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('title',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)


class ReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ('title',)
