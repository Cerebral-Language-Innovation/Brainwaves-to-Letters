import glob

def get_newer_files():
    path = 'sample_data'
    bites = []
    blinks = []
    files = glob.glob(path + '/*.csv')
    for f in files:
        if 'bad' not in f:
            if 'blink' in f:
                blinks.append(f)
            elif 'bite' in f:
                bites.append(f)
    return bites, blinks

def get_older_files():
    path = 'outdated_code/Bite and Blink Data Analysis v1'
    c1 = []
    c2 = []
    c3 = []
    files = glob.glob(path + "/*.csv")
    for f in files:
        if 'link_' in f or 'link.' in f:
            c1.append(f)
        elif 'ite_' in f or 'ite.' in f:
            c2.append(f)
        elif 'aseline_' in f or 'aseline.' in f:
            c3.append(f)
    return c1, c2, c3