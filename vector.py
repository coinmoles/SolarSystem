from __future__ import annotations
from typing import Tuple, Union
from math import sin, cos, pi


class Vector(list):  # 벡터 클래스
    def __init__(self, *arg):
        super().__init__([*arg])

    def __add__(self, rhs: Vector) -> Vector:
        if not isinstance(rhs, Vector):
            raise TypeError
        return Vector(*map(lambda x: x[0] + x[1], zip(self, rhs)))

    def __iadd__(self, rhs: Vector) -> Vector:
        return self + rhs

    def __sub__(self, rhs: Vector) -> Vector:
        if not isinstance(rhs, Vector):
            raise TypeError
        return Vector(*map(lambda x: x[0] - x[1], zip(self, rhs)))

    def __isub__(self, rhs: Vector) -> Vector:
        return self - rhs

    def __abs__(self) -> float:
        return sum(map(lambda x: x ** 2, self))**0.5

    def __mul__(self, rhs: Union[int, float]) -> Vector:
        if not isinstance(rhs, (int, float)):
            raise TypeError
        return Vector(*map(lambda x: x * rhs, self))

    def __truediv__(self, rhs: Union[int, float]) -> Vector:
        if not isinstance(rhs, (int, float)):
            raise TypeError
        return Vector(*map(lambda x: x/rhs, self))

    def __floordiv__(self, rhs: int) -> Vector:
        if not isinstance(rhs, (int, float)):
            raise TypeError
        return Vector(*map(lambda x: x//rhs, self))

    def to_int(self):
        return Vector(*map(int, self))

    def copy(self):
        return Vector(*map(lambda x: x, self))

    def normalize(self) -> Vector:
        return self * abs(self)

    def as_tuple(self) -> Tuple:
        return tuple(self)

    def rotate(self, degree):  # 회전
        degree *= 2 * pi / 360
        temp_x = self[0] * cos(degree) - self[1] * sin(degree)
        temp_y = self[0] * sin(degree) + self[1] * cos(degree)
        return Vector(temp_x, temp_y)
