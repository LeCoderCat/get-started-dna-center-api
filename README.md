[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/LeCoderCat/dna-center-api)

# get-started-dna-center-api
Example code on how to perform API calls to Cisco DNA Center using Python 3 and Postman.
The files included on this repository contain:

*Python 3 example code on how to generate the necessary JWT and subsequently do API calls to Cisco DNA Center. This would be the base code for any Python 3 script that would integrate with DNA Center.

*Postman collection to interact with DNA Center. One file for the JWT generation and examples of API calls.

## Instructions
The script should be run on the terminal on a device that has python3 and the required python packages installed.
You can find the packages needed listed on the file requirement.txt
The Postman collection requires Postman application to be installed on the computer where the API calls are to be performed, You can download the application at: https://www.postman.com/

### Setting Up to Run the script
Clone and Prep the Environment
    Clone the code repo
    git clone https://github.com/LeCoderCat/get-started-dna-center-api.git
    cd ssh-cisco-devices
   
### Setup Python Virtual Environment
    1. MacOS or Linux
    python3.6 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
        > Note: If on Linux, you will need to install the Python3.6 development files. On CentOS this is done with yum install -y python36u-devel
    2. Windows - recommendation to use git-bash terminal
    py -3 -m venv venv
    source venv/Scripts/activate
    pip install -r requirements-win.txt
        > Note: Creation and activation of a venv in Windows is slightly different.
    
### Infrastructure Resources needed to run the script
    
In order to have access to Cisco DNA Center platform, you can use one of sandboxes available at Cisco's DEVNET site. These sandboxes are preconfigured labs with all resources dedicated to you for the duration of the reservation. You have the ability to install your own application and share the lab with other users.

To start using the content of this repo on Cisco DNA Center sandboxes, click [here](https://sandboxdnac.cisco.com/).

    User: devnetuser
    Password: Cisco123!

Or to directly test API calls on DNA Center, click [here](https://developer.cisco.com/docs/dna-center/api/1-3-3-x/#!intent-api-v1-3-3-x)

### How to run the script

Here you can find examples of the output of the script running. After running, insert the needed data in order to first retrieve the JWT and then to perform API call. Every input stream is followed by text that will have a suggestion on what field is required and an example of what can be input in the field. The script is able run several API calls until interrupted.

API_DNAC.py
```bash
MAC:ssh_scripts user$ python3 API_DNAC.py
Enter the IP of the DNAC (10.48.90.165): 10.48.90.165
Enter the username of the DNAC GUI (admin): admin	
Enter the DNAC GUI password (cisco!123): 
Enter the API [GET]URL (dna/intent/api/v1/topology/site-topology): dna/intent/api/v1/site
Status Code is: 200
Success!
Response is:
 {
    "response": [
        {
            "additionalInfo": [],
            "id": "c06f98d8-e8f1-4da5-9666-8610d38b1e48",
            "instanceTenantId": "SYS0",
            "name": "Global",
            "siteHierarchy": "c06f98d8-e8f1-4da5-9666-8610d38b1e48",
            "siteNameHierarchy": "Global"
        }
    ]
}
MAC:ssh_scripts user$ 
```

Postman collection

In case the DNA Center PKI is not natively recognized by the station where Postman is installed, please disable the certificate verification on Postman's settings:

![Postman settings](/img/disable_cert_ver.png)

After that, do an API call to generate the JWT (token) to authenticate (using GUI credentials, on the Authorization tab next to Params) and perform API calls:

![Postman Token Gen](/img/token1.png)

Use the generated token to perform API calls:

![Postman API call](/img/token2.png)

