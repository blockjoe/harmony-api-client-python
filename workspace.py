from harmony.api import HarmonyAPI

api = HarmonyAPI('https://rpc.s0.t.hmny.io/', local_rosetta_url="http://localhost:9700/")

#print(api.peer_count())

#print(api.get_account_transaction_history(address="one1wmudztmxynm38vkc3998fxkeymmczg6st7sf83"))

#print(api.get_block(block_hash="0x3fff0154d3aed7ba232e63e407f713f4e39f71877e4e7c4d482ccb1f1ab0a4e5"))

#print(api.get_delegations_by_delegator('one1k9nvefx0znyg4jrpvcj6mzphecxqmqa398d5nc'))

#print(api.get_information_about_validator("one1r55rwumsrm6w3d20uhaa3hm4rxr442k0qx9gj8"))

print(api.rosetta.list_supported_networks())