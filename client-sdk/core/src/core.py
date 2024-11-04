import json

#function to serialize arguments
def serializeArgs(*args) -> str:
    return json.dumps(args)

#function to deserialize arguments
def deserializeResponse(response: str) -> any:
    return json.loads(response)

def callFunction(function_name: str, *args: list) -> any:
    print(f"Calling function '{function_name}' with arguments {args}")
    result = f"Result of {function_name} with args {args}"
    return result


def getFunctionResult(request_id: str) -> any:
    print(f"Retrieving result for request ID '{request_id}'")
    result = f"Result for request ID {request_id}"
    return result
