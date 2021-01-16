from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

class SmartContractCall(BaseModel):
    to : str = Field(..., description="Smart contract address")
    from_ : Optional[str] = Field(None, description="Wallet address", alias="from")
    gas : Optional[int] = Field(None, description="Gas to execute the smart contract call")
    gasPrice : Optional[int] = Field(None, description="Gas price to execute smart contract call")
    value : Optional[int] = Field(None, description="Value sent with the smart contract call")
    data : Optional[str] = Field(None, description="Hash of smart contract method and parameters")

class CallParameters(BaseModel):
    smart_contract_call : SmartContractCall
    block_number : int

class CallResults(BaseModel):
    result : str = Field(..., description="Return value of the executed smart contract")

class EstimateGasResults(BaseModel):
    result: str = Field(..., description="Hex of estimated gas price of smart contract call")

class GetCodeParameters(BaseModel):
    address : str = Field(..., description="The address to get the code from")
    block : str = Field(..., description="Block to query for information. Usually latest, which specifies the most recent block.")
    callback : Optional[str] = Field(None, description="Optional callback, returns an error object as first parameter and the result as second.")

class GetCodeResults(BaseModel):
    result : str = Field(..., description="The data at given address address")

class GetStorageAtParameters(BaseModel):
    address : str = Field(..., description="Smart contract address")
    storage_location : str = Field(..., description="Hex representation of storage location")
    block_number : int = Field(..., description="Block number")

class GetStorageAtResults(BaseModel):
    result : str = Field(..., description="Data stored at the smart contract location")


#Staking
## Delegation

class GetDelegationsByDelegatorParameters(BaseModel):
    address : str = Field(..., description="Delegator address")

class DelegationsByDelegator(BaseModel):
    validator_address : str = Field(..., description="Validator wallet address")
    delegator_address : str = Field(..., description="Delegator wallet address")
    amount : int = Field(..., description="Amount delegated in atto")
    reward : int = Field(..., description="Unclaimed rewards in atto")
    undelegations : List[Dict[str, Any]] = Field(..., description="List of pending undelegations")

class GetDelegationsByDelegatorResult(BaseModel):
    result : List[DelegationsByDelegator]

class GetDelegationsByDelegatorByBlockNumberParameters(BaseModel):
    address : str = Field(..., description="Delegator wallet address")
    block_number : int = Field(..., description="Block number")

class GetDelegationsByDelegatorByBlockNumberResults(BaseModel):
    result : List[DelegationsByDelegator]

class GetDelegationsByValidatorParameters(BaseModel):
    address : str = Field(..., description="Validator wallet address")

class GetDelegationsByValidatorResults(BaseModel):
    result : List[DelegationsByDelegator]

## Validator

class GetAllValidatorInformationParameters(BaseModel):
    page_request : int = Field(..., description="Page to request (page size is 100), -1 for all validators")

class GetAllValidatorInformationResults(BaseModel):
    result : List[Validator] = Field(..., description="Array of Object")

class GetAllValidatorInformationByBlockNumberParameters(BaseModel):
    page_number : int = Field(..., description="Page number, -1 for all")
    block_number : int = Field(..., description="Block number")

class GetAllValidatorInformationByBlockNumberResults(BaseModel):
    result : List[Validator] = Field(..., description="Array of Object") 

class GetElectedValidatorAddressesParameters(BaseModel):
    #empty set

class GetElectedValidatorAddressesResults(BaseModel):
    result : List[str] = Field(..., description="List of wallet addresses that are currently elected")


#start all of the classes needed for Validator class#
class Key(BaseModel):
    bls_public_key : str = Field(..., description="BLS public key")
    group_percent : str = Field(..., description="Key voting power in shard")
    effective_stake : str = Field(..., description="Effective stake of key")
    raw_stake : str = Field(..., description="Actual stake of key")
    earning_account : str = Field(..., description="Validator wallet address")
    overall_percent : str = Field(..., description="Percent of effective stake")
    shard_id : int = Field(..., description="Shard ID that key is on")

class Bls_key(BaseModel):
    key : Key = Field(..., description="Object")
    earned_reward : int = Field(..., description="Lifetime reward key has earned")

class Metrics(BaseModel):
    by_bls_key : List[Bls_key] = Field(...,description="BLS key earning metrics for current epoch")

class Blocks(BaseModel):
    to_sign : int = Field(..., description="Number of blocks available to the validator to sign")
    signed : int = Field(..., description="Number of blocks the validator has signed")

class Epoch_apr(BaseModel):
    epoch : int = Field(..., description="Epoch number")
    value : str = Field(..., description="Calculated APR for that epoch")

class Lifetime(BaseModel):
    reward_accumulated : int = Field(..., description="Lifetime reward accumulated by the validator")
    blocks : Blocks = Field(..., description="Object") 
    apr : str = Field(..., description="Approximate Return Rate")
    epoch_apr : List[Epoch_apr] = Field(..., description="List of APR per epoch")

class Validator(BaseModel):
    bls_public_keys : List[str] = Field(..., description="List of public BLS keys associated with the validator wallet address")
    last_epoch_in_committee : int = Field(..., description="Last epoch any key of the validator was elected")
    min_self_delegation : int = Field(..., description="Ammount that validator must delegate to self in Atto")
    max_total_delegation : int = Field(..., description="Total amount that validator will accept delegation until in Atto")
    rate : str = Field(...,description="Current commission rate")
    max_rate : str = Field(..., description="Max commission rate a validator can charge")
    max_change_rate : str = Field(..., description="Maximum amount the commission rate can increase in one epoch")
    update_height : int = Field(..., description="Last block validator editted their validator information")
    name : str = Field(..., description="Validator name, displayed on the Staking Dashboard")
    identity : str = Field(..., description="Validator identity, must be unique")
    website : str = Field(..., description="Validator website, displayed on the Staking Dashboard")
    security_contract : str =Field(..., description="Method to contact the validator")
    details : str = Field(..., description="Validator details, displayed on the Staking Dashboard")
    creation_height : int = Field(..., description="Block in which the validator was created")
    address : str = Field(..., description="Validator wallet address")
    delegations : List[DelegationsByDelegator]
    metrics : Metrics = Field(..., description="BLS key earning metrics for current epoch")
    total_delegation : int = Field(..., description="Total amount delegated to validator")
    currently_in_committee : bool = Field(.., description="If key is currently elected")
    epos_status : str = Field(..., description="Currently elected, eligible to be elected next epoch, or not eligible to be elected next epoch")
    epos_winning_stake : str = Field(..., description="Total effective stake of the validator")
    booted_status : str = Field(..., description="Banned status")
    active_status : str = Field(..., description="Active or inactive")
    lifetime : Lifetime = Field(..., description="Object")

#end of Validator class


class GetValidatorInformationParameters(BaseModel):
    address: str = Field(..., description="Validator wallet address")

class GetValidatorInformationResults(BaseModel):
    result : Validator = Field(..., description="Object")


#Network

class GetCurrentUtilityMetricsParameters(BaseModel):
    #empty set

class GetCurrentUtilityMetrics(BaseModel):
    accumulatorsnapshot : int = Field(..., description="Total block reward given out in Atto")
    currentstakedpercentage : str = Field(..., description="Percent of circulationg supply staked")
    deviation : str = Field(..., description="Change in percent of circulating supply staked")
    adjustment : str = Field(..., description="Change in circulationg supply staked")

class GetCurrentUtilityMetricsResults(BaseModel):
    result : GetCurrentUtilityMetrics = Field(..., description="Object")

class GetMedianRawStakeSnapShotParameters(BaseModel):
    #empty set

class Epos_slot_winners(BaseModel):
    slot_owner : str = Field(..., description="Wallet address of BLS key")
    bls_public_key : str = Field(..., description="BLS public key")
    raw_stake : str = Field(..., description="Actual stake")
    eposed_stake : str = Field(..., description="Effective stake")

class Epos_slot_candidates(BaseModel):
    stake : int = Field(..., description="Actual stake in Atto")
    keys_at_auction : List[str] = Field(..., description="List of BLS public keys")
    percentage_of_total_auction_stake : str = Field(..., description="Percent of total network stake")
    stake_per_key : int = Field(..., description="Stake per BLS key in Atto")
    validator : str = Field(..., description="Wallet address of validator")

class GetMedianRawStakeSnapShot(BaseModel):
    epos_median_stake : str = Field(..., description="Effective median stake")
    max_eternal_slots : int = Field(..., description="Number of available committee slots")
    epos_slot_winners : List[Epos_slot_winners] = Field(..., description="Details for each slot winner")
    epos_slot_candidates : List[Epos_slot_candidates] = Field(..., description="Details for each candidates")

class GetMedianRawStakeSnapShotResults(BaseModel):
    result : GetMedianRawStakeSnapShot = Field(..., description="Object")

class GetStakingNetworkInfoParameters(BaseModel):
    #empty set

class GetStakingNetworkInfo(BaseModel):
    total_supply : str = Field(..., description="Total number of pre-mined tokens")
    circulating_supply : str = Field(..., description="Number of token available in the network")
    epoch_last_block : int = Field(..., description="Last block of epoch")
    total_staking : int = Field(..., description="Total amount staked in Atto")
    median_raw_stake : str = Field(..., description="Effective median stake in Atto")

class GetStakingNetworkInfoResults(BaseModel):
    result : GetStakingNetworkInfo = Field(..., description="Object")

class GetSuperCommiteesParameters(BaseModel):
    #empty set

class Committee_members(BaseModel):
    is_harmony_slot : bool = Field(..., description="If slot is Harmony owned")
    earning_account : str = Field(..., description="Wallet address that rewards are being paid to")
    bls_public_key : str = Field(..., description="BLS public key")
    voting_power_unnormalized : str = Field(..., description="Voting power of key")
    voting_power_percent : str = Field(..., description="Normalized voting power of key")

class Shard_x(BaseModel):
    policy : str = Field(..., description="Current election policy")
    count : int = Field(..., description="Number of BLS keys on shard")
    external_validator_slot_count : int = Field(..., description="Number of external BLS keys in committee")
    committee_members: Committee_members = Field(..., description="Object")

class Previous(BaseModel):
    quorum_deciders : Shard_x = Field(..., description="Shard of committee")

class GetSuperCommitees(BaseModel):
    previous : Previous = Field(..., description="Previously elected committee")
    current : Previous = Field(..., description="Currently elected committee, same schema as previous")

class GetSuperCommiteesResults(BaseModel):
    result : GetSuperCommitees = Field(..., description="Object")

#Transaction
## Cross Shard

class GetCXReceiptByHashParameters(BaseModel):
    receipt_hash : str = Field(..., description="Cross shard receipt hash")

class Hash_object(BaseModel):
    blockHash : str = Field(..., description="Block hash")
    blockNumber : int = Field(..., description="Block number")
    hash_ : str = Field(..., description="Transaction hash", alias="hash")
    from_ : str = Field(..., description="Sender wallet address", alias="from")
    to : str = Field(..., description="Receiver wallet address")
    shardID : int = Field(..., description="From shard")
    toShardID : int = Field(..., description="To shard")
    value : int = Field(..., description="Ammount transferred in Atto")


class GetCXReceiptByHashResults(BaseModel):
    result : Hash_object = Field(..., description="Object")

class GetPendingCXReceiptsParameters(BaseModel):
    #empty set

class Receipts(BaseModel):
    txHash : str = Field(..., description="Transaction hash")
    from_ : str = = Field(..., description="Sender wallet address", alias="from")
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

class Header(BaseModel):
    shard_id : int = Field(..., description="Shard ID")
    block_header_hash : str = Field(..., description="Block header hash")
    block_number : int = Field(..., description="Block number")
    view_id : int = Field(..., description="View ID")
    epoch : int = Field(..., description="Epoch number")

class GetPending_object(BaseModel):
    receipts : List[Receipts]
    merkleProof : MerkleProof
    header : Header
    commitSig : str = Field(..., description="Hex representation of aggregated signature")
    commitBitMap : str = Field(..., description="Hex representation of aggregated signature bitmap")

class GetPendingCXReceiptsResults(BaseModel):
    result : List[GetPending_object] = Field(..., description="List of object")

class ResendCXParameters(BaseModel):
    receipt_hash : str = Field(..., description="Cross shard receipt hash")

class ResendCXResults(BaseModel):
    result : bool = Field(..., description="If cross shard receipt was successfully resent or not")

## Transaction Pool

class GetPoolStatsParameters(BaseModel):
    #empty set

class GetPool_object(BaseModel):
    executable_count : str = Field(..., description="Staking transaction hash")
    non_executable_count : str = Field(..., description="Type of staking transaction")

class GetPoolStatsResults(BaseModel):
    result : GetPool_object = Field(..., description="Object")

class PendingStakingTransactionsParameters(BaseModel):
    #empty set

class PendingStakingTransactionsResults(BaseModel):
    result : List[StakingTransactionByHash] = Field(..., description="List of staking transactions in the transaction pool")

class PendingTransactionsParameters(BaseModel):
    #empty set

class PendingTransactionsResults(BaseModel):
    result : List[StakingTransactionByHash] = Field(..., description="List of regular & smart contract transactions in the transaction pool")

## Staking

class GetCurrentStakingErrorSinkParameters(BaseModel):
    #empty set

class CurrentStakingErrorSink(BaseModel):
    tx_hash_id : str = Field(..., description="Staking transaction hash")
    directive_kind : str = Field(..., description="Type of staking transaction")
    time_at_rejection : int = Field(..., description="Unix time when the staking transaction was rejected from the pool")
    error_message : str = Field(..., description="Reason for staking transaction rejection")

class GetCurrentStakingErrorSinkResults(BaseModel):
    result : List[CurrentStakingErrorSink] = Field(..., description="Array of object")

class GetStakingTransactionByBlockNumberAndIndexParameters(BaseModel):
    block_number : int = Field(..., description="Block number")
    index : int = Field(..., description="Staking transaction index")

class GetStakingTransactionByBlockNumberAndIndexResults(BaseModel):
    result : StakingTransactionByHash = Field(..., description="Object")

class GetStakingTransactionByBlockHashAndIndexParameters(BaseModel):
    block_hash : int = Field(..., description="Block hash")
    index : int = Field(..., description="Staking transaction index")

class GetStakingTransactionByBlockHashAndIndexResults(BaseModel):
    result : StakingTransactionByHash = Field(..., description="Object")

class GetStakingTransactionByHashParameters(BaseModel):
    staking_hash : str = Field(..., description="Staking transaction hash")

class StakingTransactionByHash(BaseModel):
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

class GetStakingTransactionByHashResults(BaseModel):
    result : StakingTransactionByHash = Field(..., description="Object")

class SendRawStakingTransactionParameters(BaseModel):
    hex_transaction : str = Field(..., description="Hex representation of signed staking transaction")

class SendRawStakingTransactionResults(BaseModel):
    result : str = Field(..., description="Staking transaction hash")

##Transfer

class GetCurrentTransactionErrorSinkParameters(BaseModel):
    #empty set

class CurrentTransactionErrorSink(BaseModel):
    tx_hash_id : str = Field(..., description="Transaction hash")
    time_at_rejection : int = Field(..., description="Unix time when the transaction was rejected from the pool")
    error_message : str = Field(..., description="Reason for  transaction rejection")

class GetCurrentTransactionErrorSinkResults(BaseModel):
    result : List[CurrentTransactionErrorSink] = Field(..., description="Object")

class GetTransactionByBlockHashAndIndexParameters(BaseModel):
    block_hash : str = Field(..., description="Block hash")
    index : int = Field(..., description="Transaction index")

class TransactionByBlockHashAndIndex(BaseModel):
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
    transactionIndex : int = Field(..., description="Staking transaction index within block")
    value : int = Field(..., description="Amount transferred")
    shardID : int = Field(..., description="From shard")
    toShardID : int = Field(..., description="To shard")

class GetTransactionByBlockHashAndIndexResults(BaseModel):
    result : TransactionByBlockHashAndIndex = Field(..., description="Object")

class GetTransactionByBlockNumberAndIndexParameters(BaseModel):
    block_number : int = Field(..., description="Block number")
    index : int = Field(..., description="Transaction index")

class GetTransactionByBlockNumberAndIndex(BaseModel):
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
    transactionIndex : int = Field(..., description="Staking transaction index within block")
    value : int = Field(..., description="Amount transferred")
    shardID : int = Field(..., description="From shard")
    toShardID : int = Field(..., description="To shard")
    
class GetTransactionByBlockNumberAndIndexResults(BaseModel):
    result : GetTransactionByBlockNumberAndIndex = Field(..., description="Object")

class GetTransactionByHashParameters(BaseModel):
    hash_ : str = Field(..., description="Transaction hash", alias="hash")

class GetTransactionByHash(BaseModel):
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
    transactionIndex : int = Field(..., description="Staking transaction index within block")
    value : int = Field(..., description="Amount transferred")
    shardID : int = Field(..., description="From shard")
    toShardID : int = Field(..., description="To shard")

class GetTransactionByHashResults(BaseModel):
    result : GetTransactionByHash = Field(..., description="Object")

class GetTransactionReceiptParameters(BaseModel):
    receipt : str = Field(..., description="Transaction receipt")

class GetTransactionReceipt(BaseModel):
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

class GetTransactionReceiptResults(BaseModel):
    result : GetTransactionReceipt = Field(..., description="Object")

class SendRawTransactionParameters(BaseModel):
    hex : str = Field(..., description="Hex representation of signed transaction")

class SendRawTransactionResults(BaseModel):
    result : str = Field(..., description="Transaction hash")

#Blockchain
## Network

class BlockNumberParameters(BaseModel):
    #empty set

class BlockNumberResults(BaseModel):
    result : int = Field(..., description="Current block number")

class GetCirculatingSupplyParameters(BaseModel):
    #empty set

class GetCirculatingSupplyResults(BaseModel):
    result : int = Field(..., description="Circulation supply of tokens in ONE")

class GetEpochParameters(BaseModel):
    #empty set

class GetEpochResults(BaseModel):
    result : int = Field(..., description="Current block number")

class GetLastCrossLinksParameters(BaseModel):
    #empty set

class LastCrossLinks(BaseModel):
    hash_ : str = Field(..., description="Parent block hash", alias="hash")
    block_number : int = Field(..., description="Block number")
    view_id : int = Field(..., description="View ID")
    signature : str = Field(..., description="Hex representation of aggregated signature")
    signature_bitmap : str = Field(... description="Hex representation of aggregated signature bitmap")
    shard_id : int = Field(..., description="Shard ID")
    epoch_number : int = Field(..., description="Block epoch")

class GetLastCrossLinksResults(BaseModel):
    result : List[LastCrossLinks] = Field(..., description="Array of object")

class GetLeaderParameters(BaseModel):
    #empty set

class GetLeaderResults(BaseModel):
    result : str = Field(..., description="Wallet address of current leader")

class GasPriceParameters(BaseModel):
    #empty set

class GasPriceResults(BaseModel):
    result : int = Field(..., description="Current average gas price of transactions")

class GetShardingStructureParameters(BaseModel):
    #empty set

class GetShardingStructure(BaseModel):
    current : bool = Field(..., description="If this node is currently on this shard ID")
    http : str = Field(..., description="HTTPS API endpoint for this shard ID")
    shardID : int = Field(..., description="Shard ID")
    ws : str = Field(..., description="Websocket API endpoint for this shard ID")

class GetShardingStructureResults(BaseModel):
    result : List[GetShardingStructure] = Field(..., description="Array of object")

class GetTotalSupplyParameters(BaseModel):
    #empty set

class GetTotalSupplyResults(BaseModel):
    result : int = Field(..., description="Total number of pre-mined tokens")

class GetValidatorsParameters(BaseModel):
    epoch_number : int = Field(..., description="Epoch number")

class Validator(BaseModel):
    address : str = Field(..., description="Wallet address")
    balance : int = Field(..., description="Balance of wallet")

class GetValidators(BaseModel):
    shardID : int = Field(..., description="Shard ID")
    validators : List[Validators] = Field(..., description="Array of objects")

class GetValidatorsResults(BaseModel):
    result : GetValidators = Field(..., description="Object")

class GetValidatorKeysParameters(BaseModel):
    epoch_number : int = Field(..., description="Epoch number")

class GetValidatorKeysResults(BaseModel):
    result : List[str] = Field(..., description="List of public BLS kets in the elected committee")

## Node

class GetCurrentBadBlocksParameters(BaseModel):
    #empty set 
    #note, known issues with RPC not returning correctly

class GetCurrentBadBlocksResults(BaseModel):
    result : List[str] = Field(..., description="List of bad blocks in node memory. Note: know issue with RPC not returning correctly")

class GetNodeMetadataParameters(BaseModel):
    #empty set

class Chain_config(BaseModel):
    chain_id : int = Field(..., description="Chain ID for the network")
    cross_tx_epoch : int = Field(..., description="Epoch at which cross shard transactions were enabled")
    cross_link_epoch : int = Field(..., description="Epoch at which cross links were enabled")
    staking_epoch : int = Field(..., description="Epoch at which staking was enabled")
    prestaking_epoch : int = Field(..., description="Epoch at which pre-staking began")
    quick_unlock_epoch : int = Field(..., description="Epoch at which undelegations unlocked in one epoch")
    eip155_epoch : int = Field(..., description="Epoch at which EIP155 was enabled")
    s3_epoch : int = Field(..., description="Epoch at which Mainnet V0 was launched")
    receipt_log_epoch : int = Field(..., description="Epoch at which receipt logs were enabled")

class P2p_connectivity(BaseModel):
    total_known_peers : int = Field(..., description="Number of known peers")
    connected : int = Field(..., description="Number of connected peers")
    not_connected : int = Field(..., description="Number of known peers not connected")

class GetNodeMetadata(BaseModel):
    blskey : List[str] = Field(..., description="List of BLS keys on the node")
    version : str = Field(..., description="Harmony binary version")
    network : str = Field(..., description="Network name that the node is on (Mainnet ir Testnet)")
    chain_config : Chain_config = Field(..., description="Object")
    is_leader : bool = Field(..., description="Whether the node is currently leader or not")
    shard_id : int = Field(..., description="Shard that the node is on")
    current_epoch : int = Field(..., description="Current epoch")
    blocks_per_epoch : int = Field(..., description="Number of blacks per epoch (only available on Shard 0)")
    role : str = Field(..., description="Node type (Validator or ExplorerNode)")
    dns_zone : str = Field(..., description="Name of DNS zone")
    is_archival : bool = Field(..., description="Whether the node is currently in state pruning mode or not")
    node_unix_start_time : int = Field(..., description="Start time of node in Unix time")
    p2p_connectivity : P2p_connectivity = Field(..., description="Object")

class GetNodeMetadataResults(BaseModel):
    result : GetNodeMetadata = Field(..., description="Object")

class ProtocolVersionParameters(BaseModel):
    #empty set

class ProtocolVersionResults(BaseModel):
    result : int = Field(..., description="Protocol version")

class PeerCountParameters(BaseModel):
    #empty set

class PeerCountResults(BaseModel):
    result : str = Field(..., description="Number of peers respresented as a Hex string")

## Blocks

class Additional_blocks_data(BaseModel):
    withSigners : bool = Field(..., description="Include block signer wallet addresses")
    fullTx : bool = Field(..., description="Include full transaction data")
    inclStaking : bool = Field(..., description="Include full staking transactions")

class GetBlocksParameters(BaseModel):
    start_block : int = Field(..., description="Start block")
    end_block : int = Field(..., description="End block")
    additional_blocks_data : Additional_blocks_data = Field(..., description="Object")

class GetBlocksResults(BaseModel):
    result : List[GetBlockByNumber] = Field(..., description="List of blocks")

class Additional_blocks_data(BaseModel):
    fullTx : bool = Field(..., description="Include full transaction data")
    inclTx : bool = Field(..., description="Include regular transactions")
    inclStaking : bool = Field(..., description="Include full staking transactions")

class GetBlockByNumberParameters(BaseModel):
    block_number : int = Field(..., description="Block number")
    additional_blockbynumber_data : Additional_blocks_data = Field(..., description="Object")

class GetBlockByNumber(BaseModel):
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
    stakingTransactions : Dict[str,Any] = Field(..., description="List of staking transactions finalized in this block")
    stateRoot : str = Field(..., description="Hash of state root")
    timestamp : int = Field(..., description="Unix timestamp of the block")
    transactions : Dict[str, Any] = Field(..., description="List of transactions finalized in this block")
    transactionsRoot : str = Field(..., description="Hash of transactios root")
    uncles : Dict[str,Any] = Field(..., description="Unused, legacy from Eth")
    viewID : int = Field(..., description="View ID")

class GetBlockByNumberResults(BaseModel):
    result : GetBlockByNumber = Field(..., description="Object")

class GetBlockByHashParameters(BaseModel):
    hash_ : int = Field(..., description="Block hash", alias="hash")
    additional_blockbynumber_data : Additional_blocks_data = Field(..., description="Object")

class GetBlockByHashResults(BaseModel):
    result : GetBlockByNumber = Field(..., description="Object")

class GetBlockSignersParameters(BaseModel):
    start_block : int = Field(..., description="Start block")
    end_block : int = Field(..., description="End block")
    additional_blocks_data : Additional_blocks_data = Field(..., description="Object")

class GetBlockSignersResults(BaseModel):
    result : List[str] = Field(..., description="List of block signer wallet addresses")

class GetBlockSignersKeysParameters(BaseModel):
    block_number : int = Field(..., description="Block number")

class GetBlockSignersKeysResults(BaseModel):
    result : List[str] = Field(..., description="List of block signer public BLS keys")

class GetBlockTransactionCountByNumberParameters(BaseModel):
    block_number : int = Field(..., description="Block number")

class GetBlockTransactionCountByNumberResults(BaseModel):
    results : int = Field(..., description="Number of transaction in block")

class GetBlockTransactionCountByHashParameters(BaseModel):
    hash_ : int = Field(..., description="Block hash", alias="hash")

class GetBlockTransactionCountByHashResults(BaseModel):
    result : int = Field(..., description="Number of transactions in block")

class GetHeaderByNumberParameters(BaseModel):
    block_number : int = Field(..., description="Block number")

class GetHeaderByNumberResults(BaseModel):
    result : LastestHeader = Field(..., description="Object")

class GetLatestChainHeadersParameters(BaseModel):
    #empty set

class Chain_header(BaseModel):
    shard_id : int = Field(..., description="Shard ID")
    block_header_hash : str = Field(..., description="Block header hash")
    block_number : int = Field(..., description="Block number")
    view_id : int = Field(..., description="View ID")
    epoch : int = Field(..., description="Epoch number")


class LatestChainHeaders(BaseModel):
    beacon_chain_header : Chain_header = Field(..., description="Object")
    shard_chain_header : Chain_header = Field(..., description="Object")

class GetLatestChainHeadersResults(BaseModel):
    result : LatestChainHeaders = Field(..., description="Object")

class LatestHeaderParameters(BaseModel):
    #empty set

class LatestHeader(BaseModel):
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

class LatestHeaderResults(BaseModel):
    result : LatestHeader = Field(..., description="Object")

#Account

class GetBalanceParameters(BaseModel):
    address : str = Field(..., description="Wallet address")

class GetBalanceResults(BaseModel):
    result : int = Field(..., description="Wallet balance at given block in Atto")

class GetBalanceByBlockNumberParameters(BaseModel):
    address : str = Field(..., description="Wallet address")
    block : int = Field(..., description="Block to get balance at")

class GetBalanceByBlockNumberResults(BaseModel):
    result : int = Field(..., description="Wallet balance at given block in Atto")

class GetStakingTransactionsCountParameters(BaseModel):
    address : str = Field(..., description="Wallet address")
    transaction : str = Field(..., description="Type of staking transaction (SENT, RECEIVED, ALL)")

class GetStakingTransactionsCountResults(BaseModel):
    result : int = Field(..., "Number of staking transactions")

class TransactionHistory(BaseModel):
    address : str = Field(..., description="Wallet address")
    pageIndex : Optional[int] = Field(..., description="Optional, which page ofo transactions to return, default 0")
    pageSize : Optional[int] = Field(..., description="Optional, how many transactions to display per page, default 1000")
    fullTx : Optional[bool] = Field(..., description="Optional, return full transaction data or just transaction hashes, default false")
    txType : Optional[str] = Field(..., description="Optional, which type of transactions to display ('ALL','RECEIVED', or 'SENT'), default 'ALL'")
    order : Optional[str] = Field(..., description="Optional, sort transactions in ascending or descending order based on timestamp ('ASC' or 'DESC'), default 'ASC'")

class GetStakingTransactionsHistoryParameters(BaseModel):
    transaction_history = TransactionHistory = Field(..., description="Transaction history args")

class StakingTransactionsHistory(BaseModel):
    blockHash : str = Field(..., description="Block hash in which transaction was finalized")
    blockNumber : int = Field(..., description="Block number in which transaction was finalized")
    from_ : str = Field(..., description="Sender wallet address", alias="from")
    timestamp : int = Field(..., description="Unix time at which transaction was finalized")
    gasPrice : int = Field(..., description="Gas price of transaction in Atto")
    gas : int = Field(..., description="Gas limit of transaction")
    hash_ : int = Field(..., description="Transaction hash", alias="hash")
    nonce : int = Field(..., description="Wallet nonce of transaction")
    transactionIndex : int = Field(..., description="Staking transaction index within block, null if pending")
    type_ : str = Field(..., description="Type of staking transaction", alias="type")
    msg : Dict[str, Any] = Field(..., description="Staking transaction data, depending on the type of staking transaction")

class GetStakingTransactionsHistoryResults(BaseModel):
    result : List[str] = Field(..., description="List of staking transactions")

class GetStakingTransactionsHistoryTxTypeResults(BaseModel):
    result : StakingTransactionsHistory = Field(..., description="List of staking transactions")


class GetTransactionsCountParameters(BaseModel):
    address : str = Field(..., description="Wallet address")
    transaction : str = Field(..., description="Type of staking transaction (SENT, RECEIVED, ALL)")

class GetTransactionsCountResults(BaseModel):
    result : int = Field(..., description="Number of transactions")

class GetTransactionsHistoryParameters(BaseModel):
    transaction_history = TransactionHistory = Field(..., description="Transaction history args")

class GetTransactionsHistoryTxTypeResults(BaseModel):
    result : List[TransactionByBlockHashAndIndex] = Field(..., description="Array of object")
        
 class GetTransactionsHistoryResults(BaseModel):
    result : List[str] = Field(..., description="List of transaction hashes")

