# coding:utf-8
from django.db import models
from datetime import datetime
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
"""
每个类都包含字段及相应的OP函数，
然后在views.py直接调用
    from autonumber.models import * 
    在具体的函数里面新建对象，调用方法，返回结果作为字典参数传入render的网页模板


外键forignkey
    class B(models.Model):
        val = models.ForeignKey(类A)     类B的外键val是关联类A

多对多many-to-many
    class B(models.Model):
        val = models.ManyToManyField(类A)     类B的ManyToMany val是关联类A
        val1 = A()                            可以新建自定义类
    m = B。objects.get(id=1)
    m.val.filter(类字段名字_icontains='p')
"""

"""
class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')

    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def my_property(self):
        return self.first_name + ' ' + self.last_name
    my_property.short_description = "Full name of the person"

    full_name = property(my_property)

    def __str__(self):
        return self.first_name + self.last_name

    def __unicode__(self):
        return self.first_name + self.last_name
"""
"""
class UserGroup(models.Model):
    gid        = models.AutoField(primary_key=True)
    groupname  = models.CharField(max_length=50, default='')
    power      = models.IntegerField(default=0)
    createtime = models.IntegerField(default=0)
    updatetime = models.IntegerField(default=0)

    def __unicode__(self):
        return self.groupname

class User(models.Model):
    uid        = models.AutoField(primary_key=True)
    gid        = models.IntegerField(default=0)
    username   = models.CharField(max_length=50, default='')
    password   = models.CharField(max_length=50, default='')   #md5加密
    superman   = models.BooleanField(default=False)
    lastip     = models.CharField(max_length=50, default='')
    createtime = models.IntegerField(default=0)
    updatetime = models.IntegerField(default=0)

    def __unicode__(self):
        return self.username

class UserLog(models.Model):
    logid      = models.AutoField(primary_key=True)
    uid        = models.IntegerField(default=0)
    username   = models.CharField(max_length=50, default='')
    msg        = models.TextField(default='')
    ip         = models.CharField(max_length=50, default='')
    createtime = models.IntegerField(default=0)

    def __unicode__(self):
        return self.msg
"""


class PermissionList(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s(%s)' % (self.name,self.url)

class RoleList(models.Model):
    name = models.CharField(max_length=64)
    #permission = models.ManyToManyField(PermissionList,null=True,blank=True)
    permission = models.ManyToManyField(PermissionList)

    def __unicode__(self):
        return self.name

class UserManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user = self.create_user(email,
            username = username,
            password = password,
        )

        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True, db_index=True)
    email = models.EmailField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    nickname = models.CharField(max_length=64, null=True)
    sex = models.CharField(max_length=2, null=True)
    role = models.ForeignKey(RoleList,null=True,blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def has_perm(self,perm,obj=None):
        if self.is_active and self.is_superuser:
            return True



class CaseProperty(models.Model):
    caseproname      = models.CharField(max_length=128, default='') #案件性质类型名称
    def __unicode__(self):
        return self.caseproname

class Case(models.Model):
    caseid           = models.AutoField(primary_key=True)
    casename         = models.CharField(max_length=128, default='') #案件名称
    caseproperty     = models.ForeignKey(CaseProperty)              #案件性质/类型  下拉框
    casecreater      = models.CharField(max_length=128, default='') #立案人
    creater          = models.ForeignKey(User)              #案件录入员

    documentunit     = models.IntegerField(default=0) #文书所属单位
    documenttype     = models.IntegerField(default=0) #文书类型

    litigant         = models.CharField(max_length=30, default='') #当事人
    litiganttype     = models.IntegerField(default=0)              #当事人类型

    casevalue        = models.IntegerField(default=0) #案值/元
    fines            = models.IntegerField(default=0) #罚款金额
    forfeituremoney  = models.IntegerField(default=0) #没收金额

    forfeitureitem   = models.CharField(max_length=128, default='') #没收物品
    forfeitureamount = models.IntegerField(default='')              #没收数量

    illegalfacts     = models.TextField(default='') #违法事实
    law              = models.TextField(default='') #违反法律
    punishbasis      = models.TextField(default='') #处罚依据

    createdate       = models.DateTimeField(default=datetime.now()) #立案日期
    informdate       = models.DateTimeField(default=datetime.now()) #告知日期

    informnumber     = models.CharField(max_length=128, default='') #听证告知书/告知书编号  鹤工商告字 [2015] 00001号
    issueddate       = models.DateTimeField(default=datetime.now()) #处罚决定书发文日期   *** 处罚决定书的发文日期要大于或等于上一个发文日期
    decisionnumber   = models.CharField(max_length=128, default='')  #行政处罚决定书编号   鹤工商处字 [2015] 00001号
    handlingunit     = models.CharField(max_length=128, default='') #办案单位
    auditorman       = models.CharField(max_length=30, default='') #核审人员（法制员）

    remarkman        = models.TextField(default='') #案件备注

    def __unicode__(self):
        return self.casename


'''
class Manager(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, default='')
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    email = models.EmailField(max_length=70, default='')
    def __unicode__(self):
        return self.last_name + self.first_name

class Dba(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, default='')
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    email = models.EmailField(max_length=70, default='')
    def __unicode__(self):
        return self.last_name + self.first_name

class State(models.Model):
    id = models.AutoField(primary_key=True)
    statename = models.CharField(max_length=20, default='')
    def __unicode__(self):
        return self.statename

class Database(models.Model):
    id = models.AutoField(primary_key=True)
    databasename = models.CharField(max_length=30, default='')
    databaseip = models.CharField(max_length=30, default='')
    def __unicode__(self):
        return self.databasename + ' - ' + self.databaseip

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    creater = models.ForeignKey(User)
    manager = models.ForeignKey(Manager)
    dba = models.ForeignKey(Dba)
    state = models.ForeignKey(State)
    databases = models.ManyToManyField(Database)
    sql = models.CharField(max_length=2000,blank=True,null=True)
    desc = models.CharField(max_length=2000,blank=True, null=True)
    createdtime = models.DateTimeField()
    lastupdatedtime = models.DateTimeField(blank=True,null=True)
    dbacomment = models.CharField(max_length=2000,blank=True,null=True)
    attachment = models.FileField(upload_to='tasks',blank=True,null=True)
    def __unicode__(self):
        return str(self.id)
'''



