from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(ActionCard, ActionCardDescriptors)
admin.site.register(CharacterCard, CharacterCardDescriptors)
