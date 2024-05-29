
from django import template
from myapp.models import Review,Visitor
import math
register = template.Library()



@register.simple_tag
def get_visitor_count():
    return Visitor.objects.count()


@register.simple_tag
def discount_calculation(price,discount):
    if discount == None or discount == 0:
        return price
    sellprice = price
    sellprice = price - (price * discount/100)
    return math.floor(sellprice)

@register.filter
def rupee(price):
    return f'₹{price}'