from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    status_display=serializers.CharField(source='get_status_display', read_only=True)
    class Meta:
        model=Application
        fields=['company_name', 'role', 'link', 'location', 'applied_date', 'status', 'status_display', 'type', 'salary', 'created_at', 'updated_at']
        read_only_fields=['id', 'created_at', 'updated_at']

    def validate_salary(self, value):
        if value is not None and value<0:
            raise serializers.ValidationError("Salary Must be positive")
        return value


