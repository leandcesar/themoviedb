# -*- coding: utf-8 -*-
from typing import Type, TypeVar

from themoviedb.routes_async import (
    TV,
    Authentication,
    Base,
    Certifications,
    Collection,
    Company,
    Credit,
    Discover,
    Episode,
    EpisodeGroup,
    Find,
    Genres,
    Guest,
    Keyword,
    Movie,
    Movies,
    Network,
    People,
    Person,
    Review,
    Search,
    Season,
    Trending,
    TVs,
    WatchProviders,
)

T = TypeVar("T", bound=Base)


class aioTMDb(Base):
    """aioTMDb class.

    This class provides methods for accessing various async endpoints of the TMDb API.
    Each method returns an instance of a corresponding model class, which can be used
    to retrieve information about a specific resource.
    """

    def _get_instance(self, cls: Type[T], *args, **kwargs) -> T:
        return cls(*args, key=self.key, session=self.session, language=self.language, region=self.region, **kwargs)

    def authentication(self) -> Authentication:
        """Get model object for `themoviedb.Authentication` resource."""
        return self._get_instance(Authentication)

    def certifications(self) -> Certifications:
        """Get model object for `themoviedb.Certifications` resource."""
        return self._get_instance(Certifications)

    def collection(self, collection_id: int) -> Collection:
        """Get model object for `themoviedb.Collection` resource."""
        return self._get_instance(Collection, collection_id)

    def company(self, company_id: int) -> Company:
        """Get model object for `themoviedb.Company` resource."""
        return self._get_instance(Company, company_id)

    def credit(self, credit_id: int) -> Credit:
        """Get model object for `themoviedb.Credit` resource."""
        return self._get_instance(Credit, credit_id)

    def discover(self) -> Discover:
        """Get model object for `themoviedb.Discover` resource."""
        return self._get_instance(Discover)

    def episode(self, tv_id: int, season_id: int, episode_id: int) -> Episode:
        """Get model object for `themoviedb.Episode` resource."""
        return self._get_instance(Episode, tv_id, season_id, episode_id)

    def episode_group(self, episode_group_id: int) -> EpisodeGroup:
        """Get model object for `themoviedb.EpisodeGroup` resource."""
        return self._get_instance(EpisodeGroup, episode_group_id)

    def find(self) -> Find:
        """Get model object for `themoviedb.Find` resource."""
        return self._get_instance(Find)

    def genres(self) -> Genres:
        """Get model object for `themoviedb.Genres` resource."""
        return self._get_instance(Genres)

    def guest(self, guest_session_id: str) -> Guest:
        """Get model object for `themoviedb.Guest` resource."""
        return self._get_instance(Guest, guest_session_id)

    def keyword(self, keyword_id: int) -> Keyword:
        """Get model object for `themoviedb.Keyword` resource."""
        return self._get_instance(Keyword, keyword_id)

    def movie(self, movie_id: int) -> Movie:
        """Get model object for `themoviedb.Movie` resource."""
        return self._get_instance(Movie, movie_id)

    def movies(self) -> Movies:
        """Get model object for `themoviedb.Movies` resource."""
        return self._get_instance(Movies)

    def network(self, network_id: int) -> Network:
        """Get model object for `themoviedb.Network` resource."""
        return self._get_instance(Network, network_id)

    def people(self) -> People:
        """Get model object for `themoviedb.People` resource."""
        return self._get_instance(People)

    def person(self, person_id: int) -> Person:
        """Get model object for `themoviedb.Person` resource."""
        return self._get_instance(Person, person_id)

    def review(self, review_id: int) -> Review:
        """Get model object for `themoviedb.Review` resource."""
        return self._get_instance(Review, review_id)

    def search(self) -> Search:
        """Get model object for `themoviedb.Search` resource."""
        return self._get_instance(Search)

    def season(self, tv_id: int, season_id: int) -> Season:
        """Get model object for `themoviedb.Season` resource."""
        return self._get_instance(Season, tv_id, season_id)

    def trending(self) -> Trending:
        """Get model object for `themoviedb.Trending` resource."""
        return self._get_instance(Trending)

    def tv(self, tv_id: int) -> TV:
        """Get model object for `themoviedb.TV` resource."""
        return self._get_instance(TV, tv_id)

    def tvs(self) -> TVs:
        """Get model object for `themoviedb.TVs` resource."""
        return self._get_instance(TVs)

    def watch_providers(self) -> WatchProviders:
        """Get model object for `themoviedb.WatchProviders` resource."""
        return self._get_instance(WatchProviders)
