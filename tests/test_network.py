import pytest
from harmony.blockchain_network import (
    blockNumber
)

def test_blockNumber():
    api_url = "https://rpc.s0.t.hmny.io"
    test_result = blockNumber()
    return test_result
    #assert test_result == actual_result

x=test_blockNumber()
print(x)