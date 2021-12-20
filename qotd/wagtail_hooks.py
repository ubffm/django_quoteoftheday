from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)

from qootd.models import QuoteOfTheDayPerson, QuoteOfTheDay
from wagtail.admin.edit_handlers import FieldPanel


class QootdPersonAdmin(ModelAdmin):

    model = QuoteOfTheDayPerson
    menu_label = 'Quote of the Day Atributee'
    menu_icon = 'user'
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('name', 'description',)
    seach_fields = ('name',)

    panels = [
        FieldPanel('name', help_text='The name of a person'),
        FieldPanel('description', help_text='A short description of the person. 500 Characters max.'),
        FieldPanel('bio_link', help_text='A short link to some sort of biography. I.e. Wikipedia'),
        FieldPanel('authority_data', help_text='URL to authority data, if present. I.e. GND or VIAF.'),
    ]


class QootdAdmin(ModelAdmin):
    model = QuoteOfTheDay
    add_to_settings_menu = False
    exclude_from_explorer = False
    menu_label = 'Quote of the Day'
    menu_icon = 'doc-empty'
    list_display = ('attributed_to', 'quote_text',)
    search_fields = ('quote_text',)

    panels = [
        FieldPanel('attributed_to', help_text='Select the person this quote is attributed to. If that person is not in the list, you need to create them!'),
        FieldPanel('quote_text'),
        FieldPanel('source', help_text='Where is the quote from? Free text, max. 255 characters'),
        FieldPanel('source_link', help_text='Where is the quote from, URL to source document if available.')
    ]


class RegisterGroup(ModelAdminGroup):
    menu_label = 'Quote of the Day'
    menu_icon = 'doc-full'  # change as required
    menu_order = 400  # will put in 5th place (000 being 1st, 100 2nd)
    items = (QootdAdmin, QootdPersonAdmin,)


# When using a ModelAdminGroup class to group several ModelAdmin classes together,
# you only need to register the ModelAdminGroup class with Wagtail:
modeladmin_register(RegisterGroup)
