from typing import Optional

import requests

from ..utils.communication import format_api_data, post_request

from ..models import (
    HashParameters,
    GetCXReceiptByHashResponse,
    GetPendingCXReceiptsResponse,
    ResendCXResponse,
    GetPoolStatsResponse,
    GetCurrentStakingErrorSinkResponse,
    BlockNumberAndIndexParameters,
    HashAndIndexParameters,
    RawTransactionParameters,
    SendRawStakingTransactionResponse,
    GetCurrentTransactionErrorSinkResponse,
    GetTransactionReceiptParameters,
    GetTransactionReceiptResponse,
    SendRawTransactionResponse,
    StakingTransactionResponse,
    StakingTransactionListResponse,
    TransactionResponse,
    TransactionListResponse
)

#Cross shard

def getCXReceiptByHash(api_url : str, params : HashParameters, session : Optional[requests.Session] = None) -> GetCXReceiptByHashResponse:
    """
    params: HashParameters
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


def resendCX(api_url : str, params : HashParameters, session : Optional[requests.Session] = None) -> ResendCXResponse:
    """
    params: HashParameters
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

def pendingTransactions(api_url : str, session : Optional[requests.Session] = None) -> TransactionListResponse:
    """
    params: None
    result: TransactionListResponse
    method: hmyv2_pendingTransactions
    """
    data = format_api_data("hmyv2_pendingTransactions", None)
    resp = post_request(api_url, data, session)
    return TransactionListResponse(**resp.json())

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

def getStakingTransactionByBlockNumberAndIndex(api_url : str, params : BlockNumberAndIndexParameters, session : Optional[requests.Session] = None) -> StakingTransactionResponse:
    """
    params: BlockNumberAndIndexParameters
    result: StakingTransactionResponse
    method: hmyv2_getStakingTransactionByBlockNumberAndIndex
    """
    data = format_api_data("hmyv2_getStakingTransactionByBlockNumberAndIndex", params)
    resp = post_request(api_url, data, session)
    return StakingTransactionResponse(**resp.json())

def getStakingTransactionByBlockHashAndIndex(api_url : str, params : HashAndIndexParameters, session : Optional[requests.Session] = None) -> StakingTransactionResponse:
    """
    params: HashAndIndexParameters
    result: StakingTransactionResponse
    method: hmyv2_getStakingTransactionByBlockHashAndIndex
    """
    data = format_api_data("hmyv2_getStakingTransactionByBlockHashAndIndex", params)
    resp = post_request(api_url, data, session)
    return StakingTransactionResponse(**resp.json())

def getStakingTransactionByHash(api_url : str, params : HashParameters, session : Optional[requests.Session] = None) -> StakingTransactionResponse:
    """
    params: HashParameters
    result: StakingTransactionResponse
    method: hmyv2_getStakingTransactionByHash
    """
    data = format_api_data("hmyv2_getStakingTransactionByHash", params)
    resp = post_request(api_url, data, session)
    return StakingTransactionResponse(**resp.json())

def sendRawStakingTransaction(api_url : str, params : RawTransactionParameters, session : Optional[requests.Session] = None) -> SendRawStakingTransactionResponse:
    """
    params: RawTransactionParameters
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

def getTransactionByBlockHashAndIndex(api_url : str, params : HashAndIndexParameters, session : Optional[requests.Session] = None) -> TransactionResponse:
    """
    params: HashAndIndexParameters
    result: TransactionResponse
    method: hmyv2_getTransactionByBlockHashAndIndex
    """
    data = format_api_data("hmyv2_getTransactionByBlockHashAndIndex", params)
    resp = post_request(api_url, data, session)
    return TransactionResponse(**resp.json())

def getTransactionByBlockNumberAndIndex(api_url : str, params : BlockNumberAndIndexParameters, session : Optional[requests.Session] = None) -> TransactionResponse:
    """
    params: BlockNumberAndIndexParameters
    result: TransactionResponse
    method: hmyv2_getTransactionByBlockNumberAndIndex
    """
    data = format_api_data("hmyv2_getTransactionByBlockNumberAndIndex", params)
    resp = post_request(api_url, data, session)
    return TransactionResponse(**resp.json())

def getTransactionByHash(api_url : str, params : HashParameters, session : Optional[requests.Session] = None) -> TransactionResponse:
    """
    params: HashParameters
    result: TransactionResponse
    method: hmyv2_getTransactionByHash
    """
    data = format_api_data("hmyv2_getTransactionByHash", params)
    resp = post_request(api_url, data, session)
    return TransactionResponse(**resp.json())

def getTransactionReceipt(api_url : str, params : GetTransactionReceiptParameters, session : Optional[requests.Session] = None) -> GetTransactionReceiptResponse:
    """
    params: GetTransactionReceiptParameters
    result: GetTransactionReceiptResponse
    method: hmyv2_getTransactionReceipt
    """
    data = format_api_data("hmyv2_getTransactionReceipt", params)
    resp = post_request(api_url, data, session)
    return GetTransactionReceiptResponse(**resp.json())

def sendRawTransaction(api_url : str, params : RawTransactionParameters, session : Optional[requests.Session] = None) -> SendRawTransactionResponse:
    """
    params: RawTransactionParameters
    result: SendRawTransactionResponse
    method: hmyv2_sendRawTransaction
    """
    data = format_api_data("hmyv2_sendRawTransaction", params)
    resp = post_request(api_url, data, session)
    return SendRawTransactionResponse(**resp.json())
    
