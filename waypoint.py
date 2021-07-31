#!/usr/bin/env python3
from collections import namedtuple
from math import floor

Vec3 = namedtuple("Vec3", ["x", "y", "z"])

class NotACopiedLocation(Exception):
    def __init__(self, copied: str) -> None:
        super().__init__(f"'{copied}' is not a F3+C teleport command")

class Waypoint():
    @staticmethod
    def from_copied(copied: str):
        if not copied.startswith("/execute in "): raise NotACopiedLocation(copied)
        arguments = copied.split(" ")[2:]
        if len(arguments) < 9: raise NotACopiedLocation(copied)

        try:
            x = floor(float(arguments[4]))
            y = floor(float(arguments[5]))
            z = floor(float(arguments[6]))
        except ValueError:
            raise NotACopiedLocation(copied)
        
        return __class__(x, y, z, dimension=arguments[0])
        
    
    def __init__(self, x: int, y: int, z: int, name="unnamed", dimension="minecraft:overworld") -> None:
        self.position = Vec3(x, y, z)
        self.name = name
        self.dimension = dimension
    def __repr__(self) -> str:
        return f"Waypoint(x={self.position.x}, y={self.position.y}, z={self.position.z}, name={self.name!r}, dimension={self.dimension!r})"
    def __str__(self) -> str:
        return f"{self.position.x} {self.position.y} {self.position.z} {self.dimension}\t{self.name}"

if __name__ == "__main__":
    test_copied = "/execute in minecraft:overworld run tp @s 106.35 73.00 71.35 -1733.88 12.00"
    print(test_copied)
    test_waypoint = Waypoint.from_copied(test_copied)
    print(repr(test_waypoint))
    print(str(test_waypoint))
