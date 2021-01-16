from openapi_schema_pydantic import OpenAPI
from openapi_schema_pydantic.util import PydanticSchema, construct_open_api_with_schema_class

from harmony.models import (
    CallRequest,
    CallResponse
)

def construct_base_open_api() -> OpenAPI:
    return OpenAPI.parse_obj({
        "info" : {"title": "Harmony RPC V2 API", "version" : "2"},
        "paths" : {
            "/hmyv2_call" : {
                "description" : "Executes a smart contract code without saving state",
                "post" : {
                    "requestBody" : {"content" : {"application/json" : {
                      "schema" : PydanticSchema(schema_class=CallRequest)
                   }}},
                   "responses" : { "200": {
                     "description" : "Return value of the executed smart contract",
                     "content" : {"application/json" : {
                       "schema" : PydanticSchema(schema_class=CallResponse)
                     }},
                   }},
                }
            }

        }
    })

if __name__ == "__main__":
    open_api = construct_base_open_api()
    open_api = construct_open_api_with_schema_class(open_api)

    with open("api.json", 'w') as jf:
        jf.write(open_api.json(by_alias=True, exclude_none=True, indent=2))
