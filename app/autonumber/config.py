CONFIG = {
    #系统名字
    'sysname':'办案取号系统',
    'sessiontime':5*60,

    #文书类型对应的编号   这个顺序不能乱
    'documentnum':{
        '1':'鹤工商告字 [%s] %05d号',
        '2':'鹤工商听告字 [%s] %05d号',
        '3':'鹤工商处字 [%s] %05d号',
    },

    #文书类型
    'documenttype':{
        '1':'开工商告字',
        '2':'开工商听告字',
        '3':'开工商处字',
    },

    #案件类型
    'casetype':(
        (u'0', u''),
        (u'1', u'不正当竞争'),
        (u'2', u'侵害消费者权益'),
        (u'3', u'商标侵权、违反商标法'),
        (u'4', u'产品质量'),
        (u'5', u'食品安全'),
        (u'6', u'合同违法'),
        (u'7', u'其他市场违法行为'),
    ),

    #当事人类型
    'litiganttype':(
        (u'0', u''),
        (u'1', u'法人'),
    ),



    #左侧栏
    'left_panel':[
        {
            'name':'法规所',    #文书所属单位 
            'index':'1',
            'flag':[1,1,1],     #1为开启  0为关闭    对应着文书类型documenttype
        },
        {
            'name':'法规所',    #文书所属单位 
            'index':'2',
            'flag':[1,1,1],     #1为开启  0为关闭    对应着文书类型documenttype
        },
    ],
}