from django import template
import datetime

register = template.Library()

@register.filter(name="cut")
def myCut(value, arg):
    return value.replace(arg, "#")


@register.tag(name="current_time")
def do_current_time(parse, token):
    try:
        tag_name, format_string = token.split_contents()
    except:
        raise template.TemplateSyntaxError("syntax")
    return CurrentNode(format_string[1:-1])

class CurrentNode(template.Node):
    def __init__(self, format):
        self.format_string = str(format)

    def render(self, context):
        now = datetime.datetime.now()
        return now.strftime(self.format_string)

'''
class SetVarNode(template.Node):
    def __init__(self, var_name, var_value):
        self.var_name = var_name
        self.var_value = var_value

    def render(self, context):
        try:
            value = template.Variable(self.var_value).resolve(context)
        except template.VariableDoesNotExist:
            value = ""
        context[self.var_name] = int(value)
        return 0

@register.tag(name="set")
def set_var(parser, token):
    """
        {% set <var_name>  = <var_value> %}
    """
    parts = token.split_contents()
    if len(parts) < 4:
        raise template.TemplateSyntaxError("'set' tag must be of the form:  {% set <var_name>  = <var_value> %}")
    return SetVarNode(parts[1], parts[3])
'''


class SetVarNode(template.Node):
    def __init__(self, var_name, var_value):
        self.var_name = var_name
        self.var_value = var_value
        print(var_name+"   "+var_value)

    def render(self, context):
        try:
            value = template.Variable(self.var_name).resolve(context)
        except template.VariableDoesNotExist:
            value = ""
        context[self.var_name] = int(self.var_value)
        return ""

@register.tag(name="set")
def set_var(parser, token):
    """
        {% set <var_name>  = <var_value> %}
    """
    parts = token.split_contents()
    if len(parts) < 4:
        raise template.TemplateSyntaxError("'set' tag must be of the form:  {% set <var_name>  = <var_value> %}")
    return SetVarNode(parts[1], parts[3])

@register.filter(name="to_int")
def to_int(value):
    return int(value)


@register.filter(name="getitem")
def getitem ( item, string ):
  return item.get(string,'')

@register.filter(name="key")
def key(d, key_name):
    return d[key_name]