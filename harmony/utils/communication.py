import json
from typing import Any, Dict, Optional, Union

from pydantic import BaseModel
import requests

def post_request(url : str, data : Union[str, Dict[str, Any]], session : Optional[requests.Session] = None) -> requests.Response:
    """
    Post a request to the url with the given data,
    optionally using a provided session.
    Parameters
    ----------
    url: str
        The url to post to.
    data: dict[str, Any], str
        The json data to include in the post request.
    session: requests.Session, optional
        The persistent session to use, if None is provided
        a new one will be created and destroyed for the
        individual call.
    """
    if session is not None:
        return session.post(url, data=data)
    return requests.post(url, data=data)


def format_api_data(method : str, param_model : Optional[BaseModel], request_id : Optional[str] = "1", jsonrpc : Optional[str] = "2.0") -> str:
    data = {}
    data["jsonrpc"] = jsonrpc
    data["id"] = request_id
    data["method"] = method
    if param_model is None:
        data["params"] = []
    else:
        data["params"] = list(param_model.dict().values())
    return json.dumps(data)