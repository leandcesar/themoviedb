from themoviedb.routes_async import (
    Base,
    Authentication,
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
    TV,
    TVs,
    WatchProviders,
)


class aioTMDb(Base):
    """aioTMDb class.

    This class provides methods for accessing various async endpoints of the TMDb API.
    Each method returns an instance of a corresponding model class, which can be used
    to retrieve information about a specific resource.
    """

    def authentication(self) -> Authentication:
        """Get model object for `themoviedb.Authentication` resource."""
        return Authentication(session=self.session, language=self.language, region=self.region)

    def certifications(self) -> Certifications:
        """Get model object for `themoviedb.Certifications` resource."""
        return Certifications(session=self.session, language=self.language, region=self.region)

    def collection(self, collection_id: int) -> Collection:
        """Get model object for `themoviedb.Collection` resource."""
        return Collection(collection_id, session=self.session, language=self.language, region=self.region)

    def company(self, company_id: int) -> Company:
        """Get model object for `themoviedb.Company` resource."""
        return Company(company_id, session=self.session, language=self.language, region=self.region)

    def credit(self, credit_id: int) -> Credit:
        """Get model object for `themoviedb.Credit` resource."""
        return Credit(credit_id, session=self.session, language=self.language, region=self.region)

    def discover(self) -> Discover:
        """Get model object for `themoviedb.Discover` resource."""
        return Discover(session=self.session, language=self.language, region=self.region)

    def episode(self, tv_id: int, season_id: int, episode_id: int) -> Episode:
        """Get model object for `themoviedb.Episode` resource."""
        return Episode(tv_id, season_id, episode_id, session=self.session, language=self.language, region=self.region)

    def episode_group(self, episode_group_id: int) -> EpisodeGroup:
        """Get model object for `themoviedb.EpisodeGroup` resource."""
        return EpisodeGroup(episode_group_id, session=self.session, language=self.language, region=self.region)

    def find(self) -> Find:
        """Get model object for `themoviedb.Find` resource."""
        return Find(session=self.session, language=self.language, region=self.region)

    def genres(self) -> Genres:
        """Get model object for `themoviedb.Genres` resource."""
        return Genres(session=self.session, language=self.language, region=self.region)

    def guest(self, guest_session_id: str) -> Guest:
        """Get model object for `themoviedb.Guest` resource."""
        return Guest(guest_session_id, session=self.session, language=self.language, region=self.region)

    def keyword(self, keyword_id: int) -> Keyword:
        """Get model object for `themoviedb.Keyword` resource."""
        return Keyword(keyword_id, session=self.session, language=self.language, region=self.region)

    def movie(self, movie_id: int) -> Movie:
        """Get model object for `themoviedb.Movie` resource."""
        return Movie(movie_id, session=self.session, language=self.language, region=self.region)

    def movies(self) -> Movies:
        """Get model object for `themoviedb.Movies` resource."""
        return Movies(session=self.session, language=self.language, region=self.region)

    def network(self, network_id: int) -> Network:
        """Get model object for `themoviedb.Network` resource."""
        return Network(network_id, session=self.session, language=self.language, region=self.region)

    def people(self) -> People:
        """Get model object for `themoviedb.People` resource."""
        return People(session=self.session, language=self.language, region=self.region)

    def person(self, person_id: int) -> Person:
        """Get model object for `themoviedb.Person` resource."""
        return Person(person_id, session=self.session, language=self.language, region=self.region)

    def review(self, review_id: int) -> Review:
        """Get model object for `themoviedb.Review` resource."""
        return Review(review_id, session=self.session, language=self.language, region=self.region)

    def search(self) -> Search:
        """Get model object for `themoviedb.Search` resource."""
        return Search(session=self.session, language=self.language, region=self.region)

    def season(self, tv_id: int, season_id: int) -> Season:
        """Get model object for `themoviedb.Season` resource."""
        return Season(tv_id, season_id, session=self.session, language=self.language, region=self.region)

    def trending(self) -> Trending:
        """Get model object for `themoviedb.Trending` resource."""
        return Trending(session=self.session, language=self.language, region=self.region)

    def tv(self, tv_id: int) -> TV:
        """Get model object for `themoviedb.TV` resource."""
        return TV(tv_id, session=self.session, language=self.language, region=self.region)

    def tvs(self) -> TVs:
        """Get model object for `themoviedb.TVs` resource."""
        return TVs(session=self.session, language=self.language, region=self.region)

    def watch_providers(self) -> WatchProviders:
        """Get model object for `themoviedb.WatchProviders` resource."""
        return WatchProviders(session=self.session, language=self.language, region=self.region)
