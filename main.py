# Создайте класс, содержащий набор целых чисел. 
# В классе должна быть реализована следующая функциональность:
# ■ Сумма элементов набора.
# ■ Среднеарифметическое элементов набора.
# ■ Максимум из элементов набора.
# ■ Минимум из элементов набора.
# Протестируйте все возможности созданного класса 
# с помощью модульного тестирования(unittest).
# -----------------------------------------
class Int_nums:
    def __init__(self, nums:list|tuple) -> None:
        if isinstance(nums, (list, tuple)):
            self.__nums = nums
        else:
            self.__nums = None

    def validate(self):
        if self.__nums is None:
            print('Should be list or tuple.')
            return False

        if not self.__nums:
            print('List is empty.')
            return False

        if not all(isinstance(el, int) for el in self.__nums):
            print('Can only be integers.')
            return False
        
        return True

    def sum(self):
        if self.validate():
            return sum(self.__nums)
        return None

    def mean(self):
        if self.validate():
            return self.sum()/len(self.__nums)
        return None

    def max_num(self):
        if self.validate():
            return max(self.__nums)
        return None

    def min_num(self):
        if self.validate():
            return min(self.__nums)
        return None
