from django.contrib import admin

# Register your models here.
from learning.models import Topic
admin.site.register(Topic)

import learning.models
admin.site.site_title='第一个网站'
admin.site.site_header='网站标题'
admin.site.index_title='学习博客'