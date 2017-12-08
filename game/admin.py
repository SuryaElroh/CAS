from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(DefensiveCard)
admin.site.register(OffensiveCard)
admin.site.register(SpecialCard)
admin.site.register(CharacterCard)
admin.site.register(TypeSpecialCard)