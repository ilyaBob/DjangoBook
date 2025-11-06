from rest_framework import serializers


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    slug = serializers.CharField(read_only=True)


class ReaderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    slug = serializers.CharField(read_only=True)


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    slug = serializers.CharField(read_only=True)


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    author_id = serializers.IntegerField(required=False)
    reader_id = serializers.IntegerField(required=False)
    categories = serializers.ListField(
        child=serializers.IntegerField(),
    )
    slug = serializers.CharField(read_only=True)
    description = serializers.CharField()
    age = serializers.IntegerField()
    is_published = serializers.BooleanField(default=False)
    time = serializers.CharField()
