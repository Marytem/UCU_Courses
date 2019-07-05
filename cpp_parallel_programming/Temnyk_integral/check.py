import subprocess
import os

abs_err = 0.001
rel_err = 0.001
steps_x = 800
steps_y = 800
num_thr = 100
lower_x = -10
upper_x = 10
lower_y = -10
upper_y = 10
results = []
times = []

for _ in range(10):
    p=subprocess.Popen([os.getcwd()+'/integral',str(abs_err),str(rel_err),str(steps_x),str(steps_y),
                        str(num_thr) ,str(lower_x), str(upper_x),str(lower_y),str(upper_y)],stdout=subprocess.PIPE)
    out, err = p.communicate()
    results.append(float(out.split()[0]))
    times.append(float(out.split()[1]))
if abs(max(results)-min(results))>2*abs_err:
    raise Error("Results are not in absolute error range!")

print(results)
print(min(times))

