
import json

from apispec import APISpec
from pydantic import BaseModel, Field
from pydantic.schema import schema

from harmony.models import (
    CallParameters,
    CallRequest,
    CallResponse
)

def make_path_operations(request_name, response_name, tag=None, method_description=None, response_description=None):
    operations = {}
    post = {}
    if tag is not None:
        post["tags"] = [tag]
    if method_description is not None:
        post["description"] = method_description
    request_body = {}
    request_body["content"] = {"application/json" : { "schema" : request_name }}
    responses = {}
    if response_description is not None:
        responses["200"] = {"description" : response_description}
    responses["200"]["content"] = {"application/json" : { "schema" : response_name }}
    post["requestBody"] = request_body
    post["responses"] = responses
    operations["post"] = post
    return operations


def make_api_spec():
    spec = APISpec(
        title="Harmony",
        version="2.0.0",
        openapi_version="3.0.3",
        info=dict(description="Harmony API"),
    )
    spec.components.schema("CallRequest", CallRequest.schema())
    spec.components.schema("CallResponse", CallResponse.schema())
    spec.path(path="/hmyv2_call", operations=make_path_operations("CallRequest", "CallResponse", tag="Smart Contract", method_description="Executes a smart contract code without saving state", response_description="Return value of the executed smart contract"))
    
    return spec.to_dict()

def make_model_spec():
    models = [
        CallParameters,
        CallRequest,
        CallResponse
    ]
    s = schema(models, title="Harmony API Models")
    return s


if __name__ == "__main__":
    spec = make_api_spec()
    models = make_model_spec()
    with open("api.json", "w") as jf:
        jf.write(json.dumps(spec, indent=2))
    
    with open("models.json", "w") as mf:
        mf.write(json.dumps(models, indent=2))

