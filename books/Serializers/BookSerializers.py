
from rest_framework import serializers
from ..models import Books

class BookSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Books
        fields = "__all__"
        read_only_fields = ('book_id',)
