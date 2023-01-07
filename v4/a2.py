from a1 import record, time, numpy, trigger, windowing


def do_record(current, ref_add):
    for j in range(0, 5):
        time.sleep(2)
        print(f"ready for run {j} - {current}")
        rec = record()
        numpy.save(f"recorded/a2/{current}_{j}{ref_add}.npy", trigger(rec, 2000))
        print("2s pause")


def correlation(signal, ref):
    std_signal = numpy.std(signal)
    std_ref = numpy.std(ref)
    mean_signal = numpy.mean(signal)
    mean_ref = numpy.mean(ref)
    n = len(signal)
    sig_fg = 0
    for j in range(n):
        sig_fg += (((ref[j] - mean_ref) * (signal[j] - mean_signal)) / n)
    r_fg = sig_fg / (std_signal * std_ref)
    return r_fg


TASKS = ['hoch', 'runter', 'links', 'rechts']

# do_record(TASKS[0], '')
# do_record(TASKS[1], '')
# do_record(TASKS[2], '')
# do_record(TASKS[3], '')
# do_record(TASKS[0], '_ref')
# do_record(TASKS[1], '_ref')
# do_record(TASKS[2], '_ref')
# do_record(TASKS[3], '_ref')
# do_record(TASKS[0], '_ref_lars')
# do_record(TASKS[1], '_ref_lars')
# do_record(TASKS[2], '_ref_lars')
# do_record(TASKS[3], '_ref_lars')
spec_arr = []

for t in TASKS:
    #print(t)
    windows = []
    windows_ref = []
    windows_ref_lars = []
    for i in range(0, 5):
        data = numpy.load(f"recorded/a2/{t}_{i}.npy")
        ref_data = numpy.load(f"recorded/a2/{t}_{i}_ref.npy")
        ref_lars_data = numpy.load(f"recorded/a2/{t}_{i}_ref_lars.npy")
        windows.append(windowing(data))
        windows_ref.append(windowing(ref_data))
        windows_ref_lars.append(windowing(ref_lars_data))
    spec = numpy.array(windows).mean(axis=0)
    spec_ref = numpy.array(windows_ref).mean(axis=0)
    spec_ref_lars = numpy.array(windows_ref_lars).mean(axis=0)

    spec_arr.append((spec, t))

    # print('Spec - Spec: ', correlation(spec, spec))
    # print('Spec - Spec_Ref: ', correlation(spec, spec_ref))
    # print('Spec - Spec_Ref_Lars: ', correlation(spec, spec_ref_lars))
    # print('Spec_Ref - Spec_Ref_Lars: ', correlation(spec_ref, spec_ref_lars))



def check_input(data):
    highest_corr = 0
    curr_task = None
    for spec, task in spec_arr:
        corr = correlation(data, spec)
        print(f"Task: {task} - Correlation: {corr}")
        if corr > highest_corr:
            highest_corr = corr
            curr_task = task
    print()
    return curr_task


hits = 0
misses = 0

hits_lars = 0
misses_lars = 0

for t in TASKS:
    for i in range(0, 5):
        data = numpy.load(f"recorded/a2/{t}_{i}_ref.npy")
        spec = windowing(data)

        guessed_tasked = check_input(spec)
        if guessed_tasked == t:
            hits += 1
        else:
            misses += 1

    for i in range(0, 5):
        data = numpy.load(f"recorded/a2/{t}_{i}_ref_lars.npy")
        spec = windowing(data)

        guessed_tasked = check_input(spec)
        if guessed_tasked == t:
            hits_lars += 1
        else:
            misses_lars += 1

print(f"Hits: {hits} - Misses: {misses}")
print(f"Accuracy: {hits / (hits + misses) * 100}%")

print(f"Hits: {hits_lars} - Misses: {misses_lars}")
print(f"Accuracy: {hits_lars / (hits_lars + misses_lars) * 100}%")


