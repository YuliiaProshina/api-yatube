from rest_framework import serializers

from posts.models import User, Group, Comment, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
        ref_name = 'ReadOnlyUsers'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'title', 'slug', 'description']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'text', 'created']
        read_only_fields = ('author', 'post', 'created')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Post
        fields = ['id', 'text', 'pub_date', 'author', 'image', 'group']
        read_only_fields = (
            'author',
            'pub_date',
        )
