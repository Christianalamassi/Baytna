from django import template

register = template.Library()

@register.filter
def dropbox_direct_url(url):
    if url and "dropbox.com" in url:
        return url.replace("?dl=0", "?raw=1")
    return url
