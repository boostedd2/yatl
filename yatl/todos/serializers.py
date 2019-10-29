from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        
        fields = ('title', 'body', 'start_date', 'end_date', 'expired', 'completed',)