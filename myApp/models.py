from django.db import models

# Create your models here.
class Group(models.Model):
    GRP_NM=models.CharField(max_length=20,blank=True)
    GRP_STUS=models.BooleanField(default=True)
    CREATED_BY=models.CharField(max_length=24,blank=True)
    CREATE_TS=models.DateTimeField(auto_now_add=True, blank=True)
    UPDATED_BY=models.CharField(max_length=24,blank=True)
    UPDATE_TS=models.DateTimeField(auto_now_add=True, blank=True)
    GRP_CD=models.IntegerField()

    def __str__(self):
        return self.GRP_NM
    class Meta:
        db_table = 'BP_GROUPS'
        verbose_name='bp_group'

class Users(models.Model):
    EMAIL_ID = models.EmailField(max_length=50)
    FRST_NM = models.CharField(max_length=255)
    LST_NM = models.CharField(max_length=255)
    UESR_STUS=models.BooleanField(default=True)
    GRP_ID=models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    CREATE_TS=models.DateTimeField(auto_now_add=True, blank=True)
    UPDATE_TS=models.DateTimeField(auto_now_add=True, blank=True)
    CREATED_BY=models.CharField(max_length=24,blank=True)
    UPDATED_BY=models.CharField(max_length=24,blank=True)
    AUTH_GRP_CD=models.CharField(max_length=1,blank=True)
    EXP_DATE=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.FRST_NM} {self.LST_NM}'

    class Meta:
        db_table='BP_USERS'
        verbose_name='bp_user'

class LanID(models.Model):
    BP_LANID = models.CharField(max_length=50)

    def __unicode__(self):
        return self.BP_LANID

    class Meta:
        db_table='BP_LANID'
        verbose_name='bp_lanid'

    