import os

# List - Google DNS and Gateway IP address
ip_list = ['8.8.8.8', '192.168.0.1']


for ip in ip_list:
    response = os.popen(f'ping {ip} -n 1').read()
    if 'Received = 1' and 'Approximate' in response:
        print(f'UP {ip} Ping Successful' + '\n')
    else:
        print(f'DOWN {ip} Ping Unsuccessful' + '\n')
     
