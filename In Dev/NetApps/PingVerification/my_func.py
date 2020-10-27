import subprocess


def ping_test():
    out = subprocess.run(['ping', 'google.com'], capture_output=True)
    print('...ping google.com...')
    print(out.stdout.decode())



