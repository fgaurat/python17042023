from dataclasses import dataclass
@dataclass
class Todo:
    id:int=0
    userId:int=0
    title:str=""
    completed:bool=False