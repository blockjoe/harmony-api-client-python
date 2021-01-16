from typing import Optional

import requests

from ..utils.communication import format_api_data, post_request

from ..models import (
    GetCXReceiptByHashParameters,
    GetCXReceiptByHashResults,
    GetPendingCXReceiptsResults,
    ResendCxParameters,
    ResendCxResults,
    GetPoolStatsResults,
    GetCurrentStakingErrorSinkResults,
    GetStakingTransactionByBlockNumberAndIndexParameters,
    GetStakingTransactionByBlockHashAndIndexParameters,
    GetStakingTransactionByHashParameters,
    SendRawStakingTransactionParameters,
    SendRawStakingTransactionResults,
    GetCurrentTransactionErrorSinkResults,
    GetTransactionByBlockHashAndIndexParameters,
    GetTransactionByBlockNumberAndIndexParameters,
    GetTransactionByHashParameters,
    GetTransactionReceiptParameters,
    GetTransactionReceiptResults,
    SendRawTransactionParameters,
    SendRawTransactionResults,
    StakingTransactionResult,
    StakingTransactionListResults,
    TransactionResult
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


def getPendingCXReceipts(api_url : str, session : Optional[requests.Session] = None) -> GetPendingCXReceiptsResults:
	"""
    params: None
    result: GetPendingCXReceiptsResults
    method: hmyv2_getPendingCXReceipts
    """
    data = format_api_data("hmyv2_getPendingCXReceipts", None)
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

def getPoolStats(api_url : str, session : Optional[requests.Session] = None) -> GetPoolStatsResults:
	"""
    params: None
    result: GetPoolStatsResults
    method: hmyv2_getPoolStats
    """
    data = format_api_data("hmyv2_getPoolStats", None)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetPoolStatsResults(**results)

def pendingStakingTransactions(api_url : str, session : Optional[requests.Session] = None) -> StakingTransactionListResults:
	"""
    params: None
    result: StakingTransactionListResults
    method: hmyv2_pendingStakingTransactions
    """
    data = format_api_data("hmyv2_pendingStakingTransactions", None)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return StakingTransactionListResults(**results)

def pendingTransactions(api_url : str, session : Optional[requests.Session] = None) -> StakingTransactionListResults:
	"""
    params: None
    result: StakingTransactionListResults
    method: hmyv2_pendingTransactions
    """
    data = format_api_data("hmyv2_pendingTransactions", None)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return StakingTransactionListResults(**results)

#Staking

def getCurrentStakingErrorSink(api_url : str, session : Optional[requests.Session] = None) -> GetCurrentStakingErrorSinkResults:
	"""
    params: None
    result: GetCurrentStakingErrorSinkResults
    method: hmyv2_getCurrentStakingErrorSink
    """
    data = format_api_data("hmyv2_getCurrentStakingErrorSink", None)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetCurrentStakingErrorSinkResults(**results)

def getStakingTransactionByBlockNumberAndIndex(api_url : str, params : GetStakingTransactionByBlockNumberAndIndexParameters, session : Optional[requests.Session] = None) -> StakingTransactionResult:
	"""
    params: GetStakingTransactionByBlockNumberAndIndexParameters
    result: StakingTransactionResult
    method: hmyv2_getStakingTransactionByBlockNumberAndIndex
    """
    data = format_api_data("hmyv2_getStakingTransactionByBlockNumberAndIndex", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return StakingTransactionResult(**results)

def getStakingTransactionByBlockHashAndIndex(api_url : str, params : GetStakingTransactionByBlockHashAndIndexParameters, session : Optional[requests.Session] = None) -> StakingTransactionResult:
	"""
    params: GetStakingTransactionByBlockHashAndIndexParameters
    result: StakingTransactionResult
    method: hmyv2_getStakingTransactionByBlockHashAndIndex
    """
    data = format_api_data("hmyv2_getStakingTransactionByBlockHashAndIndex", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return StakingTransactionResult(**results)

def getStakingTransactionByHash(api_url : str, params : GetStakingTransactionByHashParameters, session : Optional[requests.Session] = None) -> StakingTransactionResult:
	"""
    params: GetStakingTransactionByHashParameters
    result: StakingTransactionResult
    method: hmyv2_getStakingTransactionByHash
    """
    data = format_api_data("hmyv2_getStakingTransactionByHash", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return StakingTransactionResult(**results)

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

def getCurrentTransactionErrorSink(api_url : str, session : Optional[requests.Session] = None) -> GetCurrentTransactionErrorSinkResults:
	"""
    params: None
    result: GetCurrentTransactionErrorSinkResults
    method: hmyv2_getCurrentTransactionErrorSink
    """
    data = format_api_data("hmyv2_getCurrentTransactionErrorSink", None)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetCurrentTransactionErrorSinkResults(**results)

def getTransactionByBlockHashAndIndex(api_url : str, params : GetTransactionByBlockHashAndIndexParameters, session : Optional[requests.Session] = None) -> TransactionResult:
	"""
    params: GetTransactionByBlockHashAndIndexParameters
    result: TransactionResult
    method: hmyv2_getTransactionByBlockHashAndIndex
    """
    data = format_api_data("hmyv2_getTransactionByBlockHashAndIndex", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return TransactionResult(**results)

def getTransactionByBlockNumberAndIndex(api_url : str, params : GetTransactionByBlockNumberAndIndexParameters, session : Optional[requests.Session] = None) -> TransactionResult:
	"""
    params: GetTransactionByBlockNumberAndIndexParameters
    result: TransactionResult
    method: hmyv2_getTransactionByBlockNumberAndIndex
    """
    data = format_api_data("hmyv2_getTransactionByBlockNumberAndIndex", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return TransactionResult(**results)

def getTransactionByHash(api_url : str, params : GetTransactionByHashParameters, session : Optional[requests.Session] = None) -> TransactionResult:
	"""
    params: GetTransactionByHashParameters
    result: TransactionResult
    method: hmyv2_getTransactionByHash
    """
    data = format_api_data("hmyv2_getTransactionByHash", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return TransactionResult(**results)

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
    