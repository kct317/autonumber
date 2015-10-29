#coding:utf-8
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import get_user_model
from app.autonumber.models import User,RoleList,PermissionList,Case
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput
from app.autonumber.config import CONFIG

'''
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
        #验证重复用户名
        users = User.objects.filter(username__iexact=self.cleaned_data["username"])
        if not users:
            return self.cleaned_data["username"]
        raise forms.ValidationError(u"该用户名已经被使用请使用其他的昵称")

    def clean_email(self):
        #验证重复email
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
        #验证重复email
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
'''


'''
用户权限类
'''
class LoginUserForm(forms.Form):
    username = forms.CharField(label=u'账 号',error_messages={'required':u'账号不能为空'},
        widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label=u'密 码',error_messages={'required':u'密码不能为空'},
        widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None

        super(LoginUserForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = auth.authenticate(username=username,password=password)
            if self.user_cache is None:
                raise forms.ValidationError(u'账号密码不匹配')
            elif not self.user_cache.is_active:
                raise forms.ValidationError(u'此账号已被禁用')
        return self.cleaned_data

    def get_user(self):
        return self.user_cache

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label=u'原始密码',error_messages={'required':'请输入原始密码'},
        widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=u'新密码',error_messages={'required':'请输入新密码'},
        widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=u'重复输入',error_messages={'required':'请重复新输入密码'},
        widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(u'原密码错误')
        return old_password

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if len(password1)<6:
            raise forms.ValidationError(u'密码必须大于6位')

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(u'两次密码输入不一致')
        return password2

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user

class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','email','nickname','sex','role','is_active')
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'nickname' : forms.TextInput(attrs={'class':'form-control'}),
            'sex' : forms.RadioSelect(choices=((u'男', u'男'),(u'女', u'女')),attrs={'class':'list-inline'}),
            'role' : forms.Select(attrs={'class':'form-control'}),
            'is_active' : forms.Select(choices=((True, u'启用'),(False, u'禁用')),attrs={'class':'form-control'}),
        }

    def __init__(self,*args,**kwargs):
        super(AddUserForm,self).__init__(*args,**kwargs)
        self.fields['username'].label=u'账 号'
        self.fields['username'].error_messages={'required':u'请输入账号'}
        self.fields['password'].label=u'密 码'
        self.fields['password'].error_messages={'required':u'请输入密码'}
        self.fields['email'].label=u'邮 箱'
        self.fields['email'].error_messages={'required':u'请输入邮箱','invalid':u'请输入有效邮箱'}
        self.fields['nickname'].label=u'姓 名'
        self.fields['nickname'].error_messages={'required':u'请输入姓名'}
        self.fields['sex'].label=u'性 别'
        self.fields['sex'].error_messages={'required':u'请选择性别'}
        self.fields['role'].label=u'角 色'
        self.fields['is_active'].label=u'状 态'

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError(u'密码必须大于6位')
        return password

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','nickname','sex','role','is_active')
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            #'password': forms.HiddenInput,
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'nickname' : forms.TextInput(attrs={'class':'form-control'}),
            'sex' : forms.RadioSelect(choices=((u'男', u'男'),(u'女', u'女')),attrs={'class':'list-inline'}),
            'role' : forms.Select(choices=[(x.name,x.name) for x in RoleList.objects.all()],attrs={'class':'form-control'}),
            'is_active' : forms.Select(choices=((True, u'启用'),(False, u'禁用')),attrs={'class':'form-control'}),
        }

    def __init__(self,*args,**kwargs):
        super(EditUserForm,self).__init__(*args,**kwargs)
        self.fields['username'].label=u'账 号'
        self.fields['username'].error_messages={'required':u'请输入账号'}
        self.fields['email'].label=u'邮 箱'
        self.fields['email'].error_messages={'required':u'请输入邮箱','invalid':u'请输入有效邮箱'}
        self.fields['nickname'].label=u'姓 名'
        self.fields['nickname'].error_messages={'required':u'请输入姓名'}
        self.fields['sex'].label=u'性 别'
        self.fields['sex'].error_messages={'required':u'请选择性别'}
        self.fields['role'].label=u'角 色'
        self.fields['is_active'].label=u'状 态'

    def clean_password(self):
        return self.cleaned_data['password']

class RoleListForm(forms.ModelForm):
    class Meta:
        model = RoleList
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'permission' : forms.SelectMultiple(attrs={'class':'form-control','size':'10','multiple':'multiple'}),
            #'permission' : forms.CheckboxSelectMultiple(choices=[(x.id,x.name) for x in PermissionList.objects.all()]),
        }

    def __init__(self,*args,**kwargs):
        super(RoleListForm,self).__init__(*args,**kwargs)
        self.fields['name'].label=u'名 称'
        self.fields['name'].error_messages={'required':u'请输入名称'}
        self.fields['permission'].label=u'URL'
        self.fields['permission'].required=False

class PermissionListForm(forms.ModelForm):
    class Meta:
        model = PermissionList
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'url' : forms.TextInput(attrs={'class':'form-control'}),
        }

    def __init__(self,*args,**kwargs):
        super(PermissionListForm,self).__init__(*args,**kwargs)
        self.fields['name'].label=u'名 称'
        self.fields['name'].error_messages={'required':u'请输入名称'}
        self.fields['url'].label=u'URL'
        self.fields['url'].error_messages={'required':u'请输入URL'}


'''
系统业务类
'''
class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ('casename','caseproperty','casecreater','documentunit','documenttype',
                  'litigant','litiganttype','casevalue','fines','forfeituremoney',
                  'forfeitureitem','forfeitureamount','illegalfacts','law','punishbasis',
                  'createdate','informdate','informnumber','issueddate','decisionnumber',
                  'handlingunit','auditorman','remarkman')
        widgets = {
            'casename' : forms.TextInput(attrs={'class':'form-control'}),
            'caseproperty' : forms.Select(attrs={'class':'form-control'}),
            'casecreater' : forms.TextInput(attrs={'class':'form-control'}),
            'creater' : forms.Select(attrs={'class':'form-control'}),

            'documentunit' : forms.TextInput(attrs={'class':'form-control'}),
            'documenttype' : forms.TextInput(attrs={'class':'form-control'}),

            'litigant' : forms.TextInput(attrs={'class':'form-control'}),
            'litiganttype' : forms.TextInput(attrs={'class':'form-control'}),

            'casevalue' : forms.TextInput(attrs={'class':'form-control'}),
            'fines' : forms.TextInput(attrs={'class':'form-control'}),
            'forfeituremoney' : forms.TextInput(attrs={'class':'form-control'}),

            'forfeitureitem' : forms.TextInput(attrs={'class':'form-control'}),
            'forfeitureamount' : forms.TextInput(attrs={'class':'form-control'}),

            'illegalfacts' : forms.TextInput(attrs={'class':'form-control'}),
            'law' : forms.TextInput(attrs={'class':'form-control'}),
            'punishbasis' : forms.TextInput(attrs={'class':'form-control'}),

            'createdate' : forms.TextInput(attrs={'class':'form-control'}),
            'informdate' : forms.TextInput(attrs={'class':'form-control'}),

            'informnumber' : forms.TextInput(attrs={'class':'form-control'}),
            'issueddate' : forms.TextInput(attrs={'class':'form-control'}),
            'decisionnumber' : forms.TextInput(attrs={'class':'form-control'}),
            'handlingunit' : forms.TextInput(attrs={'class':'form-control'}),
            'auditorman' : forms.TextInput(attrs={'class':'form-control'}),

            'remarkman' : forms.TextInput(attrs={'class':'form-control'}),
        }

    def __init__(self,*args,**kwargs):
        super(CaseForm,self).__init__(*args,**kwargs)
        self.fields['casename'].label=u'案件名称'
        self.fields['casename'].error_messages={'required':u'请输入案件名称'}
        self.fields['caseproperty'].label=u'案件性质'
        self.fields['caseproperty'].error_messages={'required':u'请选择案件性质'}
        self.fields['casecreater'].label=u'案件录入员'
        self.fields['casecreater'].required=False

        self.fields['documentunit'].label=u'文书所属单位'
        self.fields['documentunit'].required=False
        self.fields['documenttype'].label=u'文书类型'
        self.fields['documenttype'].required=False

        self.fields['litigant'].label=u'当事人'
        self.fields['litigant'].required=False
        self.fields['litiganttype'].label=u'当事人类型'
        self.fields['litiganttype'].required=False

        self.fields['casevalue'].label=u'案值/元'
        self.fields['casevalue'].required=False
        self.fields['fines'].label=u'罚款金额'
        self.fields['fines'].required=False
        self.fields['forfeituremoney'].label=u'没收金额'
        self.fields['forfeituremoney'].required=False

        self.fields['forfeitureitem'].label=u'没收物品'
        self.fields['forfeitureitem'].required=False
        self.fields['forfeitureamount'].label=u'没收数量'
        self.fields['forfeitureamount'].required=False

        self.fields['illegalfacts'].label=u'违法事实'
        self.fields['illegalfacts'].required=False
        self.fields['law'].label=u'违反法律'
        self.fields['law'].required=False
        self.fields['punishbasis'].label=u'处罚依据'
        self.fields['punishbasis'].required=False

        self.fields['createdate'].label=u'立案日期'
        self.fields['createdate'].required=False
        self.fields['informdate'].label=u'告知日期'
        self.fields['informdate'].required=False

        self.fields['informnumber'].label=u'听证告知书'
        self.fields['informnumber'].required=False
        self.fields['issueddate'].label=u'处罚决定书发文日期'
        self.fields['issueddate'].required=False
        self.fields['decisionnumber'].label=u'行政处罚决定书编号'
        self.fields['decisionnumber'].required=False
        
        self.fields['handlingunit'].label=u'办案单位'
        self.fields['handlingunit'].required=False
        self.fields['auditorman'].label=u'核审人员（法制员）'
        self.fields['auditorman'].required=False

        self.fields['remarkman'].label=u'案件备注'
        self.fields['remarkman'].required=False
