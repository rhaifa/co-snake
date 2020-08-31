from eatable_object import EatableObject


class Food(EatableObject):
    nutrition_value = None

    def get_nutrition_value(self):
        return self.__class__.nutrition_value


class Apple(Food):
    name = "Apple"
    img = None
    nutrition_value = 1


class Banana(Food):
    name = "Banana"
    img = None
    nutrition_value = 3





