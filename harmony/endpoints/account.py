from typing import Optional, Union

import requests

from ..utils.communication import format_api_data, post_request

from ..models import (
    GetBalanceParameters,
    GetBalanceResponse,
    GetBalanceByBlockNumberParameters,
    GetBalanceByBlockNumberResponse,
    GetStakingTransactionsCountParameters,
    GetStakingTransactionsCountResponse,
    GetStakingTransactionsHistoryParameters,
    GetStakingTransactionsHistoryResponse,
    GetStakingTransactionsHistoryTxTypeResponse, 
    GetTransactionsCountParameters,
    GetTransactionsCountResponse,
    GetTransactionsHistoryParameters,
    GetTransactionsHistoryResponse,
    GetTransactionsHistoryTxTypeResponse 
)

def getBalance(api_url : str, params : GetBalanceParameters, session : Optional[requests.Session] = None) -> GetBalanceResponse:
    """
    params: GetBalanceParameters
    result: GetBalanceResponse
    method: hmyv2_getBalance
    """
    data = format_api_data("hmyv2_getBalance", params)
    resp = post_request(api_url, data, session)
    
    return GetBalanceResponse(**resp.json())

def getBalanceByBlockNumber(api_url : str, params : GetBalanceByBlockNumberParameters, session : Optional[requests.Session] = None) -> GetBalanceByBlockNumberResponse:
    """
    params: GetBalanceByBlockNumberParameters
    result: GetBalanceByBlockNumberResponse
    method: hmyv2_getBalanceByBlockNumber
    """
    data = format_api_data("hmyv2_getBalanceByBlockNumber", params)
    resp = post_request(api_url, data, session)
    
    return GetBalanceByBlockNumberResponse(**resp.json())

def getStakingTransactionsCount(api_url : str, params : GetStakingTransactionsCountParameters, session : Optional[requests.Session] = None) -> GetStakingTransactionsCountResponse:
    """
    params: GetStakingTransactionsCountParameters
    result: GetStakingTransactionsCountResponse
    method: hmyv2_getStakingTransactionsCount
    """
    data = format_api_data("hmyv2_getStakingTransactionsCount", params)
    resp = post_request(api_url, data, session)
    
    return GetStakingTransactionsCountResponse(**resp.json())

def getStakingTransactionsHistory(api_url : str, params : GetStakingTransactionsHistoryParameters, session : Optional[requests.Session] = None) -> Union[GetStakingTransactionsHistoryResponse, GetStakingTransactionsHistoryTxTypeResponse]:
    """
    params: GetStakingTransactionsHistoryParameters
    result: GetStakingTransactionsHistoryResponse
    method: hmyv2_getStakingTransactionsHistory
    """
    data = format_api_data("hmyv2_getStakingTransactionsHistory", params)
    resp = post_request(api_url, data, session)
    
    if data["params"][0]["txType"]:
        return GetStakingTransactionsHistoryTxTypeResponse(**resp.json())
    return GetStakingTransactionsHistoryResponse(**resp.json())

def getTransactionsCount(api_url : str, params : GetTransactionsCountParameters, session : Optional[requests.Session] = None) -> GetTransactionsCountResponse:
    """
    params: GetTransactionsCountParameters
    result: GetTransactionsCountResponse
    method: hmyv2_getTransactionsCount
    """
    data = format_api_data("hmyv2_getTransactionsCount", params)
    resp = post_request(api_url, data, session)
    
    return GetTransactionsCountResponse(**resp.json())

def getTransactionsHistory(api_url : str, params : GetTransactionsHistoryParameters, session : Optional[requests.Session] = None) -> Union[GetTransactionsHistoryResponse, GetTransactionsHistoryTxTypeResponse]:
    """
    params: GetTransactionsHistoryParameters
    result: GetTransactionsHistoryResponse
    method: hmyv2_getTransactionsHistory
    """
    data = format_api_data("hmyv2_getTransactionsHistory", params)
    resp = post_request(api_url, data, session)
    
    if data["params"][0]["txType"]:
        return GetTransactionsHistoryTxTypeResponse(**resp.json())
    return GetTransactionsHistoryResponse(**resp.json())