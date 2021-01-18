from typing import Optional

import requests

from .models import (
    CallParameters,
    CallResponse,
    EstimateGasResponse,
    GetCodeParameters,
    GetCodeResponse,
    GetStorageAtParameters,
    GetStorageAtResponse,
    SmartContractCall
)

from .endpoints.smart_contract import (
    call_,
    estimateGas,
    getCode,
    getStorageAt   
)

def call(api_url : str, to_address : str, block_number : int,  from_address : Optional[str] = None, gas : Optional[int] = None, gas_price : Optional[int] = None, value : Optional[int] = None, data : Optional[str] = None, session : Optional[requests.Session] = None) -> CallResponse:
    """
    Executes a smart contract code without saving state
    
    Parameters
    ----------
    api_url : str
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
    session: requests.Session, optional

    Returns
    -------
    result : str
        The return value of the smart contract
    """
    sc = SmartContractCall(to=to_address, from_=from_address, gas=gas, gas_price=gas_price, value=value, data=data)
    params = CallParameters(smart_contract_call=sc, block_number=block_number)
    return call_(api_url, params, session)

def estimate_gas(api_url : str, to_address : str, block_number : int,  from_address : Optional[str] = None, gas : Optional[int] = None, gas_price : Optional[int] = None, value : Optional[int] = None, data : Optional[str] = None, session : Optional[requests.Session] = None) -> EstimateGasResponse:
    """
    Executes a smart contract transction without creating a transaction and saving data
    
    Parameters
    ----------
    api_url : str
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
    session: requests.Session, optional

    Returns
    -------
    result : str
        Hex of the esimtated gas price
    """
    sc = SmartContractCall(to=to_address, from_=from_address, gas=gas, gas_price=gas_price, value=value, data=data)
    params = CallParameters(smart_contract_call=sc, block_number=block_number)
    return estimateGas(api_url, params, session)

def get_code(api_url : str, address : str, block : Optional[str] = "latest", callback : Optional[str] = None, session : Optional[requests.Session] = None) -> GetCodeResponse:
    """
    Get the code at a specific address.

    Parameters
    ----------
    api_url : str
    address: str
        The address to get the code from
    block: str, optional
        The block to query for information, defaults to 'latest'
    callback: str, optional
        Optional callback, returns an error object as first parameter and the result as second
    session: requests.Session, optional

    Returns
    -------
    result : str
        The data at the give address
    """
    params = GetCodeParameters(address=address, block=block, callback=callback)
    return getCode(api_url, params, session)

def get_storage_at(api_url : str, address : str, storage_location : str, block_number : int, session : Optional[requests.Session] = None) -> GetStorageAtResponse:
    """
    Returns the value from a storage position at a given address.

    Parameters
    ----------
    api_url : str
    address : str
        The address of the storage
    storage_location : str
        Hex representation of the storage location
    block_number : int
        The block number
    session : requests.Session, optional

    Returns
    -------
    result : str
        The value stored at the smart contract location
    """
    params = GetStorageAtParameters(address=address, storage_location=storage_location, block_number=block_number)
    return getStorageAt(api_url, params, session)