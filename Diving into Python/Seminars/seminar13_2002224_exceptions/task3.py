# Cоздайте класс с базовым исключением и дочерние классы-исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class ProjectException(Exception):
    pass


class LevelError(ProjectException):
    pass


class AccessError(ProjectException):
    pass
