from django.urls import path

from .app.Interfaces.views import author_views, book_views, reader_views, category_views, cycle_views

urlpatterns = [
    path('api/admin/author/store', author_views.store, name="admin.author.store"),
    path('api/admin/reader/store', reader_views.store, name="admin.reader.store"),
    path('api/admin/cycle/store', cycle_views.store, name="admin.cycle.store"),
    path('api/admin/category/store', category_views.store, name="admin.category.store"),

    path('', book_views.index, name='book__index'),
    path('api/admin/book/store', book_views.store, name='book__store'),

    path('category/<slug:slug>', category_views.index, name='category.index'),
    path('<slug:slug>', book_views.show, name='book__show'),
]
