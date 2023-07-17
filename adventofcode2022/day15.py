#!/usr/bin/env python3
# --- Day 15: Beacon Exclusion Zone ---
from typing import Iterator
from dataclasses import dataclass
import re


def manhattan(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


@dataclass
class Beacon:
    x: int
    y: int


class Sensor:
    def __init__(self, x: int, y: int, beacon: Beacon) -> None:
        self._x = x
        self._y = y
        self._beacon = beacon
        self._coverage = manhattan(x, y, beacon.x, beacon.y)

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @property
    def beacon(self) -> Beacon:
        return self._beacon

    @property
    def coverage(self) -> int:
        return self._coverage

    @property
    def positions_perimeter(self) -> Iterator[tuple[int, int]]:
        perimeter_dist = self._coverage + 1
        for qx, qy in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
            for xd in range(perimeter_dist + 1):
                yd = perimeter_dist - xd
                xd *= qx
                yd *= qy
                yield (self.x + xd, self.y + yd)

    def is_point_inside_coverage(self, x: int, y: int) -> bool:
        return manhattan(self.x, self.y, x, y) <= self.coverage


class SensorMap:
    def __init__(self) -> None:
        self._sensors: list[Sensor] = []

    @property
    def sensors(self) -> list[Sensor]:
        return self._sensors

    def add_sensor(self, sensor: Sensor) -> None:
        self._sensors.append(sensor)

    def row_coverage(self, y: int) -> tuple[set[int], set[int], set[int]]:
        coverage = set()
        sensors = set()
        beacons = set()
        for sensor in self.sensors:
            if sensor.y == y:
                sensors.add(sensor.x)
            if sensor.beacon.y == y:
                beacons.add(sensor.beacon.x)
        for sensor in self.sensors:
            pos_dist = manhattan(sensor.x, y, sensor.x, sensor.y)
            delta = sensor.coverage - pos_dist
            if delta < 0:
                continue
            coverage.update([x for x in range(sensor.x - delta, sensor.x + delta + 1)])
        coverage -= sensors
        coverage -= beacons
        return coverage, sensors, beacons


def find_distress_beacon(
    sensor_map: SensorMap, min_x: int, min_y: int, max_x: int, max_y: int
) -> tuple[int, int] | None:
    candidates: list[tuple[int, int]] = []
    for sensor in sensor_map.sensors:
        candidates.extend(sensor.positions_perimeter)
    for x, y in candidates:
        if x < min_x or x > max_x or y < min_y or y > max_y:
            continue
        found = True
        for sensor in sensor_map.sensors:
            if sensor.is_point_inside_coverage(x, y):
                found = False
                break
        if found:
            return (x, y)
    return None


def tuning_frequency(x: int, y: int) -> int:
    return x * 4000000 + y


SENSOR_DATA_PATTERN = (
    r"Sensor at x=([\-\d]+), y=([\-\d]+): closest beacon is at x=([\-\d]+), y=([\-\d]+)"
)


def sensor_data_from_text(text: str) -> Sensor:
    match = re.match(SENSOR_DATA_PATTERN, text)
    assert match
    beacon = Beacon(int(match.group(3)), int(match.group(4)))
    sensor = Sensor(int(match.group(1)), int(match.group(2)), beacon)
    return sensor


def main() -> None:
    with open("input/day15.txt") as f:
        sensors = [sensor_data_from_text(x) for x in f.read().splitlines()]

    sensor_map = SensorMap()
    for sensor in sensors:
        sensor_map.add_sensor(sensor)

    coverage, _, _ = sensor_map.row_coverage(2000000)
    print(f"Part one solution: {len(coverage)}")

    coords = find_distress_beacon(sensor_map, 0, 0, 4000000, 4000000)
    assert coords is not None
    print(f"Part two solution: {tuning_frequency(coords[0], coords[1])}")


if __name__ == "__main__":
    main()
