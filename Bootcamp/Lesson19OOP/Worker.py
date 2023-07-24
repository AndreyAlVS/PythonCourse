class Worker:
    id: int
    dep_id: str
    age: int
    full_name: str
    salary: int

    def __init__(self, id: int, worker_name: str, age: int, salary: int, dep_id: int = 0) -> None:
        self.id = id
        self.full_name = worker_name
        self.age = age
        self.salary = salary
        self.dep_id = dep_id

    def __repr__(self) -> str:
        return f'id: {self.id}  Full name: {self.full_name}  age: {self.age}  salary: {self.salary}  dep id: {self.dep_id}'
