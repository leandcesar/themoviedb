from themoviedb import schemas
from themoviedb._endpoints._endpoint import Endpoint

PERSON_DETAILS = Endpoint("person/{person_id}", schemas.Person)
PERSON_EXTERNAL_IDS = Endpoint("person/{person_id}/external_ids", schemas.ExternalIDs)
PERSON_IMAGES = Endpoint("person/{person_id}/images", schemas.Images)
PERSON_COMBINED_CREDITS = Endpoint("person/{person_id}/combined_credits", schemas.CreditsCombined)
PERSON_MOVIE_CREDITS = Endpoint("person/{person_id}/movie_credits", schemas.CreditsMovie)
PERSON_TV_CREDITS = Endpoint("person/{person_id}/tv_credits", schemas.CreditsTV)
PERSON_TAGGED_IMAGES = Endpoint("person/{person_id}/tagged_images", schemas.TaggedImages)
PERSON_TRANSLATIONS = Endpoint("person/{person_id}/translations", schemas.Translations)

PEOPLE_LATEST = Endpoint("person/latest", schemas.Person)
PEOPLE_POPULAR = Endpoint("person/popular", schemas.People)
