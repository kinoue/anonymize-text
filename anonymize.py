import re
import spacy

# import name list
with open('data/person_female_lower.lst') as f:
    name_set = set(f.read().splitlines())
with open('data/person_male_lower.lst') as f:
    name_set |= set(f.read().splitlines())

with open('data/person_female_lower_ambig.lst') as f:
    ambiguous_set = set(f.read().splitlines())
with open('data/person_male_lower_ambig.lst') as f:
    ambiguous_set |= set(f.read().splitlines())
with open('data/person_lower_ambig.lst') as f:
    ambiguous_set |= set(f.read().splitlines())

nlp = spacy.load('en')


def anonymize(text):
    text = anonymize_exact_names(text)
    text = anonymize_ambiguous_names(text)
    text = anonymize_emails(text)
    text = anonymize_twitter_handles(text)
    text = anonymize_phone_numbers(text)
    return anonymize_numbers(text)

def anonymize_ambiguous_names(text)
    names = set()
    doc = nlp(text)

    for token in doc:
        if (token.pos_ == 'PROPN' and
            token.text.lower() in  ambiguous_set):
            names.add(token.text)
    
    for name in names:
        text = re.sub(name, '[Name (%d)]' % len(name), text)
    return (text)


def anonymize_exact_names(text):
    names = set()
    doc = nlp(text)

    for token in doc:
        if token.text.lower() in name_set:
            names.add(token.text)

    for name in names:
        text = re.sub(name, '[Name (%d)]' % len(name), text)
    return (text)


def anonymize_emails(text):
    return help_anonymize('(([a-zA-Z0-9]+[_|\-|\.]?)*[a-zA-Z0-9]+\@([a-zA-Z0-9]+[_|\-|\.]?)*[a-zA-Z0-9]+(\.[a-zA-Z]{2,3})+)',
        text, "Email")

def anonymize_phone_numbers(text):
    return help_anonymize('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',
        text, 'Phone')

def anonymize_numbers(text):
    return help_anonymize('\d{4}\d*', text, "Number")


def anonymize_twitter_handles(text):
    return help_anonymize('(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)',
        text, "Twitter")

# search & replace one at a time
# for insertring the length of the string
#
def help_anonymize(reg_exp, text, label):
    new_text= text 
    pattern = re.compile(reg_exp)
    while pattern.search(new_text):
        match = pattern.search(new_text)
        replace = "[%s (%d)]" % (label, match.end() - match.start())
        new_text = new_text[:match.start()] + replace + new_text[match.end():]
    return new_text

