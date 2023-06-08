from django import template


register = template.Library()

BAD_WORDS = [
    'Мышь','мышь','глупец','Глупец','плохишь','Плохишь'
]


text = 'post.article_title'


@register.filter()
def censor(title):
    list = title.split()
    censor_list = []
    for word in list:
        if word in BAD_WORDS:
            censor_word = word[0] * '*'
            censor_list.append(word.replace(word, censor_word))
        else:
            censor_list.append(word)

    return censor_list


# def censor(text,BAD_WORDS):
    # for word in bad_words:
    #     censored_word = word[0] * '*'
    #     text = text.replace(word, censored_word)
    # return text




