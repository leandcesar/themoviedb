from themoviedb import schemas
from themoviedb._endpoints._endpoint import Endpoint

MOVIE_DETAILS = Endpoint("movie/{movie_id}", schemas.Movie)
MOVIE_ALTERNATIVE_TITLES = Endpoint("movie/{movie_id}/alternative_titles", schemas.AlternativeTitles)
MOVIE_CREDITS = Endpoint("movie/{movie_id}/credits", schemas.Credits)
MOVIE_EXTERNAL_IDS = Endpoint("movie/{movie_id}/external_ids", schemas.ExternalIDs)
MOVIE_KEYWORDS = Endpoint("movie/{movie_id}/keywords", schemas.Keywords)
MOVIE_IMAGES = Endpoint("movie/{movie_id}/images", schemas.Images)
MOVIE_LISTS = Endpoint("movie/{movie_id}/lists", schemas.ItemsList)
MOVIE_RECOMMENDATIONS = Endpoint("movie/{movie_id}/recommendations", schemas.Movies)
MOVIE_RELEASE_DATES = Endpoint("movie/{movie_id}/release_dates", schemas.ReleaseDates)
MOVIE_REVIEWS = Endpoint("movie/{movie_id}/reviews", schemas.Reviews)
MOVIE_SIMILAR = Endpoint("movie/{movie_id}/similar", schemas.Movies)
MOVIE_TRANSLATIONS = Endpoint("movie/{movie_id}/translations", schemas.Translations)
MOVIE_VIDEOS = Endpoint("movie/{movie_id}/videos", schemas.Videos)
MOVIE_WATCH_PROVIDERS = Endpoint("movie/{movie_id}/watch/providers", schemas.WatchProviders)

MOVIES_LATEST = Endpoint("movie/latest", schemas.Movie)
MOVIES_NOW_PLAYING = Endpoint("movie/now_playing", schemas.Movies)
MOVIES_POPULAR = Endpoint("movie/popular", schemas.Movies)
MOVIES_TOP_RATED = Endpoint("movie/top_rated", schemas.Movies)
MOVIES_UPCOMING = Endpoint("movie/upcoming", schemas.Movies)
