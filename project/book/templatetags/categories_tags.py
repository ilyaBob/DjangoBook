from django import template

from book.app.Infrastructure.models import Category

register = template.Library()

@register.inclusion_tag('web/includes/category.html')
def categories_list():
    categories = Category.objects.all()
    return {'categories': categories}
