from typing import Any, Dict, Mapping


def normalize_response(data: Mapping[str, Any]) -> Dict[str, Any]:
    """Normalize TMDb keys that cannot be represented as Python field names."""
    normalized = data if isinstance(data, dict) else dict(data)
    if "watch/providers" in normalized:
        normalized["watch_providers"] = normalized.pop("watch/providers")
    return normalized
