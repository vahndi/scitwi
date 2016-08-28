from typing import List

from scitwi.search.types import StrOrListStr


class SearchQuery(object):
    """
    https://dev.twitter.com/rest/public/search
    https://twitter.com/search-advanced
    """
    def __init__(self, all_of: StrOrListStr=None, any_of: StrOrListStr=None, none_of: StrOrListStr=None,
                 exact_phrase: str=None, hashtags: List[str]=None, language=None,
                 from_account: StrOrListStr=None, to_account: StrOrListStr=None, mentioning_account: StrOrListStr=None,
                 near_place=None,
                 from_date=None, to_date=None,
                 positive: bool=False, negative: bool=False, question: bool=False, include_retweets: bool=False):

        pass