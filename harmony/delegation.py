from typing import Optional

import requests

from .models import (
    AddressParameters,
    AddressBlockNumberParameters,
    DelegationListResponse
)

from .endpoints.staking import (
    getDelegationsByDelegator,
    getDelegationsByDelegatorByBlockNumber,
    getDelegationsByValidator
)

def get_delegations_by_delegator(api_url : str, address : str, session : Optional[requests.Session] = None) -> DelegationListResponse:
    """
    Get delegations by delegator address

    Parameters
    -----------
    api_url : str
    address : str
        The delegator address
    session : requests.Session, optional

    Returns
    -------
    result : List[Delegation]
    """
    params = AddressParameters(address=address)
    return getDelegationsByDelegator(api_url, params, session)

def get_delegations_by_delegator_by_block_number(api_url : str, address : str, block_number : int, session : Optional[requests.Session] = None) -> DelegationListResponse:
    """
    Get delegations by delegator address and block number

    Parameters
    -----------
    api_url : str
    address : str
        The delegator address
    session : requests.Session, optional

    Returns
    -------
    result : List[Delegation]
    """
    params = AddressBlockNumberParameters(address=address, block_number=block_number)
    return getDelegationsByDelegatorByBlockNumber(api_url, params, session)

def get_delegations_by_validator(api_url : str, address : str, session : Optional[requests.Session] = None) -> DelegationListResponse:
    """
    Get delegations by validator address

    Parameters
    -----------
    api_url : str
    address : str
        The validator address
    session : requests.Session, optional

    Returns
    -------
    result : List[Delegation]
    """
    params = AddressParameters(address=address)
    return getDelegationsByValidator(api_url, params, session)