from django.contrib import admin
from pokedex.models import Pokemon, Trainer


class Pokemonadmin(admin.ModelAdmin):
    pass


class Traineradmin(admin.ModelAdmin):
    pass

admin.site.register(Pokemon, Pokemonadmin)
admin.site.register(Trainer, Traineradmin)


#Otra forma de registrarlo
#@admin.register(Trainer)
#class Trineradmin(admin.ModelAdmin):
#    pass