from django import template
from app.models import Elements
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


# Создание меню
@register.inclusion_tag('app/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu = Elements.objects.get(name=menu_name, parent=None)
    new_context = {'menu_elem': menu}

    # Получаем текущий url для определения активного элемента
    current_url = context['request'].path

    try:
        active_elem = Elements.objects.get(url=current_url)
    except ObjectDoesNotExist:
        pass
    else:
        # Получаем уже развёрнутые элементы меню
        expanded_elems = active_elem.get_last_items() + [active_elem.id]
        new_context['expanded_elems'] = expanded_elems
    return new_context


# Создание меню дочерних элементов
@register.inclusion_tag('app/menu.html', takes_context=True)
def draw_menu_subelems(context, menu_elem_id):
    menu_elem = Elements.objects.get(id=menu_elem_id)
    new_context = {'menu_elem': menu_elem}
    if 'expanded_elems' in context:
        new_context['expanded_elems'] = context['expanded_elems']
    return new_context
