#!/usr/bin/bash
"base class module"
class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects+=1
            self.id = Base.__nb_objects
    @property
    def nb_objects(self):
        return self.__nb_objects
    
    @nb_objects.setter
    def nb_objects(self,value):
        pass
        
