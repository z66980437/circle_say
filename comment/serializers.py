"""__author__ = ErYang"""
from comment.models import Comment, ComImg
from rest_framework import serializers
from user.models import User


class ComImgSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComImg
        fields = ('img_url', )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('user_id', 'nickname', 'avatar')


class CommentSerializer(serializers.ModelSerializer):
    user_info =serializers.SerializerMethodField()
    img_url = serializers.SerializerMethodField()

    @staticmethod
    def get_user_info(comment):
        return UserSerializer(comment.user).data

    @ staticmethod
    def get_img_url(comment):
        return ComImgSerializer(comment.comimg_set, many=True).data

    class Meta:
        model = Comment
        fields = ('comment_id', 'scenic', 'content', 'mark', 'clap', 'add_time', 'user_info', 'img_url')
