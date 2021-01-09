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