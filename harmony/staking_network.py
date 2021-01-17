from typing import Optional

import requests

from .models import (
    GetCurrentUtilityMetricsResponse,
    GetMedianRawStakeSnapshotResponse,
    GetStakingNetworkInfoResponse,
    GetSuperCommitteesResponse
)

from .endpoints.staking import (
    getCurrentUtilityMetrics,
    getMedianRawStakeSnapshot,
    getStakingNetworkInfo,
    getSuperCommittees
)

def get_current_utility_metrics(api_url : str, session : Optional[requests.Session] = None) -> GetCurrentUtilityMetricsResponse:
    """
    Get the current utility metrics

    Parameters
    ----------
    api_url: str
    session: requests.Session, optional

    Returns
    -------
    result : UtilityMetrics
    """
    return getCurrentUtilityMetrics(api_url, session)

def get_median_raw_stake_snapshot(api_url : str, session : Optional[requests.Session] = None) -> GetMedianRawStakeSnapshotResponse:
    """
    Get the median raw stake snapshot

    Parameters
    ----------
    api_url: str
    session: requests.Session, optional

    Returns
    -------
    result : MedianRawStakeSnapshot
    """
    return getMedianRawStakeSnapshot(api_url, session)

def get_staking_network_info(api_url : str, session : Optional[requests.Session] = None) -> GetStakingNetworkInfoResponse:
    """
    Get information about the staking network.

    Parameters
    ----------
    api_url: str
    session: requests.Session, optional

    Returns
    -------
    result : StakingNetworkInfo
    """
    return getStakingNetworkInfo(api_url, session)

def get_super_committees(api_url : str, session : Optional[requests.Session] = None) -> GetSuperCommitteesResponse:
    """
    Get information about the current and previously elected super committees.

    Parameters
    ----------
    api_url: str
    session: requests.Session, optional

    Returns
    -------
    result : SuperCommittees
    """
    return getSuperCommittees(api_url, session)