from typing import Optional, Union

import requests

from ..utils.communication import format_api_data, post_request

from ..models import (
    GetBalanceParameters,
    GetBalanceResults,
    GetBalanceByBlockNumberParameters,
    GetBalanceByBlockNumberResults,
    GetStakingTransactionsCountParameters,
    GetStakingTransactionsCountResults,
    GetStakingTransactionsHistoryParameters,
    GetStakingTransactionsHistoryResults,
    GetStakingTransactionsHistoryTxTypeResults,
    GetTransactionsCountParameters,
    GetTransactionsCountResults,
    GetTransactionsHistoryParameters,
    GetTransactionsHistoryResults,
    GetTransactionsHistoryTxTypeResults
)

def getBalance(api_url : str, params : GetBalanceParameters, session : Optional[requests.Session] = None) -> GetBalanceResults:
	"""
    params: GetBalanceParameters
    result: GetBalanceResults
    method: hmyv2_getBalance
    """
    data = format_api_data("hmyv2_getBalance", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetBalanceResults(**results)

def getBalanceByBlockNumber(api_url : str, params : GetBalanceByBlockNumberParameters, session : Optional[requests.Session] = None) -> GetBalanceByBlockNumberResults:
	"""
    params: GetBalanceByBlockNumberParameters
    result: GetBalanceByBlockNumberResults
    method: hmyv2_getBalanceByBlockNumber
    """
    data = format_api_data("hmyv2_getBalanceByBlockNumber", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetBalanceByBlockNumberResults(**results)

def getStakingTransactionsCount(api_url : str, params : GetStakingTransactionsCountParameters, session : Optional[requests.Session] = None) -> GetStakingTransactionsCountResults:
	"""
    params: GetStakingTransactionsCountParameters
    result: GetStakingTransactionsCountResults
    method: hmyv2_getStakingTransactionsCount
    """
    data = format_api_data("hmyv2_getStakingTransactionsCount", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetStakingTransactionsCountResults(**results)

def getStakingTransactionsHistory(api_url : str, params : GetStakingTransactionsHistoryParameters, session : Optional[requests.Session] = None) -> Union[GetStakingTransactionsHistoryResults, GetStakingTransactionsHistoryTxTypeResults]:
	"""
    params: GetStakingTransactionsHistoryParameters
    result: GetStakingTransactionsHistoryResults
    method: hmyv2_getStakingTransactionsHistory
    """
    data = format_api_data("hmyv2_getStakingTransactionsHistory", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    if data["txType"]:
        return GetStakingTransactionsHistoryTxTypeResults(**results)
    return GetStakingTransactionsHistoryResults(**results)

def getTransactionsCount(api_url : str, params : GetTransactionsCountParameters, session : Optional[requests.Session] = None) -> GetTransactionsCountResults:
	"""
    params: GetTransactionsCountParameters
    result: GetTransactionsCountResults
    method: hmyv2_getTransactionsCount
    """
    data = format_api_data("hmyv2_getTransactionsCount", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetTransactionsCountResults(**results)

def getTransactionsHistory(api_url : str, params : GetTransactionsHistoryParameters, session : Optional[requests.Session] = None) -> Union[GetTransactionsHistoryResults, GetTransactionsHistoryTxTypeResults]:
	"""
    params: GetTransactionsHistoryParameters
    result: GetTransactionsHistoryResults
    method: hmyv2_getTransactionsHistory
    """
    data = format_api_data("hmyv2_getTransactionsHistory", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    if data["txType"]:
        return GetTransactionsHistoryTxTypeResults(**results)
    return GetTransactionsHistoryResults(**results)