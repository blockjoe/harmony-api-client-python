import pytest

from harmony.api import HarmonyAPI

@pytest.fixture(scope="session")
def API():
    return HarmonyAPI('https://rpc.s0.t.hmny.io/')

def test_list_supported(API):
    API.rosetta.list_supported_networks()