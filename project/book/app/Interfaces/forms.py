from django import forms

from ..Infrastructure.models import Book, Category, Author, Reader, Cycle


class BookForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
    )

    class Meta:
        model = Book
        fields = (
            'title',
            'image_url',
            'description',
            'is_published',
            'age',
            'time',
            'author',
            'reader',
            'cycle',
            'cycle_number',
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

class CycleForm(forms.ModelForm):
    class Meta:
        model = Cycle
        fields = ('title',)
