from base64 import encode
from distutils.command.config import config
import numbers
from pydoc import doc
from turtle import color, shape, width
from xml.dom.minidom import Document
import fitz
import tkinter
from typing import Iterable, List
import torch
# pip install sacremoses
# pip install transformers
from transformers import pipeline, AutoModelWithLMHead, AutoTokenizer, MarianMTModel, MarianTokenizer
from typing import Sequence
import shutil
import config


class Translator:
    def __init__(self, source_lang: str, dest_lang: str) -> None:
        self.model_name = f'Helsinki-NLP/opus-mt-{source_lang}-{dest_lang}'
        self.model = MarianMTModel.from_pretrained(self.model_name)
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)

    def delete_symbols(self, text:str) -> str:
        lst = list(set([f for f in text if ord(f)<32 or ord(f)>127]))
        if len(lst)>0:
            for el in lst:
                result = text.replace(el, '')
        else:
            result= text
        return result

    def translate(self, texts: Sequence[str]) -> Sequence[str]:
        texts[0] = self.delete_symbols(text= texts[0])
        print(f'translate text {texts[0]=}')
        tokens = self.tokenizer(list(texts), return_tensors="pt", padding=True)
        translate_tokens = self.model.generate(**tokens)
        return [self.tokenizer.decode(t, max_length=500, skip_special_tokens=True) for t in translate_tokens]


marian_en_ru = Translator('en', 'ru')
# p = marian_en_ru.translate(['The other kind of instance attribute reference is a method. A method is a function that “belongs to” an object. (In Python, the term method is not unique to class instances: other object types can have methods as well. For example, list objects have methods called append, insert, remove, sort, and so on. However, in the following discussion, we’ll use the term method exclusively to mean methods of class instance objects, unless explicitly stated otherwise.) Valid method names of an instance object depend on its class. By definition, all attributes of a class that are function objects define corresponding methods of its instances. So in our example, x.f is a valid method reference, since MyClass.f is a function, but x.i is not, since MyClass.i is not. But x.f is not the same thing as MyClass.f — it is a method object, not a function object.'])
# print(f'en -> ru {p[0]=}')


class Pagem():
    def __init__(self, page) -> None:
        self.klc = []
        self.klc3 = []
        self.fontsize = 10
        self.page = page
        self.text1 = page.get_text("dict")['blocks']

        self.width_page = page.mediabox.width
        self.height_page = page.mediabox.height
        # self.rect_width = float(page.get_text("dict")["width"])
        # self.rect_height = float(page.get_text("dict")["height"])
        self.make_klc()
        # print(f'{self.klc=}')
        # self.text2 = self._get_block_form_page(self.text1)
        # self.klc2 = [self.klc.index(
        #     g) for g in self.klc for k, _ in g.items() if k == "number"]
        # self.made_klc3(self.klc2)
        # # self.dell_empty_list_text()
        # self.sort_list_text()
        # self.add_list_image()
        print(f'end of initialization')

    def join_stroke(self):

        new_lst = []
        for idx, el in enumerate(self.klc):
            txt=[]
            if 'type' in el.keys():
                continue
            up_y = el['bbox'][3]
            text = ""
            lst = [txt.append([ix,j['text'], j['bbox']]) for ix,j in enumerate(self.klc) if j['bbox'][3]==up_y]
            new_lst.append(txt)

        b=[]
        for g in new_lst:
            textt=''
            for n in g:
                textt += n[1]
            b.append([g[0][0],textt, (g[0][2][0], g[0][2][1], g[-1][2][2], g[-1][2][3])])
        for n in b:
            
            gl=0
        
        # for m in b:
        #     print(f'{m=}')

        fb = []
        [fb.append(i) for i in b if i not in fb]
        # mnb=["".join(i) for i in b]
        result=[]
        for ix,m in enumerate(self.klc):
            if 'type' in m.keys():
                result.append(m)
                continue
            if len([x[1] for x in fb if x[0]==ix]) > 0:
                m['text'] = [x[1] for x in fb if x[0]==ix][0]
                m['bbox'] = [x[2] for x in fb if x[0]==ix][0]
                result.append(m)
        
        self.klc=[]
        self.klc=[a for a in result]



    def make_klc(self,):
        for number in self.text1:
            text_ru = ''
            if 'lines' in number.keys():
                ls_number = number['lines']
                for lines in ls_number:
                    ls_lines = lines['spans']
                    for span in ls_lines:
                        if span['text'].strip() == '.':
                            self.klc[-1]['text'] += '.'
                            text_ru += '.'
                            continue
                        span['text'] = span['text'].replace('\t', ' ') + ' '
                        self.klc.append(span)
                        text_ru += span['text'].replace('\t', ' ') + ' '
                last_elem_klc = {**self.klc[-1]}
                last_elem_klc_bbox = [el for el in self.klc[-1]['bbox']]
                lx = 35.0
                ly = last_elem_klc_bbox[3]
                rx = self.width_page-25
                ry = ly + 12
                last_elem_klc['text'] = '*ru-ru-ru*'

                lst = []
                lst.append(text_ru)
                text_ru = marian_en_ru.translate(lst)[0]

                last_elem_klc['text_ru'] = text_ru.strip()
                last_elem_klc['bbox'] = (lx, ly, rx, ry)
                if text_ru != '':
                    self.klc.append(last_elem_klc)
                print(
                    f'{text_ru=} \n {self.klc[-1]["text"]=} \n {lx=} \n {ly=} \n {rx=}  \n {ry=} \n {self.klc[-1]["bbox"]=}')
            if 'image' in number.keys():
                del number['number']
                # del number['image']
                self.klc.append(number)
        self.join_stroke()


class TakeList():  # ItemsDict
    def __init__(self, listt):
        self.list = listt.klc
        self.param = self.start()
        self.index = 0  # len(self.param)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.param):
            raise StopIteration
        self.index += 1
        return self.param[self.index-1]

    def start(self) -> List:
        param = []
        for elem in self.list:
            param.append(elem)
            print('*****************')
        return param


start_point_x = 35
start_point_y = 25
doc_new = fitz.Document()
offset = 0.0
offset_last_page = 0.0


class MakePDF():
    global start_point_x
    global start_point_y
    global doc_new
    global offset
    global offset_last_page

    def __init__(self, param: list, docum: Document, width: float, height: float):
        print(f'MakePDF init ')

        self.docum = docum
        self.params = param
        self.param = []
        self.offset = offset
        self.offset_last_page = offset_last_page

        # doc.name[:-4] + f"{'_add_stroke'}" + doc.name[-4:])
        self.doc_new = doc_new

        self.width_page = width
        self.height_page = height

        self.namefont = "figo"
        self.fontname = fitz.Font(self.namefont)
        self.fontsize = 10
        self.color_code_text = (0.1, 0.1, 0.1)
        self.color_text = (0.79, 0.33, 0.30)

        self.p = fitz.Point(start_point_x, start_point_y)
        self.left_up = fitz.Point(self.p)
        self.right_down = fitz.Point(self.p) + (15.0, 15.0)

        self.language = ["en", "ru"]

        # self.dictionar = self.diction
        # self.key, self.value = self.dictionar.items()
        # self.list_key = [k for k in self.dictionar.keys()][0]
        # self.index = len(self.list_key)

        self.page = None
        self.shape = None

    def make_rect(self, left_upx, left_upy, right_downx, right_downy):
        # if left_upy >= right_downy:
        #     self.right_down.y += (left_upy - right_downy)+ self.fontsize/3
        #     self.right_down.x = self.width_page
        print(
            f'make_rect {left_upx=}, {left_upy=},{right_downx=}, {right_downy=}')
        # (self.left_up.x, self.left_up.y, self.right_down.x, self.right_down.y)
        rect = fitz.Rect(left_upx, left_upy, right_downx, right_downy)
        return rect

    def create_text(self, language):
        if ("text_ru" not in self.param.keys()):
            language == 'en'
            text = '\v' + self.param["text"].replace('\t', ' ')
        if ("text_ru" in self.param.keys()):
            text = '\v' + self.param["text_ru"]
            language == "ru"
            # lst=[]

            # lst.append(text)
            # text = marian_en_ru.translate(lst)[0]
            # lst = text.split(' ')
            # text = " ".join([g for g in lst if '&' not in g ])
        print(f'{text=}')
        return text

    def make_paragraph_img(self, add_right_down_y):
        current_img = self.param['image']
        rect = self.make_rect(self.left_up.x,
                              self.left_up.y,
                              self.right_down.x,
                              self.right_down.y)

        img_xref = 0

        img_xref = self.page.insert_image(rect, stream=current_img,
                                          xref=img_xref, keep_proportion=False)

        # self.left_up.y = self.right_down.y
        # self.left_up.x = start_point_x
        # self.right_down.y += self.fontsize/3
        # self.right_down.x = self.width_page - 30

    def make_paragraph(self,  add_right_down_y):
        language = 'en'
        print(f'make_paragraph {self.right_down.y=}')
        rect = self.make_rect(left_upx=self.left_up.x,
                              left_upy=self.left_up.y,
                              right_downx=self.right_down.x,
                              right_downy=self.right_down.y + add_right_down_y)
        if ("text_ru" in self.param.keys()):
            language = 'ru'
        rc = self.shape.insert_textbox(
            rect,
            self.create_text(language),
            # '\t   ' + self.param[2]["text_en"] if language == "en" else  '\t  ' + self.param[3]["text_ru"],
            fontsize=self.fontsize,
            # self.param[6]["font"] if (self.param[6]["font"] is not None) else "helv",
            fontname=self.namefont,
            color=self.color_text if language == "en" else self.color_code_text,
            # encoding=fitz.TEXT_ENCODING_CYRILLIC,
            align="left",
        )
        print(f'{rc=}')
        # right_down.y -= 2
        print(f'make_paragraph {self.right_down.y=}')

        return rc

    def nnew_page(self):
        print(f'function nnew_page')

        self.page = self.doc_new.new_page(
            pno=-1, width=self.width_page, height=self.height_page)
        font = fitz.Font("figo")
        self.page.insert_font(encoding=2, fontname=self.namefont,  # fontsize=self.fontsize,  # 'figo',
                              fontbuffer=font.buffer, set_simple=False)  # add)
        # start point of 1st line

        self.shape = self.page.new_shape()

    def count_coords(self):
        get_text_page_blocks = doc_new[-1].get_text("blocks")
        get_text_page_dict = doc_new[-1].get_text("dict")
        # self.left_up.x, self.left_up.y, self.right_down.x = self.param["bbox"][:3]
        if len(get_text_page_blocks)==0:
            self.left_up = fitz.Point(self.param['bbox'][0], self.param['bbox'][1])
            self.right_down = fitz.Point(self.param['bbox'][2],  self.param['bbox'][3])
        else:
            self.left_up = fitz.Point( self.param['bbox'][0] , get_text_page_blocks[-1][3])
            self.right_down = fitz.Point(self.param['bbox'][2] , self.left_up.y + (self.param['bbox'][3] - self.param['bbox'][1]))

    def cickle_while(self, ):
        global offset

        self.count_coords()
        print(f'{self.left_up.x=} *** {self.left_up.y=} *** {self.right_down.x=} *** {self.right_down.y=} ')

        rc = 12
        print(f'before while {rc=}')

        g = {**self.param}  # {key: value for key, value in self.param}
        if ('image' in g.keys()):
            del g['image']
        print(f'{g=}')

        if ('image' in self.param.keys()):

            height_img = self.param['bbox'][3]-self.param['bbox'][1]
            add_right_down_y = height_img
            if self.right_down.y > float(self.height_page + 10):
                self.nnew_page()
                self.count_coords()
            
            print(f'{self.left_up.x=} *** {self.left_up.y=} *** {self.right_down.x=} *** {self.right_down.y=} ')

            # else:
                # self.left_up.y = self.right_down.y
                # self.right_down.x, self.right_down.y = self.right_down.x, self.right_down.y + float(height_img)
            self.make_paragraph_img(add_right_down_y=add_right_down_y)

        if ('image' not in self.param.keys()):


            add_right_down_y = self.param["bbox"][3] - \
                self.param["bbox"][1]  # + self.offset
            print(f"before while {add_right_down_y=}")
            while not 0 <= rc <= 3:
                print(
                    f"while verify height {add_right_down_y=} {self.left_up.y + add_right_down_y=}")
                print(f'{self.width_page=}   {self.height_page=}')
                print(f'{self.left_up.x=} *** {self.left_up.y=} *** {self.right_down.x=} *** {self.right_down.y=} \n **** {self.offset=} ***** {self.offset_last_page=} **** {add_right_down_y=}')

                print(f'**** ** ****** {self.left_up.y + add_right_down_y=}')

                if self.left_up.y + add_right_down_y > float(self.height_page)-start_point_y:

                    self.nnew_page()
                    self.count_coords()

                if rc < 0:
                    # add_right_down_y * (rc*(-1)/100) if rc < -2 else 2.0
                    add_right_down_y += rc*(-1)
                    # self.right_down.y += rc*(-1)/3 if rc < -2 else 2.0
                if rc > 3:
                    # 2.0 if rc < 20 else add_right_down_y *(rc/100)
                    add_right_down_y -= rc
                    # self.right_down.y -= 2.0 if rc < 20 else rc/10
                print(f'{add_right_down_y=}')
                # left_up_x= self.left_up.x, left_up_y= self.left_up.y, right_down_x= self.right_down.x, right_down_y= self.right_down.y + add_right_down_y)
                rc = self.make_paragraph(add_right_down_y=add_right_down_y)

                print(f'while {rc=} ')


            print(
                f'counted {add_right_down_y=}  {self.param["bbox"][3] - self.param["bbox"][1]=} \n {self.offset=}')
            self.shape.commit()
            self.doc_new.save(
                self.docum.name[:-4] + f"{'_add_stroke'}" + self.docum.name[-4:])

            # self.left_up.x, self.left_up.y, self.right_down.x = self.param["bbox"]

            # self.left_up.x, self.left_up.y = self.p.x, self.right_down.y + add_right_down_y + self.fontsize
            # self.right_down.y += add_right_down_y + self.fontsize/3

            print(f'after while {self.left_up=} {self.right_down=}')

        # print(f'{rc=}')

    def start(self):
        print(f'calling start')

        self.offset_last_page = 0.0

        for self.param in self.params:

            print(f'MakePDF func start next param')
            if self.doc_new.page_count == 0:
                self.nnew_page()

            else:
                self.page = self.doc_new[-1]
                self.shape = self.page.new_shape()

            self.cickle_while()


# (name_file_pdf)
doc = fitz.Document('/home/serg/python_proj/fastapi/uploadfiles/Android.pdf')


# tg = Pagem(doc[86])
# list_param = TakeList(listt=tg)
# print(f'{doc[86].get_text()=}')
# print(f'{"*******************"}')
# print(f'{doc[86].get_text("blocks")=}')
# print(f'{"*******************"}')
# df = doc[86].get_text("dict")
# print(f'{"*******************"}')
# print(f'{{**df}}')
# pdf = MakePDF(list_param, doc, tg.width_page, tg.height_page)
# pdf.start()
# pdf.doc_new.save(doc.name[:-4] + f"{'_add_stroke'}" + doc.name[-4:])
# doc.close()
# pdf.doc_new.close()


for tgg in doc.pages(start=86, stop=87):
    # tg = Pagem(doc[86])
    tg = Pagem(tgg)
    list_param = TakeList(listt=tg)
    print(f'{tgg.get_text()=}')
    print(f'{"*******************"}')
    print(f'{tgg.get_text("blocks")=}')
    print(f'{"*******************"}')
    df = tgg.get_text("dict")
    print(f'{"*******************"}')
    print(f'{{**df}}')
    pdf = MakePDF(list_param, doc, tg.width_page, tg.height_page)
    pdf.start()
    pdf.doc_new.save(doc.name[:-4] + f"{'_add_stroke'}" + doc.name[-4:])
doc.close()
pdf.doc_new.close()
