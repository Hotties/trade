import os
from datetime import datetime

FILE_NAME = 'first_run.txt'
is_ran = False

if not os.path.exists(FILE_NAME):
    is_ran = True

    with open(FILE_NAME, 'w') as f:
        f.write(datetime.now())
        