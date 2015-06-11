# coding: utf-8
import re
from normality import normalize

FP_REMOVE = re.compile(u'(^.*Dr.?( h.? ?c.?)?| (von( der)?)| [A-Z]\. )')

NAME_REMOVE = [u'\\[.*\\]|\\(.*\\)', u'( de[sr])? Abg.? ',
               u'Vizepräsidentin', u'Vizepräsident', u'Präsident',
               u'Präsidentin', u'Alterspräsident', u'Alterspräsidentin',
               u'Liedvortrag', u'Bundeskanzler(in)?', u', Parl\\. .*',
               u', Staatsmin.*', u', Bundesmin.*', u', Ministe.*',
               u'Staatsministers', 'Bundesministers',
               u'Parl. Staatssekretärin',
               u'Ge ?genruf', 'Weiterer Zuruf', 'Zuruf', 'Weiterer',
               u', zur.*', u', auf die', u' an die', u', an .*', u'gewandt']
NAME_REMOVE = re.compile(u'(%s)' % '|'.join(NAME_REMOVE), re.U)
DE_HYPHEN = re.compile(r'([a-z])-([a-z])', re.U)


def clean_text(text):
    if not isinstance(text, unicode):
        try:
            text = text.decode('utf-8')
        except:
            text = text.decode('latin-1')
    text = text.replace('\r', '\n')
    text = text.replace(u'\xa0', ' ')
    text = text.replace(u'\x96', '-')
    text = text.replace(u'\u2014', '-')
    text = text.replace(u'\u2013', '-')
    return text


def clean_name(name):
    if name is None:
        return name
    name = NAME_REMOVE.sub('', name)
    name = DE_HYPHEN.sub(r'\1\2', name)
    name = name.strip('-')
    return name.strip()


def fingerprint(name):
    if name is None:
        return
    name = FP_REMOVE.sub(' ', name.strip())
    return normalize(name).replace(' ', '-')
