# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile,Entry,Likes,Genre,Interest,Follow,Saves,Writing_Style
# Register your models here.
admin.site.register(Profile)
admin.site.register(Entry)
admin.site.register(Likes)
admin.site.register(Genre)
admin.site.register(Interest)
admin.site.register(Follow)
admin.site.register(Saves)
admin.site.register(Writing_Style)