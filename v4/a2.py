from a1 import record, time, numpy, trigger, windowing, plt


def do_record(current, ref_add):
    for j in range(0, 5):
        time.sleep(2)
        print(f"ready for run {j} - {current}")
        rec = record()
        numpy.save(f"recorded/a2/{current}_{j}{ref_add}.npy", trigger(rec, 2000))
        print("2s pause")


TASKS = ['hoch', 'runter', 'links', 'rechts']

# do_record(TASKS[0], '')
# do_record(TASKS[1], '')
# do_record(TASKS[2], '')
# do_record(TASKS[3], '')
# do_record(TASKS[0], '_ref')
# do_record(TASKS[1], '_ref')
# do_record(TASKS[2], '_ref')
# do_record(TASKS[3], '_ref')
do_record(TASKS[0], '_ref_lars')
do_record(TASKS[1], '_ref_lars')
do_record(TASKS[2], '_ref_lars')
do_record(TASKS[3], '_ref_lars')

for t in TASKS:
    print(t)
    windows = []
    for i in range(0, 5):
        data = numpy.load(f"recorded/a2/{t}_{i}.npy")
        windows.append(windowing(data))
    spec = numpy.array(windows).mean(axis=0)
    plt.plot(spec)
    plt.title(t)
    plt.savefig(f"plots/{t}_spectrum.png")
    plt.show()
