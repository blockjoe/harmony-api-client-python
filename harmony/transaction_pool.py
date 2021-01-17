from typing import Optional

import requests

from .models import (
    GetPoolStatsResponse,
    StakingTransactionListResponse,
    TransactionListResponse
)

from .endpoints.transaction import (
    getPoolStats,
    pendingStakingTransactions,
    pendingTransactions
)

def get_pool_stats(api_url : str, session : Optional[requests.Session] = None) -> GetPoolStatsResponse:
    """
    Get stats on the transaction pool.

    Parameters
    ----------
    api_url : str
    session : requests.Session, optional

    Returns
    -------
    result : PoolStats
    """
    return getPoolStats(api_url, session)

def get_pending_staking_transactions(api_url : str, session : Optional[requests.Session] = None) -> StakingTransactionListResponse:
    """
    Get the staking transactions pending in the pool.

    Parameters
    ----------
    api_url : str
    session : requests.Session, optional

    Returns
    -------
    result : list[StakingTransaction]
    """
    return pendingStakingTransactions(api_url, session)

def get_pending_transactions(api_url : str, session : Optional[requests.Session] = None) -> TransactionListResponse:
    """
    Get the transactions pending in the pool.

    Parameters
    ----------
    api_url : str
    session : requests.Session, optional

    Returns
    -------
    result : list[Transaction]
    """
    return pendingTransactions(api_url, session)