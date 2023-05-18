from django import template


register = template.Library()

BAD_WORDS = [
    'Мышь','мышь','глупец','Глупец','плохишь','Плохишь'
]


title = 'post.article_title'
text = 'post.text'

@register.filter()
def censor(text):
    # list = text.split()
    # censor_list = []
    # for word in list:
    #     t1 = []
    #     if t1 in BAD_WORDS:
    pass


