from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

class ExampleParameters(BaseModel):
    a : int = Field(..., description="This is a required integer")
    b : Optional[str] = Field(None, description="This is an optional string")
    c : List[int] = Field(..., description="This is a required list (array) of ints")
    d : Optional[List[Any]] = Field(None, description="This is an optional list (array) of unknown type.")
    e : Dict[str, Any] = Field(..., description="This is a required JSON object")
    f : List[Dict[str, Any]] = Field(..., description="This is a required array of JSON objects")
    g : Optional[List[Dict[str, Any]]] = Field(..., description="This is an optional array of JSON objects")

class SmartContractCall(BaseModel):
    to : str = Field(..., description="Smart contract address")
    from : Optional[str] = Field(None, description="Wallet address")
    gas : Optional[int] = Field(None, description="Gas to execute the smart contract call")
    gasPrice : Optional[int] = Field(None, description="Gas price to execute smart contract call")
    value : Optional[int] = Field(None, description="Value sent with the smart contract call")
    data : Optional[str] = Field(None, description="Hash of smart contract method and parameters")

class CallParameters(BaseModel):
    smart_contract_call : SmartContractCall
    block_number : int

class CallResult(BaseModel):
    return_value : str = Field(..., description="Return value of the executed smart contract")

class EstimateGasResult(BaseModel):
    estimated_gas_price : str = Field(..., description="Hex of estimated gas price of smart contract call")

class GetCodeParameters(BaseModel):
    address : str = Field(..., description="The address to get the code from")
    block : str = Field(..., description="Block to query for information. Usually latest, which specifies the most recent block.")
    callback : Optional[str] = Field(None, description="Optional callback, returns an error object as first parameter and the result as second.")

class GetCodeResult(BaseModel):
    data : str = Field(..., description="The data at given address address")

class GetStorageAtParameters(BaseModel):
    address : str = Field(..., description="Smart contract address")
    storage_location : str = Field(..., description="Hex representation of storage location")
    block_number : int = Field(..., description="Block number")

class GetStorageAtResult(BaseModel):
    data : str = Field(..., description="Data stored at the smart contract location")


#Staking
## Delegation

class GetDelegationsByDelegatorParameters(BaseModel):
    address : str = Field(..., description="Delegator address")

class DelegationsByDelegator(BaseModel):
    validator_address : str = Field(..., description="Validator wallet address")
    delegator_address : str = Field(..., description="Delegator wallet address")
    amount : int = Field(..., description="Amount delegated in atto")
    reward : int = Field(..., description="Unclaimed rewards in atto")
    undelegations : List[Dict[str,any]] = Field(..., description="List of pending undelegations") ## check

class GetDelegationsByDelegatorResult(BaseModel):
    data : List[Dict[DelegationsByDelegator]] ##check

class GetDelegationsByDelegatorByBlockNumberParameters(BaseModel):
    address : str = Field(..., description="Delegator wallet address")
    block_number : int = Field(..., description="Block number")

class GetDelegationsByDelegatorByBlockNumberResults(BaseModel):
    data : List[Dict[DelegationsByDelegator]] ##check

class GetDelegationsByValidatorParameters(BaseModel):
    address : str = Field(..., description="Validator wallet address")

class GetDelegationsByValidatorResults(BaseModel):
    data : List[Dict[DelegationsByDelegator]] ##check

## Validator

class GetAllValidatorInformationParameters(BaseModel):
    page_request : int = Field(..., description="Page to request (page size is 100), -1 for all validators")

class GetAllValidatorInformationResults(BaseModel):
    validator : List[Validator] = Field(..., description="Array of Object")

class GetAllValidatorInformationByBlockNumberParameters(BaseModel):
    page_number : int = Field(..., description="Page number, -1 for all")
    block_number : int = Field(..., description="Block number")

class GetAllValidatorInformationByBlockNumberResults(BaseModel):
    validator : List[Validator] = Field(..., description="Array of Object") #check

class GetElectedValidatorAddressesParameters(BaseModel):
    #empty set

class GetElectedValidatorAddressesResults(BaseModel):
    addresses : List[str] = Field(..., description="List of wallet addresses that are currently elected")


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
    delegations : List[Dict[DelegationsByDelegator]] #check
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
    validator : Validator = Field(..., description="Object")


#Network

class GetCurrentUtilityMetricsParameters(BaseModel):
    #empty set

class GetCurrentUtilityMetricsResults(BaseModel):
    accumulatorsnapshot : int = Field(..., description="Total block reward given out in Atto")
    currentstakedpercentage : str = Field(..., description="Percent of circulationg supply staked")
    deviation : str = Field(..., description="Change in percent of circulating supply staked")
    adjustment : str = Field(..., description="Change in circulationg supply staked")


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

class GetMedianRawStakeSnapShotResults(BaseModel):
    epos_median_stake : str = Field(..., description="Effective median stake")
    max_eternal_slots : int = Field(..., description="Number of available committee slots")
    epos_slot_winners : List[Epos_slot_winners] = Field(..., description="Details for each slot winner")
    epos_slot_candidates : List[Epos_slot_candidates] = Field(..., description="Details for each candidates")


class GetStakingNetworkInfoParameters(BaseModel):
    #empty set

class GetStakingNetworkInfoResults(BaseModel):
    total_supply : str = Field(..., description="Total number of pre-mined tokens")
    circulating_supply : str = Field(..., description="Number of token available in the network")
    epoch_last_block : int = Field(..., description="Last block of epoch")
    total_staking : int = Field(..., description="Total amount staked in Atto")
    median_raw_stake : str = Field(..., description="Effective median stake in Atto")

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

class GetSuperCommiteesResults(BaseModel):
    previous : Previous = Field(..., description="Previously elected committee")
    current : Previous = Field(..., description="Currently elected committee, same schema as previous")


#Transaction
## Cross Shard

class GetCXReceiptByHashParameters(BaseModel):
    receipt_hash : str = Field(..., description="Cross shard receipt hash")

class Hash_object(BaseModel):
    blockHash : str = Field(..., description="Block hash")
    blockNumber : int = Field(..., description="Block number")
    hash : str = Field(..., description="Transaction hash")
    from : str = Field(..., description="Sender wallet address")
    to : str = Field(..., description="Receiver wallet address")
    shardID : int = Field(..., description="From shard")
    toShardID : int = Field(..., description="To shard")
    value : int = Field(..., description="Ammount transferred in Atto")


class GetCXReceiptByHashResults(BaseModel):
    data : Hash_object = Field(..., description="Object")

class GetPendingCXReceiptsParameters(BaseModel):
    #empty set

class Receipts(BaseModel):
    txHash : str = Field(..., description="Transaction hash")
    from : str = = Field(..., description="Sender wallet address")
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
    data : List[GetPending_object] = Field(..., description="List of object")

class ResendCXParameters(BaseModel):
    receipt_hash : str = Field(..., description="Cross shard receipt hash")

class ResendCXResults(BaseModel):
    success : bool = Field(..., description="If cross shard receipt was successfully resent or not")

## Transaction Pool

class GetPoolStatsParameters(BaseModel):
    #empty set

class GetPool_object(BaseModel):
    executable_count : str = Field(..., description="Staking transaction hash")
    non_executable_count : str = Field(..., description="Type of staking transaction")

class GetPoolStatsResults(BaseModel):
    data : GetPool_object = Field(..., description="Object")

class PendingStakingTransactionsParameters(BaseModel):
    #empty set

class PendingStakingTransactionsResults(BaseModel):
    data : List[StakingTransactionByHash] = Field(..., description="List of staking transactions in the transaction pool")

class PendingTransactionsParameters(BaseModel):
    #empty set

class PendingTransactionsResults(BaseModel):
    data : List[StakingTransactionByHash] = Field(..., description="List of regular & smart contract transactions in the transaction pool")

## Staking

class GetCurrentStakingErrorSinkParameters(BaseModel):
    #empty set

class CurrentStakingErrorSink(BaseModel):
    tx_hash_id : str = Field(..., description="Staking transaction hash")
    directive_kind : str = Field(..., description="Type of staking transaction")
    time_at_rejection : int = Field(..., description="Unix time when the staking transaction was rejected from the pool")
    error_message : str = Field(..., description="Reason for staking transaction rejection")

class GetCurrentStakingErrorSinkResults(BaseModel):
    data : List[CurrentStakingErrorSink] = Field(..., description="Array of object")

class GetStakingTransactionByBlockNumberAndIndexParameters(BaseModel):
    block_number : int = Field(..., description="Block number")
    index : int = Field(..., description="Staking transaction index")

class GetStakingTransactionByBlockNumberAndIndexResults(BaseModel):
    data : StakingTransactionByHash = Field(..., description="Object")

class GetStakingTransactionByBlockHashAndIndexParameters(BaseModel):
    block_hash : int = Field(..., description="Block hash")
    index : int = Field(..., description="Staking transaction index")

class GetStakingTransactionByBlockHashAndIndexResults(BaseModel):
    data : StakingTransactionByHash = Field(..., description="Object")

class GetStakingTransactionByHashParameters(BaseModel):
    staking_hash : str = Field(..., description="Staking transaction hash")

class StakingTransactionByHash(BaseModel):
    blockHash : str = Field(..., description="Block hash in which transaction was finalized")
    blockNumber : int = Field(..., description="Block number in which transaction was finalized")
    from : str = Field(..., description="Sender wallet address")
    timestamp : int = Field(..., description="Unix time at which transaction was finalized")
    gas : int = Field(..., description="Gas limit of transaction")
    gasPrice : int = Field(..., description="Gas price of transaction in Atto")
    nonce : int = Field(..., description="Wallet nonce of transaction")
    transactionIndex : int = Field(..., description="Staking transaction index within block")
    type : str = Field(..., description="Type of staking transaction")
    msg : Any = Field(..., description="Staking transaction data, depending on the type of staking transaction") #HELP not sure here

class GetStakingTransactionByHashResults(BaseModel):
    data : StakingTransactionByHash = Field(..., description="Object")

class SendRawStakingTransactionParameters(BaseModel):
    hex_transaction : str = Field(..., description="Hex representation of signed staking transaction")

class SendRawStakingTransactionResults(BaseModel):
    data : str = Field(..., description="Staking transaction hash")

##Transfer

class GetCurrentTransactionErrorSinkParameters(BaseModel):
    #empty set

class CurrentTransactionErrorSink(BaseModel):
    tx_hash_id : str = Field(..., description="Transaction hash")
    time_at_rejection : int = Field(..., description="Unix time when the transaction was rejected from the pool")
    error_message : str = Field(..., description="Reason for  transaction rejection")

class GetCurrentTransactionErrorSinkResults(BaseModel):
    data : List[CurrentTransactionErrorSink] = Field(..., description="Object")

class GetTransactionByBlockHashAndIndexParameters(BaseModel):
    block_hash : str = Field(..., description="Block hash")
    index : int = Field(..., description="Transaction index")

class GetTransactionByBlockHashAndIndexResults(BaseModel):
    blockHash : str = Field(..., description="Block hash")
    blockNumber : int = Field(..., description="Block number")
    from : str = Field(..., description="Sender wallet address")
    timestamp : int = Field(..., description="Unix time at which transaction was finalized")
    gas : int = Field(..., description="Gas limit of transaction")
    gasPrice : int = Field(..., description="Gas price of transaction in Atto")
    hash : str = Field(..., description="Transaction hash")
    input : str = Field(..., description="Transaction data, used for smart contracts")
    nonce : int = Field(..., description="Sender wallet nonce of transaction")
    to : str = Field(..., description="Receiver wallet address")
    transactionIndex : int = Field(..., description="Staking transaction index within block")
    value : int = Field(..., description="Amount transferred")
    shardID : int = Field(..., description="From shard")
    toShardID : int = Field(..., description="To shard")

class GetTransactionByBlockNumberAndIndexParameters(BaseModel):
    block_number : int = Field(..., description="Block number")
    index : int = Field(..., description="Transaction index")

class GetTransactionByBlockNumberAndIndexResults(BaseModel):
    blockHash : str = Field(..., description="Block hash")
    blockNumber : int = Field(..., description="Block number")
    from : str = Field(..., description="Sender wallet address")
    timestamp : int = Field(..., description="Unix time at which transaction was finalized")
    gas : int = Field(..., description="Gas limit of transaction")
    gasPrice : int = Field(..., description="Gas price of transaction in Atto")
    hash : str = Field(..., description="Transaction hash")
    input : str = Field(..., description="Transaction data, used for smart contracts")
    nonce : int = Field(..., description="Sender wallet nonce of transaction")
    to : str = Field(..., description="Receiver wallet address")
    transactionIndex : int = Field(..., description="Staking transaction index within block")
    value : int = Field(..., description="Amount transferred")
    shardID : int = Field(..., description="From shard")
    toShardID : int = Field(..., description="To shard")

class GetTransactionByHashParameters(BaseModel):
    hash : str = Field(..., description="Transaction hash")

class GetTransactionByHashResults(BaseModel):
    blockHash : str = Field(..., description="Block hash")
    blockNumber : int = Field(..., description="Block number")
    from : str = Field(..., description="Sender wallet address")
    timestamp : int = Field(..., description="Unix time at which transaction was finalized")
    gas : int = Field(..., description="Gas limit of transaction")
    gasPrice : int = Field(..., description="Gas price of transaction in Atto")
    hash : str = Field(..., description="Transaction hash")
    input : str = Field(..., description="Transaction data, used for smart contracts")
    nonce : int = Field(..., description="Sender wallet nonce of transaction")
    to : str = Field(..., description="Receiver wallet address")
    transactionIndex : int = Field(..., description="Staking transaction index within block")
    value : int = Field(..., description="Amount transferred")
    shardID : int = Field(..., description="From shard")
    toShardID : int = Field(..., description="To shard")

class GetTransactionReceiptParameters(BaseModel):
    receipt : str = Field(..., description="Transaction receipt")

class GetTransactionReceiptResults(BaseModel):
    blockHash : str = Field(..., description="Block hash")
    blockNumber : int = Field(..., description="Block number")
    contractAddress : str = Field(..., description="Smart contract address")
    culmulativeGasUsed : int = Field(..., description="Gas used for transaction")
    from : str = Field(..., description="Sender wallet address")
    gasUsed : int = Field(..., description="Gas used for the transaction")
    logs : List[Any] = Field(..., description="Array")
    logsBloom : str = Field(..., description="Bloom logs")
    shardID : int = Field(..., description="Shard ID")
    status : int = Field(..., description="Status of transaction (0: pending, 1: success)")
    to : str = Field(..., description="Receiver wallet address")
    transactionHash : str = Field(..., description="Transaction hash")
    transactionIndex : str = Field(..., description="Transaction index within block")

class SendRawTransactionParameters(BaseModel):
    hex : str = Field(..., description="Hex representation of signed transaction")

class SendRawTransactionResults(BaseModel):
    hash : str = Field(..., description="Transaction hash")

#Blockchain
## Network

  