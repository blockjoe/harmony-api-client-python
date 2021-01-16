from typing import Optional

import requests

from ..utils.communication import post_request
from ..utils.call_format import format_api_data

from ..models import (
    CallParameters,
    CallResults,
    EstimateGasResults,
    GetCodeParameters,
    GetCodeResults,
    GetStorageAtParameters,
    GetStorageAtResults
)

def call(api_url : str, params : CallParameters, session : Optional[requests.Session] = None) -> CallResults:
    """
    params: CallParameters
    result: CallResults
    method: hmyv2_call
    """
    data = format_api_data("hmyv2_call", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return CallResults(**results)

def estimateGas(api_url : str, params : CallParameters, session : Optional[requests.Session] = None) -> EstimateGasResults:
    """
    params: CallParameters
    result: EstimateGasResults
    method: hmyv2_estimateGas
    """
    data = format_api_data("hmyv2_estimateGas", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return EstimateGasResults(**results)

def getCode(api_url : str, params : GetCodeParameters, session : Optional[requests.Session] = None) -> GetCodeResults:
    """
    params: GetCodeParameters
    result: GetCodeResults
    method: hmyv2_getCode
    """
    data = format_api_data("hmyv2_getCode", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return CallResults(**results)


def getStorageAt(api_url : str, params : GetStorageAtParameters, session : Optional[requests.Session] = None) -> GetStorageAtResults:
    """
    params: GetStorageAtParameters
    result: GetStorageAtResults
    method: hmyv2_getStorageAt
    """
    data = format_api_data("hmyv2_getStorageAt", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetStorageAtResults(**results)
