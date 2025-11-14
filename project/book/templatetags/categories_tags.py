from django import template

from book.app.Infrastructure.Category.model import Category

register = template.Library()

@register.inclusion_tag('web/includes/category.html')
def categories_list():
    categories = Category.objects.all()
    return {'categories': categories}
