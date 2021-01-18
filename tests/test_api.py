import pytest

from harmony.api import HarmonyAPI

@pytest.fixture(scope="session")
def API():
    return HarmonyAPI('https://rpc.s0.t.hmny.io/')

def test_node_metadata(API):
    API.node_metadata()

def test_peer_count(API):
    API.peer_count()

def test_protocol_version(API):
    API.protocol_version()

#def test_current_bad_block(API):
#    API._current_bad_blocks()

def test_current_gas_price(API):
    API.current_gas_price()

def test_circulating_supply(API):
    API.circulating_supply()

def test_total_supply(API):
    API.total_supply()

def test_current_block_number(API):
    API.current_block_number()

def test_current_leader(API):
    API.current_leader()

def test_sharding_structure(API):
    API.sharding_structure()

def test_last_cross_links(API):
    API.last_cross_links()

def test_current_epoch(API):
    API.current_epoch()

def test_validators_by_epoch_withpubkeys(API):
    API.validators_by_epoch(5, True)

def test_validators_by_epoch(API):
    API.validators_by_epoch(5)

def test_current_utility_metrics(API):
    API.current_utility_metrics()

def test_staking_network_info(API):
    API.staking_network_info()

def test_latest_super_comitees(API):
    API.latest_super_committes()

def test_median_raw_stake_snapshot(API):
    API.median_raw_stake_snapshot()

def test_transaction_pool_stats(API):
    API.transaction_pool_stats()

def test_pending_staking_transactions(API):
    API.pending_staking_transactions()

def test_pending_transaction(API):
    API.pending_transactions()

def test_latest_chain_headers(API):
    API.latest_chain_headers()

def test_block_header_block_number(API):
    API.block_header(block_number=5)

def test_block_header(API):
    API.block_header()

def test_get_block_block_hash(API):
    API.get_block(block_hash="0x2ea6a10e4c9680b59020ad7bab3b4d85df3d458aefb72630dc12019cc0c2c269")

def test_get_block_block_number(API):
     API.get_block(block_number=5)

def test_get_block_signers(API):
    API.get_block_signers(8049136)

def test_get_block_signers_withpubkeys(API):
    API.get_block_signers(8049136, True)

def test_get_transaction_count_on_block_block_number(API):
    API.get_transaction_count_on_block(block_number=8049136)

def test_get_transaction_count_on_block_block_khash(API):
    API.get_transaction_count_on_block(block_hash="0x2ea6a10e4c9680b59020ad7bab3b4d85df3d458aefb72630dc12019cc0c2c269")

def test_get_blocks(API):
    API.get_blocks(13, 14)

def test_get_account_balance_withblocknumber(API):
    API.get_account_balance(address="one1wmudztmxynm38vkc3998fxkeymmczg6st7sf83" , block_number=8049136)

def test_get_account_balance(API):
    API.get_account_balance(address="one1wmudztmxynm38vkc3998fxkeymmczg6st7sf83")

def test_get_account_staking_transaction_count(API):
    API.get_account_staking_transaction_count(address="one1wmudztmxynm38vkc3998fxkeymmczg6st7sf83", transaction_type="ALL")

def test_get_account_staking_transaction_history(API):
    API.get_account_staking_transaction_history(address="one1wmudztmxynm38vkc3998fxkeymmczg6st7sf83")

def test_get_account_transaction_count(API):
    API.get_account_transaction_count(address="one1wmudztmxynm38vkc3998fxkeymmczg6st7sf83", transaction_type="ALL")

def test_get_account_transaction_history(API):
    API.get_account_transaction_history(address="one1wmudztmxynm38vkc3998fxkeymmczg6st7sf83")

def test_current_transaction_error_sink(API):
    API.current_transaction_error_sink()

def test_get_transaction(API):
    API.get_transaction("0x2ea6a10e4c9680b59020ad7bab3b4d85df3d458aefb72630dc12019cc0c2c269")

def test_get_transaction_by_block_withblocknumber(API):
    API.get_transaction_by_block(transaction_index=0, block_number=55462)

def test_get_transaction_by_block_withblockhash(API):
    API.get_transaction_by_block(transaction_index=0, block_hash="0x2ea6a10e4c9680b59020ad7bab3b4d85df3d458aefb72630dc12019cc0c2c269")

def test_current_staking_transaction_error_sink(API):
    API.current_staking_transaction_error_sink()

def test_get_staking_transaction(API):
    API.get_staking_transaction("0x9c808cac1f4a0e72bb98c4c95fa3dd436b7ab7b4b3df7177184d982ffdb03201")

def test_get_delegations_by_delegator(API):
    API.get_delegations_by_delegator("one1k9nvefx0znyg4jrpvcj6mzphecxqmqa398d5nc")

def test_get_delegations_by_validator(API):
    API.get_delegations_by_validator("one1r55rwumsrm6w3d20uhaa3hm4rxr442k0qx9gj8")

def test_get_all_validators(API):
    API.get_all_validators()

def test_get_all_elected_validators(API):
    API.get_all_elected_validators()

def test_get_information_about_validator_withblocknumber(API):
    API.get_all_validator_information(block_number=8049136)        

def test_get_information_about_validator(API):
    API.get_all_validator_information()

def test_pending_cx_receipts(API):
    API.pending_cx_receipts()
