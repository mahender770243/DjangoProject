from mongoengine import InvalidQueryError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Nexus, CallDetailRecord, CellTower
from .serializers import NexusSerializer, CallDetailRecordSerializer, CellTowerSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class NexusListView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve all Nexus records",
        responses={200: NexusSerializer(many=True)}
    )
    def get(self, request):
        nexus = Nexus.objects.all()
        serializer = NexusSerializer(nexus, many=True)
        return Response(serializer.data)


class NexusDetailView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve a single Nexus record by ID",
        responses={200: NexusSerializer()}
    )
    def get(self, request, pk):
        print(f"Received Nexus ID: {pk}")
        try:
            nexus = Nexus.objects.get(id=pk)
        except Nexus.DoesNotExist:
            return Response({"error": "Nexus record not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = NexusSerializer(nexus)
        return Response(serializer.data)


class CallDetailRecordListView(APIView):

    @swagger_auto_schema(
        operation_summary="Get all call detail records",
        responses={200: CallDetailRecordSerializer(many=True)}
    )
    def get(self, request):
        records = CallDetailRecord.objects.all()
        serializer = CallDetailRecordSerializer(records, many=True)
        return Response(serializer.data)


class CallDetailRecordDetailView(APIView):

    @swagger_auto_schema(
        operation_summary="Get a call detail record by seq_id",
        responses={200: CallDetailRecordSerializer(many=True)}
    )
    def get(self, request, pk):
        try:
            cdrs = CallDetailRecord.objects.filter(seq_id=pk)
            if not cdrs:
                return Response({'error': 'Record not found'}, status=404)
            serializer = CallDetailRecordSerializer(cdrs, many=True)
            return Response(serializer.data)
        except InvalidQueryError as e:
            return Response({'error': str(e)}, status=400)


class CellTowerListView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve all Cell Tower records",
        responses={200: CellTowerSerializer(many=True)}
    )
    def get(self, request):
        cell_tower = CellTower.objects.all()
        serializer = CellTowerSerializer(cell_tower, many=True)
        return Response(serializer.data)


class CellTowerDetailView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve a single Cell Tower record by ID",
        responses={200: CellTowerSerializer()}
    )
    def get(self, request, pk):
        print(f"Received Cell Tower ID: {pk}")
        try:
            cell_tower = CellTower.objects.get(id=pk)
        except CellTower.DoesNotExist:
            return Response({"error": "Cell Tower not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CellTowerSerializer(cell_tower)
        return Response(serializer.data)


class CellTowerSearchView(APIView):
    @swagger_auto_schema(
        operation_description="Search Cell Towers by a list of IDs",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'ids': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_STRING),
                    description="List of Cell Tower IDs"
                )
            },
            required=['ids']
        ),
        responses={200: CellTowerSerializer(many=True)}
    )
    def post(self, request):
        ids = request.data.get("ids", [])
        print(ids)
        if not isinstance(ids, list):
            return Response({"error": "Expected a list of IDs"}, status=status.HTTP_400_BAD_REQUEST)

        towers = CellTower.objects.filter(id__in=ids)
        serializer = CellTowerSerializer(towers, many=True)
        return Response(serializer.data)
