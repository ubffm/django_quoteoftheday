from django.db import models

# Create your models here.


class QuoteOfTheDay(models.Model):
    attributed_to = models.ForeignKey('QuoteOfTheDayPerson', related_name='author', on_delete=models.CASCADE)
    quote_text = models.TextField()
    source = models.CharField(max_length=255)
    source_link = models.URLField(blank=True)


class QuoteOfTheDayPerson(models.Model):

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500, blank=True, help_text="Enter a short description for the person. 500 Characters max.")
    bio_link = models.URLField(blank=True, help_text='Enter a URL to a biography for this person. For example a Wikipedia page.')
    authority_data = models.URLField(blank=True, help_text='Enter a URL to an authority dataset. For example, GND or VIAF links.')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Quote Attributee"
        verbose_name_plural = "Quote Attributee"
        ordering = ['name']
