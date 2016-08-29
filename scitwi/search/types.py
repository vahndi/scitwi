from typing import TypeVar

from scitwi.search.search_query import SearchQuery

StrOrQuery = TypeVar('StrOrQuery', str, SearchQuery)