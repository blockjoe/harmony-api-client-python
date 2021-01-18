import pytest

from harmony.api import HarmonyAPI

@pytest.fixture(scope="session")
def API():
    return HarmonyAPI('https://rpc.s0.t.hmny.io/')

def test_node_metadata(API):
    API.node_metadata()

def test_get_account_balance(API):
    API.get_account_balance("one1wx6p8kjucu5llqz79h9pmn0qf55772m2d2xt26")