from typing import Optional

import requests

from ..utils.communication import format_api_data, post_request

from ..models import (
    AddressBlockNumberParameters,
    AddressListResponse,
    AddressParameters,
    DelegationListResponse,
    GetAllValidatorInformationParameters,
    GetAllValidatorInformationByBlockNumberParameters,
    GetCurrentUtilityMetricsResponse,
    GetMedianRawStakeSnapshotResponse,
    GetStakingNetworkInfoResponse,
    GetSuperCommitteesResponse,
    ValidatorInformationResponse,
    ValidatorInformationListResponse
)

#Delegation

def getDelegationsByDelegator(api_url : str, params : AddressParameters, session : Optional[requests.Session] = None) -> DelegationListResponse:
    """
    params: AddressParameters
    result: DelegationListResponse
    method: hmyv2_getDelegationsByDelegator
    """
    data = format_api_data("hmyv2_getDelegationsByDelegator", params)
    resp = post_request(api_url, data, session)
    return DelegationListResponse(**resp.json())

def getDelegationsByDelegatorByBlockNumber(api_url : str, params : AddressBlockNumberParameters, session : Optional[requests.Session] = None) -> DelegationListResponse:
    """
    params: AddressBlockNumberParameters
    result: DelegationListResponse
    method: hmyv2_getDelegationsByDelegatorByBlockNumber
    """
    data = format_api_data("hmyv2_getDelegationsByDelegatorByBlockNumber", params)
    resp = post_request(api_url, data, session)
    return DelegationListResponse(**resp.json())

def getDelegationsByValidator(api_url : str, params : AddressParameters, session : Optional[requests.Session] = None) -> DelegationListResponse:
    """
    params: AddressParameters
    result: DelegationListResponse
    method: hmyv2_getDelegationsByValidator
    """
    data = format_api_data("hmyv2_getDelegationsByValidator", params)
    resp = post_request(api_url, data, session)
    return DelegationListResponse(**resp.json())

#Validator

def getAllValidatorAddresses(api_url : str, session : Optional[requests.Session] = None) -> AddressListResponse:
    """
    params: None
    result: AddressListResponse
    method: hmyv2_getAllValidatorAddresses
    """
    data = format_api_data("hmyv2_getAllValidatorAddresses", None)
    resp = post_request(api_url, data, session)
    return AddressListResponse(**resp.json())

def getAllValidatorInformation(api_url : str, params : GetAllValidatorInformationParameters, session : Optional[requests.Session] = None) -> ValidatorInformationListResponse:
    """
    params: GetAllValidatorInformationParameters
    result: ValidatorInformationListResponse
    method: hmyv2_getAllValidatorInformation
    """
    data = format_api_data("hmyv2_getAllValidatorInformation", params)
    resp = post_request(api_url, data, session)
    return ValidatorInformationListResponse(**resp.json())

def getAllValidatorInformationByBlockNumber(api_url : str, params : GetAllValidatorInformationByBlockNumberParameters, session : Optional[requests.Session] = None) -> ValidatorInformationListResponse:
    """
    params: GetAllValidatorInformationByBlockNumberParameters
    result: ValidatorInformationListResponse
    method: hmyv2_getAllValidatorInformationByBlockNumber
    """
    data = format_api_data("hmyv2_getAllValidatorInformationByBlockNumber", params)
    resp = post_request(api_url, data, session)
    return ValidatorInformationListResponse(**resp.json())

def getElectedValidatorAddresses(api_url : str, session : Optional[requests.Session] = None) -> AddressListResponse:
    """
    params: None
    result: AddressListResponse
    method: hmyv2_getElectedValidatorAddresses
    """
    data = format_api_data("hmyv2_getElectedValidatorAddresses", None)
    resp = post_request(api_url, data, session)
    return AddressListResponse(**resp.json())


def getValidatorInformation(api_url : str, params : AddressParameters, session : Optional[requests.Session] = None) -> ValidatorInformationResponse:
    """
    params: AddressParameters
    result: ValidatorInformationResponse
    method: hmyv2_getValidatorInformation
    """
    data = format_api_data("hmyv2_getValidatorInformation", params)
    resp = post_request(api_url, data, session)
    return ValidatorInformationResponse(**resp.json())

#Network

def getCurrentUtilityMetrics(api_url : str, session : Optional[requests.Session] = None) -> GetCurrentUtilityMetricsResponse:
    """
    params: None
    result: GetCurrentUtilityMetricsResponse
    method: hmyv2_getCurrentUtilityMetrics
    """
    data = format_api_data("hmyv2_getCurrentUtilityMetrics", None)
    resp = post_request(api_url, data, session)
    return GetCurrentUtilityMetricsResponse(**resp.json())

def getMedianRawStakeSnapshot(api_url : str, session : Optional[requests.Session] = None) -> GetMedianRawStakeSnapshotResponse:
    """
    params: None
    result: GetMedianRawStakeSnapshotResponse
    method: hmyv2_getMedianRawStakeSnapshot
    """
    data = format_api_data("hmyv2_getMedianRawStakeSnapshot", None)
    resp = post_request(api_url, data, session)
    return GetMedianRawStakeSnapshotResponse(**resp.json())

def getStakingNetworkInfo(api_url : str, session : Optional[requests.Session] = None) -> GetStakingNetworkInfoResponse:
    """
    params: None
    result: GetStakingNetworkInfoResponse
    method: hmyv2_getStakingNetworkInfo
    """
    data = format_api_data("hmyv2_getStakingNetworkInfo", None)
    resp = post_request(api_url, data, session)
    return GetStakingNetworkInfoResponse(**resp.json())

def getSuperCommittees(api_url : str, session : Optional[requests.Session] = None) -> GetSuperCommitteesResponse:
    """
    params: None
    result: GetSuperCommitteesResponse
    method: hmyv2_getSuperCommittees
    """
    data = format_api_data("hmyv2_getSuperCommittees", None)
    resp = post_request(api_url, data, session)
    return GetSuperCommitteesResponse(**resp.json())
