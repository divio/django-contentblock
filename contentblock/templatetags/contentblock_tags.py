from django import template
import re
from django.utils.safestring import mark_safe
from contentblock import models as contentblock_models

register = template.Library()

class ContentblockNode(template.Node):
    def __init__(self, code, var_name):
        self.code = code
        self.var_name = var_name
    def render(self, context):
        try:
            cb = contentblock_models.ContentBlock.objects.get(code=self.code)
        except contentblock_models.ContentBlock.DoesNotExist:
            return ''
        if not cb.text:
            return ''
        placeholder = cb.text
        rendered_placeholder = mark_safe(placeholder.render(context, None))
        if self.var_name:
            context[self.var_name] = rendered_placeholder
            return ''
        return rendered_placeholder

def do_contentblock(parser, token):
    '''
    parses the parameters of the templatetag
    {% contentblock 'my_block_name' %}
    {% contentblock 'my_block_name' as my_varname %}
    '''
    try:
        # Splitting by None == splitting by spaces.
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires arguments" % token.contents.split()[0]
    m = re.search(r'(.*?) as (\w+)$', arg)
    m2 = re.search(r'(.*?)$', arg)
    if m:
        code_string, var_name = m.groups()
    elif m2 and len(m2.groups())==1:
        code_string = m2.groups()[0]
        var_name = None
    else:
        raise template.TemplateSyntaxError, "%r tag had invalid arguments" % tag_name
    if not (code_string[0] == code_string[-1] and code_string[0] in ('"', "'")):
        raise template.TemplateSyntaxError, "%r tag's argument should be in quotes" % tag_name
    return ContentblockNode(code_string[1:-1], var_name)
register.tag('contentblock', do_contentblock)