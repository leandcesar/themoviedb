import json

import pytest

from themoviedb import utils


@pytest.fixture(scope="session", autouse=True)
def get_data():
    def _get_data(filename: str):
        with open(f"tests/mock/data/{filename}.json", "r", encoding="utf-8") as f:
            raw_data = f.read()
            data = json.loads(raw_data)
            return data

    return _get_data


@pytest.fixture(scope="session", autouse=True)
def assert_data():
    def _assert_data(testing_dataclass, assertation_data: dict):
        testing_data = utils.as_dict(testing_dataclass)

        def __assert_data(_testing_data: dict, _assertation_data: dict):
            for k, v in _assertation_data.items():
                if isinstance(v, dict):
                    __assert_data(_testing_data[k], v)
                elif isinstance(v, list):
                    for i in range(len(v)):
                        if isinstance(v[i], dict):
                            __assert_data(_testing_data[k][i], v[i])
                        else:
                            assert _testing_data[k][i] == v[i]
                else:
                    assert _testing_data[k] == v
            return True

        return __assert_data(testing_data, assertation_data)

    return _assert_data
