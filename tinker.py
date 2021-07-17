
def calculate_cw_values(f_target):
    delta_min = 10000000
    for step in range(1,2000):
        for divi in range(0,8):
            f = 125.6 * step / (divi+1)
            actual_delta = f_target - f
            delta = abs(actual_delta)
            if delta < delta_min:
                delta_min = delta
                actual_delta_target = actual_delta
                step_target = step
                divi_target = divi
                f_actual = f
    return (f_actual, actual_delta_target, step_target, divi_target)

def home_round(value):
    fp = int((value*100)%100)
    if fp>=50:
        return int(value)+1
    else:
        return int(value)

def calculate_cw_values_faster(f_target):
    delta_min = 1000
    step_best = 0
    div_best = 0
    for i in range(8):
        steps = f_target * (i+1) / 125.6
        #steps = round(steps, 0)
        #steps = int(steps)
        steps = home_round(steps)
        f_actual = 125.6 * steps / (i+1)
        delta = abs(f_target - f_actual)
        if delta < delta_min:
            delta_min = delta
            step_best = steps
            div_best = i
    return (step_best, div_best)

FREQ_MIN = 150
FREQ_MAX = 30000

'''
calc = {}
used = set()
for i in range(FREQ_MIN,FREQ_MAX):
    calc[i] = calculate_cw_values(i) 
    used.add(calc[i][3])

print(used)

max = 0
for rec in calc.values():
    if rec[2]>max:
        max = rec[2]
print(max)
'''

for i in range(FREQ_MIN, FREQ_MAX):
    (steps,div) = calculate_cw_values_faster(i)
    rec = calculate_cw_values(i)
    if rec[2] != steps or rec[3]!=div:
        print('incorrect',rec,steps,div)
    
