from transformers import MarianMTModel, MarianTokenizer
from typing import Sequence

class Translator:
    def __init__(self, source_lang: str, dest_lang: str) -> None:
        self.model_name = f'Helsinki-NLP/opus-mt-{source_lang}-{dest_lang}'
        self.model = MarianMTModel.from_pretrained(self.model_name)
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)
        
    def translate(self, texts: Sequence[str]) -> Sequence[str]:
        tokens = self.tokenizer(list(texts), return_tensors="pt", padding=True)
        translate_tokens = self.model.generate(**tokens)
        return [self.tokenizer.decode(t, skip_special_tokens=True) for t in translate_tokens]
        
        
marian_ru_en = Translator('ru', 'en')
p = marian_ru_en.translate(['что слишком сознавать — это болезнь, настоящая, полная болезнь.'])
print(f'ru -> en {p[0]=}')
# Returns: ['That being too conscious is a disease, a real, complete disease.']
marian_en_ru = Translator('en', 'ru')
p = marian_en_ru.translate(['The other kind of instance attribute reference is a method. A method is a function that “belongs to” an object. (In Python, the term method is not unique to class instances: other object types can have methods as well. For example, list objects have methods called append, insert, remove, sort, and so on. However, in the following discussion, we’ll use the term method exclusively to mean methods of class instance objects, unless explicitly stated otherwise.) Valid method names of an instance object depend on its class. By definition, all attributes of a class that are function objects define corresponding methods of its instances. So in our example, x.f is a valid method reference, since MyClass.f is a function, but x.i is not, since MyClass.i is not. But x.f is not the same thing as MyClass.f — it is a method object, not a function object.'])
# p2 = marian_en_ru.translate(['The other kind '])
f = 'clicking on a file in the project view will cause that file to be loaded into the  appropriate editing tool.  •Structure   – The structure tool provides a high level view of the structure of the  source file currently displayed in the editor. This information includes a list of  items such as classes, methods and variables in the file. Selecting an item from  the structure list will take you to that location in the source file in the editor  window.  •Favorites   – A variety of project items can be added to the favorites list. Right-  clicking on a file in the project view, for example, provides access to an   Add to  Favorites   menu option. Similarly, a method in a source file can be added as a  favorite by right-clicking on it in the Structure tool window. Anything added to  a Favorites list can be accessed through this Favorites tool window.  •Build  Variants    –  The  build  variants  tool  window  provides  a  quick  way  to  configure different build targets for the current application project (for example  different  builds  for  debugging  and  release  versions  of  the  application,  or  multiple builds to target different device categories).  •  Database Inspector   - Especially useful for database debugging, this tool allows  you  to  inspect,  query,  and  modify  your  app’s  databases  while  the  app  is  running.  •TODO   – As the name suggests, this tool provides a place to review items that  have yet to be completed on the project. Android Studio compiles this list by  scanning the source files that make up the project to look for comments that  match specified TODO patterns. These patterns can be reviewed and changed  by selecting the   File -> Settings…   menu option (  Android Studio -> Preferences…  on macOS) and navigating to the   TODO   page listed under   Editor  .•Logcat   – The Logcat tool window provides access to the monitoring log output  from a running application in addition to options for taking screenshots and  videos of the application and stopping and restarting a process.  •Terminal    –  Provides  access  to  a  terminal  window  on  the  system  on  which  Android Studio is running. On Windows systems this is the Command Prompt  interface, while on Linux and macOS systems this takes the form of a Terminal  prompt.  •  Build    -  The  build  tool  window  displays  information  about  the  build  process  while  a  project  is  being  compiled  and  packaged  and  displays  details  of  any  errors encountered.  •Run   – The run tool window becomes available when an application is currently  '.replace('•','')
p2 = marian_en_ru.translate([f])
print(f'en -> ru {p[0]=} \n {p2[0]=}')