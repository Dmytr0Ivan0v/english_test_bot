from enum import Enum


class UserLevel(str, Enum):
    A1 = "A1 - Elementary"
    A2 = "A2 - Pre-Intermediate"
    B1 = "B1 - Intermediate"
    B2 = "B2 - Upper-Intermediate"
    C1 = "C1 - Advanced"

    @classmethod
    def get_level(cls, right_answers):
        if right_answers < 15:
            return cls.A1
        elif 15 <= right_answers < 30:
            return cls.A2
        elif 30 <= right_answers < 45:
            return cls.B1
        elif 45 <= right_answers < 50:
            return cls.B2
        elif right_answers >= 50:
            return cls.C1
