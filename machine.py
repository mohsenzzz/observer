from abc import ABC, abstractmethod

def machine_state(state='idle'):
    def decorated_method(func):
        def wrapper(obj,*args, **kwargs):
            print(func(obj,*args,**kwargs))
            # print(obj.show_state())
            for component in obj.components:
                component.change_state(state)
                print(component.show_state())
        return wrapper
    return decorated_method






class Machine(ABC):
    _state_list = ['active', 'inactive', 'idle']

    @abstractmethod
    def change_state(self):
        pass
    @abstractmethod
    def show_state(self):
        pass


class Gearbox(Machine):
    _state = 'inactive'


    @classmethod
    def change_state(cls, state):
        cls._state = state
    @classmethod
    def show_state(cls):
        return f'gearbox is {cls._state}'


class Engine(Machine):
    components = [Gearbox]
    def __init__(self):
        self.state = 'inactive'

    def change_state(self, state):
        self.state = state
    @machine_state()
    def show_state(self):
        return f'Engine is {self.state}'



if __name__ == '__main__':
    m = Engine()
    g=Gearbox()

    m.show_state()

