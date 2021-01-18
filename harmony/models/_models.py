from enum import Enum

from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

from pydantic import BaseModel, Field

class BaseRequest(BaseModel):
    jsonrpc : Optional[str] = Field("2.0", description="The JSON-RPC version.")
    id_ : Optional[int] = Field(1, description="The request id, useful for asynchronous requests.", alias="id")
    method : str = Field(..., description="The method to call out to.")
    params : Sequence[Any] = Field(..., description="The parameters for the method call.")

class BaseResponse(BaseModel):
    jsonrpc : str = Field(..., description="The JSON-RPC version.")
    id_ : Optional[int] = Field(None, description="The id of the request the response is in response to.", alias="id")
    result : Optional[Any] = Field(None, description="The result of the RPC call.")
    error : Optional[Any] = Field(None, description="The error of the RPC call.")


class EmptyRequest(BaseRequest):
    params : List[str] = Field(default_factory=list, description="An empty list with no parameters")

class SmartContractCall(BaseModel):
    to : str = Field(..., description="Smart contract address")
    from_ : Optional[str] = Field(None, description="Wallet address", alias="from")
    gas : Optional[int] = Field(None, description="Gas to execute the smart contract call")
    gasPrice : Optional[int] = Field(None, description="Gas price to execute smart contract call")
    value : Optional[int] = Field(None, description="Value sent with the smart contract call")
    data : Optional[str] = Field(None, description="Hash of smart contract method and parameters")

class CallParameters(BaseModel):
    smart_contract_call : SmartContractCall
    block_number : int = Field(..., description="Block number")

class CallRequest(BaseRequest):
    params : Tuple[SmartContractCall, int]
    method : str = "hmyv2_call"

class CallResponse(BaseResponse):
    result : Optional[str] = Field(None, description="Return value of the executed smart contract")

class EstimateGasRequest(BaseRequest):
    params : Tuple[SmartContractCall, int]
    method : str = "hmyv2_estimateGas"

class EstimateGasResponse(BaseResponse):
    result: Optional[str] = Field(None, description="Hex of estimated gas price of smart contract call")

class GetCodeParameters(BaseModel):
    address : str = Field(..., description="The address to get the code from")
    block : str = Field(..., description="Block to query for information. Usually latest, which specifies the most recent block.")
    callback : Optional[str] = Field(None, description="Optional callback, returns an error object as first parameter and the result as second.")

class GetCodeRequest(BaseRequest):
    params : Union[Tuple[str, str, str], Tuple[str, str]]
    method : str = "hmyv2_getCode"

class GetCodeResponse(BaseResponse):
    result : Optional[str] = Field(None, description="The data at given address address")

class GetStorageAtParameters(BaseModel):
    address : str = Field(..., description="Smart contract address")
    storage_location : str = Field(..., description="Hex representation of storage location")
    block_number : int = Field(..., description="Block number")

class GetStorageAtRequest(BaseRequest):
    params : Tuple[str, str, int]
    method : str = "hmyv2_getStorageAt"

class GetStorageAtResponse(BaseResponse):
    result : Optional[str] = Field(None, description="Data stored at the smart contract location")


#Staking
## Delegation

class AddressParameters(BaseModel):
    address : str = Field(..., description="Address")

class GetDelegationByDelegatorRequest(BaseRequest):
    params : Tuple[str, ]
    method : str = "hmyv2_getDelegationsByDelegator"

class Delegation(BaseModel):
    validator_address : str = Field(..., description="Validator wallet address", alias="validator-address")
    delegator_address : str = Field(..., description="Delegator wallet address", alias="delegator-address")
    amount : int = Field(..., description="Amount delegated in atto")
    reward : int = Field(..., description="Unclaimed rewards in atto")
    undelegations : List[Dict[str, Any]] = Field(..., description="List of pending undelegations")

class DelegationListResponse(BaseResponse):
    result : Optional[List[Delegation]] = Field(None, description="List of Delegation Objects")

class AddressBlockNumberParameters(BaseModel):
    address : str = Field(..., description="Delegator wallet address")
    block_number : int = Field(..., description="Block number")

class GetDelegationsByDelegatorByBlockNumberRequest(BaseRequest):
    params : Tuple[str, int]
    method : str = "hmyv2_getDelegationsByDelegatorByBlockNumber"


class GetDelegationsByValidatorRequest(BaseRequest):
    params : Tuple[str,]
    method : str = "hmyv2_getDelegationsByValidator"

## Validator

class GetAllValidatorAddressesRequest(EmptyRequest):
    method : str = "hmyv2_getAllValidatorAddresses"

class AddressListResponse(BaseResponse):
    result : Optional[List[str]] = Field(None, description="List of addresses")


class Key(BaseModel):
    bls_public_key : str = Field(..., description="BLS public key", alias="bls-public-key")
    group_percent : str = Field(..., description="Key voting power in shard", alias="group-percent")
    effective_stake : str = Field(..., description="Effective stake of key", alias="effective-stake")
    raw_stake : str = Field(..., description="Actual stake of key", alias="raw-stake")
    earning_account : str = Field(..., description="Validator wallet address", alias="earning-account")
    overall_percent : str = Field(..., description="Percent of effective stake", alias="overall-percent")
    shard_id : int = Field(..., description="Shard ID that key is on", alias="shard-id")

class BlsKey(BaseModel):
    key : Key = Field(..., description="Object")
    earned_reward : int = Field(..., description="Lifetime reward key has earned", alias="earned-reward")

class Metrics(BaseModel):
    by_bls_key : List[BlsKey] = Field(...,description="BLS key earning metrics for current epoch", alias="by-bls-key")

class Blocks(BaseModel):
    to_sign : int = Field(..., description="Number of blocks available to the validator to sign", alias="to-sign")
    signed : int = Field(..., description="Number of blocks the validator has signed")

class EpochAPR(BaseModel):
    epoch : int = Field(..., description="Epoch number")
    value : str = Field(..., description="Calculated APR for that epoch")

class Lifetime(BaseModel):
    reward_accumulated : int = Field(..., description="Lifetime reward accumulated by the validator", alias="reward-accumulated")
    blocks : Blocks = Field(..., description="Blocks Object") 
    apr : str = Field(..., description="Approximate Return Rate")
    epoch_apr : List[EpochAPR] = Field(..., description="List of APR per epoch", alias="epoch-apr")


class ValidatorInformation(BaseModel):
    bls_public_keys : List[str] = Field(..., description="List of public BLS keys associated with the validator wallet address", alias="bls-public-keys")
    last_epoch_in_committee : int = Field(..., description="Last epoch any key of the validator was elected", alias="last-epoch-in-committee")
    min_self_delegation : int = Field(..., description="Ammount that validator must delegate to self in Atto", alias="min-self-delegation")
    max_total_delegation : int = Field(..., description="Total amount that validator will accept delegation until in Atto", alias="max-total-delegation")
    rate : str = Field(...,description="Current commission rate")
    max_rate : str = Field(..., description="Max commission rate a validator can charge", alias="max-rate")
    max_change_rate : str = Field(..., description="Maximum amount the commission rate can increase in one epoch", alias="max-change-rate")
    update_height : int = Field(..., description="Last block validator editted their validator information", alias="update-height")
    name : str = Field(..., description="Validator name, displayed on the Staking Dashboard")
    identity : str = Field(..., description="Validator identity, must be unique")
    website : str = Field(..., description="Validator website, displayed on the Staking Dashboard")
    security_contract : str =Field(..., description="Method to contact the validator", alias="security-contract")
    details : str = Field(..., description="Validator details, displayed on the Staking Dashboard")
    creation_height : int = Field(..., description="Block in which the validator was created", alias="creation-height")
    address : str = Field(..., description="Validator wallet address")
    delegations : List[Delegation] = Field(..., description="List of Delegation Objects")
    metrics : Metrics = Field(..., description="BLS key earning metrics for current epoch")
    total_delegation : int = Field(..., description="Total amount delegated to validator", alias="total-delegation")
    currently_in_committee : bool = Field(..., description="If key is currently elected", alias="currently-in-committee")
    epos_status : str = Field(..., description="Currently elected, eligible to be elected next epoch, or not eligible to be elected next epoch", alias="epos-status")
    epos_winning_stake : str = Field(..., description="Total effective stake of the validator", alias="epos-winning-stake")
    booted_status : str = Field(..., description="Banned status", alias="booted-status")
    active_status : str = Field(..., description="Active or inactive", alias="active-status")
    lifetime : Lifetime = Field(..., description="Lifetime Object")


class GetAllValidatorInformationParameters(BaseModel):
    page_number : int = Field(..., description="Page to request (page size is 100), -1 for all validators")

class GetAllValidatorInformationRequest(BaseRequest):
    params : Tuple[int,]
    method : str = "hmyv2_getAllValidatorInformation"

class ValidatorInformationListResponse(BaseResponse):
    result : Optional[List[ValidatorInformation]] = Field(None, description="List of ValidatorInformation Objects")

class GetAllValidatorInformationByBlockNumberParameters(BaseModel):
    page_number : int = Field(..., description="Page number, -1 for all")
    block_number : int = Field(..., description="Block number")

class GetAllValidatorInformationByBlockNumberRequest(BaseRequest):
    params : Tuple[int, int]
    method : str = "hmyv2_getAllValidatorInformationByBlockNumber"

class GetElectedValidatorAddressesRequest(EmptyRequest):
    method : str = "hmyv2_getElectedValidatorAddresses"


class GetValidatorInformationRequest(BaseRequest):
    params : Tuple[str,]
    
class ValidatorInformationResponse(BaseResponse):
    result : Optional[ValidatorInformation] = Field(None, description="Validator Object")

#Network

class UtilityMetrics(BaseModel):
    AccumulatorSnapshot : int = Field(..., description="Total block reward given out in Atto")
    CurrentStakedPercentage : str = Field(..., description="Percent of circulationg supply staked")
    Deviation : str = Field(..., description="Change in percent of circulating supply staked")
    Adjustment : str = Field(..., description="Change in circulationg supply staked")

class GetCurrentUtilityMetricsRequest(EmptyRequest):
    method : str = "hmyv2_getCurrentUtilityMetrics"

class GetMedianRawStakeSnapshotRequest(EmptyRequest):
    method : str = "hmyv2_getMedianRawStakeSnapshot"

class GetCurrentUtilityMetricsResponse(BaseResponse):
    result : Optional[UtilityMetrics] = Field(None, description="UtilityMetrics Object")


class EposSlotWinners(BaseModel):
    slot_owner : str = Field(..., description="Wallet address of BLS key", alias="slot-owner")
    bls_public_key : str = Field(..., description="BLS public key", alias="bls-public-key")
    raw_stake : str = Field(..., description="Actual stake", alias="raw-stake")
    eposed_stake : str = Field(..., description="Effective stake", alias="eposed-stake")

class EposSlotCandidates(BaseModel):
    stake : int = Field(..., description="Actual stake in Atto")
    keys_at_auction : List[str] = Field(..., description="List of BLS public keys", alias="keys-at-auction")
    percentage_of_total_auction_stake : str = Field(..., description="Percent of total network stake", alias="percentage-of-total-auction-stake")
    stake_per_key : int = Field(..., description="Stake per BLS key in Atto", alias="stake-per-key")
    validator : str = Field(..., description="Wallet address of validator")

class MedianRawStakeSnapshot(BaseModel):
    epos_median_stake : str = Field(..., description="Effective median stake", alias="epos-median-stake")
    max_eternal_slots : int = Field(..., description="Number of available committee slots", alias="max-eternal-slots")
    epos_slot_winners : List[EposSlotWinners] = Field(..., description="Details for each slot winner", alias="epos-slot-winners")
    epos_slot_candidates : List[EposSlotCandidates] = Field(..., description="Details for each candidates", alias="epos-slot-candidates")

class GetMedianRawStakeSnapshotResponse(BaseResponse):
    result : Optional[MedianRawStakeSnapshot] = Field(None, description="MedianRawStakeSnapshot Object")

class GetStakingNetworkInfoRequest(EmptyRequest):
    method : str = "hmyv2_getStakingNetworkInfoRequest"

class StakingNetworkInfo(BaseModel):
    total_supply : str = Field(..., description="Total number of pre-mined tokens", alias="total-supply")
    circulating_supply : str = Field(..., description="Number of token available in the network", alias="circulating-supply")
    epoch_last_block : int = Field(..., description="Last block of epoch", alias="epoch-last-block")
    total_staking : int = Field(..., description="Total amount staked in Atto", alias="total-staking")
    median_raw_stake : str = Field(..., description="Effective median stake in Atto", alias="median-raw-stake")

class GetStakingNetworkInfoResponse(BaseResponse):
    result : Optional[StakingNetworkInfo] = Field(None, description="StakingNetworkInfo Object")

class CommitteeMember(BaseModel):
    is_harmony_slot : bool = Field(..., description="If slot is Harmony owned", alias="is-harmony-slot")
    earning_account : str = Field(..., description="Wallet address that rewards are being paid to", alias="earning-account")
    bls_public_key : str = Field(..., description="BLS public key", alias="bls-public-key")
    voting_power_unnormalized : str = Field(..., description="Voting power of key", alias="voting-power-unnormalized")
    voting_power_percent : str = Field(..., description="Normalized voting power of key", alias="voting-power-\\%")

class CommitteeShard(BaseModel):
    policy : str = Field(..., description="Current election policy")
    count : int = Field(..., description="Number of BLS keys on shard")
    external_validator_slot_count : int = Field(..., description="Number of external BLS keys in committee", alias="external-validator-slot-count")
    committee_members: List[CommitteeMember] = Field(..., description="List of Committee Member Objects", alias="committee-members")

class ElectedCommittee(BaseModel):
    quorum_deciders : Dict[str, CommitteeShard] = Field(..., description="Shard of committee", alias="quorum-deciders")

class SuperCommittees(BaseModel):
    previous : ElectedCommittee = Field(..., description="Previously elected committee")
    current : ElectedCommittee = Field(..., description="Currently elected committee, same schema as previous")

class GetSuperCommitteesRequest(EmptyRequest):
    method : str = "hmyv2_getSuperCommittess"

class GetSuperCommitteesResponse(BaseResponse):
    result : Optional[SuperCommittees] = Field(None, description="SuperCommittees Object")

#Transaction
## Cross Shard

class HashParameters(BaseModel):
    hash_ : str = Field(..., description="hash value", alias="hash")

class GetCXReceiptByHashRequest(BaseRequest):
    params : Tuple[str, ]
    method : str = "hmyv2_getCXReceiptByHash"

class CXReceipt(BaseModel):
    blockHash : str = Field(..., description="Block hash")
    blockNumber : int = Field(..., description="Block number")
    hash_ : str = Field(..., description="Transaction hash", alias="hash")
    from_ : str = Field(..., description="Sender wallet address", alias="from")
    to : str = Field(..., description="Receiver wallet address")
    shardID : int = Field(..., description="From shard")
    toShardID : int = Field(..., description="To shard")
    value : int = Field(..., description="Ammount transferred in Atto")


class GetCXReceiptByHashResponse(BaseResponse):
    result : Optional[CXReceipt] = Field(None, description="CXReceipt Object")


class GetPendingCXReceiptsRequest(EmptyRequest):
    method : str = "hmyv2_getPendingCXReceipts"

class Receipt(BaseModel):
    txHash : str = Field(..., description="Transaction hash")
    from_ : str = Field(..., description="Sender wallet address", alias="from")
    to : str = Field(..., description="Receiver wallet address")
    shardID : int = Field(..., description="From shard")
    toShardID : int = Field(..., description="To shard")
    amount : int = Field(..., description="Amount transferred in Atto")

class MerkleProof(BaseModel):
    blockNumber : int = Field(..., description="Block number")
    blockHash : str = Field(..., description="Block hash")
    shardID : int = Field(..., description="Shard ID of orginiating block")
    receiptHash : str = Field(..., description="Transaction receipt hash")
    shardIDs : List[int] = Field(..., description="To shard")
    shardHashed : List[str] = Field(..., description="Missing desc")

class BlockHeader(BaseModel):
    shard_id : int = Field(..., description="Shard ID", alias="shard-id")
    block_header_hash : str = Field(..., description="Block header hash", alias="block-header-hash")
    block_number : int = Field(..., description="Block number", alias="block-number")
    view_id : int = Field(..., description="View ID", alias="view-id")
    epoch : int = Field(..., description="Epoch number")

class PendingCXReceipt(BaseModel):
    receipts : List[Receipt]
    merkleProof : MerkleProof
    header : BlockHeader
    commitSig : str = Field(..., description="Hex representation of aggregated signature")
    commitBitMap : str = Field(..., description="Hex representation of aggregated signature bitmap")

class GetPendingCXReceiptsResponse(BaseResponse):
    result : Optional[List[PendingCXReceipt]] = Field(None, description="List of PendingCXReceipt object")

class ResendCXRequest(BaseRequest):
    params : Tuple[str,]
    method : str = "hmyv2_resendCx"

class ResendCXResponse(BaseResponse):
    result : Optional[bool] = Field(None, description="If cross shard receipt was successfully resent or not")

## Transaction Pool


class PoolStats(BaseModel):
    executable_count : str = Field(..., description="Staking transaction hash", alias="executable-count")
    non_executable_count : str = Field(..., description="Type of staking transaction", alias="non-executable-count")

class GetPoolStatsRequest(EmptyRequest):
    method : str = "hmyv2_getPoolStats"

class GetPoolStatsResponse(BaseResponse):
    result : Optional[PoolStats] = Field(None, description="PoolStats Object")

class PendingStakingTransactionsRequest(EmptyRequest):
    method : str = "hmyv2_getPendingStakingTransactions"

class StakingTransaction(BaseModel):
    blockHash : str = Field(..., description="Block hash in which transaction was finalized")
    blockNumber : int = Field(..., description="Block number in which transaction was finalized")
    from_ : str = Field(..., description="Sender wallet address", alias="from")
    timestamp : int = Field(..., description="Unix time at which transaction was finalized")
    gas : int = Field(..., description="Gas limit of transaction")
    gasPrice : int = Field(..., description="Gas price of transaction in Atto")
    nonce : int = Field(..., description="Wallet nonce of transaction")
    transactionIndex : int = Field(..., description="Staking transaction index within block")
    type_ : str = Field(..., description="Type of staking transaction", alias="type")
    msg : Dict[str, Any] = Field(..., description="Staking transaction data, depending on the type of staking transaction")


class StakingTransactionListResponse(BaseResponse):
    result : Optional[List[StakingTransaction]] = Field(None, description="List of staking transactions")


class PendingTransactionsRequest(EmptyRequest):
    method : str = "hmyv2_pendingTransactions"

class Transaction(BaseModel):
    blockHash : str = Field(..., description="Block hash")
    blockNumber : int = Field(..., description="Block number")
    from_ : str = Field(..., description="Sender wallet address", alias="from")
    timestamp : int = Field(..., description="Unix time at which transaction was finalized")
    gas : int = Field(..., description="Gas limit of transaction")
    gasPrice : int = Field(..., description="Gas price of transaction in Atto")
    hash_ : str = Field(..., description="Transaction hash", alias="hash")
    input_ : str = Field(..., description="Transaction data, used for smart contracts", alias="input")
    nonce : int = Field(..., description="Sender wallet nonce of transaction")
    to : str = Field(..., description="Receiver wallet address")
    transactionIndex : int = Field(..., description="transaction index within block")
    value : int = Field(..., description="Amount transferred")
    shardID : int = Field(..., description="From shard")
    toShardID : int = Field(..., description="To shard")

class TransactionListResponse(BaseResponse):
    result : Optional[List[Transaction]] = Field(None, description="List of transactions")

## Staking

class GetCurrentStakingErrorSinkRequest(EmptyRequest):
    method : str = "hmyv2_getCurrentStakingErrorSink"

class StakingError(BaseModel):
    tx_hash_id : str = Field(..., description="Staking transaction hash", alias="tx-hash-id")
    directive_kind : str = Field(..., description="Type of staking transaction", alias="directive-kind")
    time_at_rejection : int = Field(..., description="Unix time when the staking transaction was rejected from the pool", alias="time-at-rejection")
    error_message : str = Field(..., description="Reason for staking transaction rejection", alias="error-message")

class GetCurrentStakingErrorSinkResponse(BaseResponse):
    result : Optional[List[StakingError]] = Field(None, description="List of StakingError objects")

class BlockNumberAndIndexParameters(BaseModel):
    block_number : int = Field(..., description="Block number")
    index : int = Field(..., description="index value")
    
class GetStakingTransactionByBlockNumberAndIndexRequest(BaseRequest):
    params : Tuple[int, int]
    method : str = "hmyv2_getStakingTransactionByBlockNumberAndIndex"

class StakingTransactionResponse(BaseResponse):
    result : Optional[StakingTransaction] = Field(None, description="StakingTransaction Object")
    
class HashAndIndexParameters(BaseModel):
    hash_ : str = Field(..., description="hash value", alias="hash")
    index : int = Field(..., description="index value")

class GetStakingTransactionByBlockHashAndIndexRequest(BaseRequest):
    params : Tuple[str, int]
    method : str = "hmyv2_getStakingTransactionByBlockHashAndIndex"

class GetStakingTransactionByHashRequest(BaseRequest):
    params : Tuple[str, ]
    method : str = "hmyv2_getStakingTransactionByHash"

class RawTransactionParameters(BaseModel):
    transaction_hex : str = Field(..., description="Hex representation of signed transaction", alias="transaction_hex")
    
class SendRawStakingTransactionRequest(BaseRequest):
    params : Tuple[str, ]
    method : str = "hmyv2_sendRawStakingTransaction"

class SendRawStakingTransactionResponse(BaseResponse):
    result : Optional[str] = Field(None, description="Staking transaction hash if it was successfully added, else an erro")

##Transfer

class GetCurrentTransactionErrorSinkRequest(EmptyRequest):
    method : str = "hmyv2_getCurrentTransactionErrorSinkRequest"

class TransactionError(BaseModel):
    tx_hash_id : str = Field(..., description="Transaction hash", alias="tx-hash-id")
    time_at_rejection : int = Field(..., description="Unix time when the transaction was rejected from the pool", alias="time-at-rejection")
    error_message : str = Field(..., description="Reason for  transaction rejection", alias="error-message")

class GetCurrentTransactionErrorSinkResponse(BaseResponse):
    result : Optional[List[TransactionError]] = Field(None, description="Object")


class GetTransactionByBlockHashAndIndexRequest(BaseRequest):
    params : Tuple[str, int]
    method : str = "hmyv2_getTransactionByBlockHashAndIndex"


class TransactionResponse(BaseResponse):
    result : Optional[Transaction] = Field(None, description="Transaction Object")


class GetTransactionByBlockNumberAndIndexRequest(BaseRequest):
    params : Tuple[int, int]
    method : str = "hmyv2_getTransactionByBlockNumberAndIndex"

class GetTransactionByHashRequest(BaseRequest):
    params : Tuple[str, ]
    method : str = "hmyv2_getTransactionByHash"

class GetTransactionReceiptParameters(BaseModel):
    receipt : str = Field(..., description="Transaction receipt")

class GetTransactionReceiptRequest(BaseRequest):
    params : Tuple[str, ]
    method : str = "hmyv2_getTransactionReceipt"

class TransactionReceipt(BaseModel):
    blockHash : str = Field(..., description="Block hash")
    blockNumber : int = Field(..., description="Block number")
    contractAddress : str = Field(..., description="Smart contract address")
    culmulativeGasUsed : int = Field(..., description="Gas used for transaction")
    from_ : str = Field(..., description="Sender wallet address", alias="from")
    gasUsed : int = Field(..., description="Gas used for the transaction")
    logs : List[Any] = Field(..., description="Array")
    logsBloom : str = Field(..., description="Bloom logs")
    shardID : int = Field(..., description="Shard ID")
    status : int = Field(..., description="Status of transaction (0: pending, 1: success)")
    to : str = Field(..., description="Receiver wallet address")
    transactionHash : str = Field(..., description="Transaction hash")
    transactionIndex : str = Field(..., description="Transaction index within block")

class GetTransactionReceiptResponse(BaseResponse):
    result : Optional[TransactionReceipt] = Field(None, description="Object")

class SendRawTransactionRequest(BaseRequest):
    params : Tuple[str, ]
    method : str = "hmyv2_sendRawTransaction"

class SendRawTransactionResponse(BaseResponse):
    result : Optional[str] = Field(None, description="Transaction hash")

#Blockchain
## Network

class BlockNumberRequest(EmptyRequest):
    method : str = "hmyv2_blockNumber"

class BlockNumberResponse(BaseResponse):
    result : Optional[int] = Field(None, description="Current block number")

class GetCirculatingSupplyRequest(EmptyRequest):
    method : str = "hmyv2_getCirculatingSupply"

class GetCirculatingSupplyResponse(BaseResponse):
    result : Optional[int] = Field(None, description="Circulation supply of tokens in ONE")

class GetEpochRequest(EmptyRequest):
    method : str = "hmyv2_getEpoch"

class GetEpochResponse(BaseResponse):
    result : Optional[int] = Field(None, description="Current block number")

class CrossLink(BaseModel):
    hash_ : str = Field(..., description="Parent block hash", alias="hash")
    block_number : int = Field(..., description="Block number", alias="block-number")
    view_id : int = Field(..., description="View ID", alias="view-id")
    signature : str = Field(..., description="Hex representation of aggregated signature")
    signature_bitmap : str = Field(..., description="Hex representation of aggregated signature bitmap", alias="signature-bitmap")
    shard_id : int = Field(..., description="Shard ID", alias="shard-id")
    epoch_number : int = Field(..., description="Block epoch", alias="epoch-number")

class GetLastCrossLinksRequest(EmptyRequest):
    method : str = "hmyv2_getLastCrossLinks"

class GetLastCrossLinksResponse(BaseResponse):
    result : Optional[List[CrossLink]] = Field(None, description="List of CrossLink objects")

class GetLeaderRequest(EmptyRequest):
    method : str = "hmyv2_getLeader"

class GetLeaderResponse(BaseResponse):
    result : Optional[str] = Field(None, description="Wallet address of current leader")

class GasPriceRequest(EmptyRequest):
    method : str = "hmyv2_gasPrice"

class GasPriceResponse(BaseResponse):
    result : Optional[int] = Field(None, description="Current average gas price of transactions")


class ShardingStructure(BaseModel):
    current : bool = Field(..., description="If this node is currently on this shard ID")
    http : str = Field(..., description="HTTPS API endpoint for this shard ID")
    shardID : int = Field(..., description="Shard ID")
    ws : str = Field(..., description="Websocket API endpoint for this shard ID")

class GetShardingStructureRequest(EmptyRequest):
    method : str = "hmyv2_getShardingStructure"

class GetShardingStructureResponse(BaseResponse):
    result : Optional[List[ShardingStructure]] = Field(None, description="List of ShardingStructure Object")

class GetTotalSupplyRequest(EmptyRequest):
    method : str = "hmyv2_getTotalSupply"

class GetTotalSupplyResponse(BaseResponse):
    result : Optional[int] = Field(None, description="Total number of pre-mined tokens")

class EphochNumberParameters(BaseModel):
    epoch_number : Optional[int] = Field(None, description="Epoch number")
    

class GetValidatorsRequest(BaseRequest):
    params : Tuple[int, ]
    method : str = "hmyv2_getValidators"

class ValidatorAddress(BaseModel):
    address : str = Field(..., description="Wallet address")
    balance : int = Field(..., description="Balance of wallet")

class ValidatorIDs(BaseModel):
    shardID : int = Field(..., description="Shard ID")
    validators : List[ValidatorAddress] = Field(..., description="Array of Validator Address objects")

class GetValidatorsResponse(BaseResponse):
    result : Optional[ValidatorIDs] = Field(None, description="ValidatorIDs Object")

class GetValidatorKeysRequest(BaseRequest):
    params : Tuple[int,]
    method : str = "hmyv2_getValidatorKeys"

class BLSKeyListResponse(BaseResponse):
    result : Optional[List[str]] = Field(None, description="List of public BLS keys in the elected committee")
    

## Node

class GetCurrentBadBlocksRequest(EmptyRequest):
    method : str = "hmyv2_getCurrentBadBlocks"

class GetCurrentBadBlocksResponse(BaseResponse):
    result : Optional[List[str]] = Field(None, description="List of bad blocks in node memory. Note: know issue with RPC not returning correctly")

class ChainConfig(BaseModel):
    chain_id : int = Field(..., description="Chain ID for the network", alias="chain-id")
    cross_tx_epoch : int = Field(..., description="Epoch at which cross shard transactions were enabled", alias="cross-tx-epoch")
    cross_link_epoch : int = Field(..., description="Epoch at which cross links were enabled", alias="cross-link-epoch")
    staking_epoch : int = Field(..., description="Epoch at which staking was enabled", alias="staking-epoch")
    prestaking_epoch : int = Field(..., description="Epoch at which pre-staking began", alias="prestaking-epoch")
    quick_unlock_epoch : int = Field(..., description="Epoch at which undelegations unlocked in one epoch", alias="quick-unlock-epoch")
    eip155_epoch : int = Field(..., description="Epoch at which EIP155 was enabled", alias="eip155-epoch")
    s3_epoch : int = Field(..., description="Epoch at which Mainnet V0 was launched", alias="s3-epoch")
    receipt_log_epoch : int = Field(..., description="Epoch at which receipt logs were enabled", alias="receipt-log-epoch")

class P2PConnectivity(BaseModel):
    total_known_peers : int = Field(..., description="Number of known peers", alias="total-known-peers")
    connected : int = Field(..., description="Number of connected peers")
    not_connected : int = Field(..., description="Number of known peers not connected", alias="not-connected")

class NodeMetadata(BaseModel):
    blskey : List[str] = Field(..., description="List of BLS keys on the node")
    version : str = Field(..., description="Harmony binary version")
    network : str = Field(..., description="Network name that the node is on (Mainnet ir Testnet)")
    chain_config : ChainConfig = Field(..., description="ChainConfig Object", alias="chain-config")
    is_leader : bool = Field(..., description="Whether the node is currently leader or not", alias="is-leader")
    shard_id : int = Field(..., description="Shard that the node is on", alias="shard-id")
    current_epoch : int = Field(..., description="Current epoch", alias="current-epoch")
    blocks_per_epoch : int = Field(..., description="Number of blacks per epoch (only available on Shard 0)", alias="blocks-per-epoch")
    role : str = Field(..., description="Node type (Validator or ExplorerNode)")
    dns_zone : str = Field(..., description="Name of DNS zone", alias="dns-zone")
    is_archival : bool = Field(..., description="Whether the node is currently in state pruning mode or not", alias="is-archival")
    node_unix_start_time : int = Field(..., description="Start time of node in Unix time", alias="node-unix-start-time")
    p2p_connectivity : P2PConnectivity = Field(..., description="P2PConnectivity Object", alias="p2p-connectivity")

class GetNodeMetadataRequest(EmptyRequest):
    method : str = "hmyv2_getNodeMetadata"

class GetNodeMetadataResponse(BaseResponse):
    result : Optional[NodeMetadata] = Field(None, description="Node Metadata Object")

class ProtocolVersionRequest(EmptyRequest):
    method : str = "hmyv2_protocolVersion"

class ProtocolVersionResponse(BaseResponse):
    result : Optional[int] = Field(None, description="Protocol version")


class PeerCountRequest(EmptyRequest):
    method : str = "net_peerCount"

class PeerCountResponse(BaseResponse):
    result : Optional[str] = Field(None, description="Number of peers respresented as a Hex string")

## Blocks

class BlocksListConfig(BaseModel):
    withSigners : bool = Field(..., description="Include block signer wallet addresses")
    fullTx : bool = Field(..., description="Include full transaction data")
    inclStaking : bool = Field(..., description="Include full staking transactions")

class BlockListParams(BaseModel):
    start_block : int = Field(..., description="Start block")
    end_block : int = Field(..., description="End block")
    blocks_config : BlocksListConfig = Field(..., description="BlocksListConfig Object")

class GetBlocksRequest(BaseRequest):
    params : Tuple[int, int, BlocksListConfig]
    method : str = "hmyv2_getBlocks"

class Block(BaseModel):
    difficulty : int = Field(..., description="Unused, legacy from Eth")
    epoch : int = Field(..., description="Epoch number of block")
    extraData : str = Field(..., description="Hex representation of extra data in the block")
    gasLimit : int = Field(..., description="Maximum gas that can be used for transactions in the block")
    gasUsed : int = Field(..., description="Amount of gas used for transactions in the block")
    hash_ : str = Field(..., description="Block hash", alias="hash")
    logsBloom : str = Field(..., description="Bloom logs")
    miner : str = Field(..., description="Wallet address of the leader that proposed this block")
    mixHash : str = Field(..., description="Unused, legacy from Eth")
    nonce : int = Field(..., description="Unused, legacy from Eth")
    number : int = Field(..., description="Block number")
    parentHash : str = Field(..., description="Hash of parent block")
    receiptsRoot : str = Field(..., description="Hash of transaction receipt root")
    size : int = Field(..., description="Block size in bytes")
    stakingTransactions : List[Dict[str, Any]] = Field(..., description="List of staking transactions finalized in this block")
    stateRoot : str = Field(..., description="Hash of state root")
    timestamp : int = Field(..., description="Unix timestamp of the block")
    transactions : List[Dict[str, Any]] = Field(..., description="List of transactions finalized in this block")
    transactionsRoot : str = Field(..., description="Hash of transactios root")
    uncles : List[Dict[str, Any]] = Field(..., description="Unused, legacy from Eth")
    viewID : int = Field(..., description="View ID")


class BlockListResponse(BaseResponse):
    result : Optional[List[Block]] = Field(None, description="List of blocks")
    
class BlockConfig(BaseModel):
    fullTx : bool = Field(..., description="Include full transaction data")
    inclTx : bool = Field(..., description="Include regular transactions")
    inclStaking : bool = Field(..., description="Include full staking transactions")

class GetBlockByNumberParameters(BaseModel):
    block_number : int = Field(..., description="Block number")
    block_config : BlockConfig = Field(..., description="BlockConfig Object")

class GetBlockByNumberRequest(BaseRequest):
    params : Tuple[int, BlockConfig]
    method : str = "hmyv2_getBlockByNumber"

class BlockResponse(BaseResponse):
    result : Optional[Block] = Field(None, description="Block Object")

class GetBlockByHashParameters(BaseModel):
    hash_ : str = Field(..., description="Block hash", alias="hash")
    block_config : BlockConfig = Field(..., description="BlockConfig Object")

class GetBlockByHashRequest(BaseRequest):
    params : Tuple[str, BlockConfig]
    method : str = "hmyv2_getBlockByHash"

class GetBlockSignersRequest(BaseRequest):
    params : Tuple[int, int, BlocksListConfig]
    method : str = "hmyv2_getBlockSigners"

class BlockNumberParameters(BaseModel):
    block_number : int = Field(..., description="Block number")

class GetBlockSignersKeysRequest(BaseRequest):
    params : Tuple[int,]
    method : str = "hmyv2_getBlockSignersKeys"

class GetBlockSignersKeysResponse(BaseResponse):
    result : Optional[List[str]] = Field(None, description="List of block signer public BLS keys")

class GetBlockTransactionCountByNumberRequest(BaseRequest):
    params : Tuple[int,]
    method : str = "hmyv2_getBlockTransactionCountByNumber"

class TransactionCountResponse(BaseResponse):
    result : Optional[int] = Field(None, description="Number of transactions")


class GetBlockTransactionCountByHashRequest(BaseRequest):
    params : Tuple[str,]
    method : str = "hmyv2_getBlockTransactionCountByHash"


class GetHeaderByNumberRequest(BaseRequest):
    params : Tuple[int,]
    method : str = "hmyv2_getHeaderByNumber"

class Header(BaseModel):
    blockHash : str = Field(..., description="Block hash")
    blockNumber : int = Field(..., description="Block number")
    shardID : int = Field(..., description="Shard ID")
    leader : str = Field(..., description="Wallet address of leader that proposed this block if prestaking, otherwise sha256 hash of leader's public bls key")
    viewID : int = Field(..., description="View ID of the block")
    epoch : int = Field(..., description="Epoch of the block")
    timestamp : int = Field(..., description="Timestamp that the block was finalized")
    unixtime : int = Field(..., description="Timestamp that the block was finalized in Unix time")
    lastCommitSig : str = Field(..., description="Hex representation of aggregated signatures of the previous block")
    lastCommitBitmap : str = Field(..., description="Hex representation of the aggregated signature bitmap of the previous block")

class HeaderResponse(BaseResponse):
    result : Optional[Header] = Field(None, description="header response")

class ChainHeader(BaseModel):
    shard_id : int = Field(..., description="Shard ID", alias="shard-id")
    block_header_hash : str = Field(..., description="Block header hash", alias="block-header-hash")
    block_number : int = Field(..., description="Block number", alias="block-number")
    view_id : int = Field(..., description="View ID", alias="view-id")
    epoch : int = Field(..., description="Epoch number")

class GetLatestChainHeadersRequest(EmptyRequest):
    method : str = "hmyv2_getLatestChainHeaders"

class LatestChainHeaders(BaseModel):
    beacon_chain_header : ChainHeader = Field(..., description="ChainHeader Object", alias="beacon-chain-header")
    shard_chain_header : ChainHeader = Field(..., description="ChainHeader Object", alias="shard-chain-header")

class GetLatestChainHeadersResponse(BaseResponse):
    result : Optional[LatestChainHeaders] = Field(None, description="LatestChainHeaders Object")

class LatestHeaderRequest(EmptyRequest):
    method : str = "hmyv2_latestHeader"

#Account

class GetBalanceRequest(BaseRequest):
    params : Tuple[str,]
    method : str = "hmyv2_getBalance"

class BalanceResponse(BaseResponse):
    result : Optional[int] = Field(None, description="Wallet balance at given block in Atto")

class GetBalanceByBlockNumberRequest(BaseRequest):
    params : Tuple[str, int]
    method : str = "hmyv2_getBalanceByBlockNumber"

class TransactionType(str, Enum):
    sent = "SENT"
    received = "RECEIVED"
    all_ = "ALL"

class TransactionsCountParameters(BaseModel):
    address : str = Field(..., description="Wallet address")
    transaction_type : TransactionType = Field(..., description="Type of staking transaction (SENT, RECEIVED, ALL)")

class GetStakingTransactionsCountRequest(BaseRequest):
    params : Tuple[str, str]
    method : str = "hmyv2_getStakingTransactionsCount"


class SortOrder(str, Enum):
    asc = "ASC"
    desc = "DESC"

class TransactionsHistoryObject(BaseModel):
    address : str = Field(..., description="Wallet address")
    pageIndex : Optional[int] = Field(0, description="Optional, which page ofo transactions to return, default 0")
    pageSize : Optional[int] = Field(1000, description="Optional, how many transactions to display per page, default 1000")
    fullTx : Optional[bool] = Field(False, description="Optional, return full transaction data or just transaction hashes, default false")
    txType : Optional[TransactionType] = Field("ALL", description="Optional, which type of transactions to display ('ALL','RECEIVED', or 'SENT'), default 'ALL'")
    order : Optional[SortOrder] = Field("ASC", description="Optional, sort transactions in ascending or descending order based on timestamp ('ASC' or 'DESC'), default 'ASC'")

class TransactionsHistoryParameters(BaseModel):
    obj : TransactionsHistoryObject

class TransactionsHashListResponse(BaseResponse):
    result : Optional[List[str]] = Field(None, description="List of transaction hashes")

class GetStakingTransactionsHistoryRequest(BaseRequest):
    params : Tuple[TransactionsHistoryObject, ]
    method : str = "hmyv2_getStakingTransactionsHistory"
    
    
class GetTransactionsCountRequest(BaseRequest):
    params : Tuple[str, str]
    method : str = "hmyv2_getTransactionsCount"

class GetTransactionsHistoryRequest(BaseRequest):
    params : Tuple[TransactionsHistoryObject,]
    method : str = "hmyv2_getTransactionsHistory"
