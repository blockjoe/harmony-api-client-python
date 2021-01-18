from typing import Optional

import requests

from ..utils.communication import format_api_data, post_request

from ..models import (
    BlockResponse,
    BlockListResponse,
    BlockNumberResponse,
    GetCirculatingSupplyResponse,
    GetEpochResponse,
    GetLastCrossLinksResponse,
    GetLeaderResponse,
    GasPriceResponse,
    GetShardingStructureResponse,
    GetTotalSupplyResponse,
    EphochNumberParameters,
    GetValidatorsResponse,
    BLSKeyListResponse,
    GetCurrentBadBlocksResponse,
    GetNodeMetadataResponse,
    ProtocolVersionResponse,
    PeerCountResponse,
    BlockListParams,
    GetBlockByNumberParameters,
    GetBlockByHashParameters,
    AddressListResponse,
    BlockNumberParameters,
    BLSKeyListResponse,
    BlockNumberParameters,
    TransactionCountResponse,
    BlockNumberParameters,
    HeaderResponse,
    GetLatestChainHeadersResponse,
    HashParameters
)

#Network

def blockNumber(api_url : str, session : Optional[requests.Session] = None) -> BlockNumberResponse:
    """
    params: None
    result: BlockNumberResponse
    method: hmyv2_blockNumber
    """
    data = format_api_data("hmyv2_blockNumber", None)
    resp = post_request(api_url, data, session)
    
    return BlockNumberResponse(**resp.json())

def getCirculatingSupply(api_url : str, session : Optional[requests.Session] = None) -> GetCirculatingSupplyResponse:
    """
    params: None
    result: GetCirculatingSupplyResponse
    method: hmyv2_getCirculatingSupply
    """
    data = format_api_data("hmyv2_getCirculatingSupply", None)
    resp = post_request(api_url, data, session)
    
    return GetCirculatingSupplyResponse(**resp.json())

def getEpoch(api_url : str, session : Optional[requests.Session] = None) -> GetEpochResponse:
    """
    params: None
    result: GetEpochResponse
    method: hmyv2_getEpoch
    """
    data = format_api_data("hmyv2_getEpoch", None)
    resp = post_request(api_url, data, session)
    
    return GetEpochResponse(**resp.json())

def getLastCrossLinks(api_url : str, session : Optional[requests.Session] = None) -> GetLastCrossLinksResponse:
    """
    params: None
    result: GetLastCrossLinksResponse
    method: hmyv2_getLastCrossLinks
    """
    data = format_api_data("hmyv2_getLastCrossLinks", None)
    resp = post_request(api_url, data, session)
    
    return GetLastCrossLinksResponse(**resp.json())

def getLeader(api_url : str, session : Optional[requests.Session] = None) -> GetLeaderResponse:
    """
    params: None
    result: GetLeaderResponse
    method: hmyv2_getLeader
    """
    data = format_api_data("hmyv2_getLeader", None)
    resp = post_request(api_url, data, session)
    
    return GetLeaderResponse(**resp.json())

def gasPrice(api_url : str, session : Optional[requests.Session] = None) -> GasPriceResponse:
    """
    params: None
    result: GasPriceResponse
    method: hmyv2_gasPrice
    """
    data = format_api_data("hmyv2_gasPrice", None)
    resp = post_request(api_url, data, session)
    
    return GasPriceResponse(**resp.json())

def getShardingStructure(api_url : str, session : Optional[requests.Session] = None) -> GetShardingStructureResponse:
    """
    params: GetShardingStructureParameters
    result: GetShardingStructureResponse
    method: hmyv2_getShardingStructure
    """
    data = format_api_data("hmyv2_getShardingStructure", None)
    resp = post_request(api_url, data, session)
    
    return GetShardingStructureResponse(**resp.json())

def getTotalSupply(api_url : str, session : Optional[requests.Session] = None) -> GetTotalSupplyResponse:
    """
    params: None
    result: GetTotalSupplyResponse
    method: hmyv2_getTotalSupply
    """
    data = format_api_data("hmyv2_getTotalSupply", None)
    resp = post_request(api_url, data, session)
    
    return GetTotalSupplyResponse(**resp.json())

def getValidators(api_url : str, params : EphochNumberParameters, session : Optional[requests.Session] = None) -> GetValidatorsResponse:
    """
    params: EphochNumberParameters
    result: GetValidatorsResponse
    method: hmyv2_getValidators
    """
    data = format_api_data("hmyv2_getValidators", params)
    resp = post_request(api_url, data, session)
    
    return GetValidatorsResponse(**resp.json())

def getValidatorKeys(api_url : str, params : EphochNumberParameters, session : Optional[requests.Session] = None) -> BLSKeyListResponse:
    """
    params: EphochNumberParameters
    result: BLSKeyListResponse
    method: hmyv2_getValidatorKeys
    """
    data = format_api_data("hmyv2_getValidatorKeys", params)
    resp = post_request(api_url, data, session)
    
    return BLSKeyListResponse(**resp.json())

#Node

def getCurrentBadBlocks(api_url : str, session : Optional[requests.Session] = None) -> GetCurrentBadBlocksResponse:
    """
    params: None
    result: GetCurrentBadBlocksResponse
    method: hmyv2_getCurrentBadBlocks
    
    NOTE: known issues with RPC not returning correctly
    """
    data = format_api_data("hmyv2_getCurrentBadBlocks", None)
    resp = post_request(api_url, data, session)
    
    return GetCurrentBadBlocksResponse(**resp.json())

def getNodeMetadata(api_url : str, session : Optional[requests.Session] = None) -> GetNodeMetadataResponse:
    """
    params: None
    result: GetNodeMetadataResponse
    method: hmyv2_getNodeMetadata
    """
    data = format_api_data("hmyv2_getNodeMetadata", None)
    resp = post_request(api_url, data, session)
    return GetNodeMetadataResponse(**resp.json())

def protocolVersion(api_url : str, session : Optional[requests.Session] = None) -> ProtocolVersionResponse:
    """
    params: None
    result: ProtocolVersionResponse
    method: hmyv2_protocolVersion
    """
    data = format_api_data("hmyv2_protocolVersion", None)
    resp = post_request(api_url, data, session)
    
    return ProtocolVersionResponse(**resp.json())

def peerCount(api_url : str, session : Optional[requests.Session] = None) -> PeerCountResponse:
    """
    params: None
    result: PeerCountResponse
    method: net_peerCount
    """
    data = format_api_data("net_peerCount", None)
    resp = post_request(api_url, data, session)
    
    return PeerCountResponse(**resp.json())

#Blocks

def getBlocks(api_url : str, params : BlockListParams, session : Optional[requests.Session] = None) -> BlockListResponse:
    """
    params: BlockListParams
    result: BlockListResponse
    method: hmyv2_getBlocks
    """
    data = format_api_data("hmyv2_getBlocks", params)
    resp = post_request(api_url, data, session)
    
    return BlockListResponse(**resp.json())

def getBlockByNumber(api_url : str, params : GetBlockByNumberParameters, session : Optional[requests.Session] = None) -> BlockResponse:
    """
    params: GetBlockByNumberParameters
    result: BlockResponse
    method: hmyv2_getBlockByNumber
    """
    data = format_api_data("hmyv2_getBlockByNumber", params)
    resp = post_request(api_url, data, session)
    
    return BlockResponse(**resp.json())

def getBlockByHash(api_url : str, params : GetBlockByHashParameters, session : Optional[requests.Session] = None) -> BlockResponse:
    """
    params: GetBlockByHashParameters
    result: BlockResponse
    method: hmyv2_getBlockByHash
    """
    data = format_api_data("hmyv2_getBlockByHash", params)
    resp = post_request(api_url, data, session)
    
    return BlockResponse(**resp.json())

def getBlockSigners(api_url : str, params : BlockListParams, session : Optional[requests.Session] = None) -> AddressListResponse:
    """
    params: BlockListParams
    result: AddressListResponse
    method: hmyv2_getBlockSigners
    """
    data = format_api_data("hmyv2_getBlockSigners", params)
    resp = post_request(api_url, data, session)
    
    return AddressListResponse(**resp.json())

def getBlockSignersKeys(api_url : str, params : BlockNumberParameters, session : Optional[requests.Session] = None) -> BLSKeyListResponse:
    """
    params: BlockNumberParameters
    result: BLSKeyListResponse
    method: hmyv2_getBlockSignersKeys
    """
    data = format_api_data("hmyv2_getBlockSignersKeys", params)
    resp = post_request(api_url, data, session)
    
    return BLSKeyListResponse(**resp.json())

def getBlockTransactionCountByNumber(api_url : str, params : BlockNumberParameters, session : Optional[requests.Session] = None) -> TransactionCountResponse:
    """
    params: BlockNumberParameters
    result: TransactionCountResponse
    method: hmyv2_getBlockTransactionCountByNumber
    """
    data = format_api_data("hmyv2_getBlockTransactionCountByNumber", params)
    resp = post_request(api_url, data, session)
    return TransactionCountResponse(**resp.json())

def getBlockTransactionCountByHash(api_url : str, params : HashParameters, session : Optional[requests.Session] = None) -> TransactionCountResponse:
    """
    params: HashParameters
    result: TransactionCountResponse
    method: hmyv2_getBlockTransactionCountByHash
    """
    data = format_api_data("hmyv2_getBlockTransactionCountByHash", params)
    resp = post_request(api_url, data, session)
    return TransactionCountResponse(**resp.json())

def getHeaderByNumber(api_url : str, params : BlockNumberParameters, session : Optional[requests.Session] = None) -> HeaderResponse:
    """
    params: BlockNumberParameters
    result: HeaderResponse
    method: hmyv2_getHeaderByNumber
    """
    data = format_api_data("hmyv2_getHeaderByNumber", params)
    resp = post_request(api_url, data, session)
    return HeaderResponse(**resp.json())

def getLatestChainHeaders(api_url : str, session : Optional[requests.Session] = None) -> GetLatestChainHeadersResponse:
    """
    params: None
    result: GetLatestChainHeadersResponse
    method: hmyv2_getLatestChainHeaders
    """
    data = format_api_data("hmyv2_getLatestChainHeaders", None)
    resp = post_request(api_url, data, session)
    return GetLatestChainHeadersResponse(**resp.json())

def latestHeader(api_url : str, session : Optional[requests.Session] = None) -> HeaderResponse:
    """
    params: None
    result: HeaderResponse
    method: hmyv2_latestHeader
    """
    data = format_api_data("hmyv2_latestHeader", None)
    resp = post_request(api_url, data, session)
    return HeaderResponse(**resp.json())
