from django.contrib import admin

from djsummoner.apps.deck_man.models import Unit, Summoner, Event, Deck


admin.site.register(Unit)
admin.site.register(Summoner)
admin.site.register(Event)
admin.site.register(Deck)
