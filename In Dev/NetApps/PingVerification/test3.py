import subprocess
  
out = subprocess.run(['ping', 'google.com'], capture_output=True)
print(out.stdout.decode())