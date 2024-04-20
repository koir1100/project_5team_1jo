from rest_framework import serializers
from books.models import RecomBooks
from django.contrib.auth.models import User
from rest_framework.response import Response
import json

#모델에 대한 시리얼라이저
class RecomBooksSerializer(serializers.Serializer):
    #필드 정의
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=100)
    recomment = serializers.CharField(max_length=2000) #자료내용(코멘트)
    recomno = serializers.CharField(max_length=20) #20자리의 번호 코드는 IntegerField의 범위를 넘음, 문자열 형태로 받아야 함
    drcode = serializers.IntegerField() #분류 번호

    #신규 생성
    def create(self, validated_data):
        return RecomBooks.objects.create(**validated_data)
    
    #인스턴스 갱신
    def update(self, instance, validated_data):
        #OrderedDict type
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.recomment = validated_data.get('recomment', instance.recomment)
        instance.recomno = validated_data.get('recomno', instance.recomno)
        instance.drcode = validated_data.get('drcode', instance.drcode)
        instance.keyword = validated_data.get('keyword', instance.keyword)
        instance.save()
        return instance

#키워드 시리얼라이저 별도
class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model= RecomBooks
        fields=['keyword']

    #시리얼라이저 적용 후 dict에 대한 ['keyword']와 동일함
    def get_keyword(self):
        instance = self.instance
        if instance:
            return instance.keyword
        return None

class RecomBooksListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    keyword = serializers.SerializerMethodField()
    recomno = serializers.CharField(max_length=20)

    class Meta:
        model = RecomBooks
        fields = ['id', 'title', 'drcode', 'author', 'keyword', 'recomno']
        datatales_always_serialize = ('id',)
    
    def get_keyword(self, obj):
        keyword = json.loads(obj.keyword)[:3]
        return keyword

class RecomBooksDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecomBooks
        fields = ['id', 'title', 'author', 'keyword', 'recomment', 'recomno']