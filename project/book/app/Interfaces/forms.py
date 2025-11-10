from django import forms

from ..Infrastructure.models import Book, Category, Author, Reader, Cycle


class BookForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
    )
    cycle = forms.ModelChoiceField(queryset=Cycle.objects.all(), required=False)
    cycle_number = forms.IntegerField(required=False)

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
