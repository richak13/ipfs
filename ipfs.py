import requests
import json

def pin_to_ipfs(data):
    assert isinstance(data, dict), "Error: pin_to_ipfs expects a dictionary"
    json_data = json.dumps(data)
    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    headers = {
        'Content-Type': 'application/json',
        'pinata_api_key': '15e6e2c3bd7b6610a7cf',
        'pinata_secret_api_key': '1cde024c70d3deff5b8bec33aba4d14f542be3200f53ffc4853df6fdaa475a8a'
    }
    
    response = requests.post(url, data=json_data, headers=headers)
    
    if response.status_code == 200:
        # Extract and return the CID (IpfsHash) from the response
        cid = response.json().get('IpfsHash')
        return cid
    else:
        # Raise an error if the request fails
        raise Exception(f"Failed to pin data to IPFS. Status code: {response.status_code}, Error: {response.text}")

def get_from_ipfs(cid, content_type="json"):
    assert isinstance(cid, str), "Error: get_from_ipfs expects a CID as a string"
    
    # Pinata gateway URL for retrieving data
    url = f"https://gateway.pinata.cloud/ipfs/{cid}"
    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            data = response.json()
            assert isinstance(data, dict), "Error: get_from_ipfs should return a dictionary"
            return data
        except ValueError:
            raise Exception("Error: The retrieved data is not in JSON format.")
    else:
        raise Exception(f"Failed to retrieve data from IPFS. Status code: {response.status_code}, Error: {response.text}")
