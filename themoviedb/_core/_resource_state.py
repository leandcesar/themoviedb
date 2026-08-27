from typing import Any, Dict


class _ResourceState:
    """Cooperate with a synchronous or asynchronous route base class."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)


class _CollectionResource(_ResourceState):
    def __init__(self, collection_id: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.collection_id = collection_id

    @property
    def _path_params(self) -> Dict[str, int]:
        return {"collection_id": self.collection_id}


class _CompanyResource(_ResourceState):
    def __init__(self, company_id: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.company_id = company_id

    @property
    def _path_params(self) -> Dict[str, int]:
        return {"company_id": self.company_id}


class _CreditResource(_ResourceState):
    def __init__(self, credit_id: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.credit_id = credit_id

    @property
    def _path_params(self) -> Dict[str, int]:
        return {"credit_id": self.credit_id}


class _EpisodeGroupResource(_ResourceState):
    def __init__(self, episode_group_id: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.episode_group_id = episode_group_id

    @property
    def _path_params(self) -> Dict[str, int]:
        return {"episode_group_id": self.episode_group_id}


class _EpisodeResource(_ResourceState):
    def __init__(self, tv_id: int, season_id: int, episode_id: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.tv_id = tv_id
        self.season_id = season_id
        self.episode_id = episode_id

    @property
    def _path_params(self) -> Dict[str, int]:
        return {"tv_id": self.tv_id, "season_id": self.season_id, "episode_id": self.episode_id}


class _GuestResource(_ResourceState):
    def __init__(self, guest_session_id: str, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.guest_session_id = guest_session_id

    @property
    def _path_params(self) -> Dict[str, str]:
        return {"guest_session_id": self.guest_session_id}


class _KeywordResource(_ResourceState):
    def __init__(self, keyword_id: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.keyword_id = keyword_id

    @property
    def _path_params(self) -> Dict[str, int]:
        return {"keyword_id": self.keyword_id}


class _MovieResource(_ResourceState):
    def __init__(self, movie_id: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.movie_id = movie_id

    @property
    def _path_params(self) -> Dict[str, int]:
        return {"movie_id": self.movie_id}


class _NetworkResource(_ResourceState):
    def __init__(self, network_id: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.network_id = network_id

    @property
    def _path_params(self) -> Dict[str, int]:
        return {"network_id": self.network_id}


class _PersonResource(_ResourceState):
    def __init__(self, person_id: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.person_id = person_id

    @property
    def _path_params(self) -> Dict[str, int]:
        return {"person_id": self.person_id}


class _ReviewResource(_ResourceState):
    def __init__(self, review_id: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.review_id = review_id

    @property
    def _path_params(self) -> Dict[str, int]:
        return {"review_id": self.review_id}


class _SeasonResource(_ResourceState):
    def __init__(self, tv_id: int, season_id: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.tv_id = tv_id
        self.season_id = season_id

    @property
    def _path_params(self) -> Dict[str, int]:
        return {"tv_id": self.tv_id, "season_id": self.season_id}


class _TVResource(_ResourceState):
    def __init__(self, tv_id: int, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.tv_id = tv_id

    @property
    def _path_params(self) -> Dict[str, int]:
        return {"tv_id": self.tv_id}
