class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()


class Observer:
    def update(self):
        print("Observer updated")


# Ejemplo de uso
subject = Subject()
observer1 = Observer()
observer2 = Observer()

subject.subscribe(observer1)
subject.subscribe(observer2)

subject.notify()
