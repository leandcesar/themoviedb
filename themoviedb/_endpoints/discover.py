from themoviedb import schemas
from themoviedb._endpoints._endpoint import Endpoint

DISCOVER_MOVIES = Endpoint("discover/movie", schemas.Movies)
DISCOVER_TV = Endpoint("discover/tv", schemas.TVs)
