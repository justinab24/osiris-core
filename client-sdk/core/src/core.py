import json

#function to serialize arguments
def serializeArgs(*args) -> str:
    return json.dumps(args)

#function to deserialize arguments
def deserializeResponse(response: str) -> any:
    return json.loads(response)

