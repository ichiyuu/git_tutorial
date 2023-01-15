class Calc(object):
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def plusCalc(self):
        result_plus_calc = self.x + self.y
        return result_plus_calc

class TriangleCalc(Calc):
    def __init__(self, x=10, y=20, base=30, height=40, passwd='1234'):
        super().__init__(x, y)
        self._base = base
        self._height = height
        self.passwd = passwd

    @property
    def base(self):
        return self._base
    @property
    def height(self):
        return self._height
    @base.setter
    def base(self, is_enable):
        if self.passwd == '1234':
            self._base = is_enable
        else:
            raise ValueError

    @height.setter
    def height(self, is_enable):
        if self.passwd == '1234':
            self.height = is_enable
        else:
            raise ValueError

    def triCalc(self):
        result_tri_calc = (self.base * self.height) / 2
        return result_tri_calc

c = Calc(10, 20)
tc = TriangleCalc(passwd='2345')
print(c.plusCalc())
print(tc.triCalc())
tc.base = 500
print(tc.plusCalc())
print(tc.triCalc())
print(tc.triCalc())
