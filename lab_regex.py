'''Starter functions for the Redacted lab.'''

import re


def has_digit(text):
    '''
    Return True if text contains at least one digit, and False otherwise.

    >>> has_digit('Campus visit #42 booked')
    True
    >>> has_digit('no numbers here')
    False
    '''
    # TODO: your regex here (re.search returns a match or None -- wrap it in bool)
    pass


def find_numbers(text):
    '''
    Return a list of every run of consecutive digits in text, as strings.

    >>> find_numbers('I booked 2 tours for 10 visitors')
    ['2', '10']
    >>> find_numbers('no numbers here')
    []
    '''
    # TODO: your regex here (re.findall with a quantifier)
    pass


def mask_digits(text):
    '''
    Return text with every digit replaced by a capital 'X'.

    >>> mask_digits('call 909-621-8088')
    'call XXX-XXX-XXXX'
    >>> mask_digits('no digits')
    'no digits'
    '''
    # TODO: your regex here (re.sub)
    pass


def find_hashtags(text):
    '''
    Return a list of the hashtags in text, each without its leading '#'.

    >>> find_hashtags('Campus visit today! #CMC #Claremont #CMC')
    ['CMC', 'Claremont', 'CMC']
    >>> find_hashtags('no tags in this one')
    []
    '''
    # TODO: your regex here (match the '#', then capture the word after it)
    pass


def find_mentions(text):
    '''
    Return a list of the @-handles in text, each without its leading '@'.

    >>> find_mentions('thank you @cmc and @pomona, see you soon @cmc')
    ['cmc', 'pomona', 'cmc']
    >>> find_mentions('nobody is mentioned here')
    []
    '''
    # TODO: your regex here (a capture group, like find_hashtags)
    pass


def find_urls(text):
    '''
    Return a list of the http and https URLs in text.

    >>> find_urls('read more at https://www.cmc.edu today and http://www.pomona.edu')
    ['https://www.cmc.edu', 'http://www.pomona.edu']
    >>> find_urls('no links in this tweet')
    []
    '''
    # TODO: your regex here (make the 's' optional, then grab the non-spaces)
    pass


def find_phone_numbers(text):
    '''
    Return a list of the US phone numbers in text, in XXX-XXX-XXXX form.

    >>> find_phone_numbers('call 909-621-8088 or 800-770-1333 today')
    ['909-621-8088', '800-770-1333']
    >>> find_phone_numbers('no phone number here')
    []
    '''
    # TODO: your regex here (three digits, dash, three digits, dash, four digits)
    pass


def area_code(phone):
    '''
    Return the three-digit area code of a XXX-XXX-XXXX phone number.

    >>> area_code('909-621-8088')
    '909'
    >>> area_code('800-770-1333')
    '800'
    '''
    # TODO: your regex here (capture the first group, then read it with .group)
    pass


def redact_emails(text):
    '''
    Return text with every email address replaced by the string '[REDACTED]'.

    >>> redact_emails('reach me at admission@cmc.edu or admission@hmc.edu')
    'reach me at [REDACTED] or [REDACTED]'
    >>> redact_emails('this line has no email')
    'this line has no email'
    '''
    # TODO: your regex here (use re.sub to replace each email address)
    pass


def redact_ssns(text):
    '''
    Return text with every US Social Security number masked as 'XXX-XX-XXXX'.

    >>> redact_ssns('SSN 123-45-6789 on file')
    'SSN XXX-XX-XXXX on file'
    >>> redact_ssns('no ssn in this record')
    'no ssn in this record'
    '''
    # TODO: your regex here (an SSN is three digits, two digits, four digits)
    pass


def mask_last_four(card):
    '''
    Return a 16-digit card number with all but its last four digits masked by '*'.

    >>> mask_last_four('1234567812345678')
    '************5678'
    >>> mask_last_four('4111111111111111')
    '************1111'
    '''
    # TODO: your regex here (a 16-digit card has twelve digits before its last four)
    pass


def is_valid_email(s):
    '''
    Return True if the whole string s is a single valid-looking email address.

    >>> is_valid_email('admission@cmc.edu')
    True
    >>> is_valid_email('not-an-email')
    False
    >>> is_valid_email('admission@cmc.edu and some extra text')
    False
    >>> is_valid_email('admission@cmc.edu' + chr(10))
    False
    '''
    # TODO: use re.fullmatch for the entire email string, then bool the result.
    pass
