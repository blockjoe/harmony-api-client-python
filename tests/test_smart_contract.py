import pytest
from harmony.smart_contract import (
    call,
    estimate_gas,
    get_code,
    get_storage_at
)

def test_call():
    api_url = "https://rpc.s0.t.hmny.io"
    to_address = "0x08AE1abFE01aEA60a47663bCe0794eCCD5763c19"
    block_number = 370000
    test_result = call(api_url , to_address, block_number)
    actual_result = {
        "jsonrpc": "2.0",
        "id": 1,
        "result": "0x0"
        }
    #return test_result
    assert test_result == actual_result

x=test_call()
print(x)
