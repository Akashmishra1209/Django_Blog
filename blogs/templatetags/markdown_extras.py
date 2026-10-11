import markdown
from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter
@stringfilter
def convert_markdown_to_html(value):
    md = markdown.markdown(
        value,
        extensions=["markdown.extensions.fenced_code",
                    "markdown.extensions.tables"],
    )
    return md