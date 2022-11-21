import threading as th
import time
class Thr1(th.Thread): # Создаём экземпляр потока Thread
    def __init__(self, var):
        th.Thread.__init__(self)
        self.daemon = True # Указываем, что этот поток - демон
        self.var = var # это интервал, передаваемый в качестве аргумента

    def run(self): # метод, который выполняется при запуске потока
        num = 1
        while True:
            y = num*num + num / (num - 10) # Вычисляем функцию
            num += 1
            print("При num =", num, " функция y =", y) # Печатаем результат
            time.sleep(self.var) # Ждём указанное количество секунд
x = Thr1(0.9)
x.start()
time.sleep(2)