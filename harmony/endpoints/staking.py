from typing import Optional

import requests

from ..utils.communication import format_api_data, post_request

from ..models import (
    GetDelegationsByDelegatorParameters,
    DelegationListResults,
    GetDelegationsByDelegatorByBlockNumberParameters,
    GetDelegationsByValidatorParameters,
    GetAllValidatorAddressesResults,
    GetAllValidatorInformationParameters,
    GetAllValidatorInformationByBlockNumberParameters,
    GetElectedValidatorAddressesResults,
    GetValidatorInformationParameters,
    GetCurrentUtilityMetricsResults,
    GetMedianRawStakeSnapshotResults,
    GetStakingNetworkInfoResults,
    GetSuperCommitteesResults,
    ValidatorListResults
)

#Delegation

def getDelegationsByDelegator(api_url : str, params : GetDelegationsByDelegatorParameters, session : Optional[requests.Session] = None) -> DelegationListResults:
    """
    params: GetDelegationsByDelegatorParameters
    result: DelegationListResults
    method: hmyv2_getDelegationsByDelegator
    """
    data = format_api_data("hmyv2_getDelegationsByDelegator", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return DelegationListResults(**results)

def getDelegationsByDelegatorByBlockNumber(api_url : str, params : GetDelegationsByDelegatorByBlockNumberParameters, session : Optional[requests.Session] = None) -> DelegationListResults:
    """
    params: GetDelegationsByDelegatorByBlockNumberParameters
    result: DelegationListResults
    method: hmyv2_getDelegationsByDelegatorByBlockNumber
    """
    data = format_api_data("hmyv2_getDelegationsByDelegatorByBlockNumber", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return DelegationListResults(**results)

def getDelegationsByValidator(api_url : str, params : GetDelegationsByValidatorParameters, session : Optional[requests.Session] = None) -> DelegationListResults:
    """
    params: GetDelegationsByValidatorParameters
    result: DelegationListResults
    method: hmyv2_getDelegationsByValidator
    """
    data = format_api_data("hmyv2_getDelegationsByValidator", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return DelegationListResults(**results)

#Validator

def getAllValidatorAddresses(api_url : str, session : Optional[requests.Session] = None) -> GetAllValidatorAddressesResults:
    """
    params: None
    result: GetAllValidatorAddressesResults
    method: hmyv2_getAllValidatorAddresses
    """
    data = format_api_data("hmyv2_getAllValidatorAddresses", None)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetAllValidatorAddressesResults(**results)

def getAllValidatorInformation(api_url : str, params : GetAllValidatorInformationParameters, session : Optional[requests.Session] = None) -> ValidatorListResults:
    """
    params: GetAllValidatorInformationParameters
    result: ValidatorListResults
    method: hmyv2_getAllValidatorInformation
    """
    data = format_api_data("hmyv2_getAllValidatorInformation", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return ValidatorListResults(**results)

def getAllValidatorInformationByBlockNumber(api_url : str, params : GetAllValidatorInformationByBlockNumberParameters, session : Optional[requests.Session] = None) -> ValidatorListResults:
    """
    params: GetAllValidatorInformationByBlockNumberParameters
    result: ValidatorListResults
    method: hmyv2_getAllValidatorInformationByBlockNumber
    """
    data = format_api_data("hmyv2_getAllValidatorInformationByBlockNumber", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return ValidatorListResults(**results)

def getElectedValidatorAddresses(api_url : str, session : Optional[requests.Session] = None) -> GetElectedValidatorAddressesResults:
    """
    params: None
    result: GetElectedValidatorAddressesResults
    method: hmyv2_getElectedValidatorAddresses
    """
    data = format_api_data("hmyv2_getElectedValidatorAddresses", None)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetElectedValidatorAddressesResults(**results)


def getValidatorInformation(api_url : str, params : GetValidatorInformationParameters, session : Optional[requests.Session] = None) -> ValidatorListResults:
    """
    params: GetValidatorInformationParameters
    result: ValidatorListResults
    method: hmyv2_getValidatorInformation
    """
    data = format_api_data("hmyv2_getValidatorInformation", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return ValidatorListResults(**results)

#Network

def getCurrentUtilityMetrics(api_url : str, session : Optional[requests.Session] = None) -> GetCurrentUtilityMetricsResults:
    """
    params: None
    result: GetCurrentUtilityMetricsResults
    method: hmyv2_getCurrentUtilityMetrics
    """
    data = format_api_data("hmyv2_getCurrentUtilityMetrics", None)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetCurrentUtilityMetricsResults(**results)

def getetMedianRawStakeSnapshot(api_url : str, session : Optional[requests.Session] = None) -> GetMedianRawStakeSnapshotResults:
    """
    params: None
    result: GetMedianRawStakeSnapshotResults
    method: hmyv2_getMedianRawStakeSnapshot
    """
    data = format_api_data("hmyv2_getMedianRawStakeSnapshot", None)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetMedianRawStakeSnapshotResults(**results)

def getStakingNetworkInfo(api_url : str, session : Optional[requests.Session] = None) -> GetStakingNetworkInfoResults:
    """
    params: None
    result: GetStakingNetworkInfoResults
    method: hmyv2_getStakingNetworkInfo
    """
    data = format_api_data("hmyv2_getStakingNetworkInfo", None)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetStakingNetworkInfoResults(**results)

def getSuperCommittees(api_url : str, session : Optional[requests.Session] = None) -> GetSuperCommitteesResults:
    """
    params: None
    result: GetSuperCommitteesResults
    method: hmyv2_getSuperCommittees
    """
    data = format_api_data("hmyv2_getSuperCommittees", None)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetSuperCommitteesResults(**results)
