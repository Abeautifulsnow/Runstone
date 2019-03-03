# -*- coding:utf-8 -*-
__author__ = 'dapeng'
__date__ = '18-10-11 下午5:43'

import xadmin

from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']
    model_icon = 'fa fa-info-circle'

class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'comments', 'add_time']
    model_icon = 'fa fa-comment'

class UserFavoriteAdmin(object):
    list_display = ['user', 'course', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'fav_id', 'fav_type', 'add_time']
    model_icon = 'fa fa-bookmark'

class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']
    model_icon = 'fa fa-comments-o'

class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']
    model_icon = 'fa fa-book'

xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)