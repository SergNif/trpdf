import os


def dubl_space_off(line: str) -> str:
    while '  ' in line:
        line = line.replace('  ', ' ')
    return line.replace('\n', '')

def distance_line(line: str) -> int:
    return (len(" ".join(line.split(' ')[:-1]))+1)/4

dct_dir = {}
dct_file = {}
with open("/home/serg/python311_proj/fastapi/app/tree.txt", 'r') as f:
    for ix, line in enumerate(f):

        no_dubl_line = dubl_space_off(line)
        if ('.' in no_dubl_line) and (len(no_dubl_line.strip()) == 1):
            continue
        if '.' in no_dubl_line:
            distance = distance_line(line)
            dct_file[ix] = [distance, line.split(' ')[-1].replace('\n','')]
        else:
            distance = distance_line(line)
            dct_dir[ix] = [distance, line.split(' ')[-1].replace('\n','')]

f.close()
print(f'{dct_dir=}')
print(f'{dct_file=}')


def create_file(name: str):
    f = open(name, 'w', encoding="utf-8")
    f.closed


def make_dir(path: str):
    try:
        os.makedirs(name=path, exist_ok=False)
    except FileExistsError:
        pass


def find_nearest_min_key_dir(num_key: int) -> list:
    res = 0
    last_elem_dict = False
    for ix, (key, val) in enumerate(dct_dir.items()):
        # print(f'{ix=} {len(dct_dir.items())=}')
        # if ix == len(dct_dir.items())-1:
        #     last_elem_dict = True
        #     res = ix
        #     break
        if key > num_key:
            res = ix-1
            break
        res=ix

    # if res > 0:
    #     res -= 1
    # else:
    #     return [0, '']

    while (res>=0) and (dct_file[num_key][0] <= list(dct_dir.items())[res][1][0]):
        res -= 1
        # print(f'{num_key=} {res=}  {dct_file[num_key]=}')
        # print(f'{list(dct_dir.items())[res][1]=}')
        # print(f'dct_file {"" if res<0 else list(dct_dir.items())[res][1]}')
    
    if res<0:
        result = [0, '']
    else:
        result = list(dct_dir.items())[res][1]

    return result 

    # if dct_file[num_key][0] >= list(dct_dir.items())[res][1][0]:
    #     print(f'{num_key=} {res=}  {dct_file[num_key]=}')
    #     print(f'{list(dct_dir.items())[res][1]=}')
    #     print(f'dct_file {"" if res-1<0 else list(dct_dir.items())[res-1][1]}')
    #     return [0, ''] if res-1<0 else list(dct_dir.items())[res-1][1]


    # return list(dct_dir.items())[res][1]


order_dir = 0
for key, val in dct_file.items():
    # print(f'onee  {key} {val}')
    list_folder = [x for x in find_nearest_min_key_dir(key)]

    folder = '' if len(list_folder[1]) == 0 else list_folder[1]+'/'
    print(f'{folder}{val[1]}')
