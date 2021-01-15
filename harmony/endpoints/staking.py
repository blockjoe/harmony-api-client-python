from typing import Optional

import requests

from ..utils.communication import post_request
from ..utils.call_format import format_api_data

from ..models import (
    CallParameters,
    CallResult,
    EstimateGasResult,
    GetCodeParameters,
    GetCodeResult,
    GetStorageAtParameters,
    GetStorageAtResult
)

#Delegation

def getDelegationsByDelegator(api_url : str, params : GetDelegationsByDelegatorParameters, session : Optional[requests.Session] = None) -> GetDelegationsByDelegatorResults:

"""
    params: GetDelegationsByDelegatorParameters
    result: GetDelegationsByDelegatorResults
    method: hmyv2_getDelegationsByDelegator
    """
    data = format_api_data("hmyv2_getDelegationsByDelegator", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetDelegationsByDelegatorResults(**results)

def getDelegationsByDelegatorByBlockNumber(api_url : str, params : GetDelegationsByDelegatorByBlockNumberParameters, session : Optional[requests.Session] = None) -> GetDelegationsByDelegatorByBlockNumberResults:

"""
    params: GetDelegationsByDelegatorByBlockNumberParameters
    result: GetDelegationsByDelegatorByBlockNumberResults
    method: hmyv2_getDelegationsByDelegatorByBlockNumber
    """
    data = format_api_data("hmyv2_getDelegationsByDelegatorByBlockNumber", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetDelegationsByDelegatorByBlockNumberResults(**results)

def getDelegationsByValidator(api_url : str, params : GetCodeParameters, session : Optional[requests.Session] = None) -> GetDelegationsByValidatorResults:

"""
    params: GetDelegationsByValidatorParameters
    result: GetDelegationsByValidatorResults
    method: hmyv2_getDelegationsByValidator
    """
    data = format_api_data("hmyv2_getDelegationsByValidator", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetDelegationsByValidatorResults(**results)

