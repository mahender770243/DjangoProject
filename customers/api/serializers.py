from rest_framework import serializers
from .models import Nexus, CellTower
from decimal import Decimal, InvalidOperation

class SafeDecimalField(serializers.DecimalField):
    def to_representation(self, value):
        try:
            return super().to_representation(value)
        except (InvalidOperation, TypeError, ValueError):
            return None  # or 0 or float(value) if needed

class NexusSerializer(serializers.Serializer):
    id = serializers.CharField()
    CDRNo_Or_ImeiNo = serializers.CharField()
    Day = serializers.IntegerField()
    Duplicate = serializers.IntegerField()
    FromDate = serializers.DateTimeField()
    Inserted = serializers.IntegerField()
    InsertedAt = serializers.DateTimeField()
    MaxDur = serializers.IntegerField()
    MinDur = serializers.IntegerField()
    Month = serializers.IntegerField()
    RecordType = serializers.CharField()
    Skipped = serializers.IntegerField()
    Tac_Or_Mobile_Code = serializers.CharField()
    ToDate = serializers.DateTimeField()
    Year = serializers.IntegerField()

class CallDetailRecordSerializer(serializers.Serializer):
    id = serializers.CharField()
    A_Party = serializers.CharField()
    a_mobile_code = serializers.CharField()
    B_Party = serializers.CharField()
    b_mobile_code = serializers.CharField()
    SDateTime = serializers.DateTimeField()
    EDateTime = serializers.DateTimeField()
    Duration = serializers.IntegerField()
    SDate = serializers.DateTimeField()
    STime = serializers.CharField()
    FileCallType = serializers.CharField()
    Call_Type = serializers.CharField()
    LRN = serializers.CharField()
    First_CGI = serializers.CharField()
    Last_CGI = serializers.CharField()
    IMEI = serializers.CharField()
    Con_Type = serializers.CharField()
    First_Lat = SafeDecimalField(max_digits=9, decimal_places=5, required=False)
    First_Long = SafeDecimalField(max_digits=9, decimal_places=5, required=False)
    Last_Lat = SafeDecimalField(max_digits=9, decimal_places=5, required=False)
    Last_Long = SafeDecimalField(max_digits=9, decimal_places=5, required=False)
    FileServiceType = serializers.CharField()
    IMEI_TAC = serializers.CharField()
    seq_id = serializers.CharField()

    First_CGI_Detail = serializers.SerializerMethodField(help_text="Detailed info of First_CGI")
    Last_CGI_Detail = serializers.SerializerMethodField(help_text="Detailed info of Last_CGI")

    def get_First_CGI_Detail(self, obj):
        try:
            tower = CellTower.objects.get(CGI=obj.First_CGI)
            return CellTowerSerializer(tower).data
        except CellTower.DoesNotExist:
            return None

    def get_Last_CGI_Detail(self, obj):
        try:
            tower = CellTower.objects.get(CGI=obj.Last_CGI)
            return CellTowerSerializer(tower).data
        except CellTower.DoesNotExist:
            return None


class CellTowerSerializer(serializers.Serializer):
    id = serializers.CharField(help_text="Cell tower unique ID")
    Address = serializers.CharField(help_text="Physical address of the tower")
    Azimuth = serializers.IntegerField(required=False, help_text="Tower azimuth angle")
    CGI = serializers.CharField(help_text="Cell Global Identity")
    CellId = serializers.CharField(help_text="Cell ID")
    Lat = serializers.DecimalField(max_digits=9, decimal_places=6, help_text="Latitude")
    Long = serializers.DecimalField(max_digits=9, decimal_places=6, help_text="Longitude")
    MainCity = serializers.CharField(required=False)
    Mcc = serializers.CharField(required=False)
    Mnc = serializers.CharField(required=False)
    SubCity = serializers.CharField(required=False)
    Type = serializers.CharField(required=False)



