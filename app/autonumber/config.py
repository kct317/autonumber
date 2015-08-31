CONFIG = {
    #系统名字
    'sysname':'办案取号系统',

    #文书类型
    'documenttype':[
        '开工商告字',
        '开工商听告字',
        '开工商处字',
    ],

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