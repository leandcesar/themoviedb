from themoviedb import schemas
from themoviedb._endpoints._endpoint import Endpoint

SEARCH_COMPANIES = Endpoint("search/company", schemas.Companies)
SEARCH_COLLECTIONS = Endpoint("search/collection", schemas.Collections)
SEARCH_KEYWORDS = Endpoint("search/keyword", schemas.Keywords)
SEARCH_MOVIES = Endpoint("search/movie", schemas.Movies)
SEARCH_MULTI = Endpoint("search/multi", schemas.Multis)
SEARCH_PEOPLE = Endpoint("search/person", schemas.People)
SEARCH_TV = Endpoint("search/tv", schemas.TVs)
