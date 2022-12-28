

""" 
1) Создать класс TrafficLight (светофор) и определить у него один атрибут 
color (цвет) и метод running (запуск). Атрибут реализовать как приватный. 
В рамках метода реализовать переключение светофора в режимы: красный, желтый, 
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, 
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
Переключение между режимами должно осуществляться только в указанном порядке 
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр 
и вызвав описанный метод. 
"""


import time

class TrafficLight():

    red_attribute = 'Красный'
    yellow_attribute = 'Желтый'
    green_attribute = 'Зеленый'
    
    time_red_attribute = 7
    time_yellow_attribute = 2
    time_green_attribute = 9

    def __init__(self, color):
        self.__color = color

    def selector(self, color, waiting_time):
        self.waiting_time = waiting_time
        print(f'{color} режим: {self.waiting_time} сек')
        time.sleep(self.waiting_time)

    def running(self, start_color = 'Красный'):
        
        start_color = self.__color
        
        if start_color == self.red_attribute:
            self.selector('Красный', self.time_red_attribute)
            self.selector('Желтый', self.time_yellow_attribute)
            self.selector('Зеленый', self.time_green_attribute)

        print('Цикл переключения между режимами завершён')


s_phor = TrafficLight('Красный')
s_phor.running()