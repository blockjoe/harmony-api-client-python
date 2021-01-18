from typing import List, Optional, Union

import requests

from .models import (
    Block,
    CrossLink,
    CXReceipt,
    Delegation,
    Header,
    LatestChainHeaders,
    NodeMetadata,
    MedianRawStakeSnapshot,
    PendingCXReceipt,
    PoolStats,
    ShardingStructure,
    SortOrder,
    StakingError,
    StakingNetworkInfo,
    StakingTransaction,
    SuperCommittees,
    Transaction,
    TransactionError,
    TransactionType,
    UtilityMetrics,
    ValidatorIDs,
    ValidatorInformation
)

from . import account as act
from . import blockchain_network as bc_net
from . import blocks as blk
from . import cross_shard as cx
from . import delegation as dlg
from . import node
from . import smart_contract as sc
from . import staking as stk
from . import staking_network as stk_net
from . import transaction_pool as tx_pool
from . import transfer as tx
from . import validator as val

class HarmonyNodeError(Exception):
    pass

class HarmonyAPI(object):

    def __init__(self, api_url : str, session : Optional[requests.Session] = None) -> None:
        """
        Parameters
        ----------
        api_url : str
            The url where the node is located
        sessions : requests.Session, optional
            An already existing requests sesion. If none is passed
            a session will be created for this object.
        """
        self._api_url = api_url
        if session is None:
            session = requests.Session()
        self._session = session

    @property
    def session(self) -> requests.Session:
        return self._session

    @property
    def url(self) -> str:
        return self._api_url

    def node_metadata(self) -> NodeMetadata:
        """
        Get metadata about the node.

        Returns
        -------
        NodeMetadata
        """
        resp = node.get_node_metadata(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def peer_count(self) -> int:
        """
        Get the number of connected peers.

        Returns
        -------
        int
        """
        resp = node.get_peer_count(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return int(resp.result, 16)

    def protocol_version(self) -> int:
        """
        Get the version of the protocol

        Returns
        -------
        int
        """
        resp = node.get_protocol_version(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def _current_bad_blocks(self) -> List[str]:
        """
        Get the hashes of the bad blocks in the node's memory

        NOTE: Known issues with RPC not returning correctly

        Returns
        --------
        list[str]
        """
        resp = node.get_current_bad_blocks(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def current_gas_price(self) -> int:
        """
        Get the current average gas price

        Returns
        -------
        int
        """
        resp = bc_net.get_current_gas_price(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result
    
    def circulating_supply(self) -> int:
        """
        Get the current circulating supply in ONE tokens.

        Returns
        -------
        int
        """
        resp = bc_net.get_circulating_supply(self.url, self.session)
    
    def total_supply(self) -> int:
        """
        Get the current total supply in ONE tokens.
        
        Returns
        -------
        int
        """
        resp = bc_net.get_total_supply(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def current_block_number(self) -> int:
        """
        Get the block number of the current block

        Returns
        -------
        int
        """
        resp = bc_net.current_block_number(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def current_leader(self) -> str:
        """
        Get the wallet address of the current leader.

        Returns
        -------
        str
        """
        resp = bc_net.get_current_leader(self.url, self.session)

    def sharding_structure(self) -> List[ShardingStructure]:
        """
        Get the sharding structure

        Returns
        -------
        list[ShardingStructure]
        """
        resp = bc_net.get_sharding_structure(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def last_cross_links(self) -> List[CrossLink]:
        """
        Get the last cross links

        Returns
        -------
        List[CrossLink]
        """
        resp = bc_net.get_last_cross_links(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def current_epoch(self) -> int:
        """
        Get the current epoch

        Returns
        -------
        int
        """
        resp = bc_net.get_epoch(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def validators_by_epoch(self, epoch_number : int, as_pubkeys : Optional[bool] = False) -> Union[ValidatorIDs, List[str]]:
        """
        Get the validators for a given epoch

        Parameters
        ----------
        epoch_number : int
        as_pubkeys : bool, optional
            Represent the validators by their public keys; defaults to False

        Returns
        -------
        ValidatorIDs if as_pubkeys is False else list[str]
        """
        if as_pubkeys:
            resp = bc_net.get_validator_keys_by_epoch(self.url, epoch_number, self.session)
        else:
            resp = bc_net.get_validators_by_epoch(self.url, epoch_number, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def current_utility_metrics(self) -> UtilityMetrics:
        """
        Get the current staking network utility metrics

        Returns
        -------
        UtilityMetrics
        """
        resp = stk_net.get_current_utility_metrics(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def staking_network_info(self) -> StakingNetworkInfo:
        """
        Get information about the staking network

        Returns
        -------
        StakingNetworkInfo
        """
        resp = stk_net.get_staking_network_info(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def latest_super_committes(self) -> SuperCommittees:
        """
        Get information about the current and previously elected super committees

        Returns
        -------
        SuperCommittees  
        """
        resp = stk_net.get_super_committees(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result
    
    def median_raw_stake_snapshot(self) -> MedianRawStakeSnapshot:
        """
        Get a snapshot of the raw median stake.

        Returns
        -------
        MedianRawStakeSnapshot
        """
        resp = stk_net.get_median_raw_stake_snapshot(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def transaction_pool_stats(self) -> PoolStats:
        """
        Get stats on the transaction pool
        
        Returns
        --------
        PoolStats
        """
        resp = tx_pool.get_pool_stats(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def pending_staking_transactions(self) -> List[StakingTransaction]:
        """
        Get the staking transactions pending in the transaction pool.

        Returns
        --------
        list[StakingTransaction]
        """
        resp = tx_pool.get_pending_staking_transactions(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def pending_transactions(self) -> List[Transaction]:
        """
        Get the transactions pending in the transaction pool.

        Returns
        -------
        list[Transaction]
        """
        resp = tx_pool.get_pending_transactions(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def latest_chain_headers(self) -> LatestChainHeaders:
        """
        Get the latest chain headers.

        Returns
        -------
        LatestChainHeaders
        """
        resp = blk.get_latest_chain_headers(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def block_header(self, block_number : Optional[int] = None) -> Header:
        """
        Get the header of the block.

        Parameters
        ----------
        block_number : int, optional
            The block number of the block to get the header for.
            If None is given, get the header of the latest block.
            Defaults to None.

        Returns
        -------
        Header
        """
        if block_number is not None:
            resp = blk.get_block_header_by_number(self.url, block_number, self.session)
        else:
            resp = blk.get_latest_block_header(self.url, self.session)
    
    def get_block(self, block_number : Optional[int] = None, block_hash : Optional[str] = None, include_full_transaction_data : Optional[bool] = False, include_regular_transactions : Optional[bool] = False, include_staking_transactions : Optional[bool] = False) -> Block:
        """
        Get a block by either block number or hash
        
        One of `block_number` and `block_hash` is required, but not both cannot be passed together.
        
        Parameters
        ----------
        block_number : int, optional
            If block_hash is not provided, this must be provided.
        block_hash : str, optional
            If block_number is not provided, this must be provided.
        include_full_transaction_data : bool, optional
            Whether to include full transaction data; defaults to False
        include_regular_transactions : bool, optional
            Whether to include regular transactions; defaults to False
        include_staking_transactions : bool, optional
            Whether to include staking transactions; defaults to False

        Returns
        -------
        Block

        Raises
        ------
        ValueError: If either neither or both the block number and block hash are provided
        """
        if block_number is None and block_hash is None:
            raise ValueError("One of `block_number` or `block_hash` is required")
        if block_number is not None and block_hash is not None:
            raise ValueError("Both `block_number` and `block_hash` can't be passed at once. Choose one.")
    
        if block_number is not None:
            resp = blk.get_block_by_number(self.url, block_number, include_full_transaction_data, include_regular_transactions, include_staking_transactions, self.session)
        else:
            resp = blk.get_block_by_hash(self.url, block_number, include_full_transaction_data, include_regular_transactions, include_staking_transactions, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def get_block_singers(self, block_number : int, as_pubkeys : Optional[bool] = False) -> List[str]:
        """
        Get the signers of the given block.
        
        Parameters
        ----------
        block_number : int
        as_pubkeys : bool, optional
            If True, identify the signers by public key instead of address;
            defaults to False

        Returns
        --------
        list[str]
            List of signer addresses, unless as_pubkeys is True, then list of public keys
        """
        if as_pubkeys:
            resp = blk.get_block_signers_keys(self.url, block_number, self.session)
        else:
            resp = blk.get_block_signers(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def get_transaction_count_on_block(self, block_number : Optional[int] = None, block_hash : Optional[str] = None) -> int:
        """
        Get a block by either block number or hash
        
        One of `block_number` and `block_hash` is required, but not both cannot be passed together.
        
        Parameters
        ----------
        block_number : int, optional
            If block_hash is not provided, this must be provided.
        block_hash : str, optional
            If block_number is not provided, this must be provided.

        Returns
        -------
        int

        Raises
        ------
        ValueError: If either neither or both the block number and block hash are provided
        """
        if block_number is None and block_hash is None:
            raise ValueError("One of `block_number` or `block_hash` is required")
        if block_number is not None and block_hash is not None:
            raise ValueError("Both `block_number` and `block_hash` can't be passed at once. Choose one.")
        
        if block_number is not None:
            resp = blk.get_block_transaction_count_by_number(self.url, block_number, self.session)
        else:
            resp = blk.get_block_transaction_count_by_hash(self.url, block_hash, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def get_blocks(self, starting_block_number : int, ending_block_number : int, include_signer_addresses : Optional[bool] = False, include_transactions : Optional[bool] = False, include_staking_transactions : Optional[bool] = False, session : Optional[requests.Session] = None) -> List[Block]:
        """
        Get the blocks between the starting and ending block number

        Parameters
        ----------
        starting_block_number : int
            The block number of the first block in the range
        ending_block_number : int
            The block number of the last block in the range
        include_signer_addresses : bool, optional
            Whether to include the wallet addresses of the block signers; defaults to False
        include_transactions : bool, optional
            Whether to include the full transaction data on the block; defaults to False
        include_staking_transactions : bool, optional
            Whether to include the full staking transaction data on the block; defaults to False
        
        Returns
        -------
        list[Block]
        """
        resp = blk.get_blocks_from_range(self.url, starting_block_number, ending_block_number, include_signer_addresses, include_transactions, include_staking_transactions, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def get_account_balance(self, address : str, block_number : Optional[int] = None) -> int:
        """
        Get the balance of an account.

        Parameters
        ----------
        address : str
        block_number : int, optional
            An optional block number specifier; defaults to None
        
        Returns
        -------
        int
        """
        if block_number is not None:
            resp = act.get_balance_by_block_number(self.url, address, block_number, self.session)
        else:
            resp = act.get_balance(self.url, address, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def get_account_staking_transaction_count(self, address : str, transaction_type : Optional[TransactionType] = "ALL") -> int:
        """
        Get the number of staking transactions on the account
        
        Parameters
        ----------
        address : str
        transaction_type : str
            Either 'SENT', 'RECEIVED', 'ALL', defaults to 'ALL'
        
        Returns
        -------
        int
        """
        resp = act.get_staking_transactions_count(self.url, address, transaction_type, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def get_account_staking_transaction_history(self, address : str, page_index : Optional[int] = 0, page_size : Optional[int] = 1000, include_full_transaction_data : Optional[bool] = False, transaction_type : Optional[TransactionType] = "ALL", sort_order : Optional[SortOrder] = "ASC") -> Union[List[str], List[StakingTransaction]]:
        """
        Get a history of the staking transactions on the account
        
        Parameters
        ----------
        address: str
            The wallet address
        page_index: int, optional
            Which page of transactions to return, defaults to 0
        page_size: int, optional
            The number of transactions per page, defaults to 1000
        include_full_transaction_data: bool, optional
            If true return the whole transaction object instead of the hash, defaults to Fasle
        transaction_type: str, optional
            Either 'SENT', 'RECEIVED', 'ALL', defaults to 'ALL'
        sort_order: str, optional
            How to sort based on timestamp, either 'ASC' or 'DESC', defaults to 'ASC'
        
        Returns
        -------
        list[str] or list[StakingTransaction]
        """
        resp = act.get_staking_transactions_history(self.url, address, page_index, page_size, include_full_transaction_data, transaction_type, sort_order, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def get_account_transaction_count(self, address : str, transaction_type : Optional[TransactionType] = "ALL") -> int:
        """
        Get the number of transactions on the account
        
        Parameters
        ----------
        address : str
        transaction_type : str
            Either 'SENT', 'RECEIVED', 'ALL', defaults to 'ALL'
        
        Returns
        -------
        int
        """
        resp = act.get_transactions_count(self.url, address, transaction_type, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def get_account_staking_transaction_history(self, address : str, page_index : Optional[int] = 0, page_size : Optional[int] = 1000, include_full_transaction_data : Optional[bool] = False, transaction_type : Optional[TransactionType] = "ALL", sort_order : Optional[SortOrder] = "ASC") -> Union[List[str], List[Transaction]]:
        """
        Get a history of the transactions on the account
        
        Parameters
        ----------
        address: str
            The wallet address
        page_index: int, optional
            Which page of transactions to return, defaults to 0
        page_size: int, optionalOne of `block_number` and `block_hash` is required, but not both cannot be passed together.
            The number of transactions per page, defaults to 1000
        include_full_transaction_data: bool, optional
            If true return the whole transaction object instead of the hash, defaults to Fasle
        transaction_type: str, optional
            Either 'SENT', 'RECEIVED', 'ALL', defaults to 'ALL'
        sort_order: str, optional
            How to sort based on timestamp, either 'ASC' or 'DESC', defaults to 'ASC'
        
        Returns
        -------
        list[str] or list[StakingTransaction]
        """
        resp = act.get_transactions_history(self.url, address, page_index, page_size, include_full_transaction_data, transaction_type, sort_order, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result
    
    def current_transaction_error_sink(self) -> List[TransactionError]:
        """
        Get the current transaction error sink.

        Returns
        -------
        list[TransactionError]
        """
        resp = tx.get_current_transaction_error_sink(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def get_transaction(self, trasaction_hash : str) -> Transaction:
        """
        Get the transaction by its hash.

        Parameters
        ----------
        transaciton_hash : str

        Returns
        --------
        Transaction
        """
        resp = tx.get_transaction_by_hash(self.url, transaction_hash, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result
    
    def get_transaction_by_block(self, transaction_index : int, block_number : Optional[int] = None, block_hash : Optional[str] = None) -> Transaction:
        """
        Get the transaction by the block specifier

        One of `block_number` and `block_hash` is required, but not both cannot be passed together.

        Parameters
        ----------
        transaction_index : int
        block_number : int, optional
            If block_hash is not provided, this must be provided.
        block_hash : str, optional
            If block_number is not provided, this must be provided.

        Returns
        -------
        Transaction

        Raises
        ------
        ValueError: If either neither or both the block number and block hash are provided
        """
        if block_number is None and block_hash is None:
            raise ValueError("One of `block_number` or `block_hash` is required")
        if block_number is not None and block_hash is not None:
            raise ValueError("Both `block_number` and `block_hash` can't be passed at once. Choose one.")

        if block_number is not None:
            resp = tx.get_transaction_by_block_number_and_index(self.url, block_number, transaction_index, self.session)
        else:
            resp = tx.get_transaction_by_block_hash_and_index(self.url, block_hash, transaction_index, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def send_raw_transaction(self, signed_transaction_hex : str) -> str:
        """
        Send the raw signed transaction

        Parameters
        ----------
        signed_transaction_hex : str
            The hex representation of the signed transaction
        
        Returns
        -------
        str
        """
        resp = tx.send_raw_transaction(self.url, signed_transaction_hex, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def current_staking_transaction_error_sink(self) -> List[StakingError]:
        """
        Get the current staking transaction error sink.

        Returns
        -------
        list[StakingError]
        """
        resp = stk.get_current_staking_error_sink(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def get_staking_transaction(self, trasaction_hash : str) -> StakingTransaction:
        """
        Get the transaction by its hash.

        Parameters
        ----------
        transaciton_hash : str

        Returns
        --------
        StakingTransaction
        """
        resp = stk.get_staking_transaction_by_hash(self.url, transaction_hash, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result
    
    def get_staking_transaction_by_block(self, transaction_index : int, block_number : Optional[int] = None, block_hash : Optional[str] = None) -> StakingTransaction:
        """
        Get the staking transaction by the block specifier

        One of `block_number` and `block_hash` is required, but not both cannot be passed together.

        Parameters
        ----------
        transaction_index : int
        block_number : int, optional
            If block_hash is not provided, this must be provided.
        block_hash : str, optional
            If block_number is not provided, this must be provided.

        Returns
        -------
        StakingTransaction

        Raises
        ------
        ValueError: If either neither or both the block number and block hash are provided
        """
        if block_number is None and block_hash is None:
            raise ValueError("One of `block_number` or `block_hash` is required")
        if block_number is not None and block_hash is not None:
            raise ValueError("Both `block_number` and `block_hash` can't be passed at once. Choose one.")

        if block_number is not None:
            resp = stk.get_staking_transaction_by_block_number_and_index(self.url, block_number, transaction_index, self.session)
        else:
            resp = stk.get_staking_transaction_by_block_hash_and_index(self.url, block_hash, transaction_index, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def send_raw_staking_transaction(self, signed_transaction_hex : str) -> str:
        """
        Send the raw signed staking transaction

        Parameters
        ----------
        signed_transaction_hex : str
            The hex representation of the signed staking transaction
        
        Returns
        -------
        str
        """
        resp = stk.send_raw_staking_transaction(self.url, signed_transaction_hex, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result
    
    
    def get_delegations_by_delegator(self, delegator_address : str, block_number : Optional[int] = None) -> List[Delegation]:
        """
        Get the delegations by a delegator

        Parameters
        ----------
        delegator_address : str
        block_number : int, optional
            Optionally filter by block number, defaults to None

        Returns
        -------
        list[Delegation]
        """
        if block_number is not None:
            resp = dlg.get_delegations_by_delegator(self.url, delegator_address, self.session)
        else:
            resp = dlg.get_delegations_by_delegator_by_block_number(self.url, delegator_address, block_number, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def get_delegations_by_validator(self, validator_address : str) -> List[Delegation]:
        """
        Get the delegations by a validator

        Parameters
        ----------
        validator_address : str

        Returns
        -------
        list[Delegation]
        """
        resp = dlg.get_delegations_by_validator(self.url, validator_address, self.session)
        return resp.result

    def get_all_validators(self) -> List[str]:
        """
        Get the addresses of all the validators.

        Returns
        -------
        list[str]
        """
        resp = val.get_all_elected_validator_addresses(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def get_all_elected_validators(self) -> List[str]:
        """
        Get the addresses of all the elected validators.

        Returns
        -------
        list[str]
        """
        resp = val.get_all_elected_validator_addresses(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def get_information_about_validator(self, validator_address : str) -> ValidatorInformation:
        """
        Get detailed information about a given validator.

        Returns
        -------
        ValidatorInformation
        """
        resp = val.get_all_validator_information(self.url, validator_address, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result
    
    def get_all_validator_information(self, page_number : Optional[int] = -1, block_number : Optional[int] = None) -> List[ValidatorInformation]:
        """
        Get detailed information about all the validators.

        Parameters
        ----------
        page_number : int, optional 
            The page number of validators to get (100 results per page)
            with -1 getting all results, defaults to -1
        block_number : int
            The block number to optionally filter on
        
        Returns
        -------
        list[ValidatorInformation]
        """
        if block_number is not None:
            resp = val.get_all_validator_information_by_block_number(self.url, block_number, page_number, self.session)
        else:
            resp = val.get_all_validator_information(self.url, page_number, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def get_cx_reciept(self, cx_receipt_hash : str) -> CXReceipt:
        """
        Get the cross shard receipt

        Parameters
        ----------
        cx_receipt_hash : str

        Returns
        -------
        CXReceipt
        """
        resp = cx.get_cx_receipt_by_hash(self.url, cx_receipt_hash, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def pending_cx_receipts(self) -> List[PendingCXReceipt]:
        """
        Get the currently pending cross shard receipts

        Returns
        -------
        list[PendingCXReceipt]
        """
        resp = cx.get_pending_cx_receipts(self.url, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def resend_cx_receipt(self, cx_receipt_hash : str) -> bool:
        """
        Use this to resend the cross shard receipt to the receiving shard to re-process if the transaction did not pay out 

        Parameters
        ----------
        cx_receipt_hash : str

        Returns
        -------
        bool
            True if the resend was successful
        """
        resp = cx.resend_cx_receipt(self.url, cx_receipt_hash, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def call_smart_contract(self, to_address : str, block_number : str, from_address : Optional[str] = None, gas: Optional[int] = None, gas_price : Optional[int] = None, value : Optional[int] = None, data : Optional[str] = None) -> str:
        """
        Execute a smart contract call without saving state.

        Parameters
        ----------
        to_address : str
            The desitination wallet
        block_number: int
        from_address : str, optional
            The source address
        gas : int, optional
            Gas to execute the call
        gas_price : int, optional
            Gase price to execute the call
        value : int, optional
            Value sent with the smart contract
        data : str, optional
            Hash of smart contract method and parameters

        Returns
        -------
        str
            The return value of the call
        """
        resp = sc.call(self.url, to_address, block_number, from_address, gas, gas_price, value, data, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def estimate_smart_contract_gas_price(to_address : str, block_number : str, from_address : Optional[str] = None, gas: Optional[int] = None, gas_price : Optional[int] = None, value : Optional[int] = None, data : Optional[str] = None) -> str:
        """
        Executes a smart contract transction without creating a transaction and saving data


        Parameters
        ----------
        to_address : str
            The desitination wallet
        block_number: int
        from_address : str, optional
            The source address
        gas : int, optional
            Gas to execute the call
        gas_price : int, optional
            Gase price to execute the call
        value : int, optional
            Value sent with the smart contract
        data : str, optional
            Hash of smart contract method and parameters

        Returns
        -------
        str
            Hex of the estimated gas price
        """
        resp = sc.estimate_gas(self.url, to_address, block_number, from_address, gas, gas_price, value, data, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def get_smart_contract_code(self, address : str, block : Optional[str] = "latest", callback : Optional[str] = None) -> str:
        """
        Get the code at a specific address.

        Parameters
        ----------
        address: str
            The address to get the code from
        block: str, optional
            The block to query for information, defaults to 'latest'
        callback: str, optional
            Optional callback, returns an error object as first parameter and the result as second

        Returns
        -------
        str
            The data at the give address
        """
        resp = sc.get_code(self.url, address, block, callback, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result

    def get_value_at_smart_contract_storage(self, address : str, sotrage_location : str, block_number : int) -> str:
        """
        Get the value from a sotrage postition at a given address.

        Paramters
        ---------
        address : str
            The address of the storage
        storage_location : str
            Hex representation of the storage location
        block_number : int
            The block number

        Returns
        -------
        str
            The value stored at the smart contract location
        """
        resp = sc.get_storage_at(self.url, address, storage_location, block_number, self.session)
        if resp.error is not None:
            raise HarmonyNodeError("The Node responded with the following error.\nCode {}: {}".format(resp.error["code"], resp.error["message"]))
        return resp.result
    