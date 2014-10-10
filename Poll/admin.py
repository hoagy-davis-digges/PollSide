from django.contrib import admin
from Poll.models import *

admin.site.register(Question)
admin.site.register(Subquestion)
admin.site.register(Poll)
admin.site.register(Pollster)
admin.site.register(Group)
admin.site.register(Answer)
admin.site.register(Category)
admin.site.register(Result)
