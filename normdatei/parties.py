# coding: utf-8
import re
from normality import normalize

PARTIES_SPLIT = re.compile(r'(, (auf|an|zur|zum)( die| den )?(.* gewandt)?)')
PARTIES_REGEX = {
    'cducsu': re.compile(' cdu ?(csu)?'),
    'spd': re.compile(' spd'),
    'linke': re.compile(' (die|der|den) linken?'),
    'fdp': re.compile(' fdp'),
    'gruene': re.compile(' bund ?nis\-?(ses)? ?90 die gru ?nen'),
}


def search_party_names(text):
    if text is None:
        return
    text = PARTIES_SPLIT.split(text)
    text = normalize(text[0])
    parties = set()
    for party, rex in PARTIES_REGEX.items():
        if rex.findall(text):
            parties.add(party)
    if not len(parties):
        return
    parties = ':'.join(sorted(parties))
    return parties
