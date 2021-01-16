from typing import Optional

import requests

from ..utils.communication import format_api_data, post_request

from ..models import (
    CallParameters,
    CallResponse,
    EstimateGasResponse,
    GetCodeParameters,
    GetCodeResponse,
    GetStorageAtParameters,
    GetStorageAtResponse
)

def call(api_url : str, params : CallParameters, session : Optional[requests.Session] = None) -> CallResponse:
    """
    params: CallParameters
    result: CallResponse
    method: hmyv2_call
    """
    data = format_api_data("hmyv2_call", params)
    resp = post_request(api_url, data, session)
    
    return CallResponse(**resp.json())

def estimateGas(api_url : str, params : CallParameters, session : Optional[requests.Session] = None) -> EstimateGasResponse:
    """
    params: CallParameters
    result: EstimateGasResponse
    method: hmyv2_estimateGas
    """
    data = format_api_data("hmyv2_estimateGas", params)
    resp = post_request(api_url, data, session)
    
    return EstimateGasResponse(**resp.json())

def getCode(api_url : str, params : GetCodeParameters, session : Optional[requests.Session] = None) -> GetCodeResponse:
    """
    params: GetCodeParameters
    result: GetCodeResponse
    method: hmyv2_getCode
    """
    data = format_api_data("hmyv2_getCode", params)
    resp = post_request(api_url, data, session)
    
    return CallResponse(**resp.json())


def getStorageAt(api_url : str, params : GetStorageAtParameters, session : Optional[requests.Session] = None) -> GetStorageAtResponse:
    """
    params: GetStorageAtParameters
    result: GetStorageAtResponse
    method: hmyv2_getStorageAt
    """
    data = format_api_data("hmyv2_getStorageAt", params)
    resp = post_request(api_url, data, session)
    
    return GetStorageAtResponse(**resp.json())
