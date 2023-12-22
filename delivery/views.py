from datetime import datetime
from http import HTTPStatus
import os
from django.http import HttpResponse
from django.shortcuts import render
import csv
from ZywaDelivery.settings import BASE_DIR
from delivery.models import CsvFiles, Delivery

from delivery.serializers import DeliverySerializer, FileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

@api_view(['POST', 'GET'])
def file_upload(request):
    if request.method == 'GET':
        return render(request, 'FileUploadTemplate.html')
    
    elif request.method == 'POST':
        payload = request.FILES['file']
        file = CsvFiles.objects.create(file=payload, file_name=payload)

        with open(str(file.file), 'r') as importedFile:
            csvFile = csv.DictReader(importedFile)
            for row in csvFile:
                try:
                    contact = row.get('User Mobile').strip("\"") if len(row.get('User Mobile')) == 9 else row.get('User Mobile')[2:].strip("\"")
                except:
                    contact = row.get('User contact').strip("\"") if len(row.get('User contact')) == 9 else row.get('User contact')[2:].strip("\"")
                
                data = Delivery.objects.create(
                    card_id = row.get('Card ID'),
                    user_contact = contact,
                    timestamp = row.get('Timestamp'),
                    comment = row.get('Comment')
                )
                
        return HttpResponse('Done')

@api_view(['GET'])
def all_status(request, id):
    try:
        card_status = Delivery.objects.filter(Q(card_id = id) | Q(user_contact = id))
        serializer = DeliverySerializer(card_status, many=True)
        return Response(data=serializer.data, status=HTTPStatus.OK)
    except:
        return Response(data=None, status=HTTPStatus.BAD_REQUEST)

@api_view(['GET'])
def current_status(request, id):
    try:
        card_status = Delivery.objects.filter(Q(card_id = id) | Q(user_contact = id)).order_by('timestamp')[::-1][0]
        serializer = DeliverySerializer(card_status)
        return Response(data=serializer.data, status=HTTPStatus.OK)
    except:
        return Response(data=None, status=HTTPStatus.BAD_REQUEST)