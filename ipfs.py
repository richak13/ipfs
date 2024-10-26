import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	json_data = json.dumps(data)
	url = "https://ipfs.io/api/v0/add"
	files = {
			'file': ('data.json', json_data)
	}
	response = requests.post(url, files=files)
	cid = response.json()['Hash']

	return cid

def get_from_ipfs(cid,content_type="json"):
	
    assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
    url = f"https://ipfs.io/ipfs/{cid}"
    response = requests.get(url)
    data = response.json()

    assert isinstance(data,dict), f"get_from_ipfs should return a dict"
    return data

# import requests
# import json

# def pin_to_ipfs(data):
#     assert isinstance(data, dict), "Error: pin_to_ipfs expects a dictionary"
#     json_data = json.dumps(data)
    
#     # Using Infura endpoint for pinning
#     url = "https://ipfs.io/api/v0/add"
#     files = {'file': ('data.json', json_data)}
#     response = requests.post(url, files=files)

#     response = requests.post(url, files=files)
#     cid = response.json()['Hash']

#     return cid
    
    

# def get_from_ipfs(cid, content_type="json"):
#     assert isinstance(cid, str), "Error: get_from_ipfs expects a CID as a string"
    
#     # Accessing the data via Infura gateway
#     url = f"https://ipfs.infura.io:5001/api/v0/cat?arg={cid}"
#     response = requests.post(url)
    
#     # Check if response is successful and content type is JSON
#     if response.status_code == 200:
#         try:
#             data = response.json()
#             assert isinstance(data, dict), "Error: get_from_ipfs should return a dictionary"
#             return data
#         except ValueError:
#             raise Exception("Error: The retrieved data is not in JSON format.")
#     else:
#         raise Exception(f"Failed to retrieve data from IPFS. Status code: {response.status_code}, Error: {response.text}")
