from typing import Optional, Union

import requests

from ..utils.communication import format_api_data, post_request

from ..models import (
    AddressParameters,
    AddressBlockNumberParameters,
    BalanceResponse,
    TransactionsCountParameters,
    TransactionCountResponse,
    TransactionsHashListResponse,
    TransactionsHistoryParameters,
    TransactionListResponse,
    StakingTransactionListResponse

)

def getBalance(api_url : str, params : AddressParameters, session : Optional[requests.Session] = None) -> BalanceResponse:
    """
    params: AddressParameters
    result: BalanceResponse
    method: hmyv2_getBalance
    """
    data = format_api_data("hmyv2_getBalance", params)
    resp = post_request(api_url, data, session)
    return BalanceResponse(**resp.json())

def getBalanceByBlockNumber(api_url : str, params : AddressBlockNumberParameters, session : Optional[requests.Session] = None) -> BalanceResponse:
    """
    params: AddressBlockNumberParameters
    result: BalanceResponse
    method: hmyv2_getBalanceByBlockNumber
    """
    data = format_api_data("hmyv2_getBalanceByBlockNumber", params)
    resp = post_request(api_url, data, session)
    return BalanceResponse(**resp.json())

def getStakingTransactionsCount(api_url : str, params : TransactionsCountParameters, session : Optional[requests.Session] = None) -> TransactionCountResponse:
    """
    params: TransactionsCountParameters
    result: TransactionCountResponse
    method: hmyv2_getStakingTransactionsCount
    """
    data = format_api_data("hmyv2_getStakingTransactionsCount", params)
    resp = post_request(api_url, data, session)
    return TransactionCountResponse(**resp.json())

def getStakingTransactionsHistory(api_url : str, params : TransactionsHistoryParameters, session : Optional[requests.Session] = None) -> Union[TransactionsHashListResponse, StakingTransactionListResponse]:
    """
    params: TransactionsHistoryParameters
    result: TransactionsHashListResponse or StakingTransactionListResponse
    method: hmyv2_getStakingTransactionsHistory
    """
    data = format_api_data("hmyv2_getStakingTransactionsHistory", params)
    resp = post_request(api_url, data, session)
    
    if params.obj.fullTx:
        return StakingTransactionListResponse(**resp.json())
    return TransactionsHashListResponse(**resp.json())

def getTransactionsCount(api_url : str, params : TransactionsCountParameters, session : Optional[requests.Session] = None) -> TransactionCountResponse:
    """
    params: TransactionsCountParameters
    result: TransactionCountResponse
    method: hmyv2_getTransactionsCount
    """
    data = format_api_data("hmyv2_getTransactionsCount", params)
    resp = post_request(api_url, data, session)
    return TransactionCountResponse(**resp.json())

def getTransactionsHistory(api_url : str, params : TransactionsHistoryParameters, session : Optional[requests.Session] = None) -> Union[TransactionsHashListResponse, TransactionListResponse]:
    """
    params: TransactionsHistoryParameters
    result: TransactionsHashListResponse or TransactionListResponse
    method: hmyv2_getTransactionsHistory
    """
    data = format_api_data("hmyv2_getTransactionsHistory", params)
    resp = post_request(api_url, data, session)
    if params.obj.fullTx:
        return TransactionListResponse(**resp.json())
    return TransactionsHashListResponse(**resp.json())