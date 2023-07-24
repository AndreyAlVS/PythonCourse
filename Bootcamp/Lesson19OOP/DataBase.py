from Worker import Worker
from Department import Department


class DataBase:
    dep_table: list[Department]
    worker_table: list[Worker]

    def __init__(self) -> None:
        self.dep_table = []
        self.worker_table = []

    def append_worker(self, worker: Worker) -> None:
        self.worker_table.append(worker)

    def append_dep(self, dep: Department) -> None:
        self.dep_table.append(dep)

    def select_all_dep(self) -> str:
        output: str = ""

        for d in self.dep_table:
            output += f'{d.title}\n'
        return output

    def select_all_worker(self) -> str:
        output = ""

        for w in self.worker_table:
            output += f'{w.full_name}  {w.age}\n'
        return output

    def report(self) -> list[tuple]:
        rep: list[tuple] = []
        for w in self.worker_table:
            rep.append((w.full_name, w.age, self.dep_table[w.dep_id].title))
        return rep
