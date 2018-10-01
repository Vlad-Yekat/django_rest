from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import PostsSerializer, VideoSerializer, AudioSerializer, TextsSerializer
from .serializers import PostVer2ObjectRelatedField, PostVer2Serializer, PostVer2DetailSerializer
from insidepages.models import MixPost, Video, Audio, Texts
from insidepages.models import PostVer2, VideoVer2, AudioVer2, TextVer2
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'newver2': reverse('ver2-list', request=request, format=format),
    })


class VideoView(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class AudioView(viewsets.ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer


class TextsView(viewsets.ModelViewSet):
    queryset = Texts.objects.all()
    serializer_class = TextsSerializer


class TextVer2View(viewsets.ModelViewSet):
    queryset = TextVer2.objects.all()
    serializer_class = TextsSerializer


class PostVer2List(generics.ListAPIView):
    queryset = PostVer2.objects.all().order_by('pk')
    serializer_class = PostVer2Serializer


class PostsList(generics.ListAPIView):
    queryset = MixPost.objects.all().order_by('pk')
    serializer_class = PostsSerializer
    # pagination_class = PageNumberPagination

    # print('aaa2')
    # aaa = MixPost(id = 4)
    # aaa.counter = 5
    # aaa.save()

    # def perform_create(self, serializer):
    #    serializer.save()


class PostsDetail(generics.RetrieveAPIView):
    lookup_field = 'pk'
    #queryset = MixPost.objects.all()
    serializer_class = PostsSerializer


    def get(self, request, pk, format=None):
        one_post = self.get_object()
        one_post.counter = one_post.counter + 1
        serializer = PostsSerializer(one_post)
        one_post.save()
        return Response(serializer.data)


    # def post(self, request, format=None):
    #    pass

    # def perform_create(self, serializer):
    #   pass  #  todo update

    def get_queryset(self):
        qs = MixPost.objects.all()
        #obb = self.get_object()
        print('******')
        print(self.request.data)
        return qs

    # def get_object(self):
    #    print('!!!')
    #    print(self)
    #    print('*-------')

    # print('aaa1')
    # user.set_password(serializer.data['password'])
    # user.save()

    # queryset     = MixPost.objects.all()

    # def get_queryset(self):
    #    print('aaa11')
    #    return MixPost.objects.all()

    # def get_object(self):
    #    pk = self.kwargs.get("pk")
    #    sss = MixPost.objects.get(pk=pk)
    #    print('aaa')
    #    return MixPost.objects.get(pk=pk)

    # def put(self, request, *args, **kwargs):
    #   return self.update(request, *args, **kwargs)

    # def update(self, request, pk=None):
    #     print('aaa12')
    #    pass


class PostVer2Detail(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = PostVer2DetailSerializer

    def get(self, request, pk, format=None):
        one_post = self.get_object()
        one_post.counter = one_post.counter + 1
        serializer = PostVer2DetailSerializer(one_post)
        one_post.save()
        return Response(serializer.data)

    def get_queryset(self):
        qs = PostVer2.objects.all()
        return qs


