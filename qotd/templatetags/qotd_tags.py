from django import template

from qootd.models import QuoteOfTheDay

from random import randint

register = template.Library()


@register.inclusion_tag('quote.html')
def qotd():

    all_quotes = QuoteOfTheDay.objects.all()

    if len(all_quotes) > 0:
        quote = all_quotes[randint(0,len(all_quotes) - 1)]
    else:
        quote = False

    return {'quote':quote}
