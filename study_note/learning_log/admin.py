from django.contrib import admin
from learning_log.models import Topic, Entry

# Register your models here.

from learning_log.models import Topic

admin.site.register(Topic)
admin.site.register(Entry)