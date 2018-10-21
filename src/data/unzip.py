import os
import zipfile
import glob2

import settings

fns = glob2.glob(settings.EXTERNAL_DATA + '/*.zip')

for fn in fns:
    out_dir = '/'.join(fn.split('.')[:-1]).replace('external', 'raw')
    if os.path.exists(out_dir):
        continue
    zip_ref = zipfile.ZipFile(fn, 'r')
    zip_ref.extractall(out_dir)
    zip_ref.close()


