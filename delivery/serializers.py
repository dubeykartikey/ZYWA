from rest_framework import serializers

from delivery.models import CsvFiles, Delivery

class FileSerializer(serializers.Serializer):
    class Meta:
        model = CsvFiles
        fields = ['file']
        
class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['id', 'user_contact', 'card_id', 'timestamp', 'comment', 'created_date']