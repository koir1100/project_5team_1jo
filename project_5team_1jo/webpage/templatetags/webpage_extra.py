from django import template

register = template.Library()

@register.simple_tag
def replace_category_name(value):
    mapping_dict = {"11": "문학", "6": "인문사회", "5": "사회과학", "4": "자연과학", "425": "테마"}
    return mapping_dict.get(str(value), "전체 분야")
