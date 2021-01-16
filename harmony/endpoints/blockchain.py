from typing import Optional

import requests

from ..utils.communication import post_request
from ..utils.call_format import format_api_data

from ..models import (
    BlockNumberParameters,
    BlockNumberResults,
    GetCirculatingSupplyParameters,
    GetCirculatingSupplyResults,
    GetEpochParameters,
    GetEpochResults,
    GetLastCrossLinksParameters,
    GetLastCrossLinksResults,
    GetLeaderParameters,
    GetLeaderResults,
    GasPriceParameters,
    GasPriceResults,
    GetShardingStructureParameters,
    GetShardingStructureResults,
    GetTotalSupplyParameters,
    GetTotalSupplyResults,
    GetValidatorsParameters,
    GetValidatorsResults,
    GetValidatorKeysParameters,
    GetValidatorKeysResults,
    GetValidatorKeyParameters,
    GetCurrentBadBlocksParameters,
    GetCurrentBadBlocksResults,
    GetNodeMetadataParameters,
    GetNodeMetadataResults,
    ProtocolVersionParameters,
    ProtocolVersionResults,
    PeerCountParameters,
    PeerCountResults,
    GetBlocksParameters,
    GetBlocksResults,
    GetBlockByNumberParameters,
    GetBlockByNumberResults,
    GetBlockByHashParameters,
    GetBlockByHashResults,
    GetBlockSignersParameters,
    GetBlockSignersResults,
    GetBlockSignersKeysParameters,
    GetBlockSignersKeysResults,
    GetBlockTransactionCountByNumberParameters,
    GetBlockTransactionCountByNumberResults,
    GetHeaderByNumberParameters,
    GetHeaderByNumberResults,
    GetLatestChainHeadersParameters,
    GetLatestChainHeadersResults,
    LatestHeaderParameters,
    LatestHeaderResults
)

#Network

def blockNumber(api_url : str, params : BlockNumberParameters, session : Optional[requests.Session] = None) -> BlockNumberResults:
	"""
    params: BlockNumberParameters
    result: BlockNumberResults
    method: hmyv2_blockNumber
    """
    data = format_api_data("hmyv2_blockNumber", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return BlockNumberResults(**results)

def getCirculatingSupply(api_url : str, params : GetCirculatingSupplyParameters, session : Optional[requests.Session] = None) -> GetCirculatingSupplyResults:
	"""
    params: GetCirculatingSupplyParameters
    result: GetCirculatingSupplyResults
    method: hmyv2_getCirculatingSupply
    """
    data = format_api_data("hmyv2_getCirculatingSupply", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetCirculatingSupplyResults(**results)

def getEpoch(api_url : str, params : GetEpochParameters, session : Optional[requests.Session] = None) -> GetEpochResults:
	"""
    params: GetEpochParameters
    result: GetEpochResults
    method: hmyv2_getEpoch
    """
    data = format_api_data("hmyv2_getEpoch", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetEpochResults(**results)

def getLastCrossLinks(api_url : str, params : GetLastCrossLinksParameters, session : Optional[requests.Session] = None) -> GetLastCrossLinksResults:
	"""
    params: GetLastCrossLinksParameters
    result: GetLastCrossLinksResults
    method: hmyv2_getLastCrossLinks
    """
    data = format_api_data("hmyv2_getLastCrossLinks", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetLastCrossLinksResults(**results)

def getLeader(api_url : str, params : GetLeaderParameters, session : Optional[requests.Session] = None) -> GetLeaderResults:
	"""
    params: GetLeaderParameters
    result: GetLeaderResults
    method: hmyv2_getLeader
    """
    data = format_api_data("hmyv2_getLeader", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetLeaderResults(**results)

def gasPrice(api_url : str, params : GasPriceParameters, session : Optional[requests.Session] = None) -> GasPriceResults:
	"""
    params: GasPriceParameters
    result: GasPriceResults
    method: hmyv2_gasPrice
    """
    data = format_api_data("hmyv2_gasPrice", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GasPriceResults(**results)

def getShardingStructure(api_url : str, params : GetShardingStructureParameters, session : Optional[requests.Session] = None) -> GetShardingStructureResults:
	"""
    params: GetShardingStructureParameters
    result: GetShardingStructureResults
    method: hmyv2_getShardingStructure
    """
    data = format_api_data("hmyv2_getShardingStructure", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetShardingStructureResults(**results)

def getTotalSupply(api_url : str, params : GetTotalSupplyParameters, session : Optional[requests.Session] = None) -> GetTotalSupplyResults:
	"""
    params: GetTotalSupplyParameters
    result: GetTotalSupplyResults
    method: hmyv2_getTotalSupply
    """
    data = format_api_data("hmyv2_getTotalSupply", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetTotalSupplyResults(**results)

def getValidators(api_url : str, params : GetValidatorsParameters, session : Optional[requests.Session] = None) -> GetValidatorsResults:
	"""
    params: GetValidatorsParameters
    result: GetValidatorsResults
    method: hmyv2_getValidators
    """
    data = format_api_data("hmyv2_getValidators", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetValidatorsResults(**results)

def getValidatorKeys(api_url : str, params : GetValidatorKeysParameters, session : Optional[requests.Session] = None) -> GetValidatorKeysResults:
	"""
    params: GetValidatorKeysParameters
    result: GetValidatorKeysResults
    method: hmyv2_getValidatorKeys
    """
    data = format_api_data("hmyv2_getValidatorKeys", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetValidatorKeysResults(**results)

#Node

def getCurrentBadBlocks(api_url : str, params : GetCurrentBadBlocksParameters, session : Optional[requests.Session] = None) -> GetCurrentBadBlocksResults:
	"""
    params: GetCurrentBadBlocksParameters
    result: GetCurrentBadBlocksResults
    method: hmyv2_getCurrentBadBlocks
    """
    data = format_api_data("hmyv2_getCurrentBadBlocks", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetCurrentBadBlocksResults(**results)

def getNodeMetadata(api_url : str, params : GetNodeMetadataParameters, session : Optional[requests.Session] = None) -> GetNodeMetadataResults:
	"""
    params: GetNodeMetadataParameters
    result: GetNodeMetadataResults
    method: hmyv2_getNodeMetadata
    """
    data = format_api_data("hmyv2_getNodeMetadata", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetNodeMetadataResults(**results)

def protocolVersion(api_url : str, params : ProtocolVersionParameters, session : Optional[requests.Session] = None) -> ProtocolVersionResults:
	"""
    params: ProtocolVersionParameters
    result: ProtocolVersionResults
    method: hmyv2_protocolVersion
    """
    data = format_api_data("hmyv2_protocolVersion", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return ProtocolVersionResults(**results)

def peerCount(api_url : str, params : PeerCountParameters, session : Optional[requests.Session] = None) -> PeerCountResults:
	"""
    params: PeerCountParameters
    result: PeerCountResults
    method: net_peerCount
    """
    data = format_api_data("net_peerCount", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return PeerCountResults(**results)

#Blocks

def getBlocks(api_url : str, params : GetBlocksParameters, session : Optional[requests.Session] = None) -> GetBlocksResults:
	"""
    params: GetBlocksParameters
    result: GetBlocksResults
    method: hmyv2_getBlocks
    """
    data = format_api_data("hmyv2_getBlocks", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetBlocksResults(**results)

def getBlockByNumber(api_url : str, params : GetBlockByNumberParameters, session : Optional[requests.Session] = None) -> GetBlockByNumberResults:
	"""
    params: GetBlockByNumberParameters
    result: GetBlockByNumberResults
    method: hmyv2_getBlockByNumber
    """
    data = format_api_data("hmyv2_getBlockByNumber", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetBlockByNumberResults(**results)

def getBlockByHash(api_url : str, params : GetBlockByHashParameters, session : Optional[requests.Session] = None) -> GetBlockByHashResults:
	"""
    params: GetBlockByHashParameters
    result: GetBlockByHashResults
    method: hmyv2_getBlockByHash
    """
    data = format_api_data("hmyv2_getBlockByHash", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetBlockByHashResults(**results)

def getBlockSigners(api_url : str, params : GetBlockSignersParameters, session : Optional[requests.Session] = None) -> GetBlockSignersResults:
	"""
    params: GetBlockSignersParameters
    result: GetBlockSignersResults
    method: hmyv2_getBlockSigners
    """
    data = format_api_data("hmyv2_getBlockSigners", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetBlockSignersResults(**results)

def getBlockSignersKeys(api_url : str, params : GetBlockSignersKeysParameters, session : Optional[requests.Session] = None) -> GetBlockSignersKeysResults:
	"""
    params: GetBlockSignersKeysParameters
    result: GetBlockSignersKeysResults
    method: hmyv2_getBlockSignersKeys
    """
    data = format_api_data("hmyv2_getBlockSignersKeys", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetBlockSignersKeysResults(**results)

def getBlockTransactionCountByNumber(api_url : str, params : GetBlockTransactionCountByNumberParameters, session : Optional[requests.Session] = None) -> GetBlockTransactionCountByNumberResults:
	"""
    params: GetBlockTransactionCountByNumberParameters
    result: GetBlockTransactionCountByNumberResults
    method: hmyv2_getBlockTransactionCountByNumber
    """
    data = format_api_data("hmyv2_getBlockTransactionCountByNumber", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetBlockTransactionCountByNumberResults(**results)

def getHeaderByNumber(api_url : str, params : GetHeaderByNumberParameters, session : Optional[requests.Session] = None) -> GetHeaderByNumberResults:
	"""
    params: GetHeaderByNumberParameters
    result: GetHeaderByNumberResults
    method: hmyv2_getHeaderByNumber
    """
    data = format_api_data("hmyv2_getHeaderByNumber", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetHeaderByNumberResults(**results)

def getLatestChainHeaders(api_url : str, params : GetLatestChainHeadersParameters, session : Optional[requests.Session] = None) -> GetLatestChainHeadersResults:
	"""
    params: GetLatestChainHeadersParameters
    result: GetLatestChainHeadersResults
    method: hmyv2_getLatestChainHeaders
    """
    data = format_api_data("hmyv2_getLatestChainHeaders", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return GetLatestChainHeadersResults(**results)

def latestHeader(api_url : str, params : LatestHeaderParameters, session : Optional[requests.Session] = None) -> LatestHeaderResults:
	"""
    params: LatestHeaderParameters
    result: LatestHeaderResults
    method: hmyv2_latestHeader
    """
    data = format_api_data("hmyv2_latestHeader", params)
    resp = post_request(api_url, data, session)
    results = {"result" : resp.json()["result"]}
    return LatestHeaderResults(**results)