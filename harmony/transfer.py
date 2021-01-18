from typing import Optional

import requests

from .models import (
    BlockNumberAndIndexParameters,
    GetCurrentTransactionErrorSinkResponse,
    HashParameters,
    HashAndIndexParameters,
    RawTransactionParameters,
    SendRawTransactionResponse,
    TransactionResponse
)

from .endpoints.transaction import (
    getCurrentTransactionErrorSink,
    getTransactionByBlockHashAndIndex,
    getTransactionByBlockNumberAndIndex,
    getTransactionByHash,
    sendRawTransaction    
)

def get_current_transaction_error_sink(api_url : str, session : Optional[requests.Session] = None) -> GetCurrentTransactionErrorSinkResponse:
    """
    Get the current transaction errors
    
    Parameters
    ----------
    api_url : str
    session : requests.Session, optional

    Returns
    -------
    result : list[TransactionError]
    """
    return getCurrentTransactionErrorSink(api_url, session)

def get_transaction_by_block_number_and_index(api_url : str, block_number : int, index : int, session : Optional[requests.Session] = None) -> TransactionResponse:
    """
    Get the transaction by block number and index

    Parameters
    ----------
    api_url : str
    block_number : int
    index : int
        transaction index
    session : requests.Session, optional

    Returns
    -------
    result : Transaction
    """
    params = BlockNumberAndIndexParameters(block_number=block_number, index=index)
    return getTransactionByBlockNumberAndIndex(api_url, params, session)

def get_transaction_by_block_hash_and_index(api_url : str, block_hash : str, index : int, session : Optional[requests.Session] = None) -> TransactionResponse:
    """
    Get the transaction by block hash and index

    Parameters
    ----------
    api_url : str
    block_hash : str
    index : int
        transaction index
    session : requests.Session, optieronal

    Returns
    -------
    result : Transaction
    """
    params = HashAndIndexParameters(hash=block_hash, index=index)
    return getTransactionByBlockNumberAndIndex(api_url, params, session)

def get_transaction_by_hash(api_url : str, transaction_hash : str, session : Optional[requests.Session] = None) -> TransactionResponse:
    """
    Get the transaction by its hash

    Parameters
    ----------
    api_url : str
    transaction_hash : str
    session : requests.Session, optional

    Returns
    -------
    result : Transaction
    """
    params = HashParameters(hash=transaction_hash)
    return getTransactionByHash(api_url, params, session)

def send_raw_transaction(api_url : str, transaction_hex : str, session : Optional[requests.Session] = None) -> TransactionResponse:
    """
    Send the raw transaction

    Parameters
    ----------
    api_url : str
    transaction_hex : str
        Hex representation of signed transaction
    session : requests.Session, optional

    Returns
    -------
    result : str
        The transaction hash if it was successfully added to the pool
    """
    params = RawTransactionParameters(transaction_hex=transaction_hex)
    return sendRawTransaction(api_url, params, session)
