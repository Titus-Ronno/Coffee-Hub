from django.contrib import admin
from .models import Coffee, Card, Reply, Gallery, TrainingSession, Event

# Register your models here.


class coffeeAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity')
admin.site.register(Coffee, coffeeAdmin)

class cardAdmin(admin.ModelAdmin):
    list_display = ('image','title','text')
admin.site.register(Card, cardAdmin)

class replyAdmin(admin.ModelAdmin):
    list_display = ('name','email','comment')
admin.site.register(Reply, replyAdmin)

class galleryAdmin(admin.ModelAdmin):
    list_display = ('image',)
admin.site.register(Gallery, galleryAdmin)

class trainingAdmin(admin.ModelAdmin):
    list_display = ('user','date','time','duration','details')
admin.site.register(TrainingSession, trainingAdmin)

class eventAdmin(admin.ModelAdmin):
    list_display = ('title','date','time','description')
admin.site.register(Event, eventAdmin)


