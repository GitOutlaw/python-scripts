import os

results_file = open('results.txt', 'w')

ip_list = []

for ip in range(1,256):
    ip_list.append('192.168.1' + str(ip))
    
    
for ip in ip_list:
    response = os.popen(f'ping {ip} -n 1').read()
    if 'Received = 1' and 'Approximate' in response:
        print(f'UP {ip} Ping Successful' + '\n')
    else:
        print(f'DOWN {ip} Ping Unsuccessful' + '\n')
     
    

