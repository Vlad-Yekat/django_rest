from __future__ import print_function
from rest_framework import serializers

from insidepages.models import MixPost, Video, Audio, Texts
from insidepages.models import PostVer2, VideoVer2, AudioVer2, TextVer2


class PostVer2ObjectRelatedField(serializers.RelatedField):
    class Meta:
        model = PostVer2
        fields = 'content_type'
        read_only_fields = ['content_type']

    def to_representation(self, value):
        date = super(PostVer2ObjectRelatedField, self).to_representation(value)

        if isinstance(value, VideoVer2):
            serializer = VideoSerializer(value)
        elif isinstance(value, AudioVer2):
            serializer = AudioSerializer(value)
        elif isinstance(value, TextVer2):
            serializer = TextsSerializer(value)
        else:
            raise Exception('Unexpected type of content')

        return serializer.data


class PostVer2Serializer(serializers.ModelSerializer):

    class Meta:
        model = PostVer2
        fields = ('url', 'pk', 'title', 'counter', 'content_type', 'object_id')

    def to_representation(self, instance):
        main_arr = []
        row_arr = {}
        date = super(PostVer2Serializer, self).to_representation(instance)

        for row_dict, val in date.items():
            print(row_dict, val)
            if row_dict == 'content_type':
                res_arr = []
                if val == 14:
                    qs = VideoVer2.objects.get(pk=instance.object_id)  # including instance
                    res_arr.append('Video:')
                    res_arr.append('ref on file: '+qs.ref_video)
                    res_arr.append('ref on subtitres: '+qs.ref_subs)
                    row_arr.update([('content', res_arr)])
                elif val == 11:
                    qsa = AudioVer2.objects.get(pk=instance.object_id)
                    res_arr.append('Audio:')
                    res_arr.append('bitrate: ' + qsa.bit_rate)
                    row_arr.update([('content', res_arr)])
                elif val == 13:
                    qst = TextVer2.objects.get(pk=instance.object_id)
                    res_arr.append('Text:')
                    res_arr.append('descr: ' + qst.short)
                    res_arr.append('descr: ' + qst.full)
                    row_arr.update([('content', res_arr)])
                else:
                    res_arr.append('Unknown content')
                    row_arr.update([('content', res_arr)])
            else:
                row_arr.update([(row_dict, val)])

        main_arr.append(row_arr)

        return main_arr


class PostVer2DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostVer2
        fields = ('pk', 'title', 'counter', 'content_type', 'object_id')

    def to_representation(self, instance):
        main_arr = []
        row_arr = {}
        date = super(PostVer2DetailSerializer, self).to_representation(instance)
        print('date=', date)
        print('type(date)=', type(date))
        print('type(main_Arr)=', type(main_arr))

        for row_dict, val in date.items():
            print(row_dict, val)

            if row_dict == 'content_type':
                res_arr = []
                if val == 14:
                    qs = VideoVer2.objects.get(pk=instance.object_id)  # including instance
                    res_arr.append('Video:')
                    res_arr.append('ref on file: ' + qs.ref_video)
                    res_arr.append('ref on subtitres: ' + qs.ref_subs)
                    row_arr.update([('content', res_arr)])
                elif val == 11:
                    qsa = AudioVer2.objects.get(pk=instance.object_id)
                    res_arr.append('Audio:')
                    res_arr.append('bitrate: ' + qsa.bit_rate)
                    row_arr.update([('content', res_arr)])
                elif val == 13:
                    qst = TextVer2.objects.get(pk=instance.object_id)
                    res_arr.append('Text:')
                    res_arr.append('descr: ' + qst.short)
                    res_arr.append('descr: ' + qst.full)
                    row_arr.update([('content', res_arr)])
                else:
                    res_arr.append('Unknown content')
                    row_arr.update([('content', res_arr)])
                print(row_arr)

            else:
                pass

        return main_arr


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('pk', 'url', 'ref_video', 'ref_subs')


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ('pk', 'url', 'bit_rate')


class TextsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Texts
        fields = ('pk', 'url', 'TextDetail')


class TextVer2Serializer(serializers.ModelSerializer):
    class Meta:
        model = TextVer2
        fields = ('pk', 'short', 'full')


class PostsSerializer(serializers.ModelSerializer):

    content = serializers.StringRelatedField(many=True)
    content_type = serializers.SerializerMethodField()

    class Meta:
        model = MixPost
        fields = ('pk', 'title', 'counter', 'ref_content', 'type_content', 'content', 'content_type')

    def get_content_type(self, obj):
        return 'some describe '
