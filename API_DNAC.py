import requests, json, getpass, urllib3, ipaddress, sys
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#first function to generate JWT (necessary token to perform API calls)
def postAuthToken(dnac_IP, dnac_username , dnac_password):

    #To generate the token we need DNA Center GUI username and password
    data = dnac_username + ":" + dnac_password

    #DNA Center API call to generate the token
    URL = "https://" + dnac_IP + "/dna/system/api/v1/auth/token"

    header = {}
    header['content-type'] =  'application/json'

    req = requests.post(url=URL, verify=False, headers=header, auth=(dnac_username, dnac_password))

    token = req.content
    extract_token = json.loads(token)
    token_content = extract_token['Token']

    return [dnac_IP, token_content]

#Function to perform API call
def getSiteTopology(dnac_IP, APIcall, my_token):

    URL = "https://" + dnac_IP + "/" + APIcall
    header = {}
    header['content-type'] = 'application/json'
    header['x-auth-token'] = my_token
      
    req = requests.get(url=URL, verify=False, headers=header)

    cont = req.content

    #The reply will be on JSON format, therefore we are parsing the JSON content
    parsed_cont = json.loads(cont)
    json_cont = json.dumps(parsed_cont, indent=4, sort_keys=True)

    stat = req.status_code
    print ("Status Code is:", stat)

    if req.status_code == 200:
        print("Success!")
        print ("Response is:\n", json_cont)
    elif req.status_code == 401:
        print("Unauthorized.")

#variable input/verification and run functions
while True:

    try:
        set_dnac_IP = input("Enter the IP of the DNAC (10.48.90.165): ")
        ipaddress.ip_address(set_dnac_IP)
    except ValueError:
        print('Invalid input, try a valid IPv4 address format')
        continue

    set_username = input("Enter the username of the DNAC GUI (admin): ")
    set_password = getpass.getpass("Enter the DNAC GUI password (cisco!123): ")

    try:
        result = postAuthToken(set_dnac_IP, set_username, set_password)
    except:
        print('Token not generated, try a valid username/password')
        continue
    
    set_DNACIP = result[0]
    set_token = result[1]
    
    while True:

        try:
            set_APIcall = input("Enter the API [GET]URL (dna/intent/api/v1/topology/site-topology): ")
            result2 = getSiteTopology(set_DNACIP, set_APIcall, set_token)
        
        except KeyboardInterrupt:
            sys.exit()
        
        except:
            print('Invalid API call, try the URL in the format dna/intent/api/.... ')
            continue
            
