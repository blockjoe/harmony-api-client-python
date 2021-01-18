import pytest
import requests

from harmony.transaction_staking import (
    get_current_staking_error_sink
)

#def test_blockNumber():
#    api_url = "https://rpc.s0.t.hmny.io"
#    test_result = get_current_staking_error_sink(api_url)
#    return test_result
#    #assert test_result == actual_result

#x=test_blockNumber()
api_url = "https://rpc.s0.t.hmny.io"
print(get_current_staking_error_sink(api_url).json())