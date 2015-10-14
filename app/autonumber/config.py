CONFIG = {
    #系统名字
    'sysname':'办案取号系统',
    'sessiontime':5*60,

    #文书类型
    'documenttype':{
        '1':['开工商告字','鹤工商告字 [%s] %05d号'],
        '2':['开工商听告字','鹤工商听告字 [%s] %05d号'],
        '3':['开工商处字','鹤工商处字 [%s] %05d号'],
    },

    #案件类型
    'casetype':set([
        '不正当竞争',
        '侵害消费者权益',
        '商标侵权、违反商标法',
        '产品质量',
        '食品安全',
        '合同违法',
        '其他市场违法行为',
    ]),

    #左侧栏
    'left_panel':[
        {
            'id':1,
            'name':'法规所',
            'list':{
                '开工商告字':'unit=1&type=1',# /id/documenttype
                '开工商听告字':'unit=1&type=2',
                '开工商处字':'unit=1&type=3',
            },
        },
        {
            'id':2,
            'name':'蒸够明',
            'list':{
                '样衰衰':'unit=2&type=1',# /id/documenttype
                '懒狗':'unit=2&type=2',
                '低B':'unit=2&type=3',
            },
        },
    ],
    
}