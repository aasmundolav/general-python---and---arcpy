import gzip, os
import shutil
print(__file__)
for file in os.listdir(os.path.dirname(__file__)):
    for f in [".gz", ".zip"]:
        if file.endswith(f):
            with gzip.open(file, 'rb') as f_in:
                with open(file.replace(f,""), 'wb') as f_out:
                    print "unzipping %s" % file
                    shutil.copyfileobj(f_in, f_out)
