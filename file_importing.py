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
