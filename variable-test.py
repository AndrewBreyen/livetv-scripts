import logging
import os
import sys
import time
from pathlib import Path
from time import strftime



from dotenv import load_dotenv, dotenv_values 

load_dotenv()

print(os.getenv("TESTENV"))



# /path/to/series/show/season/vid.ext
file_path = sys.argv[1]

####
#### FILE_PATH
####
# Full path to source .ts file
print('file_path:')
print(file_path)
print('')

# vid
print('basename_int:')
basename_int = os.path.basename(file_path).rsplit('.', 1)
print(basename_int)

basename_int = basename_int[0].replace('.',' ')
print(file_path)


basename = basename_int
print('basename:')
print(basename)
print('')



# vid.ext
file_name = os.path.basename(file_path)
print('file_name:')
print(file_name)
print('')

# /path/to/series/show/season/
vid_dir = str(Path(file_path).parents[0])

print('vid_dir:')
print(vid_dir)
print('')





# vid.mp4
out_file = basename + ".mp4"

print('out_file:')
print(out_file)
print('')

####
#### OUT_PATH
####
# Full path to .mp4, periods removed
# /path/to/series/show/season/vid.mp4
out_path = vid_dir + "/" + out_file

print('out_path:')
print(out_path)
print('')


# /path/to/OLDFILES
move_to = str(Path(file_path).parents[2]) + "/OLDFILES"

print('move_to:')
print(move_to)
print('')


# /path/to/OLDFILES/BAK_vid.ext
bak_file_path = move_to + "/BAK_" + file_name

print('bak_file_path:')
print(bak_file_path)
print('')