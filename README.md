# retry-decorator

Python retry decorator with exponential backoff and jitter.

## Features
- Configurable max attempts
- Exponential backoff with cap
- Optional jitter to avoid thundering herd
- Custom exception filtering

## Usage
```python
from retrylib import retry

@retry(max_attempts=5, backoff=0.5, exceptions=(IOError, TimeoutError))
def fetch_data(url):
    ...
```

## License
MIT
