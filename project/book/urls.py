from django.urls import path

from .app.Interfaces.views import author_views, book_views

urlpatterns = [
    path('admin/author/store', author_views.store, name="admin.author.store"),

    path('', book_views.index, name='book__index'),
    path('admin/book/store', book_views.store, name='book__store'),
    path('<slug:slug>', book_views.show, name='book__show'),
]
