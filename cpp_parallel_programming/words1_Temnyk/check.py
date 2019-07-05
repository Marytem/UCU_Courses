import subprocess
import os
times = [];
for _ in range(10):
    p=subprocess.Popen([os.getcwd()+'/words'],stdout=subprocess.PIPE)
    out, err = p.communicate()
    times.append(float(out.split()[5]))

print(min(times))

