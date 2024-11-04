import json
import aiohttp
import asyncio
import os

class Environment:
    DEVELOPMENT = "development"
    PRODUCTION = "production"

env = os.getenv("ENV", Environment.DEVELOPMENT)  #Defaults to development if ENV not set

async def callFunctionAsync(function_name: str, *args: list) -> any:
    if env == Environment.DEVELOPMENT:
        baseURL = "http://127.0.0.1:5000/"  #Local development server for testing
    else:
        baseURL = "https://production.example.com/"  #Placeholder for Osiris platform endpoint
    
    url = f"{baseURL}{function_name}"
    payload = json.dumps(args)#function args as JSON string payload
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, data=payload, headers={"Content-Type": "application/json"}) as response:#send POST request to url
                if response.status == 200:
                    return await response.json()
                else:#return error of HTTP status code is not 200
                    return {'error': f"HTTP Error: {response.status}", 'details': await response.text()}
        except Exception as e:#catches any other error
            return {'error': 'Exception', 'details': str(e)}

async def main():
    result = await callFunctionAsync("addNumbers", 2, 7)
    print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())
import json

#function to serialize arguments
def serializeArgs(*args) -> str:
    return json.dumps(args)

#function to deserialize arguments
def deserializeResponse(response: str) -> any:
    return json.loads(response)

def setTimeout(timeout: int) -> None:
    global timeout_duration
    if timeout <= 0:
        raise ValueError("Timeout must be a positive integer.")
    
    timeout_duration = timeout

def cancelRequest(request_id: str) -> bool:
    requests = []
    if request_id in requests: 
        requests.remove(request_id)
        return True
    else: 
        return False
    
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
