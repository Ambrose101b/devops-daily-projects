import requests
import sys

url = "https://www.github.com"
print(f"Checking {url}...")

try:
    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        print("website is UP")
        sys.exit(0)
    else:
        print(f"Unexpected status: {response.status_code}")
        sys.exit(1)

except Exception as e:
    print(f"Website down ERROR: {e}")
    sys.exit(1)
