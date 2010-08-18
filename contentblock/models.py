from django.db import models
from multilingual.translation import TranslationModel
from cms.models.fields import PlaceholderField
from cms.utils import placeholder
from django.utils.translation import ugettext_lazy as _

class ContentBlock(models.Model):
    code = models.CharField(max_length=16, unique=True, db_index=True, primary_key=True)
    name = models.CharField(max_length=255, blank=True, default='')
    class Translation(TranslationModel):
        text = PlaceholderField(slotname='contentblock_text',
                                verbose_name=_('text'),
                                actions=placeholder.MLNGPlaceholderActions,
                                related_name='contentblock_texts')
    noml = models.Manager()
