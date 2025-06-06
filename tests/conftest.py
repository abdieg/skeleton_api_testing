import os
import pytest
from common.token import get_token


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Target environment: dev, qa, prod"
    )


def pytest_configure(config):
    env = config.getoption("--env")
    os.environ["TEST_ENV"] = env  # this is what settings.py will read


@pytest.fixture(scope="session")
def auth_token():
    return get_token()
