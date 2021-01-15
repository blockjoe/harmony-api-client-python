from typing import Optional

import requests

from ..models import (
    CallParameters,
    CallResult,
    EstimateGasResult,
    GetCodeParameters,
    GetCodeResult,
    GetStorageAtParameters,
    GetStorageAtResult
)

def call(api_url : str, params : CallParameters, session : Optional[requests.Session] = None) -> CallResult:
    """
    params: CallParameters
    result: CallResult
    method: hmyv2_call
    """

def estimateGas(api_url : str, params : CallParameters, session : Optional[requests.Session] = None) -> EstimateGasResult:
    """
    params: CallParameters
    result: EstimateGasResult
    method: hmyv2_estimateGas
    """

def getCode(api_url : str, params : GetCodeParameters, session : Optional[requests.Session] = None) -> GetCodeResult:
    """
    params: GetCodeParameters
    result: GetCodeResult
    method: hmyv2_getCode
    """

def getStorageAt(api_url : str, params : GetStorageAtParameters, session : Optional[requests.Session] = None) -> GetStorageAtResult:
    """
    params: GetStorageAtParameters
    result: GetStorageAtResult
    method: hmyv2_getStorageAt
    """