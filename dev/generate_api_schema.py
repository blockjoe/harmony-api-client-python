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
    spec.components.schema("EmptyRequest", EmptyRequest.schema())

    spec.components.schema("CallRequest", CallRequest.schema())
    spec.components.schema("CallResponse", CallResponse.schema())
    spec.path(path="/hmyv2_call", operations=make_path_operations("CallRequest", "CallResponse", tag="Smart Contract", method_description="Executes a smart contract code without saving state", response_description="Return value of the executed smart contract"))
    
    #spec.components.schema("CallRequest", CallRequest.schema())
    spec.components.schema("EstimateGasResponse", EstimateGasResponse.schema())
    spec.path(path="/hmyv2_estimateGas", operations=make_path_operations("CallRequest", "EstimateGasResponse", tag="Smart Contract", method_description="Executes a smart contract transction without created a transaction and saving data", response_description="Hex of estimated gas price of smart contract call"))
    
    spec.components.schema("GetCodeRequest", GetCodeRequest.schema())
    spec.components.schema("GetCodeResponse", GetCodeResponse.schema())
    spec.path(path="/hmyv2_getCode", operations=make_path_operations("GetCodeRequest", "GetCodeResponse", tag="Smart Contract", method_description=None, response_description=None))
    
    spec.components.schema("GetStorageAtRequest", GetStorageAtRequest.schema())
    spec.components.schema("GetStorageAtResponse", GetStorageAtResponse.schema())
    spec.path(path="/hmyv2_getStorageAt", operations=make_path_operations("GetStorageAtRequest", "GetStorageAtResponse", tag="Smart Contract", method_description=None, response_description="Data stored at the smart contract location"))

    #Staking
    spec.components.schema("GetDelegationByDelegatorRequest", GetDelegationByDelegatorRequest.schema())
    #spec.components.schema("DelegationListResponse", DelegationListResponse.schema())
    spec.path(path="/hmyv2_getDelegationsByDelegator", operations=make_path_operations("GetDelegationByDelegatorRequest", "DelegationListResponse", tag="Staking", method_description=None, response_description=None))

    spec.components.schema("GetDelegationsByDelegatorByBlockNumberRequest", GetDelegationsByDelegatorByBlockNumberRequest.schema())
    spec.components.schema("DelegationListResponse", DelegationListResponse.schema())
    spec.path(path="/hmyv2_getDelegationsByDelegatorByBlockNumber", operations=make_path_operations("GetDelegationsByDelegatorByBlockNumberRequest", "DelegationListResponse", tag="Staking", method_description=None, response_description=None))

    spec.components.schema("GetDelegationsByValidatorRequest", GetDelegationsByValidatorRequest.schema())
    spec.components.schema("ValidatorListResponse", ValidatorListResponse.schema())
    spec.path(path="/hmyv2_getDelegationsByValidator", operations=make_path_operations("GetDelegationsByValidatorRequest", "ValidatorListResponse", tag="Staking", method_description=None, response_description=None))

    spec.components.schema("GetAllValidatorAddressesResponse", GetAllValidatorAddressesResponse.schema())
    spec.path(path="/hmyv2_getAllValidatorAddresses", operations=make_path_operations("EmptyRequest", "GetAllValidatorAddressesResponse", tag="Staking", method_description=None, response_description="List of wallet addresses that have created validators on the network"))

    spec.components.schema("GetAllValidatorInformationRequest", GetAllValidatorInformationRequest.schema())
    spec.path(path="/hmyv2_getAllValidatorInformation", operations=make_path_operations("GetAllValidatorInformationRequest", "ValidatorListResponse", tag="Staking", method_description=None, response_description=None))

    spec.components.schema("GetAllValidatorInformationByBlockNumberRequest", GetAllValidatorInformationByBlockNumberRequest.schema())
    spec.path(path="/hmyv2_getAllValidatorInformationByBlockNumber", operations=make_path_operations("GetAllValidatorInformationByBlockNumberRequest", "ValidatorListResponse", tag="Staking", method_description=None, response_description="NOTE: metrics field is overwritten & will always display current epoch data"))

    spec.components.schema("GetElectedValidatorAddressesResponse", GetElectedValidatorAddressesResponse.schema())
    spec.path(path="/hmyv2_getElectedValidatorAddresses", operations=make_path_operations("EmptyRequest", "GetElectedValidatorAddressesResponse", tag="Staking", method_description=None, response_description="List of wallet addresses that are currently elected"))

    spec.components.schema("GetValidatorInformationRequest", GetValidatorInformationRequest.schema())
    spec.path(path="/hmyv2_getValidatorInformation", operations=make_path_operations("GetValidatorInformationRequest", "ValidatorListResponse", tag="Staking", method_description=None, response_description=None))

    spec.components.schema("GetCurrentUtilityMetricsResponse", GetCurrentUtilityMetricsResponse.schema())
    spec.path(path="/hmyv2_getCurrentUtilityMetrics", operations=make_path_operations("EmptyRequest", "GetCurrentUtilityMetricsResponse", tag="Staking", method_description=None, response_description=None))

    spec.components.schema("GetMedianRawStakeSnapshotResponse", GetMedianRawStakeSnapshotResponse.schema())
    spec.path(path="/hmyv2_getMedianRawStakeSnapshot", operations=make_path_operations("EmptyRequest", "GetMedianRawStakeSnapshotResponse", tag="Staking", method_description=None, response_description=None))

    spec.components.schema("GetStakingNetworkInfoResponse", GetStakingNetworkInfoResponse.schema())
    spec.path(path="/hmyv2_getStakingNetworkInfo", operations=make_path_operations("EmptyRequest", "GetStakingNetworkInfoResponse", tag="Staking", method_description=None, response_description=None))

    spec.components.schema("GetSuperCommitteesResponse", GetSuperCommitteesResponse.schema())
    spec.path(path="/hmyv2_getSuperCommittees", operations=make_path_operations("EmptyRequest", "GetSuperCommitteesResponse", tag="Staking", method_description=None, response_description=None))
    
    #Transaction
    spec.components.schema("StakingTransactionResult", StakingTransactionResult.schema())
    spec.components.schema("TransactionResult", TransactionResult.schema())

    spec.components.schema("GetCXReceiptByHashRequest", GetCXReceiptByHashRequest.schema())
    spec.components.schema("GetCXReceiptByHashResponse", GetCXReceiptByHashResponse.schema())
    spec.path(path="/hmyv2_getCXReceiptByHash", operations=make_path_operations("GetCXReceiptByHashRequest", "GetCXReceiptByHashResponse", tag="Transaction", method_description="Query the CX receipt hash on the receiving shard endpoint", response_description=None))

    spec.components.schema("GetPendingCXReceiptsResponse", GetPendingCXReceiptsResponse.schema())
    spec.path(path="/hmyv2_getPendingCXReceipts", operations=make_path_operations("EmptyRequest", "GetPendingCXReceiptsResponse", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("ResendCXRequest", ResendCXRequest.schema())
    spec.components.schema("ResendCXResponse", ResendCXResponse.schema())
    spec.path(path="/hmyv2_resendCX", operations=make_path_operations("ResendCXRequest", "ResendCXResponse", tag="Transaction", method_description="Use this API call to resend the cross shard receipt to the receiving shard to re-process if the transaction did not pay out ", response_description="If cross shard receipt was successfully resent or not"))

    spec.components.schema("GetPoolStatsResponse", GetPoolStatsResponse.schema())
    spec.path(path="/hmyv2_getPoolStats", operations=make_path_operations("EmptyRequest", "GetPoolStatsResponse", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("StakingTransactionListResponse", StakingTransactionListResponse.schema())
    spec.path(path="/hmyv2_pendingStakingTransactions", operations=make_path_operations("EmptyRequest", "StakingTransactionListResponse", tag="Transaction", method_description=None, response_description="List of staking transactions in the transaction pool"))

    spec.path(path="/hmyv2_pendingTransactions", operations=make_path_operations("EmptyRequest", "StakingTransactionListResponse", tag="Transaction", method_description=None, response_description="List of regular & smart contract transactions in the transaction pool"))

    spec.components.schema("GetCurrentStakingErrorSinkResponse", GetCurrentStakingErrorSinkResponse.schema())
    spec.path(path="/hmyv2_getCurrentStakingErrorSink", operations=make_path_operations("EmptyRequest", "GetCurrentStakingErrorSinkResponse", tag="Transaction", method_description=None, response_description="staking transaction hash - if the transaction has been added to the pool - else - error"))

    spec.components.schema("GetStakingTransactionByBlockNumberAndIndexRequest", GetStakingTransactionByBlockNumberAndIndexRequest.schema())
    spec.path(path="/hmyv2_getStakingTransactionByBlockNumberAndIndex", operations=make_path_operations("GetStakingTransactionByBlockNumberAndIndexRequest", "StakingTransactionResult", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("GetStakingTransactionByBlockHashAndIndexRequest", GetStakingTransactionByBlockHashAndIndexRequest.schema())
    spec.path(path="/hmyv2_getStakingTransactionByBlockHashAndIndex", operations=make_path_operations("GetStakingTransactionByBlockHashAndIndexRequest", "StakingTransactionResult", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("GetStakingTransactionByHashRequest", GetStakingTransactionByHashRequest.schema())
    spec.path(path="/hmyv2_getStakingTransactionByHash", operations=make_path_operations("GetStakingTransactionByHashRequest", "StakingTransactionResult", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("SendRawStakingTransactionRequest", SendRawStakingTransactionRequest.schema())
    spec.components.schema("SendRawStakingTransactionResponse", SendRawStakingTransactionResponse.schema())
    spec.path(path="/hmyv2_sendRawStakingTransaction", operations=make_path_operations("SendRawStakingTransactionRequest", "SendRawStakingTransactionResponse", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("GetCurrentTransactionErrorSinkResponse", GetCurrentTransactionErrorSinkResponse.schema())
    spec.path(path="/hmyv2_getCurrentTransactionErrorSink", operations=make_path_operations("EmptyRequest", "GetCurrentTransactionErrorSinkResponse", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("GetTransactionByBlockHashAndIndexRequest", GetTransactionByBlockHashAndIndexRequest.schema())
    spec.path(path="/hmyv2_getTransactionByBlockHashAndIndex", operations=make_path_operations("GetTransactionByBlockHashAndIndexRequest", "TransactionResult", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("GetTransactionByBlockNumberAndIndexRequest", GetTransactionByBlockNumberAndIndexRequest.schema())
    spec.path(path="/hmyv2_getTransactionByBlockNumberAndIndex", operations=make_path_operations("GetTransactionByBlockNumberAndIndexRequest", "TransactionResult", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("GetTransactionByHashRequest", GetTransactionByHashRequest.schema())
    spec.path(path="/hmyv2_getTransactionByHash", operations=make_path_operations("GetTransactionByHashRequest", "TransactionResult", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("GetTransactionReceiptRequest", GetTransactionReceiptRequest.schema())
    spec.components.schema("GetTransactionReceiptResponse", GetTransactionReceiptResponse.schema())
    spec.path(path="/hmyv2_getTransactionReceipt", operations=make_path_operations("GetTransactionReceiptRequest", "GetTransactionReceiptResponse", tag="Transaction", method_description=None, response_description=None))

    spec.components.schema("SendRawTransactionRequest", SendRawTransactionRequest.schema())
    spec.components.schema("SendRawTransactionResponse", SendRawTransactionResponse.schema())
    spec.path(path="/hmyv2_sendRawTransaction", operations=make_path_operations("SendRawTransactionRequest", "SendRawTransactionResponse", tag="Transaction", method_description=None, response_description="staking transaction hash - if the transaction has been added to the pool - else - error"))


    #Blockchain
    spec.components.schema("BlockResult",BlockResult.schema())
    spec.components.schema("BlockListResponse",BlockListResponse.schema())

    spec.components.schema("BlockNumberResponse",BlockNumberResponse.schema())
    spec.path(path="/hmyv2_blockNumber", operations=make_path_operations("EmptyRequest", "BlockNumberResponse", tag="Blockchain", method_description=None, response_description="Current block number"))
    
    spec.components.schema("GetCirculatingSupplyResponse",GetCirculatingSupplyResponse.schema())
    spec.path(path="/hmyv2_getCirculatingSupply", operations=make_path_operations("EmptyRequest", "GetCirculatingSupplyResponse", tag="Blockchain", method_description=None, response_description="Circulation supply of tokens in ONE"))

    spec.components.schema("GetEpochResponse",GetEpochResponse.schema())
    spec.path(path="/hmyv2_getEpoch", operations=make_path_operations("EmptyRequest", "GetEpochResponse", tag="Blockchain", method_description=None, response_description="Current block number"))

    spec.components.schema("GetLastCrossLinksResponse",GetLastCrossLinksResponse.schema())
    spec.path(path="/hmyv2_getLastCrossLinks", operations=make_path_operations("EmptyRequest", "GetLastCrossLinksResponse", tag="Blockchain", method_description=None, response_description=None))

    spec.components.schema("GetLeaderResponse",GetLeaderResponse.schema())
    spec.path(path="/hmyv2_getLeader", operations=make_path_operations("EmptyRequest", "GetLeaderResponse", tag="Blockchain", method_description=None, response_description="Wallet address of current leader"))
    
    spec.components.schema("GasPriceResponse",GasPriceResponse.schema())
    spec.path(path="/hmyv2_gasPrice", operations=make_path_operations("EmptyRequest", "GasPriceResponse", tag="Blockchain", method_description=None, response_description="Current average gas price of transactions"))

    spec.components.schema("GetShardingStructureRequest",GetShardingStructureResponse.schema())
    spec.components.schema("GetShardingStructureResponse",GetShardingStructureResponse.schema())
    spec.path(path="/hmyv2_getShardingStructure", operations=make_path_operations("GetShardingStructureRequest", "GetShardingStructureResponse", tag="Blockchain", method_description=None, response_description=None))

    spec.components.schema("GetTotalSupplyResponse",GetTotalSupplyResponse.schema())
    spec.path(path="/hmyv2_getTotalSupply", operations=make_path_operations("EmptyRequest", "GetTotalSupplyResponse", tag="Blockchain", method_description=None, response_description="Total number of pre-mined tokens"))

    spec.components.schema("GetValidatorsRequest",GetValidatorsRequest.schema())
    spec.components.schema("GetValidatorsResponse",GetValidatorsResponse.schema())
    spec.path(path="/hmyv2_getValidators", operations=make_path_operations("GetValidatorsRequest", "GetValidatorsResponse", tag="Blockchain", method_description=None, response_description=None))

    spec.components.schema("GetValidatorKeysRequest",GetValidatorKeysRequest.schema())
    spec.components.schema("GetValidatorKeysResponse",GetValidatorKeysResponse.schema())
    spec.path(path="/hmyv2_getValidatorKeys", operations=make_path_operations("GetValidatorKeysRequest", "GetValidatorKeysResponse", tag="Blockchain", method_description=None, response_description="List of public BLS keys in the elected committee"))

    spec.components.schema("GetCurrentBadBlocksResponse",GetCurrentBadBlocksResponse.schema())
    spec.path(path="/hmyv2_getCurrentBadBlocks", operations=make_path_operations("EmptyRequest", "GetCurrentBadBlocksResponse", tag="Blockchain", method_description="Known issues with RPC not returning correctly", response_description="List of bad blocks in node memory"))

    spec.components.schema("GetNodeMetadataResponse",GetNodeMetadataResponse.schema())
    spec.path(path="/hmyv2_getNodeMetadata", operations=make_path_operations("EmptyRequest", "GetNodeMetadataResponse", tag="Blockchain", method_description=None, response_description=None))

    spec.components.schema("ProtocolVersionResponse",ProtocolVersionResponse.schema())
    spec.path(path="/hmyv2_protocolVersion", operations=make_path_operations("EmptyRequest", "ProtocolVersionResponse", tag="Blockchain", method_description=None, response_description="Protocol version"))

    spec.components.schema("PeerCountResponse",PeerCountResponse.schema())
    spec.path(path="/hmyv2_peerCount", operations=make_path_operations("EmptyRequest", "PeerCountResponse", tag="Blockchain", method_description=None, response_description="Number of peers represented as a Hex string"))

    spec.components.schema("GetBlocksRequest",GetBlocksRequest.schema())
    spec.path(path="/hmyv2_getBlocks", operations=make_path_operations("GetBlocksRequest", "BlockListResponse", tag="Blockchain", method_description=None, response_description="List of blocks"))

    spec.components.schema("GetBlockByNumberRequest",GetBlockByNumberRequest.schema())
    spec.path(path="/hmyv2_getBlockbyNumber", operations=make_path_operations("GetBlockbyNumberRequest", "BlockResult", tag="Blockchain", method_description=None, response_description=None))

    spec.components.schema("GetBlockByHashRequest",GetBlockByHashRequest.schema())
    spec.path(path="/hmyv2_getBlockbyHash", operations=make_path_operations("GetBlockbyHashRequest", "BlockResult", tag="Blockchain", method_description=None, response_description=None))

    spec.components.schema("GetBlockSignersRequest",GetBlockSignersRequest.schema())
    spec.components.schema("GetBlockSignersResponse",GetBlockSignersResponse.schema())
    spec.path(path="/hmyv2_getBlockSigners", operations=make_path_operations("GetBlockSignersRequest", "GetBlockSignersResponse", tag="Blockchain", method_description=None, response_description="List of block signer wallet addresses"))

    spec.components.schema("GetBlockSignersKeysRequest",GetBlockSignersKeysRequest.schema())
    spec.components.schema("GetBlockSignersKeysResponse",GetBlockSignersKeysResponse.schema())
    spec.path(path="/hmyv2_getBlockSignersKeys", operations=make_path_operations("GetBlockSignersKeysRequest", "GetBlockSignersKeysResponse", tag="Blockchain", method_description=None, response_description="List of block signer public BLS keys"))

    spec.components.schema("GetBlockTransactionCountByNumberRequest",GetBlockTransactionCountByNumberRequest.schema())
    spec.components.schema("GetBlockTransactionCountByNumberResponse",GetBlockTransactionCountByNumberResponse.schema())
    spec.path(path="/hmyv2_getBlockTransactionCountbyNumber", operations=make_path_operations("GetBlockTransactionCountbyNumberRequest", "GetBlockTransactionCountbyNumberResponse", tag="Blockchain", method_description=None, response_description="Number of transactions in block"))

    spec.components.schema("GetHeaderByNumberRequest",GetHeaderByNumberRequest.schema())
    spec.components.schema("GetHeaderByNumberResponse",GetHeaderByNumberResponse.schema())
    spec.path(path="/hmyv2_getHeaderbyNumber", operations=make_path_operations("GetHeaderbyNumberRequest", "GetHeaderbyNumberResponse", tag="Blockchain", method_description=None, response_description="Number of transactions in block"))

    spec.components.schema("GetLatestChainHeadersResponse",GetLatestChainHeadersResponse.schema())
    spec.path(path="/hmyv2_getLatestChainHeaders", operations=make_path_operations("EmptyRequest", "GetLatestChainHeadersResponse", tag="Blockchain", method_description=None, response_description=None))

    spec.components.schema("LatestHeaderResponse",LatestHeaderResponse.schema())
    spec.path(path="/hmyv2_latestHeader", operations=make_path_operations("latestHeaderRequest", "latestHeaderResponse", tag="Blockchain", method_description=None, response_description=None))

    #Account
    spec.components.schema("GetBalanceRequest",GetBalanceRequest.schema())
    spec.components.schema("GetBalanceResponse",GetBalanceResponse.schema())
    spec.path(path="/hmyv2_getBalance", operations=make_path_operations("GetBalanceRequest", "GetBalanceResponse", tag="Blockchain", method_description=None, response_description="Wallet balance at given block in Atto"))

    spec.components.schema("GetBalanceByBlockNumberRequest",GetBalanceByBlockNumberRequest.schema())
    spec.components.schema("GetBalanceByBlockNumberResponse",GetBalanceByBlockNumberResponse.schema())
    spec.path(path="/hmyv2_getBalanceByBlockNumber", operations=make_path_operations("GetBalanceByBlockNumberRequest", "GetBalanceByBlockNumberResponse", tag="Blockchain", method_description=None, response_description="Wallet balance at given block in Atto"))

    spec.components.schema("GetStakingTransactionsCountRequest",GetStakingTransactionsCountRequest.schema())
    spec.components.schema("GetStakingTransactionsCountResponse",GetStakingTransactionsCountResponse.schema())
    spec.path(path="/hmyv2_getStakingTransactionsCount", operations=make_path_operations("GetStakingTransactionsCountRequest", "GetStakingTransactionsCountResponse", tag="Blockchain", method_description=None, response_description="Number of staking transactions"))

    spec.components.schema("GetStakingTransactionsHistoryRequest",GetStakingTransactionsHistoryRequest.schema())
    spec.components.schema("GetStakingTransactionsHistoryResponse",GetStakingTransactionsHistoryResponse.schema())
    spec.components.schema("GetStakingTransactionsHistoryTxTypeResponse", GetStakingTransactionsHistoryTxTypeResponse.schema())
    spec.path(path="/hmyv2_getStakingTransactionsHistory", operations=make_path_operations("GetStakingTransactionsHistoryRequest", ("GetStakingTransactionsHistoryResponse", "GetStakingTransactionsHistoryTxTypeResponse"), tag="Blockchain", method_description=None, response_description="If txType was False, only the hashes will be provided as opposed to the whole transaction."))

    spec.components.schema("GetTransactionsCountRequest",GetTransactionsCountRequest.schema())
    spec.components.schema("GetTransactionsCountResponse",GetTransactionsCountResponse.schema())
    spec.path(path="/hmyv2_getTransactionsCount", operations=make_path_operations("GetTransactionsCountRequest", "GetTransactionsCountResponse", tag="Blockchain", method_description=None, response_description="Number of transactions"))

    spec.components.schema("GetTransactionsHistoryRequest",GetTransactionsHistoryRequest.schema())
    spec.components.schema("GetTransactionsHistoryResponse",GetTransactionsHistoryResponse.schema())
    spec.components.schema("GetTransactionsHistoryTxTypeResponse", GetTransactionsHistoryTxTypeResponse.schema())
    spec.path(path="/hmyv2_getTransactionsHistory", operations=make_path_operations("GetTransactionsHistoryRequest", ("GetTransactionsHistoryResponse", "GetTransactionsHistoryTxTypeResponse"), tag="Blockchain", method_description=None, response_description="If txType was False, only the hashes will be provided as opposed to the whole transaction."))

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

