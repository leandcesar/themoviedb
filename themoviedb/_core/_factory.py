from typing import Any, Protocol, Type, TypeVar

from themoviedb._core.config import ClientConfig


class _Resource(Protocol):
    """Constructor contract shared by route resource classes."""

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...


T = TypeVar("T", bound=_Resource)


class _ClientFactory:
    """Create resources that share a client's configuration and transport.

    Concrete clients deliberately retain their explicit public factory methods.
    This helper only owns the common wiring behind those methods.
    """

    _config: ClientConfig
    _transport: Any

    def _get_instance(self, cls: Type[T], *args: Any, **kwargs: Any) -> T:
        return cls(*args, _config=self._config, _transport=self._transport, **kwargs)
