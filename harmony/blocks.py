from typing import Optional

import requests

from .models import (
    AddressListResponse,
    BlockConfig,
    BlockNumberParameters,
    BlockResponse,
    BlocksListConfig,
    BlockListParams,
    BlockListResponse,
    BLSKeyListResponse,
    GetBlockByHashParameters,
    GetBlockByNumberParameters,
    GetLatestChainHeadersResponse,
    HashParameters,
    HeaderResponse,
    TransactionCountResponse
)

from .endpoints.blockchain import (
    getBlocks,
    getBlockByHash,
    getBlockByNumber,
    getBlockSigners,
    getBlockSignersKeys,
    getBlockTransactionCountByHash,
    getBlockTransactionCountByNumber,
    getHeaderByNumber,
    getLatestChainHeaders,
    latestHeader,
)

def get_blocks_from_range(api_url : str, starting_block_number : int, ending_block_number : int, include_signer_addresses : Optional[bool] = False, include_transactions : Optional[bool] = False, include_staking_transactions : Optional[bool] = False, session : Optional[requests.Session] = None) -> BlockListResponse:
    """
    Get the blocks in the given range

    Parameters
    ----------
    api_url : str
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
    session : requests.Session, optional

    Returns
    -------
    result : list[Block]
    """
    list_opts = BlockConfig(withSigners=include_signer_addresses, fullTx=include_transactions, inclStaking=include_staking_transactions)
    params = BlockListParams(start_block=starting_block_number, end_block=ending_block_number, blocks_config=list_opts)
    return getBlocks(api_url, params, session)

def get_block_by_number(api_url : str, block_number : int, include_full_transaction_data : Optional[bool] = False, include_regular_transactions : Optional[bool] = False, include_staking_transactions : Optional[bool] = False, session : Optional[requests.Session] = None) -> BlockResponse:
    """
    Get the block of the specified block number.

    Parameters
    ----------
    api_url : str
    block_number : int
    include_full_transaction_data : bool, optional
        Whether to include full transaction data; defaults to False
    include_regular_transactions : bool, optional
        Whether to include regular transactions; defaults to False
    include_staking_transactions : bool, optional
        Whether to include staking transactions; defaults to False
    session : requests.Session

    Returns
    -------
    result : Block
    """
    block_opts = BlockConfig(fullTx=include_full_transaction_data, inclTx=include_regular_transactions, inclStaking=include_staking_transactions)
    params = GetBlockByNumberParameters(block_number=block_number, block_config=block_opts)
    return getBlockByNumber(api_url, params, session)

def get_block_by_hash(api_url : str, block_hash : str, include_full_transaction_data : Optional[bool] = False, include_regular_transactions : Optional[bool] = False, include_staking_transactions : Optional[bool] = False, session : Optional[requests.Session] = None) -> BlockResponse:
    """
    Get the block of the specified block number.

    Parameters
    ----------
    api_url : str
    block_hash : str
    include_full_transaction_data : bool, optional
        Whether to include full transaction data; defaults to False
    include_regular_transactions : bool, optional
        Whether to include regular transactions; defaults to False
    include_staking_transactions : bool, optional
        Whether to include staking transactions; defaults to False
    session : requests.Session

    Returns
    -------
    result : Block
    """
    block_opts = BlockConfig(fullTx=include_full_transaction_data, inclTx=include_regular_transactions, inclStaking=include_staking_transactions)
    params = GetBlockByHashParameters(block_hash=block_hash, block_config=block_opts)
    return getBlockByNumber(api_url, params, session)

def _get_block_signers(api_url : str, starting_block_number : int, ending_block_number : int, include_signer_addresses : Optional[bool] = False, include_transactions : Optional[bool] = False, include_staking_transactions : Optional[bool] = False, session : Optional[requests.Session] = None) -> AddressListResponse:
    """
    Get the wallet addresses signers of the block

    NOTE: This is how the getBlockSigners method is documented, but I don't think this is right.

    Parameters
    ----------
    api_url : str
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
    session : requests.Session, optional

    Returns
    -------
    result : list[str]
        List of addresses
    """
    list_opts = BlockConfig(withSigners=include_signer_addresses, fullTx=include_transactions, inclStaking=include_staking_transactions)
    params = BlockListParams(start_block=starting_block_number, end_block=ending_block_number, blocks_config=list_opts)
    return getBlockSigners(api_url, params, session)

def get_block_signers(api_url : str, block_number : int, session : Optional[requests.Session] = None) -> AddressListResponse:
    """
    Get the addresses of signers on the block

    NOTE: This doesn't match the docs, but I'm pretty sure this is how it should work.

    Parameters
    -----------
    api_url : str
    block_number : int
    session : requests.Session, optional

    Returns
    -------
    result : list[str]
        List of addresses
    """
    params = BlockNumberParameters(block_number=block_number)
    return getBlockSigners(api_url, params, session)

def get_block_signers_keys(api_url : str, block_number : int, session : Optional[requests.Session] = None) -> BLSKeyListResponse:
    """
    Get the public keys of signers on the block

    NOTE: This doesn't match the docs, but I'm pretty sure this is how it should work.

    Parameters
    -----------
    api_url : str
    block_number : int
    session : requests.Session, optional

    Returns
    -------
    result : list[str]
        List of public keys
    """
    params = BlockNumberParameters(block_number=block_number)
    return getBlockSignersKeys(api_url, params, session)

def get_block_transaction_count_by_number(api_url : str, block_number : int, session : Optional[requests.Session] = None) -> TransactionCountResponse:
    """
    Get the number of transactions on the given block

    Parameters
    ----------
    api_url : str
    block_number : int
    session : requests.Session, optional

    Returns
    -------
    result : int
        The number of transactions on the block
    """
    params = BlockNumberParameters(block_number=block_number)
    return getBlockTransactionCountByNumber(api_url, params, session)

def get_block_transaction_count_by_hash(api_url : str, block_hash : str, session : Optional[requests.Session] = None) -> TransactionCountResponse:
    """
    Get the number of transactions on the given block

    Parameters
    ----------
    api_url : str
    block_hash : str
    session : requests.Session, optional

    Returns
    -------
    result : int
        The number of transactions on the block
    """
    params = HashParameters(block_hash=block_hash)
    return getBlockTransactionCountByHash(api_url, params, session)

def get_block_header_by_number(api_url : str, block_number : int, session : Optional[requests.Session] = None) -> HeaderResponse:
    """
    Get the header of the block

    Parameters
    ----------
    api_url : str
    block_number : int
    session : requests.Session, optional

    Parameters
    Returns
    -------
    result : Header
    """
    params = BlockNumberParameters(block_number=block_number)
    return getHeaderByNumber(api_url, params, session)

def get_latest_chain_headers(api_url : str, session : Optional[requests.Session] = None) -> GetLatestChainHeadersResponse:
    """
    Get the latest headers of the chains

    Parameters
    ----------
    api_url : str
    session : requests.Session, optional

    Returns
    -------
    result : LatestChainHeaders
    """
    return getLatestChainHeaders(api_url, session)

def get_latest_block_header(api_url : str, session : Optional[requests.Session] = None) -> HeaderResponse:
    """
    Get the header of the latest block

    Parameters
    ----------
    api_url : str
    session : requests.Sesison, optional

    Returns
    -------
    result : Header
    """
    return latestHeader(api_url, session)
