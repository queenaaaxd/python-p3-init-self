#!/usr/bin/env python3
import ipdb

class Dog:
    # Remember that all methods use "self".
    def __init__(self, name, breed = "Mutt"):
        # print("A dog is born!")
        # print(f"{name} is born!")
        self.name = name
        self.breed = breed

    # def bark(self):
    #     print("Woof!")

    # def showing_self(self):
    #     return self

    # ipdb> fido = Dog("Fido")
    # Fido is born!
    # ipdb> fido.showing_self()
    # <__main__.Dog object at 0x1058a3640>
    # ipdb> fido
    # <__main__.Dog object at 0x1058a3640>
    # fido is fido.showing_self() # true
