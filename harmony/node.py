from typing import Optional

import requests

from .models import (
    GetCurrentBadBlocksResponse,
    GetNodeMetadataResponse,
    PeerCountResponse,
    ProtocolVersionResponse
)

from .endpoints.blockchain import (
    getCurrentBadBlocks,
    getNodeMetadata,
    peerCount,
    protocolVersion
)

def get_current_bad_blocks(api_url : str, session : Optional[requests.Session] = None) -> GetCurrentBadBlocksResponse:
    """
    Get the bad blocks currently in the node memory

    NOTE: Known issues with RPC not returning correctly

    Parameters
    ----------
    api_url : str
    session : requests.Session, optional

    Returns
    -------
    result : list[str]
        List of bad block hashes in memory
    """
    return getCurrentBadBlocks(api_url, session)

def get_node_metadata(api_url : str, session : Optional[requests.Session] = None) -> GetNodeMetadataResponse:
    """
    Get metadata about the node

    Parameters
    ----------
    api_url : str
    session : requests.Session, optional

    Returns
    -------
    result : NodeMetadata
    """
    return getNodeMetadata(api_url, session)

def get_peer_count(api_url : str, session : Optional[requests.Session] = None) -> PeerCountResponse:
    """
    Get the number of peers on the network.

    Parameters
    ----------
    api_url : str
    session : requests.Session, optional

    Returns
    -------
    result : str
        The number of peers represented as a hex string
    """
    return peerCount(api_url, session)

def get_protocol_version(api_url : str, session : Optional[requests.Session] = None) -> ProtocolVersionResponse:
    """
    Get the protocol version

    Parameters
    ----------
    api_url : str
    session : requests.Session, optional

    Returns
    -------
    result : int
        The protocol version
    """
    return protocolVersion(api_url, session)