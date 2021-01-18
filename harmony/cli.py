from enum import Enum

import typer

from .api import HarmonyAPI

api = HarmonyAPI('https://rpc.s0.t.hmny.io/', "http://localhost:9700/") 

app = typer.Typer()

class CurrentObject(str, Enum):
    metadata = "metadata"
    peers = "peers"
    protocol = "protocol"
    bad_blocks = "bad_blocks"
    gas_price = "gas_price"
    circulating_supply = "circulating_supply"
    total_supply = "total_supply"
    block_number = "block_number"
    block_header = "block_header"
    block = "block"
    leader = "leader"
    sharding_structure = "sharding_structure"
    epoch = "epoch"
    utility_metrics = "utility_metrics"
    staking_network_info = "staking_network_info"
    super_committees = "super_committees"
    median_stake = "median_stake"
    tx_pool_stats = "tx_pool_stats"
    pending_txs = "pending_txs"
    pending_staking_txs = "pending_staking_txs"
    chain_header = "chain_header"
    validators = "validators"
    tx_errors = "tx_errors"
    staking_tx_errors = "staking_tx_errors"
    elected = "elected"

class RosettaAction(str, Enum):
    get_networks = "get-networks"
    discover_networks = "discover-networks"

@app.command()
def rosetta(rosetta_action : RosettaAction):
    if rosetta_action == "get-networks":
        res = api.rosetta.list_supported_networks()
        start = typer.style("Supported Networks:\n", fg=typer.colors.GREEN, bold=True)
        out = '\n'.join([str(r) for r in res])
        typer.echo(start + out)
    elif rosetta_action == "discover-networks":
        res = api.rosetta.discover_networks()
        start = typer.style("Networks:\n", fg=typer.colors.GREEN, bold=True)
        out = '\n'.join([str(r) for r in res])
        typer.echo(start + out)

@app.command()
def current(item : CurrentObject):
    """
    View the current status of the desired item.
    """
    if item == "metadata":
        res = api.node_metadata()
    elif item == "peers":
        start = typer.style("Number of peers: ", fg=typer.colors.GREEN, bold=True)
        n = api.peer_count()
        typer.echo(start + str(n))
    elif item == "protocol":
        res = api.protocol_version()
    elif item == "bad_blocks":
        res = api._current_bad_blocks()
    elif item == "gas_price":
        res = api.current_gas_price()
    elif item == "circulating_supply":
        res = api.circulating_supply()
        start = typer.style("Circulating Supply: ", fg=typer.colors.GREEN, bold=True)
        end = typer.style(" ONE", fg=typer.colors.BRIGHT_BLUE, bold=True)
        typer.echo(start + str(res) + end)
    elif item == "total_supply":
        res = api.total_supply()
        start = typer.style("Circulating Supply: ", fg=typer.colors.GREEN, bold=True)
        end = typer.style(" ONE", fg=typer.colors.BRIGHT_BLUE, bold=True)
        typer.echo(start + str(res) + end)
    elif item == "block_number":
        res = api.current_block_number()
    elif item == "block_header":
        res = api.block_header()
    elif item == "block":
        block_num = api.current_block_number()
        res = api.get_block(block_number=block_num)
    elif item == "leader":
        res = api.current_leader()
    elif item == "sharding_structure":
        res = api.sharding_structure()
    elif item == "epoch":
        res = api.current_epoch()
    elif item == "utility_metrics":
        res = api.current_utility_metrics()
    elif item == "staking_network_info":
        res = api.staking_network_info()
    elif item == "super_committees":
        res = api.latest_super_committes()
    elif item == "median_stake":
        res = api.median_raw_stake_snapshot()
    elif item == "tx_pool_stats":
        res = api.transaction_pool_stats()
    elif item == "pending_txs":
        res = api.pending_transactions()
    elif item == "pending_staking_txs":
        res = api.pending_staking_transactions()
    elif item == "chain_header":
        res = api.latest_chain_headers()
    elif item == "validators":
        res = api.get_all_validators()
        start = typer.style("Current Validators:\n")
        typer.echo(start)
        for val in res:
            typer.echo("  - {}".format(val))
    elif item == "tx_errors":
        res = api.current_transaction_error_sink()
    elif item == "staking_tx_errors":
        res = api.current_staking_transaction_error_sink()
    elif item == "elected":
        res = api.get_all_elected_validators()

def main():
    app()

if __name__ == '__main__':
    main()