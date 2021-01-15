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

def getDelegationsByValidator(api_url : str, params : GetDelegationsByValidatorParameters, session : Optional[requests.Session] = None) -> GetDelegationsByValidatorResults:
    """
    params: GetDelegationsByValidatorParameters
    result: GetDelegationsByValidatorResults
    method: hmyv2_getDelegationsByValidator
    """
    data = format_api_data("hmyv2_getDelegationsByValidator", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetDelegationsByValidatorResults(**results)

#Validator

def getAllValidatorAddresses(api_url : str, params : GetAllValidatorAddressesParameters, session : Optional[requests.Session] = None) -> GetAllValidatorAddressesResults:
    """
    params: GetAllValidatorAddressesParameters
    result: GetAllValidatorAddressesResults
    method: hmyv2_getAllValidatorAddresses
    """
    data = format_api_data("hmyv2_getAllValidatorAddresses", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetAllValidatorAddressesResults(**results)

def getAllValidatorInformation(api_url : str, params : GetAllValidatorInformationParameters, session : Optional[requests.Session] = None) -> GetAllValidatorInformationResults:
    """
    params: GetAllValidatorInformationParameters
    result: GetAllValidatorInformationResults
    method: hmyv2_getAllValidatorInformation
    """
    data = format_api_data("hmyv2_getAllValidatorInformation", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetAllValidatorInformationesults(**results)

def getAllValidatorInformationByBlockNumber(api_url : str, params : GetAllValidatorInformationByBlockNumberParameters, session : Optional[requests.Session] = None) -> GetAllValidatorInformationByBlockNumberResults:
    """
    params: GetAllValidatorInformationByBlockNumberParameters
    result: GetAllValidatorInformationByBlockNumberResults
    method: hmyv2_getAllValidatorInformationByBlockNumber
    """
    data = format_api_data("hmyv2_getAllValidatorInformationByBlockNumber", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetAllValidatorInformationByBlockNumberResults(**results)

def getElectedValidatorAddresses(api_url : str, params : G___Parameters, session : Optional[requests.Session] = None) -> GetElectedValidatorAddressesResults:
    """
    params: GetElectedValidatorAddressesParameters
    result: GetElectedValidatorAddressesResults
    method: hmyv2_getElectedValidatorAddresses
    """
    data = format_api_data("hmyv2_getElectedValidatorAddresses", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetElectedValidatorAddressesResults(**results)


def getValidatorInformation(api_url : str, params : GetValidatorInformationParameters, session : Optional[requests.Session] = None) -> GetValidatorInformationResults:
    """
    params: GetValidatorInformationParameters
    result: GetValidatorInformationResults
    method: hmyv2_getValidatorInformation
    """
    data = format_api_data("hmyv2_getValidatorInformation", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetValidatorInformationResults(**results)

#Network

def getCurrentUtilityMetrics(api_url : str, params : GetCurrentUtilityMetricsParameters, session : Optional[requests.Session] = None) -> GetCurrentUtilityMetricsResults:
	"""
    params: GetCurrentUtilityMetricsParameters
    result: GetCurrentUtilityMetricsResults
    method: hmyv2_getCurrentUtilityMetrics
    """
    data = format_api_data("hmyv2_getCurrentUtilityMetrics", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetCurrentUtilityMetricsResults(**results)

def getetMedianRawStakeSnapshot(api_url : str, params : GetMedianRawStakeSnapshotParameters, session : Optional[requests.Session] = None) -> GetMedianRawStakeSnapshotResults:
	"""
    params: GetMedianRawStakeSnapshotParameters
    result: GetMedianRawStakeSnapshotResults
    method: hmyv2_getMedianRawStakeSnapshot
    """
    data = format_api_data("hmyv2_getMedianRawStakeSnapshot", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetMedianRawStakeSnapshotResults(**results)

def getStakingNetworkInfo(api_url : str, params : GetStakingNetworkInfoParameters, session : Optional[requests.Session] = None) -> GetStakingNetworkInfoResults:
	"""
    params: GetStakingNetworkInfoParameters
    result: GetStakingNetworkInfoResults
    method: hmyv2_get___
    """
    data = format_api_data("hmyv2_getStakingNetworkInfo", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetStakingNetworkInfoResults(**results)

def getSuperCommittees(api_url : str, params : GetSuperCommitteesParameters, session : Optional[requests.Session] = None) -> GetSuperCommitteesResults:
	"""
    params: GetSuperCommitteesParameters
    result: GetSuperCommitteesResults
    method: hmyv2_getSuperCommittees
    """
    data = format_api_data("hmyv2_getSuperCommittees", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetSuperCommitteesResults(**results)
