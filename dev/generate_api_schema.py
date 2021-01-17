import json

from apispec import APISpec
from pydantic import BaseModel, Field
from pydantic.schema import schema

from harmony.models import *

def make_path_operations(request_name, response_name, tag=None, method_description=None, response_description=None):
    operations = {}
    post = {}
    if tag is not None:
        post["tags"] = [tag]
    if method_description is not None:
        post["description"] = method_description
    request_body = {}
    request_body["content"] = {"application/json" : { "schema" : request_name }}
    responses = {}
    responses["200"] = {}
    if response_description is not None:
        responses["200"]["description"] = response_description
    if isinstance(response_name, (tuple, list)): 
        responses["200"]["content"] = {"application/json" : { "schema" :  {"oneOf" : [{"$ref" : "#/components/schemas/{}".format(resp)} for resp in response_name] }}}
    else:
        responses["200"]["content"] = {"application/json" : { "schema" : response_name }}
    post["requestBody"] = request_body
    post["responses"] = responses
    operations["post"] = post
    return operations


def make_api_spec():
    spec = APISpec(
        title="Harmony",
        version="2.0.0",
        openapi_version="3.0.3",
        info=dict(description="Harmony API"),
    )
    #Smart Contract
    spec.components.schema("CallRequest", CallRequest.schema())
    spec.components.schema("CallResponse", CallResponse.schema())
    spec.path(path="/hmyv2_call", operations=make_path_operations("CallRequest", "CallResponse", tag="Smart Contract", method_description="Executes a smart contract code without saving state", response_description="Return value of the executed smart contract"))
    
    spec.components.schema("EstimateGasRequest", EstimateGasRequest.schema())
    spec.components.schema("EstimateGasResponse", EstimateGasResponse.schema())
    spec.path(path="/hmyv2_estimateGas", operations=make_path_operations("EstimateGasRequest", "EstimateGasResponse", tag="Smart Contract", method_description="Executes a smart contract transction without created a transaction and saving data", response_description="Hex of estimated gas price of smart contract call"))
    
    spec.components.schema("GetCodeRequest", GetCodeRequest.schema())
    spec.components.schema("GetCodeResponse", GetCodeResponse.schema())
    spec.path(path="/hmyv2_getCode", operations=make_path_operations("GetCodeRequest", "GetCodeResponse", tag="Smart Contract", method_description=None, response_description=None))
    
    spec.components.schema("GetStorageAtRequest", GetStorageAtRequest.schema())
    spec.components.schema("GetStorageAtResponse", GetStorageAtResponse.schema())
    spec.path(path="/hmyv2_getStorageAt", operations=make_path_operations("GetStorageAtRequest", "GetStorageAtResponse", tag="Smart Contract", method_description=None, response_description="Data stored at the smart contract location"))

    #Staking
    spec.components.schema("GetDelegationByDelegatorRequest", GetDelegationByDelegatorRequest.schema())
    spec.components.schema("DelegationListResponse", DelegationListResponse.schema())
    spec.path(path="/hmyv2_getDelegationsByDelegator", operations=make_path_operations("GetDelegationByDelegatorRequest", "DelegationListResponse", tag="Staking", method_description=None, response_description=None))

    spec.components.schema("GetDelegationsByDelegatorByBlockNumberRequest", GetDelegationsByDelegatorByBlockNumberRequest.schema())
    
    spec.path(path="/hmyv2_getDelegationsByDelegatorByBlockNumber", operations=make_path_operations("GetDelegationsByDelegatorByBlockNumberRequest", "DelegationListResponse", tag="Staking", method_description=None, response_description=None))

    spec.components.schema("GetDelegationsByValidatorRequest", GetDelegationsByValidatorRequest.schema())
    spec.components.schema("ValidatorInformationListResponse", ValidatorInformationListResponse.schema())
    spec.path(path="/hmyv2_getDelegationsByValidator", operations=make_path_operations("GetDelegationsByValidatorRequest", "ValidatorInformationListResponse", tag="Staking", method_description=None, response_description=None))

    spec.components.schema("GetAllValidatorAddressesRequest", GetAllValidatorAddressesRequest.schema())
    spec.components.schema("AddressListResponse", AddressListResponse.schema())
    spec.path(path="/hmyv2_getAllValidatorAddresses", operations=make_path_operations("GetAllValidatorAddressesRequest", "AddressListResponse", tag="Staking", method_description=None, response_description="List of wallet addresses that have created validators on the network"))

    spec.components.schema("GetAllValidatorInformationRequest", GetAllValidatorInformationRequest.schema())
    spec.path(path="/hmyv2_getAllValidatorInformation", operations=make_path_operations("GetAllValidatorInformationRequest", "ValidatorInformationListResponse", tag="Staking", method_description=None, response_description=None))

    spec.components.schema("GetAllValidatorInformationByBlockNumberRequest", GetAllValidatorInformationByBlockNumberRequest.schema())
    spec.path(path="/hmyv2_getAllValidatorInformationByBlockNumber", operations=make_path_operations("GetAllValidatorInformationByBlockNumberRequest", "ValidatorInformationListResponse", tag="Staking", method_description=None, response_description="NOTE: metrics field is overwritten & will always display current epoch data"))

    spec.components.schema("GetElectedValidatorAddressesRequest", GetElectedValidatorAddressesRequest.schema())
    spec.path(path="/hmyv2_getElectedValidatorAddresses", operations=make_path_operations("GetElectedValidatorAddressesRequest", "AddressListResponse", tag="Staking", method_description=None, response_description="List of wallet addresses that are currently elected"))

    spec.components.schema("GetValidatorInformationRequest", GetValidatorInformationRequest.schema())
    spec.components.schema("ValidatorInformationResponse", ValidatorInformationResponse.schema())
    spec.path(path="/hmyv2_getValidatorInformation", operations=make_path_operations("GetValidatorInformationRequest", "ValidatorInformationResponse", tag="Staking", method_description=None, response_description=None))

    
    spec.components.schema("GetCurrentUtilityMetricsRequest", GetCurrentUtilityMetricsRequest.schema())
    spec.components.schema("GetCurrentUtilityMetricsResponse", GetCurrentUtilityMetricsResponse.schema())
    spec.path(path="/hmyv2_getCurrentUtilityMetrics", operations=make_path_operations("GetCurrentUtilityMetricsRequest", "GetCurrentUtilityMetricsResponse", tag="Staking", method_description=None, response_description=None))

    spec.components.schema("GetMedianRawStakeSnapshotRequest", GetMedianRawStakeSnapshotRequest.schema())
    spec.components.schema("GetMedianRawStakeSnapshotResponse", GetMedianRawStakeSnapshotResponse.schema())
    spec.path(path="/hmyv2_getMedianRawStakeSnapshot", operations=make_path_operations("GetMedianRawStakeSnapshotRequest", "GetMedianRawStakeSnapshotResponse", tag="Staking", method_description=None, response_description=None))

    spec.components.schema("GetStakingNetworkInfoRequest", GetStakingNetworkInfoRequest.schema())
    spec.components.schema("GetStakingNetworkInfoResponse", GetStakingNetworkInfoResponse.schema())
    spec.path(path="/hmyv2_getStakingNetworkInfo", operations=make_path_operations("GetStakingNetworkInfoRequest", "GetStakingNetworkInfoResponse", tag="Staking", method_description=None, response_description=None))

    spec.components.schema("GetSuperCommitteesRequest", GetSuperCommitteesRequest.schema())
    spec.components.schema("GetSuperCommitteesResponse", GetSuperCommitteesResponse.schema())
    spec.path(path="/hmyv2_getSuperCommittees", operations=make_path_operations("GetSuperCommitteesRequest", "GetSuperCommitteesResponse", tag="Staking", method_description=None, response_description=None))
    
    #Transaction

    spec.components.schema("GetCXReceiptByHashRequest", GetCXReceiptByHashRequest.schema())
    spec.components.schema("GetCXReceiptByHashResponse", GetCXReceiptByHashResponse.schema())
    spec.path(path="/hmyv2_getCXReceiptByHash", operations=make_path_operations("GetCXReceiptByHashRequest", "GetCXReceiptByHashResponse", tag="Transaction", method_description="Query the CX receipt hash on the receiving shard endpoint", response_description=None))

    spec.components.schema("GetPendingCXReceiptsRequest", GetPendingCXReceiptsRequest.schema())
    spec.components.schema("GetPendingCXReceiptsResponse", GetPendingCXReceiptsResponse.schema())
    spec.path(path="/hmyv2_getPendingCXReceipts", operations=make_path_operations("GetPendingCXReceiptsRequest", "GetPendingCXReceiptsResponse", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("ResendCXRequest", ResendCXRequest.schema())
    spec.components.schema("ResendCXResponse", ResendCXResponse.schema())
    spec.path(path="/hmyv2_resendCX", operations=make_path_operations("ResendCXRequest", "ResendCXResponse", tag="Transaction", method_description="Use this API call to resend the cross shard receipt to the receiving shard to re-process if the transaction did not pay out ", response_description="If cross shard receipt was successfully resent or not"))

    spec.components.schema("GetPoolStatsRequest", GetPoolStatsRequest.schema())
    spec.components.schema("GetPoolStatsResponse", GetPoolStatsResponse.schema())
    spec.path(path="/hmyv2_getPoolStats", operations=make_path_operations("GetPoolStatsRequest", "GetPoolStatsResponse", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("PendingStakingTransactionsRequest", PendingStakingTransactionsRequest.schema())
    spec.components.schema("StakingTransactionListResponse", StakingTransactionListResponse.schema())
    spec.path(path="/hmyv2_pendingStakingTransactions", operations=make_path_operations("PendingStakingTransactionsRequest", "StakingTransactionListResponse", tag="Transaction", method_description=None, response_description="List of staking transactions in the transaction pool"))

    spec.components.schema("PendingTransactionsRequest", PendingTransactionsRequest.schema())
    spec.components.schema("TransactionListResponse", TransactionListResponse.schema())
    spec.path(path="/hmyv2_pendingTransactions", operations=make_path_operations("PendingTransactionsRequest", "TransactionListResponse", tag="Transaction", method_description=None, response_description="List of regular & smart contract transactions in the transaction pool"))

    spec.components.schema("GetCurrentStakingErrorSinkRequest", GetCurrentStakingErrorSinkRequest.schema())
    spec.components.schema("GetCurrentStakingErrorSinkResponse", GetCurrentStakingErrorSinkResponse.schema())
    spec.path(path="/hmyv2_getCurrentStakingErrorSink", operations=make_path_operations("GetCurrentStakingErrorSinkRequest", "GetCurrentStakingErrorSinkResponse", tag="Transaction", method_description=None, response_description="staking transaction hash - if the transaction has been added to the pool - else - error"))

    spec.components.schema("GetStakingTransactionByBlockNumberAndIndexRequest", GetStakingTransactionByBlockNumberAndIndexRequest.schema())
    spec.components.schema("StakingTransactionResponse", StakingTransactionResponse.schema())
    spec.path(path="/hmyv2_getStakingTransactionByBlockNumberAndIndex", operations=make_path_operations("GetStakingTransactionByBlockNumberAndIndexRequest", "StakingTransactionResponse", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("GetStakingTransactionByBlockHashAndIndexRequest", GetStakingTransactionByBlockHashAndIndexRequest.schema())
    spec.path(path="/hmyv2_getStakingTransactionByBlockHashAndIndex", operations=make_path_operations("GetStakingTransactionByBlockHashAndIndexRequest", "StakingTransactionResponse", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("GetStakingTransactionByHashRequest", GetStakingTransactionByHashRequest.schema())
    spec.path(path="/hmyv2_getStakingTransactionByHash", operations=make_path_operations("GetStakingTransactionByHashRequest", "StakingTransactionResponse", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("SendRawStakingTransactionRequest", SendRawStakingTransactionRequest.schema())
    spec.components.schema("SendRawStakingTransactionResponse", SendRawStakingTransactionResponse.schema())
    spec.path(path="/hmyv2_sendRawStakingTransaction", operations=make_path_operations("SendRawStakingTransactionRequest", "SendRawStakingTransactionResponse", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("GetCurrentTransactionErrorSinkRequest", GetCurrentTransactionErrorSinkRequest.schema())
    spec.components.schema("GetCurrentTransactionErrorSinkResponse", GetCurrentTransactionErrorSinkResponse.schema())
    spec.path(path="/hmyv2_getCurrentTransactionErrorSink", operations=make_path_operations("GetCurrentTransactionErrorSinkRequest", "GetCurrentTransactionErrorSinkResponse", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("GetTransactionByBlockHashAndIndexRequest", GetTransactionByBlockHashAndIndexRequest.schema())
    spec.components.schema("TransactionResponse", TransactionResponse.schema())
    spec.path(path="/hmyv2_getTransactionByBlockHashAndIndex", operations=make_path_operations("GetTransactionByBlockHashAndIndexRequest", "TransactionResponse", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("GetTransactionByBlockNumberAndIndexRequest", GetTransactionByBlockNumberAndIndexRequest.schema())
    spec.path(path="/hmyv2_getTransactionByBlockNumberAndIndex", operations=make_path_operations("GetTransactionByBlockNumberAndIndexRequest", "TransactionResponse", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("GetTransactionByHashRequest", GetTransactionByHashRequest.schema())
    spec.path(path="/hmyv2_getTransactionByHash", operations=make_path_operations("GetTransactionByHashRequest", "TransactionResponse", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("GetTransactionReceiptRequest", GetTransactionReceiptRequest.schema())
    spec.components.schema("GetTransactionReceiptResponse", GetTransactionReceiptResponse.schema())
    spec.path(path="/hmyv2_getTransactionReceipt", operations=make_path_operations("GetTransactionReceiptRequest", "GetTransactionReceiptResponse", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("SendRawTransactionRequest", SendRawTransactionRequest.schema())
    spec.components.schema("SendRawTransactionResponse", SendRawTransactionResponse.schema())
    spec.path(path="/hmyv2_sendRawTransaction", operations=make_path_operations("SendRawTransactionRequest", "SendRawTransactionResponse", tag="Transaction", method_description=None, response_description="staking transaction hash - if the transaction has been added to the pool - else - error"))


    #Blockchain
    spec.components.schema("BlockNumberRequest", BlockNumberRequest.schema())
    spec.components.schema("BlockNumberResponse", BlockNumberResponse.schema())
    spec.path(path="/hmyv2_blockNumber", operations=make_path_operations("BlockNumberRequest", "BlockNumberResponse", tag="Blockchain", method_description=None, response_description="Current block number"))
    
    spec.components.schema("GetCirculatingSupplyRequest", GetCirculatingSupplyRequest.schema())
    spec.components.schema("GetCirculatingSupplyResponse",GetCirculatingSupplyResponse.schema())
    spec.path(path="/hmyv2_getCirculatingSupply", operations=make_path_operations("GetCirculatingSupplyRequest", "GetCirculatingSupplyResponse", tag="Blockchain", method_description=None, response_description="Circulation supply of tokens in ONE"))

    spec.components.schema("GetEpochRequest", GetEpochRequest.schema())
    spec.components.schema("GetEpochResponse", GetEpochResponse.schema())
    spec.path(path="/hmyv2_getEpoch", operations=make_path_operations("GetEpochRequest", "GetEpochResponse", tag="Blockchain", method_description=None, response_description="Current block number"))

    spec.components.schema("GetLastCrossLinksRequest", GetLastCrossLinksRequest.schema())
    spec.components.schema("GetLastCrossLinksResponse", GetLastCrossLinksResponse.schema())
    spec.path(path="/hmyv2_getLastCrossLinks", operations=make_path_operations("GetLastCrossLinksRequest", "GetLastCrossLinksResponse", tag="Blockchain", method_description=None, response_description=None))

    spec.components.schema("GetLeaderRequest", GetLeaderRequest.schema())
    spec.components.schema("GetLeaderResponse", GetLeaderResponse.schema())
    spec.path(path="/hmyv2_getLeader", operations=make_path_operations("GetLeaderRequest", "GetLeaderResponse", tag="Blockchain", method_description=None, response_description="Wallet address of current leader"))
    
    spec.components.schema("GasPriceRequest", GasPriceRequest.schema())
    spec.components.schema("GasPriceResponse", GasPriceResponse.schema())
    spec.path(path="/hmyv2_gasPrice", operations=make_path_operations("GasPriceRequest", "GasPriceResponse", tag="Blockchain", method_description=None, response_description="Current average gas price of transactions"))

    spec.components.schema("GetShardingStructureRequest", GetShardingStructureRequest.schema())
    spec.components.schema("GetShardingStructureResponse", GetShardingStructureResponse.schema())
    spec.path(path="/hmyv2_getShardingStructure", operations=make_path_operations("GetShardingStructureRequest", "GetShardingStructureResponse", tag="Blockchain", method_description=None, response_description=None))

    spec.components.schema("GetTotalSupplyRequest", GetTotalSupplyRequest.schema())
    spec.components.schema("GetTotalSupplyResponse", GetTotalSupplyResponse.schema())
    spec.path(path="/hmyv2_getTotalSupply", operations=make_path_operations("GetTotalSupplyRequest", "GetTotalSupplyResponse", tag="Blockchain", method_description=None, response_description="Total number of pre-mined tokens"))

    spec.components.schema("GetValidatorsRequest", GetValidatorsRequest.schema())
    spec.components.schema("GetValidatorsResponse", GetValidatorsResponse.schema())
    spec.path(path="/hmyv2_getValidators", operations=make_path_operations("GetValidatorsRequest", "GetValidatorsResponse", tag="Blockchain", method_description=None, response_description=None))

    spec.components.schema("GetValidatorKeysRequest", GetValidatorKeysRequest.schema())
    spec.components.schema("BLSKeyListResponse", BLSKeyListResponse.schema())
    spec.path(path="/hmyv2_getValidatorKeys", operations=make_path_operations("GetValidatorKeysRequest", "BLSKeyListResponse", tag="Blockchain", method_description=None, response_description="List of public BLS keys in the elected committee"))

    spec.components.schema("GetCurrentBadBlocksRequest", GetCurrentBadBlocksRequest.schema())
    spec.components.schema("GetCurrentBadBlocksResponse", GetCurrentBadBlocksResponse.schema())
    spec.path(path="/hmyv2_getCurrentBadBlocks", operations=make_path_operations("GetCurrentBadBlocksRequest", "GetCurrentBadBlocksResponse", tag="Blockchain", method_description="Known issues with RPC not returning correctly", response_description="List of bad blocks in node memory"))

    spec.components.schema("GetNodeMetadataRequest", GetNodeMetadataRequest.schema())
    spec.components.schema("GetNodeMetadataResponse", GetNodeMetadataResponse.schema())
    spec.path(path="/hmyv2_getNodeMetadata", operations=make_path_operations("GetNodeMetadataRequest", "GetNodeMetadataResponse", tag="Blockchain", method_description=None, response_description=None))

    spec.components.schema("ProtocolVersionRequest", ProtocolVersionRequest.schema())
    spec.components.schema("ProtocolVersionResponse", ProtocolVersionResponse.schema())
    spec.path(path="/hmyv2_protocolVersion", operations=make_path_operations("ProtocolVersionRequest", "ProtocolVersionResponse", tag="Blockchain", method_description=None, response_description="Protocol version"))

    spec.components.schema("PeerCountRequest", PeerCountRequest.schema())
    spec.components.schema("PeerCountResponse", PeerCountResponse.schema())
    spec.path(path="/net_peerCount", operations=make_path_operations("PeerCountRequest", "PeerCountResponse", tag="Blockchain", method_description=None, response_description="Number of peers represented as a Hex string"))

    spec.components.schema("GetBlocksRequest", GetBlocksRequest.schema())
    spec.components.schema("BlockListResponse", BlockListResponse.schema())
    spec.path(path="/hmyv2_getBlocks", operations=make_path_operations("GetBlocksRequest", "BlockListResponse", tag="Blockchain", method_description=None, response_description="List of blocks"))

    spec.components.schema("GetBlockByNumberRequest", GetBlockByNumberRequest.schema())
    spec.components.schema("BlockResponse", BlockResponse.schema())
    spec.path(path="/hmyv2_getBlockByNumber", operations=make_path_operations("GetBlockByNumberRequest", "BlockResponse", tag="Blockchain", method_description=None, response_description=None))

    spec.components.schema("GetBlockByHashRequest", GetBlockByHashRequest.schema())
    spec.path(path="/hmyv2_getBlockByHash", operations=make_path_operations("GetBlockByHashRequest", "BlockResponse", tag="Blockchain", method_description=None, response_description=None))

    spec.components.schema("GetBlockSignersRequest", GetBlockSignersRequest.schema())
    spec.path(path="/hmyv2_getBlockSigners", operations=make_path_operations("GetBlockSignersRequest", "AddressListResponse", tag="Blockchain", method_description=None, response_description="List of block signer wallet addresses"))

    spec.components.schema("GetBlockSignersKeysRequest", GetBlockSignersKeysRequest.schema())
    spec.path(path="/hmyv2_getBlockSignersKeys", operations=make_path_operations("GetBlockSignersKeysRequest", "BLSKeyListResponse", tag="Blockchain", method_description=None, response_description="List of block signer public BLS keys"))

    spec.components.schema("GetBlockTransactionCountByNumberRequest", GetBlockTransactionCountByNumberRequest.schema())
    spec.components.schema("TransactionCountResponse", TransactionCountResponse.schema())
    spec.path(path="/hmyv2_getBlockTransactionCountByNumber", operations=make_path_operations("GetBlockTransactionCountByNumberRequest", "TransactionCountResponse", tag="Blockchain", method_description=None, response_description="Number of transactions in block"))

    spec.components.schema("GetBlockTransactionCountByHashRequest", GetBlockTransactionCountByHashRequest.schema())
    spec.path(path="/hmyv2_getBlockTransactionCountByHash", operations=make_path_operations("GetBlockTransactionCountByHashRequest", "TransactionCountResponse", tag="Blockchain", method_description=None, response_description="Number of transactions in block"))
    
    spec.components.schema("GetHeaderByNumberRequest", GetHeaderByNumberRequest.schema())
    spec.components.schema("HeaderResponse", HeaderResponse.schema())
    spec.path(path="/hmyv2_getHeaderByNumber", operations=make_path_operations("GetHeaderByNumberRequest", "HeaderResponse", tag="Blockchain", method_description=None, response_description="Number of transactions in block"))

    spec.components.schema("GetLatestChainHeadersRequest", GetLatestChainHeadersRequest.schema())
    spec.components.schema("GetLatestChainHeadersResponse", GetLatestChainHeadersResponse.schema())
    spec.path(path="/hmyv2_getLatestChainHeaders", operations=make_path_operations("GetLatestChainHeadersRequest", "GetLatestChainHeadersResponse", tag="Blockchain", method_description=None, response_description=None))

    spec.components.schema("LatestHeaderRequest", LatestHeaderRequest.schema())
    spec.path(path="/hmyv2_latestHeader", operations=make_path_operations("LatestHeaderRequest", "HeaderResponse", tag="Blockchain", method_description=None, response_description=None))

    #Account
    spec.components.schema("GetBalanceRequest", GetBalanceRequest.schema())
    spec.components.schema("BalanceResponse", BalanceResponse.schema())
    spec.path(path="/hmyv2_getBalance", operations=make_path_operations("GetBalanceRequest", "BalanceResponse", tag="Account", method_description=None, response_description="Wallet balance at given block in Atto"))

    spec.components.schema("GetBalanceByBlockNumberRequest", GetBalanceByBlockNumberRequest.schema())
    spec.path(path="/hmyv2_getBalanceByBlockNumber", operations=make_path_operations("GetBalanceByBlockNumberRequest", "BalanceResponse", tag="Account", method_description=None, response_description="Wallet balance at given block in Atto"))

    spec.components.schema("GetStakingTransactionsCountRequest", GetStakingTransactionsCountRequest.schema())
    spec.path(path="/hmyv2_getStakingTransactionsCount", operations=make_path_operations("GetStakingTransactionsCountRequest", "TransactionCountResponse", tag="Account", method_description=None, response_description="Number of staking transactions"))

    spec.components.schema("GetStakingTransactionsHistoryRequest", GetStakingTransactionsHistoryRequest.schema())
    spec.components.schema("TransactionsHashListResponse", TransactionsHashListResponse.schema())
    spec.path(path="/hmyv2_getStakingTransactionsHistory", operations=make_path_operations("GetStakingTransactionsHistoryRequest", ("TransactionsHashListResponse", "StakingTransactionListResponse"), tag="Account", method_description=None, response_description="If txType was False, only the hashes will be provided as opposed to the whole transaction."))

    spec.components.schema("GetTransactionsCountRequest", GetTransactionsCountRequest.schema())
    spec.path(path="/hmyv2_getTransactionsCount", operations=make_path_operations("GetTransactionsCountRequest", "TransactionCountResponse", tag="Account", method_description=None, response_description="Number of transactions"))

    spec.components.schema("GetTransactionsHistoryRequest", GetTransactionsHistoryRequest.schema())
    spec.path(path="/hmyv2_getTransactionsHistory", operations=make_path_operations("GetTransactionsHistoryRequest", ("TransactionsHashListResponse", "TransactionListResponse"), tag="Account", method_description=None, response_description="If txType was False, only the hashes will be provided as opposed to the whole transaction."))

    return spec.to_dict()

def make_model_spec():
    s = schema(TOP_LEVEL_MODELS, title="Harmony API Models")
    return s


if __name__ == "__main__":
    spec = make_api_spec()
    models = make_model_spec()
    with open("api.json", "w") as jf:
        jf.write(json.dumps(spec, indent=2))
    
    with open("models.json", "w") as mf:
        mf.write(json.dumps(models, indent=2))

