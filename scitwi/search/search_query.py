from datetime import datetime

from scitwi.utils.formatting import listify
from scitwi.utils.types import StrOrListStr


class SearchQuery(object):
    """
    https://dev.twitter.com/rest/public/search
    https://twitter.com/search-advanced
    """
    def __init__(self, all_of: StrOrListStr=None, any_of: StrOrListStr=None, none_of: StrOrListStr=None,
                 exact_phrase: str=None, hashtags: StrOrListStr=None, language=None,
                 from_account: StrOrListStr=None, to_account: StrOrListStr=None, mentioning_account: StrOrListStr=None,
                 near_place=None,
                 from_date: datetime=None, to_date: datetime=None,
                 positive: bool=False, negative: bool=False, question: bool=False, include_retweets: bool=False):

        self.all_of = listify(all_of)
        self.any_of = listify(any_of)
        self.none_of = listify(none_of)
        self.exact_phrase = listify(exact_phrase)
        self.hashtags = listify(hashtags)
        self.language = listify(language)
        self.from_account = listify(from_account)
        self.to_account = listify(to_account)
        self.mentioning_account = listify(mentioning_account)
        self.near_place = near_place
        self.from_date = from_date
        self.to_date = to_date
        self.positive = positive
        self.negative = negative
        self.question = question
        self.include_retweets = include_retweets

    def __str__(self):

        def add_list_items(to_query, items, prepend: str='', append: str='', joiner: str=' '):
            new_query = to_query
            if items:
                new_query += ' '
                items = ['%s%s%s' % (prepend, i, append) if not i.startswith(prepend)
                         else i for i in items]
                new_query += joiner.join(i for i in items)
            return new_query

        str_query = ''
        str_query = add_list_items(str_query, self.all_of)
        str_query = add_list_items(str_query, self.any_of, joiner=' OR ')
        str_query = add_list_items(str_query, self.none_of, prepend='-')
        str_query = add_list_items(str_query, self.exact_phrase, prepend='"', append='"')
        str_query = add_list_items(str_query, self.language, prepend='lang:')
        str_query = add_list_items(str_query, self.from_account, prepend='from:')
        str_query = add_list_items(str_query, self.to_account, prepend='to:')
        str_query = add_list_items(str_query, self.mentioning_account, prepend='@')
        str_query = add_list_items(str_query, [self.from_date.strftime('%Y-%m-%d')], prepend='since:')
        str_query = add_list_items(str_query, [self.from_date.strftime('%Y-%m-%d')], prepend='until:')
        if self.positive:
            str_query += ' :)'
        if self.negative:
            str_query += ' :('
        if self.question:
            str_query += ' ?'
        if self.include_retweets:
            str_query += ' include:retweets'

        return str_query
