from themoviedb import schemas
from themoviedb._endpoints._endpoint import Endpoint

COLLECTION_DETAILS = Endpoint("collection/{collection_id}", schemas.Collection)
COLLECTION_IMAGES = Endpoint("collection/{collection_id}/images", schemas.Images)
COLLECTION_TRANSLATIONS = Endpoint("collection/{collection_id}/translations", schemas.Translations)

COMPANY_DETAILS = Endpoint("company/{company_id}", schemas.Company)
COMPANY_ALTERNATIVE_NAMES = Endpoint("company/{company_id}/alternative_names", schemas.AlternativeNames)
COMPANY_IMAGES = Endpoint("company/{company_id}/images", schemas.Images)

NETWORK_DETAILS = Endpoint("network/{network_id}", schemas.Network)
NETWORK_ALTERNATIVE_NAMES = Endpoint("network/{network_id}/alternative_names", schemas.AlternativeNames)
NETWORK_IMAGES = Endpoint("network/{network_id}/images", schemas.Images)

CREDIT_DETAILS = Endpoint("credit/{credit_id}", schemas.Credit)

EPISODE_DETAILS = Endpoint("tv/{tv_id}/season/{season_id}/episode/{episode_id}", schemas.Episode)
EPISODE_CREDITS = Endpoint("tv/{tv_id}/season/{season_id}/episode/{episode_id}/credits", schemas.Credits)
EPISODE_EXTERNAL_IDS = Endpoint(
    "tv/{tv_id}/season/{season_id}/episode/{episode_id}/external_ids", schemas.ExternalIDs
)
EPISODE_IMAGES = Endpoint("tv/{tv_id}/season/{season_id}/episode/{episode_id}/images", schemas.Images)
EPISODE_TRANSLATIONS = Endpoint(
    "tv/{tv_id}/season/{season_id}/episode/{episode_id}/translations", schemas.Translations
)
EPISODE_VIDEOS = Endpoint("tv/{tv_id}/season/{season_id}/episode/{episode_id}/videos", schemas.Videos)

SEASON_DETAILS = Endpoint("tv/{tv_id}/season/{season_id}", schemas.Season)
SEASON_AGGREGATE_CREDITS = Endpoint("tv/{tv_id}/season/{season_id}/aggregate_credits", schemas.Credits)
SEASON_CREDITS = Endpoint("tv/{tv_id}/season/{season_id}/credits", schemas.Credits)
SEASON_EXTERNAL_IDS = Endpoint("tv/{tv_id}/season/{season_id}/external_ids", schemas.ExternalIDs)
SEASON_IMAGES = Endpoint("tv/{tv_id}/season/{season_id}/images", schemas.Images)
SEASON_TRANSLATIONS = Endpoint("tv/{tv_id}/season/{season_id}/translations", schemas.Translations)
SEASON_VIDEOS = Endpoint("tv/{tv_id}/season/{season_id}/videos", schemas.Videos)
