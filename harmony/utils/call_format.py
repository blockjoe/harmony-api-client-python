import json
from typing import Any, Dict, Optional

from pydantic import BaseModel

def format_api_call(method : str, param_model : BaseModel, request_id : Optional[str] = "1", jsonrpc : Optional[str] = "2.0") -> Dict[str, Any]:
    data = {}
    data["jsonrpc"] = jsonrpc
    data["id"] = request_id
    data["method"] = method
    data["params"] = list(param_model.dict().values())
    return data