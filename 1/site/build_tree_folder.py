import os


def dubl_space_off(line: str) -> str:
    while '  ' in line:
        line = line.replace('  ', ' ')
    return line.replace('\n', '')


def distance_line(line: str) -> int:
    return int((len(" ".join(line.split(' ')[:-1]))+1)/4)


dct_dir = {}
dct_file = {}
with open("/home/serg/python311_proj/fastapi/app/tree.txt", 'r') as f:
    for ix, line in enumerate(f):

        no_dubl_line = dubl_space_off(line)
        if ('.' in no_dubl_line) and (len(no_dubl_line.strip()) == 1):
            continue
        if '.' in no_dubl_line:
            distance = distance_line(line)
            dct_file[ix] = [distance, line.split(' ')[-1].replace('\n', '')]
        else:
            distance = distance_line(line)
            dct_dir[ix] = [distance, line.split(' ')[-1].replace('\n', '')]

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

        if key > num_key:
            res = ix-1
            break
        res = ix

    while (res >= 0) and (dct_file[num_key][0] <= list(dct_dir.items())[res][1][0]):
        res -= 1

    if res < 0:
        result = [[0, [0, '']], res]
    else:
        result = [list(dct_dir.items())[res], res]

    return result


for key, val in dct_file.items():

    list_folder = find_nearest_min_key_dir(key)

    name = list_folder[0][1][1]
    if list_folder[0][1][0] > 1:
        order_folder = list_folder[0][1][0]
        for el in range(list_folder[1], -1, -1):
            if order_folder > list(dct_dir.items())[el][1][0]:
                name = list(dct_dir.items())[el][1][1] + '/' + name
                if list(dct_dir.items())[el][1][0] == 1:
                    break

    folder = '' if len(list_folder[0][1][1]) == 0 else name+'/'
    print(f'{folder}\n{val[1]}')

    if len(folder) > 0:
        make_dir(path=folder)

    create_file(name=folder+val[1])
