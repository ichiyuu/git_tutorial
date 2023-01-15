class MondayFood(object):
    def __init__(self, name='ハンバーグ定食', price='800円'):
        self.name = name
        self.price = price

    def display(self):
        print('月曜日のメニューは{}で、価格は{}です。'.format(self.name, self.price))

class TuesdayFood(object):
    def __init__(self, name='生姜焼き定食', price='980円'):
        self.name = name
        self.price = price

    def display(self):
        print('火曜日のメニューは{}で、価格は{}です。'.format(self.name, self.price))

monday = MondayFood()
tuesday = TuesdayFood()

print(monday.display())
print(tuesday.display())

def weekend_menu(object):
    print(object.display())

weekend_menu(monday)
