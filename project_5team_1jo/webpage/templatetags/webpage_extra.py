from django import template

register = template.Library()

@register.simple_tag
def replace_category_name(value):
    mapping_dict = {"11": "문학", "6": "인문\n사회", "5": "사회\n과학", "4": "자연\n과학", "425": "테마"}
    return mapping_dict.get(str(value), "전체 분야")
