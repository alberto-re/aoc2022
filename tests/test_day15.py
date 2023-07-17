from adventofcode2022.day15 import (
    sensor_data_from_text,
    SensorMap,
    find_distress_beacon,
    tuning_frequency,
)

EXAMPLE_INPUT = """\
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""


def test_sensor_data_from_text():
    sensors = [sensor_data_from_text(x) for x in EXAMPLE_INPUT.splitlines()]
    assert sensors[0].x == 2
    assert sensors[0].y == 18
    assert sensors[3].x == 12
    assert sensors[3].y == 14


def test_map_add_sensor():
    sensors = [sensor_data_from_text(x) for x in EXAMPLE_INPUT.splitlines()]
    sensor_map = SensorMap()
    for sensor in sensors:
        sensor_map.add_sensor(sensor)
    assert len(sensor_map.sensors) == 14


def test_map_row_coverage():
    sensors = [sensor_data_from_text(x) for x in EXAMPLE_INPUT.splitlines()]
    sensor_map = SensorMap()
    for sensor in sensors:
        sensor_map.add_sensor(sensor)
    covered, _, _ = sensor_map.row_coverage(10)
    assert len(covered) == 26


def test_find_distress_beacon():
    sensors = [sensor_data_from_text(x) for x in EXAMPLE_INPUT.splitlines()]
    sensor_map = SensorMap()
    for sensor in sensors:
        sensor_map.add_sensor(sensor)
    coords = find_distress_beacon(sensor_map, 0, 0, 20, 20)
    assert coords == (14, 11)
    assert tuning_frequency(coords[0], coords[1]) == 56000011
