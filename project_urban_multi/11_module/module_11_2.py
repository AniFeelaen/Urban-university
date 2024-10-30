# import inspect
class Inspection:
    
    def __init__(self,x):
        self.x = x
        
    def method(self):
        pass

    def introspection_info(obj):
        result = {}
        result['Тип -'] = type(obj).__name__
        methods_attributes =dir(obj)
        methods = []
        attributes = []
        for item in methods_attributes:
            if callable(getattr(obj, item)):
                methods.append(item)
            else:
                attributes.append(item)
        result['Аттрибуты - '] = attributes
        result["Методы - "] = methods
        module_name = getattr(type(obj), '__module__', None)
        if module_name is not None:
            result['Модуль - '] = module_name

        return result
def main():
    # Здесь находится ваш основной код
    print("Программа запущена!")

if __name__ == "__main__":
    main() 

# obj = Inspection(10)
# print(obj)
number_info = Inspection.introspection_info(42)
for key, value in number_info.items():
    print(f"{key}: {value}")
number_info = Inspection.introspection_info("42")
for key, value in number_info.items():
    print(f"{key}: {value}")
number_info = Inspection.introspection_info([1,'2'])
for key, value in number_info.items():
    print(f"{key}: {value}")