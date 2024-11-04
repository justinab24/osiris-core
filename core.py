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


