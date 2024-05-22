from django.contrib import admin
from .models import (About,
                     Client,
                     Payment,
                     Users,
                     Team,
                     Video_lessons,
                     Web_Images,
                     Websites)

admin.site.register(Client)
admin.site.register(Payment)
admin.site.register(Users)
admin.site.register(About)
admin.site.register(Team)
admin.site.register(Video_lessons)
admin.site.register(Websites)
admin.site.register(Web_Images)

