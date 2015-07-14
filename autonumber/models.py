# coding:utf-8
from django.db import models

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


class Case(models.Model):
    casename = models.CharField(max_length=128) #案件名称

    litigant = models.CharField(max_length=30) #当事人
    litiganttype = models.IntegerField() #当事人类型

    caseproperty = models.IntegerField() #案件性质/类型  下拉框
    casevalue = models.IntegerField() #案值/元

    fines = models.IntegerField() #罚款金额
    forfeituremoney = models.IntegerField() #没收金额

    forfeitureitem = models.CharField(max_length=128) #没收物品
    forfeitureamount = models.IntegerField() #没收数量

    illegalfacts = models.TextField() #违法事实
    law = models.TextField() #违反法律
    punishbasis = models.TextField() #处罚依据

    createdate = models.DateField() #立案日期
    informdate = models.DateField() #告知日期

    informnumber = models.CharField(max_length=128) #听证告知书/告知书编号
    issueddate = models.DateField() #处罚决定书发文日期   *** 处罚决定书的发文日期要大于或等于上一个发文日期
    decisionnumber = models.CharField(max_length=128)  #行政处罚决定书编号
    handlingunit = models.CharField(max_length=128) #办案单位
    auditorman = models.CharField(max_length=30) #核审人员（法制员）

    remarkman = models.TextField() #案件备注

    def __unicode__(self):
        return self.name

