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
import shutil, app.config



x = torch.rand(5, 3)
print(x)

# fontsize = 10
# fontname = fontname = "Helvetica"
add_height = 5.0  # добавка к высоте прямоугольника для текста
width_page = 0
height_page = 0
start_point_y = 45
start_point_x = 35
point_left_up = fitz.Point()
point_right_down = fitz.Point()
doc = fitz.Document()
docnew = fitz.Document()


class Translator:
    def __init__(self, source_lang: str, dest_lang: str) -> None:
        self.model_name = f'Helsinki-NLP/opus-mt-{source_lang}-{dest_lang}'
        self.model = MarianMTModel.from_pretrained(self.model_name)
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)

    def translate(self, texts: Sequence[str]) -> Sequence[str]:
        tokens = self.tokenizer(list(texts), return_tensors="pt", padding=True)
        translate_tokens = self.model.generate(**tokens)
        return [self.tokenizer.decode(t, max_length=500, skip_special_tokens=True) for t in translate_tokens]


marian_en_ru = Translator('en', 'ru')
# p = marian_en_ru.translate(['The other kind of instance attribute reference is a method. A method is a function that “belongs to” an object. (In Python, the term method is not unique to class instances: other object types can have methods as well. For example, list objects have methods called append, insert, remove, sort, and so on. However, in the following discussion, we’ll use the term method exclusively to mean methods of class instance objects, unless explicitly stated otherwise.) Valid method names of an instance object depend on its class. By definition, all attributes of a class that are function objects define corresponding methods of its instances. So in our example, x.f is a valid method reference, since MyClass.f is a function, but x.i is not, since MyClass.i is not. But x.f is not the same thing as MyClass.f — it is a method object, not a function object.'])
# print(f'en -> ru {p[0]=}')


class Pagem:
    def __init__(self, page):
        self.klc = []
        self.klc3 = []
        self.fontsize = 10
        self.page = page
        self.text1 = page.get_text("dict")
        self.rect_width = float(self.text1["width"])
        self.rect_height = float(self.text1["height"])
        self.text2 = self._get_block_form_page(self.text1)
        self.klc2 = [self.klc.index(
            g) for g in self.klc for k, _ in g.items() if k == "number"]
        self.made_klc3(self.klc2)
        # self.dell_empty_list_text()
        self.sort_list_text()
        self.add_list_image()
        print(f'end of initialization')

    def del_many_points(self, strok):
        while (('. .' in strok) or ('..' in strok)):
            strok = strok.replace('..', '.')
            strok = strok.replace('. .', '.')
        return strok

    def find_origin_line_text(self, find_bbox):
        # empty_m = 0
        for indx, m in enumerate(self.klc3):
            #     if ((len(m.keys()) == 0) and (len(m.values()) == 0)):
            #         empty_m += 1

            for k, v in m.items():
                # print_bbox = v[1]['bbox']
                bbox = v[1]['bbox'][1]
                # print(
                #     f'find_origin_line_text {k=} \n {print_bbox=} \n {bbox=}  \n {find_bbox=}')
                if bbox >= find_bbox:
                    return indx  # -empty_m

        return -1

    # def dell_empty_list_text(self,):
    #     for indx, m in enumerate(self.klc3):
    #         if ((len(m.keys()) == 0) and (len(m.values()) == 0)):
    #             self.klc3.remove(m)
    #     # print(f'{self.klc3=}')

    def add_list_image(self):
        images = self.page.get_image_info(xrefs=True)
        for i, image in enumerate(images):
            # print(f'{i=} {image=}')
            g = True

            find = self.find_origin_line_text(image['bbox'][1])
            # print(f'{find=}')
            if find < 0:
                find = len(self.klc3)-1
            self.klc3.insert(find, {'number': [str(image['number']) + 'img',
                                               {'bbox': image['bbox']},
                                               {'width': image['width']},
                                               {'height_rect': image['height']},
                                               {'page_num': self.page.number},
                                               ]})

    def sort_list_text(self):

        for i in range(len(self.klc3)+1):
            lst = self.klc3

        for indx, m in enumerate(lst):

            for k, v in m.items():
                # print_bbox = v[1]['bbox']
                bbox = v[1]['bbox'][1]
                # print(f'{k=} \n {print_bbox=} \n {bbox=}  \n {find_bbox=}')
                find = self.find_origin_line_text(bbox)

                # txt = v[2]['text_en']
                # print(f'sort_list_text {find=} {txt=}')
                if find < 0:
                    find = len(self.klc3)-1
            self.klc3.remove(m)
            self.klc3.insert(find, m)
        print(f'sort_list_text {self.klc3=}')
        # print(f'sort_list_text {lst=}')

    def made_klc3(self, klc):
        for n in klc[0:len(klc)-1]:
            txt = ""
            d, d1, d2, d4, d5 = {}, {}, {}, {}, {}
            d3 = {"trans": True}
            for i, m in enumerate(self.klc[n: klc[klc.index(n)+1]]):
                k = list(m.keys())[0]
                v = list(m.values())[0]
                # k,v = m.items()
                if k == "number":
                    d1 = v
                    # kl3.append(m)
                if (k == "bbox") and (i == 1):
                    d2 = m
                    # kl3.append(m)
                if k == "text":
                    txt += v
                if k == "color":
                    d4["color"] = v
                    if (v != 2645391) and (v != 0):
                        d3["trans"] = False
                if k == "font":
                    d5["font"] = v

            if (d3["trans"]):
                lst = []
                if len(txt.strip()) > 0:
                    lst.append(self.del_many_points(txt))
                    text = marian_en_ru.translate(lst)
                    txt_en = txt.strip()  # "\n" + text[0]
                    txt_ru = text[0].strip()

            if (not d3["trans"]):
                txt_en = txt  # .strip()
                txt_ru = ""
                font = fitz.Font("figo")
            len_stroke = float(fitz.get_text_length(txt, fontname='helv'))
            height_stroke = float(len_stroke/self.rect_width)
            height_stroke = float(
                int(height_stroke) + bool(height_stroke % 1))
            self.rect_height += height_stroke
            # print(f'{len_stroke/self.rect_width=}\n{txt} ')

            if len(txt) > 0:
                d["number"] = [d1, d2, {"text_en": txt_en},  {"text_ru": txt_ru}, {"width_rect": len_stroke}, {
                    "height_rect": float(height_stroke * self.fontsize * 1.31 + add_height)}, d4, d5, ]
            if ((len(d.keys()) > 0) and (len(d.values()) > 0)):
                self.klc3.append(d)
            # print(f'{self.klc3[-1:]=}')

    def _get_block_form_page(self, field):
        for b in field["blocks"]:
            m = list(self.lisf_of_all_field(b))
        return m

    # def lisf_of_all_field(self, dfg):
    #     return list(self._lisf_of_all_field(dfg))

    def lisf_of_all_field(self, dfg):
        if isinstance(dfg, dict):
            # print("yes")
            for k, v in dfg.items():
                if (k == "color" or k == "text" or k == "number" or k == "bbox" or k == "font"):
                    # print(f'{k=} {v=}')
                    self.klc.append(dict([(k, v)]))
                    # print(f'{self.klc[:-1]}')
                yield from self.lisf_of_all_field(v)
        elif isinstance(dfg, list):  # or list, set, ... only
            for v in dfg:
                yield from self.lisf_of_all_field(v)
        else:
            yield dfg


class MakePDF():
    def __init__(self,param,docnew):

        self.params = param
        self.param = []
        

        self.namefont = "figo"
        self.fontname = fitz.Font(self.namefont)
        self.fontsize = 12
        self.color_code_text = (0.1, 0.1, 0.1)
        self.color_text = (0.79, 0.33, 0.30)

        self.p = fitz.Point(start_point_x, start_point_y)
        self.left_up = fitz.Point(self.p)
        self.right_down = fitz.Point(self.p)#+(15.0, 15.0)

        self.language = ["en", "ru"]

        # self.dictionar = self.diction
        # self.key, self.value = self.dictionar.items()
        # self.list_key = [k for k in self.dictionar.keys()][0]
        # self.index = len(self.list_key)

        self.page = None
        self.shape = None
        # self.start()
        # if docnew.page_count == 0:
        #     self.page = self.new_page()

    # def __iter__(self):
    #     return self

    # def __next__(self):
    #     if self.index == 0:
    #         raise StopIteration
    #     self.index = self.index - 1
    #     return self.dictionar[self.list_key[self.index]]

    # def give(self):
    #     for key, val in self.dictionar:
    #         yield (key, val)
        # self.dict = dictt
        # self.index = 0  # len(self.param)
        # self.main_start()
        # self.start()

    # def __iter__(self):
    #     return self

    # def __next__(self):
    #     if self.index == len(self.param):
    #         raise StopIteration
    #     self.index += 1
    #     return self.param[self.index-1]

    # def main_start(self) -> List:
    #     # param = []
    #     vc = 0
    #     for k, v in self.dict.items():
    #         print('*****************')
    #         # print(' ')
    #         # print(' ')
    #         # print(f'{k=} {v=}')
    #         # print(' ')

    #         for n in v:
    #             print(f'{vc=} \n \n {n=} ')  # \n \n {v=}')
    #             vc += 1
    #             # if "text_en" in n["number"][2].keys():
    #             if ((len(n) == 0) or (("text_en" in n["number"][2].keys()) and (len(n["number"][2]["text_en"].strip()) == 0))):
    #                 continue
    #             self.params.append(n["number"])
    #     print(f'******************************************')
    #     # print(f'{self.params=}')
    #     print(f'******************************************')
    #     # return param

    def make_rect(self, left_upx, left_upy, right_downx, right_downy):
        if left_upy >= right_downy:
            self.right_down.y += (self.left_up.y - self.right_down.y)+ add_height
            self.right_down.x = width_page
        print(
            f'make_rect {self.left_up.x=}, {self.left_up.y=},{self.right_down.x=}, {self.right_down.y=}')
        rect = fitz.Rect(self.left_up.x, self.left_up.y, self.right_down.x, self.right_down.y)
        return rect

    def create_text(self, language):
        if language == 'en':
            text = '\t   ' + self.param[2]["text_en"]
        if language == "ru":
            text = '\t  ' + self.param[3]["text_ru"]
        # print(f'{text=}')
        return text

    def make_paragraph_img(self):
        current_page = int(self.param[4]['page_num'])
        current_img = int(self.param[0].replace('img', ''))
        jj = doc[current_page].get_image_info(hashes=False, xrefs=True)
        print(f' make_paragraph_img {jj=}')
        rect = fitz.Rect([h for h in jj if h['number'] == current_img]
                         [0]['bbox'])
        height_rect = rect.height
        rect.y0 = self.left_up.y
        rect.y1 = rect.y0 + height_rect
        # rect.bottom_left.y = rect.top_left.y + rect.height
        # rect.bottom_right.y = rect.bottom_left.y + rect.height
        # rect += (0.0, self.left_up.y, 0.0, self.left_up.y)
        pix = doc[current_page].get_pixmap(
            clip=[h for h in jj if h['number'] == current_img][0]['bbox'])
        print(f'make_paragraph_img {pix=}')

        img_xref = self.page.insert_image(rect,  # stream=jj[0]["digest"],
                                          # xref=pix,#int(jj[0]["xref"]),
                                          pixmap=pix,
                                          keep_proportion=False,  # 2nd time reuses existing image
                                          )
        # self.p.y += self.param[3]['height_rect']
        # self.right_down.y = self.p.y + add_height
        self.left_up = rect.bottom_right
        self.left_up.x = self.p.x
        self.right_down.y = rect.bottom_right.y + 2*add_height
        self.right_down.x = width_page

        point_left_up.x = self.left_up.x
        point_left_up.y = self.left_up.y
        point_right_down.x = self.right_down.x
        point_right_down.y = self.right_down.y
        
        print(f'make_paragraph_img {self.left_up=} {self.right_down=}')

    def make_paragraph(self, language):
        # rect = fitz.Rect(left_up.x, left_up.y, right_down.x, right_down.y)
        print(f'make_paragraph {self.right_down.y=}')
        rect = self.make_rect(self.left_up.x, self.left_up.y,
                              self.right_down.x , self.right_down.y)
        # draw bacground rectangles
        # self.shape.draw_rect(rect)
        # self.shape.finish(width=2, color=(1,0.5,0.8), fill=(0.2,0.1,0.4))

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

    def count_right_down(self):
        if 'img' in (str(self.param[0]) if isinstance(self.param[0], int) else self.param[0]):
            self.right_down += float(width_page), self.p.y + \
                float(self.param[3]["height_rect"])
            # self.right_down.x, self.right_down.y = width_page, self.p.y + \
            #     float(self.param[3]["height_rect"])
        else:
            self.right_down = self.right_down + (width_page, self.p.y +
                                                 float(self.param[5]["height_rect"]))

    def nnew_page(self):
        print(f'function nnew_page')
        self.page = docnew.new_page()
        font = fitz.Font("figo")
        self.page.insert_font(encoding=2, fontname=self.namefont,  # fontsize=self.fontsize,  # 'figo',
                              fontbuffer=font.buffer, set_simple=False)  # add)
        # start point of 1st line
        self.p = fitz.Point(start_point_x, start_point_y)
        self.left_up.x, self.left_up.y = self.p.x, self.p.y
        # print(f'{self.param=}')
        # self.count_right_down()
        self.right_down.x, self.right_down.y = float(width_page), float(self.p.y + add_height)
        self.shape = self.page.new_shape()
        # float(self.param[5]["height_rect"])
        # return [page,p]
        # return [self.page, self.p]

    def cickle_while(self, ):
        for language in self.language:  # ["en", "ru"]:
            if (('img' not in (str(self.param[0]) if isinstance(self.param[0], int) else self.param[0]))
                and (language == "ru")
                    and (len(self.param[3]["text_ru"].strip()) == 0)):

                break

            rc = 12
            print(f'before while {rc=}')
            print(f'{self.param=}')
            # print(f'{len(self.param[3]["text_ru"].strip())=}')

            # def count_coordinates_nnew_page():
            #     # print(f'{self.right_down.y=} {height_page=}')
            #     # fn = self.nnew_page()
            #     self.nnew_page
            #     # p = fn[1]
            #     # self.p = fn[1]
            #     # self.page = fn[0]
            #     # return [self.p, self.page]

            if (('img' in (str(self.param[0]) if isinstance(self.param[0], int) else self.param[0]))
                    and (language == "en")):
                height_img = self.param[1]['bbox'][3] - self.param[1]['bbox'][1]
                if self.right_down.y + float(height_img) > float(height_page + 50):
                    # ls = count_coordinates_nnew_page()
                    # count_coordinates_nnew_page()
                    self.nnew_page()
                    # self.p = ls[0]
                    # self.page = ls[1]
                # self.shape = self.page.new_self.shape()
                else:
                    self.left_up.y = self.right_down.y
                    self.right_down.x, self.right_down.y = self.right_down.x, self.right_down.y + float(height_img)
                self.make_paragraph_img()

            if 'img' not in (str(self.param[0]) if isinstance(self.param[0], int) else self.param[0]):
                while not 5 < rc < 10:
                    if self.right_down.y + float(self.param[5]['height_rect'])> float(height_page + 150):
                        # ls = count_coordinates_nnew_page()
                        # count_coordinates_nnew_page()
                        self.nnew_page()
                        # self.p = ls[0]
                        # self.page = ls[1]
                        # self.p, self.page = count_coordinates_new_page()
                        # print(f'{self.right_down.y=} {height_page=}')
                        # fn = self.new_page()
                        # # p = fn[1]
                        # self.p = fn[1]
                        # self.page = fn[0]
                        ### page = docnew.new_page()
                        ### font = fitz.Font("figo")
                        # page.insert_font(encoding=2, fontname='figo',
                        # fontbuffer=font.buffer, set_simple=False)  # add)
                        # p = fitz.Point(start_point_x, start_point_y)  # start point of 1st line
                        ### left_up.x, left_up.y = p.x, p.y
                        ### right_down.x, right_down.y = width_page, p.y + float(self.param[5]["height_rect"])
                        # self.shape = self.page.new_shape()
                    if rc <= 5:
                        self.right_down.y += 2.0
                    if rc >= 10:
                        self.right_down.y -= 2.0

                    rc = self.make_paragraph(language)
                    print(f'while {rc=}')
                # if ((language=="ru") and (len(self.param[3]["text_ru"].strip())==0)):
                self.shape.commit()

            # print(f'{self.right_down.y=}')

            # float(self.param[5]["height_rect"]))
            # self.p += (0, self.right_down.y - self.left_up.y+add_height)
                
                self.left_up.x, self.left_up.y = self.p.x, self.right_down.y 
                self.right_down.y += add_height
                point_left_up.x = self.left_up.x
                point_left_up.y = self.left_up.y
                point_right_down.x = self.right_down.x
                point_right_down.y = self.right_down.y
                # if len(self.param[3]["text_ru"].strip()) > 0:
                #     print(f'after while {self.left_up.x=} {self.left_up.y=}')
                #     self.right_down.x, self.right_down.y = float(width_page), float(self.right_down.y + add_height)  # -left_up.y
                #     print(
                #         f'after while  {self.right_down.x=} {self.right_down.y=}')
                print(f'after while {self.left_up=} {self.right_down=}')

            # print(f'{rc=}')

    def start(self):
        global point_left_up
        global point_right_down
        for self.param in self.params:
            if docnew.page_count == 0:
                self.nnew_page()
                point_left_up = fitz.Point(start_point_x, start_point_y)
                point_right_down = fitz.Point(start_point_x, start_point_y)
            else:
                self.page = docnew[-1]
                self.shape = self.page.new_shape()
                self.left_up = fitz.Point(point_left_up.x, point_left_up.y)
                self.right_up = fitz.Point(point_right_down.x, point_right_down.y+4*add_height)
            self.cickle_while()

            point_left_up = fitz.Point(self.left_up.x , self.left_up.y)
            point_right_down = fitz.Point(self.right_down.x, self.right_down.y)


class Dictionar():  # ItemsDict
    def __init__(self, dictt):
        self.dict = dictt
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
        vc = 0
        for k, v in self.dict.items():
            print('*****************')
            # print(' ')
            # print(' ')
            # print(f'{k=} {v=}')
            # print(' ')

            for n in v:
                print(f'{vc=} \n \n {n=} ')  # \n \n {v=}')
                vc += 1
                # if "text_en" in n["number"][2].keys():
                if ((len(n) == 0) or (("text_en" in n["number"][2].keys()) and (len(n["number"][2]["text_en"].strip()) == 0))):
                    continue
                param.append(n["number"])
        return param

def translate(name_file_pdf: str):
    work_name = "jet.pdf"
    work_name_new = "jet_new.pdf"
    print(f'start translate {name_file_pdf} {name_file_pdf_translate}')
    shutil.move('oldname', 'renamedfiles/newname')
    doc = fitz.Document(app.config.UPLOAD_FOLDER+f'{name_file_pdf}')
    name_file_pdf_translate = app.config.UPLOAD_FOLDER + name_file_pdf + f'_translate' 
    f = open(name_file_pdf_translate, 'w', encoding="utf-8")
    f.write("Test\n")
    f.close()
    docnew = fitz.Document()

    where = fitz.Point(50, 100)
    # page = docnew.new_page()
    # page.insert_text(where, "PDF created with PyMuPDF", fontsize=10)

    # docnew.save("j2.pdf")
    kl = []
    # ditt = {}
    # pag = Pagem()
    for pagge in doc.pages(start=1, stop=10):
        ditt = {}
        print(f'{pagge.number=}')
        page_cl = Pagem(pagge)
        width_page = page_cl.rect_width
        height_page = page_cl.rect_height
        # if len(page_cl.klc3) == 0:
        #     page_cl.klc3 = ['empty']
        ditt[f'page_num {pagge.number}'] = page_cl.klc3

        # list_param = MakePDF(dictt=ditt)
        # list_param.start()
        list_param = Dictionar(dictt=ditt)
        pdf = MakePDF(list_param, docnew)
        pdf.start()

        print(f'before save {pagge.number=}')
        docnew.save(name_file_pdf_translate)
        # kl.append(page_cl.klc3)
        # d[f'page_num {pagge.number}'] = list(page_cl.lisf_of_all_field(doc.load_page(pagge.number)))

    # p = fitz.Point(start_point_x, start_point_y)  # start point of 1st line
    # vc = 0


    # list_param = Dictionar(dictt=ditt)
    # pdf = MakePDF(list_param, docnew)
    # pdf.start()

    docnew.save(name_file_pdf_translate)
    docnew.close()
    doc.close()
