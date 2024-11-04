import json

#function to serialize arguments
def serializeArgs(*args) -> str:
    return json.dumps(args)

#function to deserialize arguments
def deserializeResponse(response: str) -> any:
    return json.loads(response)

def handleFunctionError(error_code: int, error_message: str) -> None:

    print(f"Error {error_code}: {error_message}")
    
    error_actions = {
        #list of common errors encountered
        #For now we create a dictionary and then later depending on the functions we can implement error logging with docker, call a specfic function etc. 
        400: "Can be extended to log the error, retry the function call, or take other appropriate actions.",
        401: "Can be extended to log the error, retry the function call, or take other appropriate actions.",
        403: "Can be extended to log the error, retry the function call, or take other appropriate actions.",
        404: "Can be extended to log the error, retry the function call, or take other appropriate actions.",
        408: "Can be extended to log the error, retry the function call, or take other appropriate actions.",
        429: "Can be extended to log the error, retry the function call, or take other appropriate actions.",
        500: "Can be extended to log the error, retry the function call, or take other appropriate actions.",
        502: "Can be extended to log the error, retry the function call, or take other appropriate actions.",
        503: "Can be extended to log the error, retry the function call, or take other appropriate actions.",
        504: "Can be extended to log the error, retry the function call, or take other appropriate actions.",
    }

    #if it is another error other than the one in the dictionary above, then just return like default msg
    if error_code in error_actions:
        print(f"Action: {error_actions[error_code]}")
    else:
        print("Unhandled error.")


# checking 
# handleFunctionError(404, "Function not found")
# handleFunctionError(500, "Internal server error")
# handleFunctionError(429, "Too many requests")
