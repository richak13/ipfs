import requests
import json

def pin_to_ipfs(data):
    assert isinstance(data, dict), "Error: pin_to_ipfs expects a dictionary"
    json_data = json.dumps(data)
    ipfs_url = "https://ipfs.infura.io:5001/api/v0/add"
    headers = {
        "Authorization": "Bearer f474620ee28c4a6185ac4f3facbd6cf6"  # replace if Infura requires API token in headers
    }
    files = {'file': json_data}
    response = requests.post(ipfs_url, files=files, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        cid = result['Hash']
        return cid
    else:
        print("Error:", response.status_code, response.content)
        raise Exception("Failed to pin data to IPFS via Infura")

def get_from_ipfs(cid):
    assert isinstance(cid, str), "Error: get_from_ipfs expects CID as a string"
    ipfs_url = "https://ipfs.infura.io:5001/api/v0/cat"
    headers = {
        "Authorization": "Bearer f474620ee28c4a6185ac4f3facbd6cf6"
    }
    response = requests.post(ipfs_url, params={'arg': cid}, headers=headers)
    
    if response.status_code == 200:
        try:
            data = json.loads(response.content.decode('utf-8'))
            assert isinstance(data, dict), "Error: get_from_ipfs should return a dictionary"
            return data
        except json.JSONDecodeError:
            raise Exception("Failed to parse JSON content from IPFS")
    else:
        print("Error:", response.status_code, response.content)
        raise Exception("Failed to retrieve data from IPFS via Infura")

