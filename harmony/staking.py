from typing import Optional

import requests

from .models import (
    BlockNumberAndIndexParameters,
    GetCurrentStakingErrorSinkResponse,
    HashParameters,
    HashAndIndexParameters,
    RawTransactionParameters,
    SendRawStakingTransactionResponse,
    StakingTransactionResponse
)

from .endpoints.transaction import (
    getCurrentStakingErrorSink,
    getStakingTransactionByBlockHashAndIndex,
    getStakingTransactionByBlockNumberAndIndex,
    getStakingTransactionByHash,
    sendRawStakingTransaction    
)

def get_current_staking_error_sink(api_url : str, session : Optional[requests.Session] = None) -> GetCurrentStakingErrorSinkResponse:
    """
    Get the current staking errors
    
    Parameters
    ----------
    api_url : str
    session : requests.Session, optional

    Returns
    -------
    result : list[StakingError]
    """
    return getCurrentStakingErrorSink(api_url, session)

def get_staking_transaction_by_block_number_and_index(api_url : str, block_number : int, index : int, session : Optional[requests.Session] = None) -> StakingTransactionResponse:
    """
    Get the staking transaction by block number and index

    Parameters
    ----------
    api_url : str
    block_number : int
    index : int
        staking transaction index
    session : requests.Session, optional

    Returns
    -------
    result : StakingTransaction
    """
    params = BlockNumberAndIndexParameters(block_number=block_number, index=index)
    return getStakingTransactionByBlockNumberAndIndex(api_url, params, session)

def get_staking_transaction_by_block_hash_and_index(api_url : str, block_hash : str, index : int, session : Optional[requests.Session] = None) -> StakingTransactionResponse:
    """
    Get the staking transaction by block hash and index

    Parameters
    ----------
    api_url : str
    block_hash : str
    index : int
        staking transaction index
    session : requests.Session, optional

    Returns
    -------
    result : StakingTransaction
    """
    params = HashAndIndexParameters(hash=block_hash, index=index)
    return getStakingTransactionByBlockNumberAndIndex(api_url, params, session)

def get_staking_transaction_by_hash(api_url : str, staking_transaction_hash : str, session : Optional[requests.Session] = None) -> StakingTransactionResponse:
    """
    Get the staking transaction by its hash

    Parameters
    ----------
    api_url : str
    staking_transaction_hash : str
    session : requests.Session, optional

    Returns
    -------
    result : StakingTransaction
    """
    params = HashParameters(hash=staking_transaction_hash)
    return getStakingTransactionByHash(api_url, params, session)

def send_raw_staking_transaction(api_url : str, staking_transaction_hex : str, session : Optional[requests.Session] = None) -> StakingTransactionResponse:
    """
    Send the raw staking transaction

    Parameters
    ----------
    api_url : str
    staking_transaction_hex : str
        Hex representation of signed staking transaction
    session : requests.Session, optional

    Returns
    -------
    result : str
        The staking transaction hash if it was successfully added to the pool
    """
    params = RawTransactionParameters(transaction_hex=staking_transaction_hex)
    return sendRawStakingTransaction(api_url, params, session)
