import requests
import json

def pin_to_ipfs(data):
    assert isinstance(data, dict), "Error: pin_to_ipfs expects a dictionary"
    json_data = json.dumps(data)
    ipfs_url = "https://ipfs.infura.io:5001/api/v0/add"
    files = {'file': json_data}
    response = requests.post(ipfs_url, files=files)
    
    if response.status_code == 200:
        result = response.json()
        cid = result['Hash']
        return cid
    else:
        raise Exception("Failed to pin data to IPFS via Infura")

def get_from_ipfs(cid, content_type="json"):
    assert isinstance(cid, str), "Error: get_from_ipfs expects CID as a string"
    ipfs_url = "https://ipfs.infura.io:5001/api/v0/cat"
    response = requests.post(ipfs_url, params={'arg': cid})
    
    if response.status_code == 200:
        data = response.json()
        assert isinstance(data, dict), "Error: get_from_ipfs should return a dictionary"
        return data
    else:
        raise Exception("Failed to retrieve data from IPFS via Infura")

def get_from_ipfs_pinata(cid, content_type="json"):
    assert isinstance(cid, str), "Error: get_from_ipfs expects CID as a string"
    ipfs_url = f"https://gateway.pinata.cloud/ipfs/{cid}"
    response = requests.get(ipfs_url)
    
    if response.status_code == 200:
        data = response.json()
        assert isinstance(data, dict), "Error: get_from_ipfs should return a dictionary"
        return data
    else:
        raise Exception("Failed to retrieve data from IPFS via Pinata")
