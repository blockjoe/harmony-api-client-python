from typing import Optional

import requests

from .models import (
    BlockNumberResponse,
    BLSKeyListResponse,
    EphochNumberParameters,
    GetCirculatingSupplyResponse,
    GetEpochResponse,
    GetLastCrossLinksResponse,
    GetLeaderResponse,
    GetShardingStructureResponse,
    GasPriceResponse,
    GetTotalSupplyResponse,
    GetValidatorsResponse
)

from .endpoints.blockchain import (
    blockNumber,
    getCirculatingSupply,
    getEpoch,
    getLastCrossLinks,
    getLeader,
    gasPrice, 
    getShardingStructure,
    getTotalSupply,
    getValidators,
    getValidatorKeys
)

def current_block_number(api_url : str, session : Optional[requests.Session] = None) -> BlockNumberResponse:
    """
    Get the current blocknumber

    Parameters
    ----------
    api_url : str
    session : requests.Session, optional

    Returns
    -------
    result : int 
        The current block number
    """
    return blockNumber(api_url, session)

def get_circulating_supply(api_url : str, session : Optional[requests.Session] = None) -> GetCirculatingSupplyResponse:
    """
    Get the current circulating supply of tokens
    
    Parameters
    ----------
    api_url : str
    session : requests.Session, optional

    Returns
    -------
    result : int
        The circulating supply of tokens in ONE
    """
    return getCirculatingSupply(api_url, session)

def get_epoch(api_url : str, session : Optional[requests.Session] = None) -> GetEpochResponse:
    """
    Get the current node shard epoch

    Parameters
    ----------
    api_url : str
    session : requests.Session, optional

    Returns
    -------
    result : int
        The current node shard epoch in decimal
    """
    return getEpoch(api_url, session)

def get_last_cross_links(api_url : str, session : Optional[requests.Session] = None) -> GetLastCrossLinksResponse:
    """
    Parameters
    ----------
    api_url : str
    session : requests.Session, optional

    Returns
    -------
    result : list[CrossLink]
    """
    return getLastCrossLinks(api_url, session)

def get_current_leader(api_url : str, session : Optional[requests.Session] = None) -> GetLeaderResponse:
    """
    Get the wallet address of the current leader

    Parameters
    ----------
    api_url : str
    session : requests.Session, optional

    Returns
    -------
    result : str
        The wallet address of the current leader
    """
    return getLeader(api_url, session)

def get_current_gas_price(api_url : str, session : Optional[requests.Session] = None) -> GasPriceResponse:
    """
    Get the current average gas price of transactions

    Parameters
    ----------
    api_url : str
    session : requests.Session, optional

    Returns
    -------
    result : int
        The current average gas price
    """
    return gasPrice(api_url, session)

def get_sharding_structure(api_url : str, session : Optional[requests.Session] = None) -> GetShardingStructureResponse:
    """
    Get the the current shard of the node and the API and WebSocket endpoints for each shard.

    Parameters
    ----------
    api_url : str
    session : requests.Session, optional

    Returns
    -------
    result : list[ShardingStructure]
    """
    return getShardingStructure(api_url, session)

def get_total_supply(api_url : str, session : Optional[requests.Session] = None) -> GetTotalSupplyResponse:
    """
    Get the total number of mined tokens

    Parameters
    ----------
    api_url : str
    session : requests.Session, optional

    Returns
    -------
    result : int
        The total number of mined tokens
    """
    return getTotalSupply(api_url, session)

def get_validators_by_epoch(api_url : str, epoch_number : int, session : Optional[requests.Session] = None) -> GetValidatorsResponse:
    """
    Get the validators for a given epoch

    Parameters
    ----------
    api_url : str
    epoch_number : int
    session : requests.Session, optional

    Returns
    -------
    result : ValidatorIDs
        The validator addresses and balances on a given shard
    """
    params = EphochNumberParameters(epoch_number=epoch_number)
    return getValidators(api_url, params, session)

def get_validator_keys_by_epoch(api_url : str, epoch_number : int, session : Optional[requests.Session] = None) -> GetValidatorsResponse:
    """
    Get the public keys of the validator for a given epoch

    Parameters
    ----------
    api_url : str
    epoch_number : int
    session : requests.Session, optional

    Returns
    -------
    result : list[str]
        List of public keys
    """
    params = EphochNumberParameters(epoch_number=epoch_number)
    return getValidatorKeys(api_url, params, session)
