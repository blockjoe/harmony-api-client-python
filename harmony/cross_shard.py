from typing import Optional

import requests

from .models import (
    HashParameters,
    GetCXReceiptByHashResponse,
    GetPendingCXReceiptsResponse,
    ResendCXResponse
)

from .endpoints.transaction import (
    getCXReceiptByHash,
    getPendingCXReceipts,
    resendCX
)

def get_cx_receipt_by_hash(api_url : str, cross_shard_receipt_hash : str, session : Optional[requests.Session] = None) -> GetCXReceiptByHashResponse:
    """
    Get the cx receipt by hash.

    Note: Query the CX receipt hash on the receiving shard endpoint

    Parameters
    ----------
    api_url : str
    cross_shard_receipt_hash : str
        The hash of the cross shard receipt
    session : requests.Session, optional

    Returns
    -------
    result : CXReceipt
    """
    params = HashParameters(hash=cross_shard_receipt_hash)
    return getCXReceiptByHash(api_url, params, session)

def get_pending_cx_receipts(api_url : str, session : Optional[requests.Session] = None) -> GetPendingCXReceiptsResponse:
    """
    Get the currently pending cx receipts.

    Parameters
    ----------
    api_url : str
    session : requests.Session, optional

    Returns
    -------
    result : list[PendingCXReceipt]
    """
    return getPendingCXReceipts(api_url, session)

def resend_cx_receipt(api_url : str, cross_shard_receipt_hash : str, session : Optional[requests.Session] = None) -> ResendCXResponse:
    """
    Use this API call to resend the cross shard receipt to the receiving shard to re-process if the transaction did not pay out 

    Parameters
    ----------
    api_url : str
    cross_shard_receipt_hash : str
        The hash of the cross shard receipt
    session : requests.Session, optional

    Returns
    -------
    result : bool
        True if the resend was successful
    """
    params = HashParameters(hash=cross_shard_receipt_hash)
    return resendCX(api_url, params, session)