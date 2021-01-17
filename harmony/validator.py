from typing import Optional

import requests

from .models import (
    AddressListResponse,
    AddressParameters,
    GetAllValidatorInformationParameters,
    GetAllValidatorInformationByBlockNumberParameters,
    ValidatorInformationListResponse,
    ValidatorInformationResponse
)

from .endpoints.staking import (
    getAllValidatorAddresses,
    getAllValidatorInformation,
    getAllValidatorInformationByBlockNumber,
    getElectedValidatorAddresses,
    getValidatorInformation
)

def get_all_validator_addresses(api_url : str, session : Optional[requests.Session] = None) -> AddressListResponse:
    """
    Get all the wallet address of all the validators

    Parameters
    ----------
    api_url : str
    session : requests.Session, optional

    Returns
    -------
    result : list[str]
        List of validator wallet addresses
    """
    return getAllValidatorAddresses(api_url, session)

def get_all_validator_information(api_url : str, page_number : Optional[int] = -1, session : Optional[requests.Session] = None) -> ValidatorInformationListResponse:
    """
    Get the information about all the validators.

    Parameters
    ----------
    api_url : str
    page_number : int, optional
        The page to request (100 results per page), -1 gives all validators, defautls to -1
    session : requests.Session, optional

    Returns
    --------
    result : list[ValidatorInformation]
        List of ValidatorInformatoin objects
    """
    params = GetAllValidatorInformationParameters(page_number=page_number)
    return getAllValidatorInformation(api_url, params, session)

def get_all_validator_information(api_url : str, block_number : int, page_number : Optional[int] = -1, session : Optional[requests.Session] = None) -> ValidatorInformationListResponse:
    """
    Get the information about all the validators by block number.

    Parameters
    ----------
    api_url : str
    block_number : int
        The block number
    page_number : int, optional
        The page to request (100 results per page), -1 gives all validators, defautls to -1
    session : requests.Session, optional

    Returns
    --------
    result : list[ValidatorInformation]
        List of ValidatorInformatoin objects
    """
    params = GetAllValidatorInformationByBlockNumberParameters(page_number=page_number, block_number=block_number)
    return getAllValidatorInformation(api_url, params, session)

def get_all_elected_validator_addresses(api_url : str, session : Optional[requests.Session] = None) -> AddressListResponse:
    """
    Get all the wallet address of all the elected validators

    Parameters
    ----------
    api_url : str
    session : requests.Session, optional

    Returns
    -------
    result : list[str]
        List of validator wallet addresses
    """
    return getElectedValidatorAddresses(api_url, session)

def get_validator_information(api_url : str, address : str, session : Optional[requests.Session] = None) -> ValidatorInformationResponse:
    """
    Get the information about a given validator wallet address

    Parameters
    ----------
    api_url : str
    address : str
        The wallet address of the validator to get information about
    session : requests.Session, optional

    Returns
    -------
    result : ValidatorInfomration
    """
    parmas = AddressParameters(address=address)
    return getValidatorInformation(api_url, params, session)