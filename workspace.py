from harmony.api import HarmonyAPI

api = HarmonyAPI('https://rpc.s0.t.hmny.io/')

print(api.peer_count())
print(api.node_metadata())
