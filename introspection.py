def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    obj_attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]

    # Получаем методы объекта
    obj_methods = [method for method in dir(obj) if callable(getattr(obj, method))]

    # Получаем модуль, к которому принадлежит объект
    obj_module = obj.__class__.__module__

    # Создаем словарь с информацией об объекте
    info = {
        'type': obj_type,
        'attributes': obj_attributes,
        'methods': obj_methods,
        'module': obj_module,
    }

    # Дополнительная информация в зависимости от типа объекта
    if isinstance(obj, (int, float, str, list, dict, set, tuple)):
        info['value'] = obj
    elif isinstance(obj, type):
        info['bases'] = [base.__name__ for base in obj.__bases__]
        info['doc'] = obj.__doc__

    return info


# Пример использования функции с встроенным типом
number_info = introspection_info(42)
print(number_info)


# Создаем собственный класс для демонстрации
class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")


# Пример использования функции с объектом собственного класса
my_obj = MyClass(10)
my_obj_info = introspection_info(my_obj)
print(my_obj_info)
