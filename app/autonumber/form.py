#coding:utf-8
from django import forms
from django.db import models
from django.contrib.auth.models import User
from app.autonumber.models import Manager, Database, CaseProperty
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput
from app.autonumber.config import CONFIG

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=u"用户名",
        error_messages={'required': '请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"用户名",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label=u"密码",
        error_messages={'required': u'请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"密码",
            }
        ),
    )   
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"用户名和密码为必填项")
        else:
            cleaned_data = super(LoginForm, self).clean() 

class ChangepwdForm(forms.Form):
    oldpassword = forms.CharField(
        required=True,
        label=u"原密码",
        error_messages={'required': u'请输入原密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"原密码",
            }
        ),
    ) 
    newpassword1 = forms.CharField(
        required=True,
        label=u"新密码",
        error_messages={'required': u'请输入新密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"新密码",
            }
        ),
    )
    newpassword2 = forms.CharField(
        required=True,
        label=u"确认密码",
        error_messages={'required': u'请再次输入新密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"确认密码",
            }
        ),
     )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"所有项都为必填项")
        elif self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
            raise forms.ValidationError(u"两次输入的新密码不一样")
        else:
            cleaned_data = super(ChangepwdForm, self).clean()
        return cleaned_data

class RegisterForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=u"用户名",
        error_messages={'required': '请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"用户名",
            }
        ),
    )
    password1 = forms.CharField(
        required=True,
        label=u"密码",
        error_messages={'required': u'请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"密码",
            }
        ),
    )
    password2 = forms.CharField(
        required=True,
        label=u"确认密码",
        error_messages={'required': u'请再次输入新密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"确认密码",
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        label=u"邮箱",
        error_messages={'required': u'请再次输入邮箱'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"邮箱",
            }
        ),
    )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"所有项都为必填项")
        elif self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError(u"两次输入的密码不一样")
        else:
            cleaned_data = super(RegisterForm, self).clean()
        return cleaned_data

    def clean_username(self):
        '''验证重复用户名'''
        users = User.objects.filter(username__iexact=self.cleaned_data["username"])
        if not users:
            return self.cleaned_data["username"]
        raise forms.ValidationError(u"该用户名已经被使用请使用其他的昵称")

    def clean_email(self):
        '''验证重复email'''
        emails = User.objects.filter(email__iexact=self.cleaned_data["email"])
        if not emails:
            return self.cleaned_data["email"]
        raise forms.ValidationError(u"该邮箱已经被使用请使用其他的")

class ForgetPwdForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label=u"邮箱",
        error_messages={'required': u'请再次输入邮箱'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"邮箱",
            }
        ),
    )

    def clean_email(self):
        '''验证重复email'''
        emails = User.objects.filter(email__iexact=self.cleaned_data["email"])
        if emails:
            return self.cleaned_data["email"]
        raise forms.ValidationError(u"该邮箱还没注册")

class CreatetaskForm(forms.Form):
    creater = forms.CharField(
        label=u"创建者",
        widget=BootstrapUneditableInput()
    )
    manager = forms.ModelChoiceField(
        queryset=Manager.objects.all(),
        required=True,
        label=u"项目负责人",
        error_messages={'required': u'必选项'},
    )  
    databases = forms.ModelMultipleChoiceField(
        queryset=Database.objects.order_by('id'),
        required=True,
        label=u"数据库",
        error_messages={'required': u'至少选择一个'},
        widget=forms.CheckboxSelectMultiple,
    )    
    sql = forms.CharField(
        required=False,
        label=u"执行SQL",
        widget=forms.Textarea(
            attrs={
                'placeholder':"请在表名前加上schema，如hospital要写成p95169.hospital",
                'rows':5,
                'style':"width:100%",
            }
        ),
    )
    desc = forms.CharField(
        required=False,
        label=u"描述",
        widget=forms.Textarea(
            attrs={
                'placeholder':"如果不是执行SQL(如数据的导入导出等)，一定要在描述里说清楚",
                'rows':5,
                'style':"width:100%",
            }
        ),
    ) 
    attachment = forms.FileField(
        required=False,
        label=u"附件",
        help_text=u"如果SQL文本过长，超过2000个字符，请上传附件"
    )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"以下红色标记部分为必选项")
        elif self.cleaned_data['sql'] == u'' and self.cleaned_data['desc'] == u'' :
            raise forms.ValidationError(u"如果执行SQL为空，描述为必填项")
        else:
            cleaned_data = super(CreatetaskForm, self).clean() 
        return cleaned_data

class CreateCaseForm(forms.Form):
    creater = forms.CharField(
        label=u"创建者",
        widget=BootstrapUneditableInput()
    )
    casename = forms.CharField(
        required=True,
        label=u"案件名称",
        widget=BootstrapUneditableInput()
    )
    caseproname = forms.ModelChoiceField(
        queryset=CaseProperty.objects.values_list("caseproname",flat=True),
        required=True,
        label=u"案件类型",
        error_messages={'required': u'必选项'},
    )
    litigant = forms.CharField(
        required=False,
        label=u"当事人",
        error_messages={'required': '请输入当事人'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"当事人",
            }
        ),
    )
    litiganttype = forms.CharField(
        required=False,
        label=u"当事人类型",
        error_messages={'required': '请输入当事人类型'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"当事人类型",
            }
        ),
    )
    casevalue = forms.CharField(
        required=False,
        label=u"案值",
        error_messages={'required': '请输入案值'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"案值",
            }
        ),
    )
    fines = forms.CharField(
        required=False,
        label=u"罚款金额",
        error_messages={'required': '请输入罚款金额'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"罚款金额",
            }
        ),
    )
    forfeituremoney = forms.CharField(
        required=False,
        label=u"没收金额",
        error_messages={'required': '请输入没收金额'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"没收金额",
            }
        ),
    )
    forfeitureitem = forms.CharField(
        required=False,
        label=u"没收物品",
        error_messages={'required': '请输入没收物品'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"没收物品",
            }
        ),
    )
    illegalfacts = forms.CharField(
        required=False,
        label=u"违法事实",
        error_messages={'required': '请输入违法事实'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"违法事实",
            }
        ),
    )
    law = forms.CharField(
        required=False,
        label=u"违反法律",
        error_messages={'required': '请输入违反法律'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"违反法律",
            }
        ),
    )
    punishbasis = forms.CharField(
        required=True,
        label=u"处罚依据",
        error_messages={'required': '请输入处罚依据'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"处罚依据",
            }
        ),
    )
    #createdate = forms.DateTimeField(
    #    widget=widgets.AdminDateWidget(), 
    #    label=u'立案日期'
    #)
    informdate = forms.CharField(
        required=True,
        label=u"立案日期",
        error_messages={'required': '请输入立案日期'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"立案日期",
            }
        ),
    )
    litiganttype = forms.CharField(
        required=True,
        label=u"当事人类型",
        error_messages={'required': '请输入当事人类型'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"当事人类型",
            }
        ),
    )
    litiganttype = forms.CharField(
        required=True,
        label=u"当事人类型",
        error_messages={'required': '请输入当事人类型'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"当事人类型",
            }
        ),
    )
    litiganttype = forms.CharField(
        required=True,
        label=u"当事人类型",
        error_messages={'required': '请输入当事人类型'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"当事人类型",
            }
        ),
    )
    litiganttype = forms.CharField(
        required=True,
        label=u"当事人类型",
        error_messages={'required': '请输入当事人类型'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"当事人类型",
            }
        ),
    )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"以下红色标记部分为必选项")
        elif self.cleaned_data['sql'] == u'' and self.cleaned_data['desc'] == u'' :
            raise forms.ValidationError(u"如果执行SQL为空，描述为必填项")
        else:
            cleaned_data = super(CreatetaskForm, self).clean() 
        return cleaned_data


"""
#登录相关form    旧版

from django import forms
class UserForm(forms.Form): 
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

    def as_myp(self):
        "Returns this form rendered as HTML <p>s."
        return self._html_output(
            normal_row = '<div class="form-group">%(label)s</div> <div class="form-group">%(field)s</div>',
            #normal_row = '<p%(html_class_attr)s>%(label)s</p> <p%>(field)s</p>',
            error_row = '%s',
            row_ender = '</p>',
            help_text_html = ' <span class="helptext">%s</span>',
            errors_on_separate_row = True)

    def as_plain(self):
        "Returns this form rendered as HTML <tr>s -- excluding the <table></table>."
        return self._html_output(
            normal_row = '%(label)s%(errors)s%(field)s%(help_text)s',
            error_row = '%s',
            row_ender = ' ',
            help_text_html = '<br /><span class="helptext">%s</span>',
            errors_on_separate_row = False)
"""