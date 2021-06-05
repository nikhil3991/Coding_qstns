import subprocess
output=subprocess.Popen(["ls","-lrt"],stdout=subprocess.PIPE)
# output.communicate()
print(output.communicate())