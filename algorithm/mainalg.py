import numpy as np


class House:
    def __init__(self, data_of_house):
        """
        data_of_house принимаем в ввиде {"name": "house1", ....}
        """
        self.data = data_of_house

    def __str__(self):
        return str(self.data)

    def get_parameter(self, parameter):
        """
        Функция для выдучи необходимого параметра
        """
        return self.data[parameter]

    def set_weight(self, weight):
        """
        Назначаем "вес" данному дому
        """
        self.data["weight"] = weight


class Criteria:
    def __init__(self, data_of_criteria):
        """
        data_of_criteria принимаем в ввиде {"name": "price", ....}
        """
        self.data = data_of_criteria

    def __str__(self):
        return str(self.data)

    def get_parameter(self, parameter):
        return self.data[parameter]

    def set_weight(self, weight):
        """
        Назначаем "вес" данному критерию
        """
        self.data["weight"] = weight


def create_array_of_houses(data_of_houses):
    """
    Создаем спикос объектов домов из списка словарей
    """
    array = []

    for data_of_house in data_of_houses:
        array.append(House(data_of_house))

    return array


def create_array_of_criteria(data_of_criteria):
    """
    Создаем спикос объектов критериев из списка словарей
    """
    array = []

    for data_of_criteria in data_of_criteria:
        array.append(Criteria(data_of_criteria))

    return array


def check_function(i, j, minimum, index, mas):
    """
    Функция для определения находится ли минимум в том же десятичном отрезке, что и заданное число
    Так же мы используем 0.000000001 для учета ошибки в вычислениях числе с плавающей точкой
    """
    flag1 = (0.1 * i) - minimum <= 0.000000001
    flag2 = 0.1 + (0.1 * i) - minimum >= 0.000000001
    flag3 = (0.1 * j) - mas[index] <= 0.000000001
    flag4 = 0.1 + (0.1 * j) - mas[index] >= 0.000000001

    return flag1 and flag2 and flag3 and flag4


def more_function(array_of_parameters):
    """
    Функция которая расчитывает приоритеты обьектов и дает больший приоритет тому, кто имеет
    значение параметра выше чем у других.
    """
    matrix = []  # Создаем матрицу и инициализируем
    for i in range(len(array_of_parameters)):
        matrix.append([])
        for j in range(len(array_of_parameters)):
            matrix[i].append(None)

    # Нормируем значения
    total_sum = sum(array_of_parameters)
    for i in range(len(array_of_parameters)):
        array_of_parameters[i] = array_of_parameters[i] / total_sum

    # Находими минимальное значение среди всех значений параметра
    min_parameter = min(array_of_parameters)
    min_index = array_of_parameters.index(min_parameter)

    # Заполняем матрицу по алгоритму
    for index in range(len(array_of_parameters)):
        for i in range(10):
            for j in range(10):
                if check_function(i, j, min_parameter, index, array_of_parameters):
                    l = j
                    k = i
                    matrix[index][min_index] = l - k + 1
                    matrix[min_index][index] = 1 / matrix[index][min_index]

    # Все значения на диагонали равны 1
    for i in range(len(array_of_parameters)):
        matrix[i][i] = 1
    # Все остальные обратно пропорциональны элементам,
    # какие симметричны данному относительно диагонали
    for i in range(len(array_of_parameters)):
        for j in range(len(array_of_parameters)):
            if matrix[i][j] is None:
                matrix[i][j] = matrix[min_index][j] / matrix[min_index][i]

    np_array = np.array(matrix)
    eig = np.linalg.eig(np_array)  # вычисляем собственные значения и ветокра
    eigenvalue = eig[0]  # собственные значения
    eig_vector = eig[1]  # собственные вектора

    weight = []  # массив весов объектов
    ma_eig = max(eigenvalue)  # находим максимальное собственное число

    max_index = list(eigenvalue).index(ma_eig)
    for i in range(len(eig_vector)):
        weight.append(eig_vector[i][max_index])

    return weight # возвращаем вес соответстуещего обьекта


def less_function(array_of_parameters):
    """
    Функция которая расчитывает приоритеты обьектов и дает больший приоритет тому, кто имеет
    значение параметра ниже чем у других.
    """
    matrix = []  # Создаем матрицу и инициализируем
    for i in range(len(array_of_parameters)):
        matrix.append([])
        for j in range(len(array_of_parameters)):
            matrix[i].append(None)

    # Нормируем значения
    total_sum = sum(array_of_parameters)
    for i in range(len(array_of_parameters)):
        array_of_parameters[i] = array_of_parameters[i] / total_sum

    # Находими минимальное значение среди всех значений параметра
    min_parameter = min(array_of_parameters)
    min_index = array_of_parameters.index(min_parameter)

    # Заполняем матрицу по алгоритму
    for index in range(len(array_of_parameters)):
        for i in range(10):
            for j in range(10):
                if check_function(i, j, min_parameter, index, array_of_parameters):
                    l = j
                    k = i
                    matrix[min_index][index] = l - k + 1
                    matrix[index][min_index] = 1 / matrix[min_index][index]

    # Все значения на диагонали равны 1
    for i in range(len(array_of_parameters)):
        matrix[i][i] = 1
    # Все остальные обратно пропорциональны элементам,
    # какие симметричны данному относительно диагонали
    for i in range(len(array_of_parameters)):
        for j in range(len(array_of_parameters)):
            if matrix[i][j] is None:
                matrix[i][j] = matrix[min_index][j] / matrix[min_index][i]

    np_array = np.array(matrix)
    eig = np.linalg.eig(np_array)  # вычисляем собственные значения и ветокра
    eigenvalue = eig[0]  # собственные значения
    eig_vector = eig[1]  # собственные вектора

    weight = []  # массив весов объектов
    ma_eig = max(eigenvalue)  # находим максимальное собственное число

    max_index = list(eigenvalue).index(ma_eig)
    for i in range(len(eig_vector)):
        weight.append(eig_vector[i][max_index])

    return weight # возвращаем вес соответстуещего обьекта


def calculate_weight_of_criteria(criteria):
    """
    Вычисляем веса критериев
    """
    array = []
    for cr in criteria:
        array.append(cr.get_parameter("priority"))

    points = more_function(array)

    for iterator in range(len(criteria)):
        criteria[iterator].set_weight(points[iterator])


def new_less_function(array_of_parameter):
    """
    Функция оценки параметров в которой большая оценка дается тому, кто имеет меньшее
    значение параметра
    """
    array = [1 / value for value in array_of_parameter]
    result_sum = sum(array)

    return [value / result_sum for value in array]


def new_more_function(array_of_parameter):
    """
    Функция оценки параметров в которой большая оценка дается тому, кто имеет большее
    значение параметра
    """
    result_sum = sum(array_of_parameter)

    return [value / result_sum for value in array_of_parameter]


def calculate_weight_of_houses(houses, criterias):
    """
    Вычисляем веса домов
    """
    total_points = [0 for i in range(len(houses))]

    for criteria in criterias:
        characteristic = []
        for house in houses:
            characteristic.append(house.get_parameter(criteria.get_parameter("name")))

        points = new_less_function(characteristic)

        for j in range(len(points)):
            total_points[j] += (points[j]) * criteria.get_parameter("weight")

    for i, v in enumerate(total_points):
        houses[i].set_weight(v)


def main(hou , cri):
    #hou = [{"name": "house1", "price": 100, "len_to_metro": 3000},
    #       {"name": "house1", "price": 60, "len_to_metro": 5000}]  # Пример данных про дома
    array = create_array_of_houses(hou)  # Создаем массив объектов домов

    #cri = [{"name": "price", "priority": 4}, {"name": "len_to_metro", "priority": 6}] # Пример данных про критерии
    ar = create_array_of_criteria(cri)  # Создаем массив объектов критериев
    calculate_weight_of_criteria(ar)  # Вычисляем вес критериев
    calculate_weight_of_houses(array, ar)  # Вычисляем вес домов

    return array

