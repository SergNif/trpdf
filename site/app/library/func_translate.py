from pathlib import Path
import os
from library.translate import *
def translate(folder, filename):
    UPLOAD_FOLDER = folder
    pathlist = Path(UPLOAD_FOLDER).rglob('*.pdf')
    for path in pathlist:
        print(f'{str(path)=}  {UPLOAD_FOLDER=}')
        docum=fitz.Document(str(path))
        print(f'{type(docum)=}')
        translate_doc(doc=docum, folder=folder, filename=filename)
        if os.path.isfile(path=path):
            try:
                os.remove(path=path)
            except FileNotFoundError:
                print(f'file {path} not found')

        # because path is object not string