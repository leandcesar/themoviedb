from themoviedb import schemas
from themoviedb._endpoints._endpoint import Endpoint

CERTIFICATIONS_MOVIE = Endpoint("certification/movie/list", schemas.Certifications)
CERTIFICATIONS_TV = Endpoint("certification/tv/list", schemas.Certifications)
GENRES_MOVIE = Endpoint("genre/movie/list", schemas.Genres)
GENRES_TV = Endpoint("genre/tv/list", schemas.Genres)

KEYWORD_DETAILS = Endpoint("keyword/{keyword_id}", schemas.Keyword)
KEYWORD_MOVIES = Endpoint("keyword/{keyword_id}/movies", schemas.Movies)
REVIEW_DETAILS = Endpoint("review/{review_id}", schemas.Review)
EPISODE_GROUP_DETAILS = Endpoint("tv/episode_group/{episode_group_id}", schemas.EpisodeGroup)

TRENDING_MOVIE_DAY = Endpoint("trending/movie/day", schemas.Movies)
TRENDING_MOVIE_WEEK = Endpoint("trending/movie/week", schemas.Movies)
TRENDING_PERSON_DAY = Endpoint("trending/person/day", schemas.People)
TRENDING_PERSON_WEEK = Endpoint("trending/person/week", schemas.People)
TRENDING_TV_DAY = Endpoint("trending/tv/day", schemas.TVs)
TRENDING_TV_WEEK = Endpoint("trending/tv/week", schemas.TVs)

WATCH_PROVIDERS_MOVIE = Endpoint("watch/providers/movie", schemas.WatchProvidersData)
WATCH_PROVIDERS_REGIONS = Endpoint("watch/providers/regions", schemas.Regions)
WATCH_PROVIDERS_TV = Endpoint("watch/providers/tv", schemas.WatchProvidersData)

FIND = Endpoint("find/{external_id}", schemas.MultiResults)
GUEST_RATED_MOVIES = Endpoint("guest_session/{guest_session_id}/rated/movies", schemas.RatedMovies)
GUEST_RATED_TV = Endpoint("guest_session/{guest_session_id}/rated/tv", schemas.RatedTVs)
GUEST_RATED_EPISODES = Endpoint("guest_session/{guest_session_id}/rated/episodes", schemas.RatedEpisodes)
