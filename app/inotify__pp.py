import inotify.adapters
from  translate_pdf import *
import config
# UPLOAD_FOLDER='/home/serg/python_proj/fastapi/uploadfiles/'

def _inotify():
    print(f'start inotify')
    i = inotify.adapters.Inotify()
    print(f'{config.UPLOAD_FOLDER=}')
    i.add_watch(config.UPLOAD_FOLDER)

    # with open(UPLOAD_FOLDER, 'w'):
    #     pass

    for event in i.event_gen(yield_nones=False,):
        (_, type_names, path, filename) = event
        list_path=[]
        list_filename=[]
        # print("PATH=[{}] FILENAME=[{}] EVENT_TYPES={}".format(
        #     path, filename, type_names))
        if ('IN_CLOSE_WRITE' in type_names)  :
            print(f'{path=} {filename=}')
            print('in if')
            list_path.append(path)
            list_filename.append(filename)
            list_path = list(map("".join, zip(list(list_path),list(list_filename))))
            print(f'{list_path=}')
            for file in list_path:
                print(f'{file=}')
                translate(file)

# PATH=[/tmp/test_file2] FILENAME=[] EVENT_TYPES=['IN_ACCESS', 'IN_ISDIR']
# PATH=[/tmp/test_file2] FILENAME=[] EVENT_TYPES=['IN_CLOSE_NOWRITE', 'IN_ISDIR']
# PATH=[/tmp/test_file2] FILENAME=[] EVENT_TYPES=['IN_OPEN', 'IN_ISDIR']
# PATH=[/tmp/test_file2] FILENAME=[] EVENT_TYPES=['IN_ACCESS', 'IN_ISDIR']
# PATH=[/tmp/test_file2] FILENAME=[] EVENT_TYPES=['IN_CLOSE_NOWRITE', 'IN_ISDIR']
# PATH=[/tmp/test_file2] FILENAME=[] EVENT_TYPES=['IN_OPEN', 'IN_ISDIR']
# PATH=[/tmp/test_file2] FILENAME=[] EVENT_TYPES=['IN_ACCESS', 'IN_ISDIR']
# PATH=[/tmp/test_file2] FILENAME=[] EVENT_TYPES=['IN_CLOSE_NOWRITE', 'IN_ISDIR']
# PATH=[/tmp/test_file2] FILENAME=[runtime.txt] EVENT_TYPES=['IN_DELETE']
# PATH=[/tmp/test_file2] FILENAME=[] EVENT_TYPES=['IN_OPEN', 'IN_ISDIR']
# PATH=[/tmp/test_file2] FILENAME=[] EVENT_TYPES=['IN_ACCESS', 'IN_ISDIR']
# PATH=[/tmp/test_file2] FILENAME=[] EVENT_TYPES=['IN_CLOSE_NOWRITE', 'IN_ISDIR']
# PATH=[/tmp/test_file2] FILENAME=[runtime.txt] EVENT_TYPES=['IN_MOVED_TO']

# if __name__ == '__inotify__pp__':
_inotify()
    