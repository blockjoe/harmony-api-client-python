from typing import Optional, Union

import requests

from .models import (
    AddressParameters,
    AddressBlockNumberParameters,
    BalanceResponse,
    TransactionsCountParameters,
    TransactionCountResponse,
    TransactionsHashListResponse,
    TransactionsHistoryObject,
    TransactionsHistoryParameters,
    TransactionType,
    SortOrder,
    StakingTransactionListResponse
)

from .endpoints.account import (
    getBalance,
    getBalanceByBlockNumber,
    getStakingTransactionsHistory,
    getStakingTransactionsCount,
    getTransactionsCount,
    getTransactionsHistory
)

def get_balance(api_url : str, address : str, session : Optional[requests.Session] = None) -> BalanceResponse:
    """
    Get the balance of the given wallet address

    Parameters
    ----------
    api_url : str
    address: str
        The wallet address
    session : requests.session, optional
    
    Returns
    -------
    BalanceResponse
    """
    params = AddressParameters(address=address)
    return getBalance(api_url, params, session)

def get_balance_by_block_number(api_url : str, address : str, block_number : int , session : Optional[requests.Session] = None) -> BalanceResponse:
    """
    Get the balance of the given wallet address at the given block
    
    Parameters
    ----------
    api_url : str
    address: str
        The wallet address
    block_number: int
        The block number
    session : requests.session, optional

    Returns    GetTransactionsHistoryTxTypeResponse,

    -------
    BalanceResponse
    """
    params = AddressBlockNumberParameters(address=address, block_number=block_number)
    return getBalanceByBlockNumber(api_url, params, session)

def get_staking_transactions_count(api_url : str, address : str, transaction_type : Optional[TransactionType] = "ALL", session : Optional[requests.Session] = None) -> TransactionCountResponse:
    """
    Get the number of staking transactions on the wallet
    
    Parameters
    ----------
    api_url : str
    address: str
        The wallet address
    transaction_type: str, optional
        Either 'SENT', 'RECEIVED', 'ALL', defaults to 'ALL'
    session : requests.session, optional

    Returns
    -------
    TransactionCountResponse
    """
    params = TransactionsCountParameters(address=address, transaction_type=transaction_type)
    return getStakingTransactionsCount(api_url, params, session)

def get_staking_transactions_history(api_url : str, address : str, page_index : Optional[int] = 0, page_size : Optional[int] = 1000, full_tx : Optional[bool] = False, txType : Optional[TransactionType] = "ALL", order : Optional[SortOrder] = "ASC", session : Optional[requests.Session] = None) -> Union[TransactionsHashListResponse, StakingTransactionListResponse]:
    """
    Get the history of staking transactions on the wallet.
    
    Parameters
    ----------
    api_url : str
    address: str
        The wallet address
    page_index: int, optional
        Which page of transactions to return, defaults to 0
    page_size: int, optional
        The number of transactions per page, defaults to 1000
    full_tx: bool, optional
        If true display the whole transaction object instead of the hash, defaults to Fasle
    transaction_type: str, optional
        Either 'SENT', 'RECEIVED', 'ALL', defaults to 'ALL'
    sort_order: str, optional
        How to sort based on timestamp, either 'ASC' or 'DESC', defaults to 'ASC'
    session : requests.session, optional

    Returns
    -------
    TransactionsHashListResponse if full_tx was True else StakingTransactionListResponse
    """
    obj = TransactionsHistoryObject(address=address, pageIndex=page_index, pageSize=page_size, fullTx=full_tx, txType=transaction_type, order=sort_order)
    params = TransactionsHistoryParameters(obj=obj)
    return getStakingTransactionsHistory(api_url, params, session)

def get_transactions_count(api_url : str, address : str, transaction_type : Optional[TransactionType] = "ALL", session : Optional[requests.Session] = None) -> TransactionCountResponse:
    """
    Get the number of transactions on the wallet
    
    Parameters
    ----------
    api_url : str
    address: str
        The wallet address
    transaction_type: str, optional
        Either 'SENT', 'RECEIVED', 'ALL', defaults to 'ALL'
    session : requests.session, optional

    Returns
    -------
    TransactionCountResponse
    """
    params = TransactionsCountParameters(address=address, transaction_type=transaction_type)
    return getTransactionsCount(api_url, params, session)

def get_transactions_history(api_url : str, address : str, page_index : Optional[int] = 0, page_size : Optional[int] = 1000, full_tx : Optional[bool] = False, txType : Optional[TransactionType] = "ALL", order : Optional[SortOrder] = "ASC", session : Optional[requests.Session] = None) -> Union[TransactionsHashListResponse, TransactionListResponse]:
    """
    Get the history of transactions on the wallet.
    
    Parameters
    ----------
    api_url : str
    address: str
        The wallet address
    page_index: int, optional
        Which page of transactions to return, defaults to 0
    page_size: int, optional
        The number of transactions per page, defaults to 1000
    full_tx: bool, optional
        If true display the whole transaction object instead of the hash, defaults to Fasle
    transaction_type: str, optional
        Either 'SENT', 'RECEIVED', 'ALL', defaults to 'ALL'
    sort_order: str, optional
        How to sort based on timestamp, either 'ASC' or 'DESC', defaults to 'ASC'
    session : requests.session, optional

    Returns
    -------
    TransactionsHashListResponse if full_tx was True else TransactionListResponse
    """
    obj = TransactionsHistoryObject(address=address, pageIndex=page_index, pageSize=page_size, fullTx=full_tx, txType=transaction_type, order=sort_order)
    params = TransactionsHistoryParameters(obj=obj)
    return getTransactionsHistory(api_url, params, session)