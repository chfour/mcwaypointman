#!/usr/bin/env python3
from collections import namedtuple

Vec3 = namedtuple("Vec3", ["x", "y", "z"])

class Waypoint():
    def __init__(self, x: int, y: int, z: int, name="unnamed", dimension="minecraft:overworld") -> None:
        self.position = Vec3(x, y, z)
        self.name = name
        self.dimension = dimension
    def __repr__(self) -> str:
        return f"Waypoint(x={self.position.x}, y={self.position.y}, z={self.position.z}, name={self.name!r}, dimension={self.dimension!r})"
    def __str__(self) -> str:
        return f"{self.position.x} {self.position.y} {self.position.z} {self.dimension}\t{self.name}"

if __name__ == "__main__":
    test_waypoint = Waypoint(-10, 60, 20, name="my waypoint", dimension="minecraft:the_end")
    print(repr(test_waypoint))
    print(str(test_waypoint))
