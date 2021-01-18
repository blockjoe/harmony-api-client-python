# Quickstart

A python client and CLI for interacting with Harmony endpoints designed for the Harmony's Hack the Horizon Hackathon.

## Installing

System Dependencies:
  - Python 3.7+

Python Requirements:
  - requests
  - pydantic
  - Typer
  - [rosetta-api-client-python](https://github.com/blockjoe/rosetta-api-client-python)

```sh
$ git clone https://github.com/blockjoe/harmony-api-client-python
$ cd harmony-api-client-python
$ pip install -e .
```
## Quickstart

To run with the rosetta endpoints, I reccomend following the node deployment instructions [found here](https://community.rosetta-api.org/t/harmonys-rosetta-data-construction-api/293).

I've included a bash script, `start-harmony-node.sh` for convience in launching it. When running locally with this configuration, the rosetta endpoints are exposed at <http://localhost:9700>.

Some basic usage in Python (assuming running from a local node)

Initializing:


```
>>> from harmony import HarmonyAPI
>>> api = HarmonyAPI('http://localhost:9500', local_rosetta_url='http://localhost:9700')
```

Getting information about the node:

```python
>>> api.node_metadata()
NodeMetadata(blskey=['000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'], version='Harmony (C) 2020. harmony, version v6686-v3.0.0-24-gddf70381 (@ 2020-12-16T05:38:22+0000)', network='mainnet', chain_config=ChainConfig(chain_id=1, cross_tx_epoch=28, cross_link_epoch=186, staking_epoch=186, prestaking_epoch=185, quick_unlock_epoch=191, eip155_epoch=28, s3_epoch=28, receipt_log_epoch=101), is_leader=False, shard_id=0, current_epoch=0, blocks_per_epoch=16384, role='ExplorerNode', dns_zone='t.hmny.io', is_archival=True, node_unix_start_time=1610955232, p2p_connectivity=P2PConnectivity(total_known_peers=387, connected=242, not_connected=145))
>>> api.protocol_version()
1
>>> api.peer_count()
387
```


## TODO

There's some housekeeping I'm going need to come back to in the near future.

- [] Get unit test coverage for Rosetta endpoints.
- [] Clean up the Sphinx docs.
- [] Get unit test coverage for the smart contract, cross shard, and raw transaction endpoints.
- [] Improve the Typer CLI
- [] Make the objects print nicer

## Notes for hacking/building on this

My main goal was to make sure to build this out in a way that could be easily expanded or built upon down the road.

The basic flow pattern is as follows.

1) `harmony/api.py` provides a layer for bundling together the session and url(s), while also condensing down some endpoints into a single interface,
2) The rest of the modules under `harmony` provide functions for calling each of the endpoints, useful if you don't have any interest in keeping a persistent session.
3) The modules under the `harmony/endpoints` subpackage handle constructing the payload from a constructed "Parameters" object
4) The networking calls happen in the `harmony/utils/communication.py`.

The motivation for making the seperation between 2 and 3 comes from the fact that I chose to leverage pydantic from the start. The reason for doing this was to plan
ahead for the goal of being able to use codegen tools for building out the validation models for the requests and responses. When I pulled up Rosetta's documetation and
was able to auto generate the requests and responses into objects that handled input validation and json parsing with a single command line call, I figured if anything, my goal for this hackathon was to get better aquainted with the concepts of codegen and the OpenAPI format. 

I had more intentions of flushing out the interface design for the CLI, especially since I was excited at the concept of Rosetta being a universal layer, but I found myself spending a good chunk of time fighting to get the Harmony RPC API into a form that would be better suitable for codegen.

In the `/dev` directory I've left a script `generate_api_schema.py` that's done a chunk of the initial lifting at getting the RPC v2 parameters/methods/responses into that generalizable format. Unfortunately, out of the box, OpenAPI 3.0 (formerly swagger), is not designed to support RPC. I've hacked aroudn that a little bit by making the unique paths just the method name, with the idea that it might be worth a little time to dig into a tool like [swagger-codegen](https://swagger.io/tools/swagger-codegen/) or [openapi-generator](https://github.com/OpenAPITools/openapi-generator) to override/template the client side behavior to just use the same domain for every request. The `make_api_spec` function tries to force the current RPC sepc into the OpenAPI format, and that gets dumped to the `/dev/api.json` file. If that seems like too much of a pie in the sky idea, I also decided to dump the parameters, requests, and response models into JSON schema in the `/dev/models.json` file. I chose to use the parameters models when building the Python interface just because it gave me a place where I could easily reference, validate, and even document the expected parameters. I then simply ignore the keys and just dump the values into a list when passing it through the request body. On the python end of things, I use (datamodel-code-generator)[https://koxudaxi.github.io/datamodel-code-generator/]. 


Any development dependencies I've left listed as optional, and could be installed directly with `pip install -e ".[dev]"`. This includes the tools I used to go from spec to code when playing with Rosetta, as well as now from code to spec in the case of the RPC endpoints. 

## Additional Usage Examples

Getting information about the blockchain network:

```python
>>> api.current_block_number()
82570
>>> api.circulating_supply()
8754866999.999996
>>> api.total_supply()
12600000000.0
>>> api.current_epoch()
0
>>> api.current_leader()
one1gh043zc95e6mtutwy5a2zhvsxv7lnlklkj42ux
>>> api.sharding_structure()
[ShardingStructure(current=True, http='https://api.s0.t.hmny.io', shardID=0, ws='wss://ws.s0.t.hmny.io'), ShardingStructure(current=False, http='https://api.s1.t.hmny.io', shardID=1, ws='wss://ws.s1.t.hmny.io'), ShardingStructure(current=False, http='https://api.s2.t.hmny.io', shardID=2, ws='wss://ws.s2.t.hmny.io'), ShardingStructure(current=False, http='https://api.s3.t.hmny.io', shardID=3, ws='wss://ws.s3.t.hmny.io')]
>>> api.current_gas_price()
1
>>> api.validators_by_epoch(0)
ValidatorIDs(shardID=0, validators=[ValidatorAddress(address='one1gh043zc95e6mtutwy5a2zhvsxv7lnlklkj42ux', balance=21079976502885862933750), ValidatorAddress(address='one1jyvcqu4k0rszgf3r2a02tm89dzd68arw5lz9vl', balance=21061942126983757348668), ValidatorAddress(address='one1nn2c86kwaq4nk8lda50fnepepqr9y73kd9w2z3', balance=21078398443366275981766), ValidatorAddress(address='one1u7jzpkd3sr40kzw62vjval85dkzeyn3g2shz83', balance=21079278293570103981559), ... )]
>>> api.validators_by_epoch(0, as_pubkeys=True)
['ca23704be46ce9c4704681ac9c08ddc644f1858a5c28ce236e1b5d9dee67c1f5a28075b5ef089adeffa8a372c1762007', '50b20b4eb89041aa4715e87e4aa6430e674658959d8be657d43e4d3d4c35d7507d6a40aec5188218dcbb5460e354fd12', '5ecf182ef0cfe449470d900dbe4ce312d534c882765e639c59525f2710d9f96a04abd871e4f0afadc1bd4b07a54ea106', '6350958f98fad3d2aa3d8655d11f60acd67a8f9574f580b5f09bd602c644365c548484a0d2a06714124b9f6e01dcd794', ... ]
```

Getting information about the staking network:

```python
>>> api.staking_network_info()
StakingNetworkInfo(total_supply='12600000000.000000000000000000', circulating_supply='8754866999.999996400000000000', epoch_last_block=344063, total_staking=0, median_raw_stake='0.000000000000000000')
>>> api.current_utility_metrics()
UtilityMetrics(AccumulatorSnapshot=0, CurrentStakedPercentage='0.000000000000000000', Deviation='0.350000000000000000', Adjustment='14000000000000000000.000000000000000000')
>>> api.median_raw_stake_snapshot()
MedianRawStakeSnapshot(epos_median_stake='0.000000000000000000', max_external_slots=160, epos_slot_winners=[], epos_slot_candidates=[])
```

Getting information about the transaciton pool:

```python
>>> api.transaction_pool_stats()
PoolStats(executable_count='0', non_executable_count='0')
```

Getting Blocks:


```python
>>> api.get_block(35578)
Block(difficulty=0, epoch=0, extraData='0x', gasLimit=500000000000000000, gasUsed=0, hash_='0xf9b615fff47cc367eacb2a99540932599391825e9fe82abbf115780fa8e60c1d', logsBloom='0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', miner='one1gh043zc95e6mtutwy5a2zhvsxv7lnlklkj42ux', mixHash='0x0000000000000000000000000000000000000000000000000000000000000000', nonce=0, number=35578, parentHash='0x90393dec0f919b7aca4567f8bba51b2448f5feccf0616451ea3d6823c7d3b11b', receiptsRoot='0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421', size=629, stakingTransactions=[], stateRoot='0xbb667254146ee94503d24f8fa9f1acb32b421bebb32f593aa85c437cae5c9ec1', timestamp=1562026425, transactions=[], transactionsRoot='0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421', uncles=[], viewID=35577)
>>> api.get_block_signers(35578)
['one1gh043zc95e6mtutwy5a2zhvsxv7lnlklkj42ux', 'one1jyvcqu4k0rszgf3r2a02tm89dzd68arw5lz9vl', 'one1nn2c86kwaq4nk8lda50fnepepqr9y73kd9w2z3', 'one1u7jzpkd3sr40kzw62vjval85dkzeyn3g2shz83', 'one1tfrpfvrgj5tnxj029xsdkl33hmrsry056nrpvt', 'one1fg0nrc7djkm2p47tjsuhd8n9435mz9ed57dj8v', ... ]
```


Rosetta Endpoints:

Rosetta endpoints are exposed under the `.rosetta` property on the api object. See `rosetta-api-client-python` for those supported endpoints.

(Currently untested and being cleaned up)

```python
>>> api.rosetta.list_supported_networks()
[NetworkIdentifier(blockchain='Harmony', network='Mainnet', sub_network_identifier=SubNetworkIdentifier(network='shard 0', metadata={'is_beacon': True}))]
```

## Useful Resources

* [rosetta-api-client-python](https://github.com/blockjoe/rosetta-api-client-python): the Python client library that faciliates the Rosetta API calls.
* [Harmony API Documentation](https://docs.harmony.one/home/developers/api): Harmony's official API docs
* [Rosetta Harmony API Documentation](https://api.hmny.io/): Harmony's API docs that include documentation on the Rosetta endpoints.
* [Rosetta Harmony Community Post](https://community.rosetta-api.org/t/harmonys-rosetta-data-construction-api/293): the official page for Harmony's rosetta integration



