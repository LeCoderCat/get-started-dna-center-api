import requests, json, getpass, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def postAuthToken(dnac_IP, dnac_username , dnac_password):

    data = dnac_username + ":" + dnac_password

    URL = "https://" + dnac_IP + "/dna/system/api/v1/auth/token"

    header = {}
    header['content-type'] =  'application/json'

    req = requests.post(url=URL, verify=False, headers=header, auth=(dnac_username, dnac_password))

    token = req.content
    extract_token = json.loads(token)
    token_content = extract_token['Token']

    return [dnac_IP, token_content]

def getSiteTopology(dnac_IP, APIcall, my_token):

    URL = "https://" + dnac_IP + "/" + APIcall
    header = {}
    header['content-type'] = 'application/json'
    header['x-auth-token'] = my_token
      
    req = requests.get(url=URL, verify=False, headers=header)

    cont = req.content

    parsed_cont = json.loads(cont)
    json_cont = json.dumps(parsed_cont, indent=4, sort_keys=True)

    stat = req.status_code
    print "Status Code is:", stat

    if req.status_code == 200:
        print("Success!")
        print "Response is:\n", json_cont
    elif req.status_code == 401:
        print("Unauthorized.")

set_dnac_IP = raw_input("Enter the IP of the DNAC: ")
set_username = raw_input("Enter the username of the DNAC GUI: ")
set_password = getpass.getpass("Enter the DNAC GUI password: ")
result = postAuthToken(set_dnac_IP, set_username, set_password)
set_DNACIP = result[0]
set_token = result[1]
set_APIcall = raw_input("Enter the API [GET]URL (dna/intent/api/v1/topology/site-topology): ")
result2 = getSiteTopology(set_DNACIP, set_APIcall, set_token)