class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    @classmethod
    def from_sum(cls, v1, v2):
        return cls(v1 + v2)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)

        self.symbol = '€'

    def __repr__(self):
        # return f'<Euro {self.symbol}{self.amount:.2f}>'
        return "<Euro {}{:.2f}>".format(self.symbol, self.amount)


ff_object = FixedFloat(56.060)
print(ff_object)

# calling the static method
print(FixedFloat.from_sum(50.350, 25.500))

euro_obj = Euro(35.8780)
print(euro_obj)
print(euro_obj.from_sum(50.890, 45.304))