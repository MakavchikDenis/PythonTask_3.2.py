
class Inventory:
    procent=10 #ежегодный процент амортизации

    def __init__(self,nameInventory,year,pricePurch):
        self.nameInventory=nameInventory
        self.year=year
        self.pricePurch=pricePurch
        self.price=Inventory.funCountingPrice(self)

    def funCountingPrice(self):
        return self.pricePurch -self.pricePurch*(((2020-self.year)*Inventory.procent)/100)

    def get(self):
        return str(f"Название: {self.nameInventory}\n"
                f"Год закупки: {self.year}\n" 
                f"Закупочная стоимость: {self.pricePurch} р.\n"
                f"Остаточная стоимость: {self.price} р.")

class Bench(Inventory):

    def __init__(self,nameInventory,year,pricePurch,color,lenght):
        super(). __init__(nameInventory,year,pricePurch)
        self.color=color
        self.lenght=lenght

    def get(self):
        return str(f"Название: {self.nameInventory}\n"
                f"Год закупки: {self.year}\n" 
                f"Закупочная стоимость: {self.pricePurch} р.\n"
                f"Остаточная стоимость: {self.price} р.\n"
                f"Цвет: {self.color}\n"
                f"Длинна: {self.lenght}")

class Skids(Bench):

    def __init__(self,nameInventory,year,pricePurch,color,lenght,width):
        super().__init__(nameInventory,year,pricePurch,color,lenght)
        self.width=width

    def funGetSkids(self):
        return str(super().get()+"\n"
                   f"Ширина: {self.width}")



class Ball(Inventory):

    def __init__(self,nameInventory,year,pricePurch,color,nameModel):
        super(). __init__(nameInventory,year,pricePurch)
        self.color=color
        self.nameModel=nameModel

    def get(self):
        return str(f"Название: {self.nameInventory} \n"
                   f"Год закупки:{self.year} \n"
                   f"Закупочная стоимость: {self.pricePurch} р.\n"
                   f"Остаточная стоимость: {self.price} р.\n"
                   f"Цвет: {self.color}\n"
                   f"Производитель: {self.nameModel}")

class Mates(Skids):

    def __init__(self,nameInventory,year,pricePurch,color,lenght,width,nameModel):
        super().__init__(nameInventory,year,pricePurch,color,lenght,width)
        self.nameModel=nameModel

    def funGetMates(self):
        return str(super().funGetSkids()+"\n"
                   f"Производитель: {self.nameModel}")
