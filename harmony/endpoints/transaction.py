from typing import Optional

import requests

from ..utils.communication import post_request
from ..utils.call_format import format_api_data

from ..models import (
    GetCXReceiptByHashParameters,
    GetCXReceiptByHashResults,
    GetPendingCXReceiptsParameters,
    GetPendingCXReceiptsResults,
    ResendCxParameters,
    ResendCxResults,
    GetPoolStatsParameters,
    GetPoolStatsResults,
    PendingStakingTransactionsParameters,
    PendingStakingTransactionsResults,
    PendingTransactionsParameters,
    PendingTransactionsResults,
    GetCurrentStakingErrorSinkParameters,
    GetCurrentStakingErrorSinkResults,
    GetStakingTransactionByBlockNumberAndIndexParameters,
    GetStakingTransactionByBlockNumberAndIndexResults,
    GetStakingTransactionByBlockHashAndIndexParameters,
    GetStakingTransactionByBlockHashAndIndexResults,
    GetStakingTransactionByHashParameters,
    GetStakingTransactionByHashResults,
    SendRawStakingTransactionParameters,
    SendRawStakingTransactionResults,
    GetCurrentTransactionErrorSinkParameters,
    GetCurrentTransactionErrorSinkResults,
    GetTransactionByBlockHashAndIndexParameters,
    GetTransactionByBlockHashAndIndexResults,
    GetTransactionByBlockNumberAndIndexParameters,
    GetTransactionByBlockNumberAndIndexResults,
    GetTransactionByHashParameters,
    GetTransactionByHashResults,
    GetTransactionReceiptParameters,
    GetTransactionReceiptResults,
    SendRawTransactionParameters,
    SendRawTransactionResults,
)

#Cross shard

def getCXReceiptByHash(api_url : str, params : GetCXReceiptByHashParameters, session : Optional[requests.Session] = None) -> GetCXReceiptByHashResults:
	"""
    params: GetCXReceiptByHashParameters
    result: GetCXReceiptByHashResults
    method: hmyv2_getCXReceiptByHash
    """
    data = format_api_data("hmyv2_getCXReceiptByHash", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetCXReceiptByHashResults(**results)


def getPendingCXReceipts(api_url : str, params : GetPendingCXReceiptsParameters, session : Optional[requests.Session] = None) -> GetPendingCXReceiptsResults:
	"""
    params: GetPendingCXReceiptsParameters
    result: GetPendingCXReceiptsResults
    method: hmyv2_getPendingCXReceipts
    """
    data = format_api_data("hmyv2_getPendingCXReceipts", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetPendingCXReceiptsResults(**results)


def resendCx(api_url : str, params : ResendCxParameters, session : Optional[requests.Session] = None) -> ResendCxResults:
	"""
    params: ResendCxParameters
    result: ResendCxResults
    method: hmyv2_resendCx
    """
    data = format_api_data("hmyv2_resendCx", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return ResendCxResults(**results)

#Transaction Pool

def getPoolStats(api_url : str, params : GetPoolStatsParameters, session : Optional[requests.Session] = None) -> GetPoolStatsResults:
	"""
    params: GetPoolStatsParameters
    result: GetPoolStatsResults
    method: hmyv2_getPoolStats
    """
    data = format_api_data("hmyv2_getPoolStats", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetPoolStatsResults(**results)

def pendingStakingTransactions(api_url : str, params : PendingStakingTransactionsParameters, session : Optional[requests.Session] = None) -> PendingStakingTransactionsResults:
	"""
    params: PendingStakingTransactionsParameters
    result: PendingStakingTransactionsResults
    method: hmyv2_pendingStakingTransactions
    """
    data = format_api_data("hmyv2_pendingStakingTransactions", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return PendingStakingTransactionsResults(**results)

def pendingTransactions(api_url : str, params : PendingTransactionsParameters, session : Optional[requests.Session] = None) -> PendingTransactionsResults:
	"""
    params: PendingTransactionsParameters
    result: PendingTransactionsResults
    method: hmyv2_pendingTransactions
    """
    data = format_api_data("hmyv2_pendingTransactions", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return PendingTransactionsResults(**results)

#Staking

def getCurrentStakingErrorSink(api_url : str, params : GetCurrentStakingErrorSinkParameters, session : Optional[requests.Session] = None) -> GetCurrentStakingErrorSinkResults:
	"""
    params: GetCurrentStakingErrorSinkParameters
    result: GetCurrentStakingErrorSinkResults
    method: hmyv2_getCurrentStakingErrorSink
    """
    data = format_api_data("hmyv2_getCurrentStakingErrorSink", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetCurrentStakingErrorSinkResults(**results)

def getStakingTransactionByBlockNumberAndIndex(api_url : str, params : GetStakingTransactionByBlockNumberAndIndexParameters, session : Optional[requests.Session] = None) -> GetStakingTransactionByBlockNumberAndIndexResults:
	"""
    params: GetStakingTransactionByBlockNumberAndIndexParameters
    result: GetStakingTransactionByBlockNumberAndIndexResults
    method: hmyv2_getStakingTransactionByBlockNumberAndIndex
    """
    data = format_api_data("hmyv2_getStakingTransactionByBlockNumberAndIndex", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetStakingTransactionByBlockNumberAndIndexResults(**results)

def getStakingTransactionByBlockHashAndIndex(api_url : str, params : GetStakingTransactionByBlockHashAndIndexParameters, session : Optional[requests.Session] = None) -> GetStakingTransactionByBlockHashAndIndexResults:
	"""
    params: GetStakingTransactionByBlockHashAndIndexParameters
    result: GetStakingTransactionByBlockHashAndIndexResults
    method: hmyv2_getStakingTransactionByBlockHashAndIndex
    """
    data = format_api_data("hmyv2_getStakingTransactionByBlockHashAndIndex", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetStakingTransactionByBlockHashAndIndexResults(**results)

def getStakingTransactionByHash(api_url : str, params : GetStakingTransactionByHashParameters, session : Optional[requests.Session] = None) -> GetStakingTransactionByHashResults:
	"""
    params: GetStakingTransactionByHashParameters
    result: GetStakingTransactionByHashResults
    method: hmyv2_getStakingTransactionByHash
    """
    data = format_api_data("hmyv2_getStakingTransactionByHash", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetStakingTransactionByHashResults(**results)

def sendRawStakingTransaction(api_url : str, params : SendRawStakingTransactionParameters, session : Optional[requests.Session] = None) -> SendRawStakingTransactionResults:
	"""
    params: SendRawStakingTransactionParameters
    result: SendRawStakingTransactionResults
    method: hmyv2_sendRawStakingTransaction
    """
    data = format_api_data("hmyv2_sendRawStakingTransaction", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return SendRawStakingTransactionResults(**results)

#Transfer

def getCurrentTransactionErrorSink(api_url : str, params : GetCurrentTransactionErrorSinkParameters, session : Optional[requests.Session] = None) -> GetCurrentTransactionErrorSinkResults:
	"""
    params: GetCurrentTransactionErrorSinkParameters
    result: GetCurrentTransactionErrorSinkResults
    method: hmyv2_getCurrentTransactionErrorSink
    """
    data = format_api_data("hmyv2_getCurrentTransactionErrorSink", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetCurrentTransactionErrorSinkResults(**results)

def getTransactionByBlockHashAndIndex(api_url : str, params : GetTransactionByBlockHashAndIndexParameters, session : Optional[requests.Session] = None) -> GetTransactionByBlockHashAndIndexResults:
	"""
    params: GetTransactionByBlockHashAndIndexParameters
    result: GetTransactionByBlockHashAndIndexResults
    method: hmyv2_getTransactionByBlockHashAndIndex
    """
    data = format_api_data("hmyv2_getTransactionByBlockHashAndIndex", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetTransactionByBlockHashAndIndexResults(**results)

def getTransactionByBlockNumberAndIndex(api_url : str, params : GetTransactionByBlockNumberAndIndexParameters, session : Optional[requests.Session] = None) -> GetTransactionByBlockNumberAndIndexResults:
	"""
    params: GetTransactionByBlockNumberAndIndexParameters
    result: GetTransactionByBlockNumberAndIndexResults
    method: hmyv2_getTransactionByBlockNumberAndIndex
    """
    data = format_api_data("hmyv2_getTransactionByBlockNumberAndIndex", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetTransactionByBlockNumberAndIndexResults(**results)

def getTransactionByHash(api_url : str, params : GetTransactionByHashParameters, session : Optional[requests.Session] = None) -> GetTransactionByHashResults:
	"""
    params: GetTransactionByHashParameters
    result: GetTransactionByHashResults
    method: hmyv2_getTransactionByHash
    """
    data = format_api_data("hmyv2_getTransactionByHash", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetTransactionByHashResults(**results)

def getTransactionReceipt(api_url : str, params : GetTransactionReceiptParameters, session : Optional[requests.Session] = None) -> GetTransactionReceiptResults:
	"""
    params: GetTransactionReceiptParameters
    result: G_Results
    method: hmyv2_getTransactionReceipt
    """
    data = format_api_data("hmyv2_getTransactionReceipt", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetTransactionReceiptResults(**results)

def sendRawTransaction(api_url : str, params : SendRawTransactionParameters, session : Optional[requests.Session] = None) -> SendRawTransactionResults:
	"""
    params: SendRawTransactionParameters
    result: SendRawTransactionResults
    method: hmyv2_sendRawTransaction
    """
    data = format_api_data("hmyv2_sendRawTransaction", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return SendRawTransactionResults(**results)
    