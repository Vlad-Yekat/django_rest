from django.contrib import admin

# Register your models here.
from .models import MixPost, Video, Audio, Texts
from .models import PostVer2, VideoVer2, TextVer2, AudioVer2


class MixPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'counter', 'type_content', 'contents')

    def contents(self, obj):
        if obj.type_content == 'Video':
            return "video file:"
        elif obj.type_content == 'Audio':
            return "track file:"


class PostVer2Admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'counter', 'content_type')
    search_fields = ['^title']  # with begin of title only


class VideoVer2Admin(admin.ModelAdmin):
    list_display = ('id', 'ref_video', 'ref_subs')


class AudioVer2Admin(admin.ModelAdmin):
    list_display = ('id', 'bit_rate')


class TextVer2Admin(admin.ModelAdmin):
    list_display = ('id', 'short', 'full')


admin.site.register(PostVer2, PostVer2Admin)
admin.site.register(VideoVer2, VideoVer2Admin)
admin.site.register(AudioVer2, AudioVer2Admin)
admin.site.register(TextVer2, TextVer2Admin)
