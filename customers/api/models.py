
from mongoengine import Document, StringField, DateTimeField, IntField, DecimalField

class Nexus(Document):
    meta ={'collection':'DataNexus','db_alias':'cdr_db'}
    id = StringField(primary_key=True)  # <--- Important
    CDRNo_Or_ImeiNo = StringField()
    Day = IntField()
    Duplicate = IntField()
    FromDate = DateTimeField()
    Inserted = IntField()
    InsertedAt = DateTimeField()
    MaxDur = IntField()
    MinDur = IntField()
    Month = IntField()
    RecordType = StringField()
    Skipped = IntField()
    Tac_Or_Mobile_Code = StringField()
    ToDate = DateTimeField()
    Year = IntField()

class CallDetailRecord(Document):
    meta = {'collection': 'CallDetailRecords','strict': False ,'db_alias':'cdr_db'}  # Optional, to explicitly set the collection name

    id = StringField(primary_key=True)  # Mongo _id field is a string
    A_Party = StringField()
    a_mobile_code = StringField()
    B_Party = StringField()
    b_mobile_code = StringField()
    SDateTime = DateTimeField()
    EDateTime = DateTimeField()
    Duration = IntField()
    SDate = DateTimeField()
    STime = StringField()
    FileCallType = StringField()
    Call_Type = StringField()
    LRN = StringField()
    First_CGI = StringField()
    Last_CGI = StringField()
    IMEI = StringField()
    Con_Type = StringField()
    First_Lat = DecimalField(precision=5)
    First_Long = DecimalField(precision=5)
    Last_Lat = DecimalField(precision=5)
    Last_Long = DecimalField(precision=5)
    FileServiceType = StringField()
    IMEI_TAC = StringField()
    seq_id = StringField(required=True)

class CellTower(Document):
    meta = {'collection': 'TowerAddress', 'strict': False, 'db_alias': 'cell_db','indexes':["CGI"]}
    id = StringField(primary_key=True)  # Assuming _id is a string
    Address = StringField(required=True)
    Azimuth = IntField()
    CGI = StringField(required=True)
    CellId = StringField(required=True)
    Lat = DecimalField(required=True)  # Lat as DecimalField
    Long = DecimalField(required=True)  # Long as DecimalField
    MainCity = StringField()
    Mcc = StringField()
    Mnc = StringField()
    SubCity = StringField()
    Type = StringField()
