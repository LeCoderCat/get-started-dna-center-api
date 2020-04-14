# dna-center-api
Example code on how to perform API calls to Cisco DNA Center using Python 3 and Postman.
The files included on this repository contain:
1. Python 3 example code on how to generate the necessary JWT and subsequently do API calls to Cisco DNA Center. This would be the base code for any Python 3 script that would integrate with DNA Center.
2. Postman collection to interact with DNA Center. One file for the JWT generation and examples of API calls.

## Instructions
The script should be run on the terminal on a device that has python3 and the required python packages installed.
You can find the packages needed listed on the file requirement.txt
The Postman collection requires Postman application to be installed on the computer where the API calls are to be performed, You can download the application at: https://www.postman.com/

### Setting Up to Run the script
Clone and Prep the Environment
    Clone the code repo
    git clone https://github.com/LeCoderCat/dna-center-api.git
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
    
In order to have access to Cisco DNA Center platform, you can use reservation-based sandboxes available at Cisco's DEVNET site. These sandboxes are private, preconfigured labs with all resources dedicated to you for the duration of the reservation. You have the ability to install your own application and share the lab with other users.

To access Cisco DNA Center sandboxes, click [here](https://developer.cisco.com/docs/dna-center/#!sandboxes/cisco-dna-center-sandboxes).

### How to run the script

Here you can find examples of the output of the script running. After running insert the needed data in order to first retrieve the JWT and then to perform API call. Every input stream is followed by text that will have a suggestion on what field is required and an example of what can be input in the field. 

DNAC_SSH.py (same way to run DNAC.py)
```bash
MAC:ssh_scripts user$ python3 DNAC_SSH.py 
Logged in DNAC. . .

logout 
NAMESPACE                  NAME                                                     READY     STATUS      RESTARTS   AGE       IP              NODE            NOMINATED NODE
assurance-backend          collector-cli-5fc77585d8-79ttt                           1/1       Running     1          40d       172.31.5.6      192.168.21.18   <none>
assurance-backend          collector-iosxe-db-5b6856d9f6-n4bxd                      1/1       Running     1          40d       172.31.5.28     192.168.21.18   <none>
assurance-backend          grpc-collector-6d9f8776c9-mt4v6                          1/1       Running     1          40d       192.168.21.18   192.168.21.18   <none>
assurance-backend          nsa-webapp-5c955f6dd-g7wjx                               1/1       Running     1          40d       172.31.4.244    192.168.21.18   <none>
assurance-backend          serviceability-656f45df7b-kf56l                          1/1       Running     1          40d       172.31.5.45     192.168.21.18   <none>
assurance-backend          skype-collector-7d6d588cc-6q7jw                          1/1       Running     1          40d       172.31.4.207    192.168.21.18   <none>
assurance-backend          wirelesscollector-bf99f5f99-jhjjm                        1/1       Running     1          40d       172.31.4.247    192.168.21.18   <none>
dnacaap                    daas-runtime-85858c9bdf-jk6tn                            1/1       Running     1          40d       172.31.4.240    192.168.21.18   <none>
<...>
dnacaap                    dna-event-runtime-6d749f8b9d-ff497                       1/1       Running     1          40d       172.31.4.194    192.168.21.18   <none>
ndp                        redis-0                                                  2/2       Running     3          40d       172.31.4.249    192.168.21.18   <none>
ndp                        schemaregistry-5c948f8f8b-q5g5w                          1/1       Running     1          40d       172.31.4.250    192.168.21.18   <none>
ndp                        writestore-6fcd4798c8-h6rlf                              1/1       Running     4          40d       172.31.4.205    192.168.21.18   <none>
sensor-assurance-backend   sensor-assurance-backend-66cbffd66d-rmq7t                1/1       Running     1          40d       172.31.4.195    192.168.21.18   <none>
MAC:ssh_scripts user$ 
```

PRIME_SSH.py
```bash
MAC:ssh_scripts user$ python3 PRIME_SSH.py 
Logged in Prime. . .

show clock

exit

WARNING: Unsuccessful login attempts :

admin    ssh:notty    Thu Feb 20 22:25 - 22:25  (00:00)     192.168.0.1
--------------------------------------
css-dna-pi/admin# show clock
Thu Feb 27 12:52:54 CET 2020
css-dna-pi/admin# exit
MAC:ssh_scripts user$
```
