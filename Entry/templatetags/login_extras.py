from django import template
from django.contrib.auth.models import User,Group
from ..models import Profile,Entry,Likes,Saves

register = template.Library()


@register.filter(name='has_group') 
def has_group(user, group_name):
    group =  Group.objects.get(name=group_name) 
    return True if group in user.groups.all() else False

@register.filter(name='does_exist') 
def does_exist(user, user2):

    profile = None
    if Profile.objects.filter(user=user).exists():
        profile = Profile.objects.get(user=user)
    return True if profile is not None else False
    # Do 

@register.filter(name='has_liked') 
def has_liked(user, entry):
    like =  Likes.objects.filter(user=user).filter(entry=entry).count()

    if like:
        return True
    else :
        return False


@register.filter(name='has_bookmarked') 
def has_bookmarked(user, entry):
    bookmark =  Saves.objects.filter(user=user).filter(entry=entry).count()

    if bookmark:
        return True
    else :
        return False