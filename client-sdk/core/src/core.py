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
