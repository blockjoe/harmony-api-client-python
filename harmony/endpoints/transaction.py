from typing import Optional

import requests

from ..utils.communication import format_api_data, post_request

from ..models import (
    GetCXReceiptByHashParameters,
    GetCXReceiptByHashResponse,
    GetPendingCXReceiptsResponse,
    ResendCXParameters,
    ResendCXResponse,
    GetPoolStatsResponse,
    GetCurrentStakingErrorSinkResponse,
    GetStakingTransactionByBlockNumberAndIndexParameters,
    GetStakingTransactionByBlockHashAndIndexParameters,
    GetStakingTransactionByHashParameters,
    SendRawStakingTransactionParameters,
    SendRawStakingTransactionResponse,
    GetCurrentTransactionErrorSinkResponse,
    GetTransactionByBlockHashAndIndexParameters,
    GetTransactionByBlockNumberAndIndexParameters,
    GetTransactionByHashParameters,
    GetTransactionReceiptParameters,
    GetTransactionReceiptResponse,
    SendRawTransactionParameters,
    SendRawTransactionResponse,
    StakingTransactionResult,
    StakingTransactionListResponse,
    TransactionResult
)

#Cross shard

def getCXReceiptByHash(api_url : str, params : GetCXReceiptByHashParameters, session : Optional[requests.Session] = None) -> GetCXReceiptByHashResponse:
    """
    params: GetCXReceiptByHashParameters
    result: GetCXReceiptByHashResponse
    method: hmyv2_getCXReceiptByHash
    """
    data = format_api_data("hmyv2_getCXReceiptByHash", params)
    resp = post_request(api_url, data, session)
    return GetCXReceiptByHashResponse(**resp.json())


def getPendingCXReceipts(api_url : str, session : Optional[requests.Session] = None) -> GetPendingCXReceiptsResponse:
    """
    params: None
    result: GetPendingCXReceiptsResponse
    method: hmyv2_getPendingCXReceipts
    """
    data = format_api_data("hmyv2_getPendingCXReceipts", None)
    resp = post_request(api_url, data, session)
    return GetPendingCXReceiptsResponse(**resp.json())


def resendCX(api_url : str, params : ResendCXParameters, session : Optional[requests.Session] = None) -> ResendCXResponse:
    """
    params: ResendCXParameters
    result: ResendCXResponse
    method: hmyv2_resendCX
    """
    data = format_api_data("hmyv2_resendCX", params)
    resp = post_request(api_url, data, session)
    return ResendCXResponse(**resp.json())

#Transaction Pool

def getPoolStats(api_url : str, session : Optional[requests.Session] = None) -> GetPoolStatsResponse:
    """
    params: None
    result: GetPoolStatsResponse
    method: hmyv2_getPoolStats
    """
    data = format_api_data("hmyv2_getPoolStats", None)
    resp = post_request(api_url, data, session)
    
    return GetPoolStatsResponse(**resp.json())

def pendingStakingTransactions(api_url : str, session : Optional[requests.Session] = None) -> StakingTransactionListResponse:
    """
    params: None
    result: StakingTransactionListResponse
    method: hmyv2_pendingStakingTransactions
    """
    data = format_api_data("hmyv2_pendingStakingTransactions", None)
    resp = post_request(api_url, data, session)
    return StakingTransactionListResponse(**resp.json())

def pendingTransactions(api_url : str, session : Optional[requests.Session] = None) -> StakingTransactionListResponse:
    """
    params: None
    result: StakingTransactionListResponse
    method: hmyv2_pendingTransactions
    """
    data = format_api_data("hmyv2_pendingTransactions", None)
    resp = post_request(api_url, data, session)
    return StakingTransactionListResponse(**resp.json())

#Staking

def getCurrentStakingErrorSink(api_url : str, session : Optional[requests.Session] = None) -> GetCurrentStakingErrorSinkResponse:
    """
    params: None
    result: GetCurrentStakingErrorSinkResponse
    method: hmyv2_getCurrentStakingErrorSink
    """
    data = format_api_data("hmyv2_getCurrentStakingErrorSink", None)
    resp = post_request(api_url, data, session)
    return GetCurrentStakingErrorSinkResponse(**resp.json())

def getStakingTransactionByBlockNumberAndIndex(api_url : str, params : GetStakingTransactionByBlockNumberAndIndexParameters, session : Optional[requests.Session] = None) -> StakingTransactionResult:
    """
    params: GetStakingTransactionByBlockNumberAndIndexParameters
    result: StakingTransactionResult
    method: hmyv2_getStakingTransactionByBlockNumberAndIndex
    """
    data = format_api_data("hmyv2_getStakingTransactionByBlockNumberAndIndex", params)
    resp = post_request(api_url, data, session)
    return StakingTransactionResult(**resp.json())

def getStakingTransactionByBlockHashAndIndex(api_url : str, params : GetStakingTransactionByBlockHashAndIndexParameters, session : Optional[requests.Session] = None) -> StakingTransactionResult:
    """
    params: GetStakingTransactionByBlockHashAndIndexParameters
    result: StakingTransactionResult
    method: hmyv2_getStakingTransactionByBlockHashAndIndex
    """
    data = format_api_data("hmyv2_getStakingTransactionByBlockHashAndIndex", params)
    resp = post_request(api_url, data, session)
    return StakingTransactionResult(**resp.json())

def getStakingTransactionByHash(api_url : str, params : GetStakingTransactionByHashParameters, session : Optional[requests.Session] = None) -> StakingTransactionResult:
    """
    params: GetStakingTransactionByHashParameters
    result: StakingTransactionResult
    method: hmyv2_getStakingTransactionByHash
    """
    data = format_api_data("hmyv2_getStakingTransactionByHash", params)
    resp = post_request(api_url, data, session)
    return StakingTransactionResult(**resp.json())

def sendRawStakingTransaction(api_url : str, params : SendRawStakingTransactionParameters, session : Optional[requests.Session] = None) -> SendRawStakingTransactionResponse:
    """
    params: SendRawStakingTransactionParameters
    result: SendRawStakingTransactionResponse
    method: hmyv2_sendRawStakingTransaction
    """
    data = format_api_data("hmyv2_sendRawStakingTransaction", params)
    resp = post_request(api_url, data, session)
    return SendRawStakingTransactionResponse(**resp.json())

#Transfer

def getCurrentTransactionErrorSink(api_url : str, session : Optional[requests.Session] = None) -> GetCurrentTransactionErrorSinkResponse:
    """
    params: None
    result: GetCurrentTransactionErrorSinkResponse
    method: hmyv2_getCurrentTransactionErrorSink
    """
    data = format_api_data("hmyv2_getCurrentTransactionErrorSink", None)
    resp = post_request(api_url, data, session)
    return GetCurrentTransactionErrorSinkResponse(**resp.json())

def getTransactionByBlockHashAndIndex(api_url : str, params : GetTransactionByBlockHashAndIndexParameters, session : Optional[requests.Session] = None) -> TransactionResult:
    """
    params: GetTransactionByBlockHashAndIndexParameters
    result: TransactionResult
    method: hmyv2_getTransactionByBlockHashAndIndex
    """
    data = format_api_data("hmyv2_getTransactionByBlockHashAndIndex", params)
    resp = post_request(api_url, data, session)
    return TransactionResult(**resp.json())

def getTransactionByBlockNumberAndIndex(api_url : str, params : GetTransactionByBlockNumberAndIndexParameters, session : Optional[requests.Session] = None) -> TransactionResult:
    """
    params: GetTransactionByBlockNumberAndIndexParameters
    result: TransactionResult
    method: hmyv2_getTransactionByBlockNumberAndIndex
    """
    data = format_api_data("hmyv2_getTransactionByBlockNumberAndIndex", params)
    resp = post_request(api_url, data, session)
    return TransactionResult(**resp.json())

def getTransactionByHash(api_url : str, params : GetTransactionByHashParameters, session : Optional[requests.Session] = None) -> TransactionResult:
    """
    params: GetTransactionByHashParameters
    result: TransactionResult
    method: hmyv2_getTransactionByHash
    """
    data = format_api_data("hmyv2_getTransactionByHash", params)
    resp = post_request(api_url, data, session)
    return TransactionResult(**resp.json())

def getTransactionReceipt(api_url : str, params : GetTransactionReceiptParameters, session : Optional[requests.Session] = None) -> GetTransactionReceiptResponse:
    """
    params: GetTransactionReceiptParameters
    result: G_Response
    method: hmyv2_getTransactionReceipt
    """
    data = format_api_data("hmyv2_getTransactionReceipt", params)
    resp = post_request(api_url, data, session)
    return GetTransactionReceiptResponse(**resp.json())

def sendRawTransaction(api_url : str, params : SendRawTransactionParameters, session : Optional[requests.Session] = None) -> SendRawTransactionResponse:
    """
    params: SendRawTransactionParameters
    result: SendRawTransactionResponse
    method: hmyv2_sendRawTransaction
    """
    data = format_api_data("hmyv2_sendRawTransaction", params)
    resp = post_request(api_url, data, session)
    return SendRawTransactionResponse(**resp.json())
    
