from django import template


register = template.Library()

BAD_WORDS = [
    'Мышь','мышь','глупец','Глупец','плохишь','Плохишь'
]


title = 'post.article_title'
text = 'post.text'

@register.filter()
def censor(text):
    list = text.split()
    censor_list = []
    for word in list:
        if word in BAD_WORDS:
            censor_word = word[0] * '*'
            censor_list.append(word.replace(word, censor_word))
        else:
            censor_list.append(word)

    return censor_list




