from django.contrib import admin
from .models import Lekarze, Specjalizacja, Wizyta, Lek, Recepta, Skierowanie, Badanie

# Register your models here.

admin.site.register(Lekarze)
admin.site.register(Specjalizacja)
admin.site.register(Wizyta)
admin.site.register(Lek)
admin.site.register(Recepta)
admin.site.register(Badanie)
admin.site.register(Skierowanie)