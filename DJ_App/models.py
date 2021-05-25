from django.db import models


# Create your models here.
class user_date(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    username = models.CharField(max_length=20, unique=True, null=False)
    password = models.CharField(max_length=50, null=False)


class memInfoList(models.Model):
    id = models.AutoField(primary_key=True, null=False, unique=True)
    username = models.CharField(max_length=20, null=False)
    nation = models.CharField(max_length=20, null=False)
    NP = models.CharField(max_length=20, null=False)
    birthplace = models.CharField(max_length=30, null=False)
    sex = models.CharField(max_length=10, null=False)
    birthday = models.CharField(max_length=30, null=False)
    health = models.CharField(max_length=10, null=False)
    tel = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=50, null=False)
    education = models.CharField(max_length=6, null=False)
    expText = models.CharField(max_length=10000, null=True)
    writername = models.CharField(max_length=20, null=False, unique=True)
    writedate = models.CharField(max_length=100, null=False)


class COMECOList(models.Model):
    id = models.AutoField(primary_key=True, null=False, unique=True)
    ProjectNM = models.CharField(max_length=100, null=False)
    ProjectCost = models.FloatField(null=False)
    ProjectClass = models.CharField(max_length=50, null=False, default='其它项目')
    writername = models.CharField(max_length=20, null=False)
    writedate = models.CharField(max_length=100, null=False)


class COMECIList(models.Model):
    id = models.AutoField(primary_key=True, null=False, unique=True)
    ProjectNM = models.CharField(max_length=100, null=False)
    ProjectGot = models.FloatField(null=False)
    ProjectClass = models.CharField(max_length=50, null=False, default='其它项目')
    writername = models.CharField(max_length=20, null=False)
    writedate = models.CharField(max_length=100, null=False)


class ProductionList(models.Model):
    id = models.AutoField(primary_key=True, null=False, unique=True)
    ProductionNM = models.CharField(max_length=100, null=False)
    ProductionUnitPrice = models.FloatField(null=False)
    ProductionSoldNum = models.FloatField(null=False)
    ProductionPrice = models.FloatField(null=False)
    ProductionSoldDate = models.CharField(max_length=100, null=False)


class InfoList(models.Model):
    id = models.AutoField(primary_key=True, null=False, unique=True)
    TextContent = models.CharField(max_length=10000, null=False)
    writername = models.CharField(max_length=20, null=False)
    writedate = models.CharField(max_length=100, null=False)


class administratorNameList(models.Model):
    id = models.AutoField(primary_key=True, null=False, unique=True)
    adminname = models.CharField(max_length=20, null=False)
    adminPVLevel = models.IntegerField(null=False)
