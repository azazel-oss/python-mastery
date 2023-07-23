import csv
from collections import namedtuple

RowTuple = namedtuple("RowTuple", ["route", "date", "daytype", "rides"])


class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


class RowSlots:
    __slots__ = ["route", "date", "daytype", "rides"]

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_tuples(filename):
    """
    Read the bus ride data as a list of tuples
    """
    tracemalloc.start()
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    print(
        "Memory Use in Class Instance: Current %d, Peak %d"
        % tracemalloc.get_traced_memory()
    )
    tracemalloc.stop()
    return records


def read_rides_as_class_instance(filename):
    """
    Read the bus ride data as a list of class instances
    """
    tracemalloc.start()
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    print("Memory Use in tuples: Current %d, Peak %d" % tracemalloc.get_traced_memory())
    tracemalloc.stop()
    return records


def read_rides_as_class_with_slots(filename):
    """
    Read the bus ride data as a list of class instance with slots
    """
    tracemalloc.start()
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = RowSlots(route, date, daytype, rides)
            records.append(record)
    print(
        "Memory Use in classes with slots: Current %d, Peak %d"
        % tracemalloc.get_traced_memory()
    )
    tracemalloc.stop()
    return records


def read_rides_as_named_tuple(filename):
    """
    Read the bus ride data as a list of named tuples
    """
    tracemalloc.start()
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = RowTuple(route, date, daytype, rides)
            records.append(record)
    print(
        "Memory Use in named tuples: Current %d, Peak %d"
        % tracemalloc.get_traced_memory()
    )
    tracemalloc.stop()
    return records


def read_rides_as_dictionary(filename):
    """
    Read the bus ride data as a list of dictionary
    """
    tracemalloc.start()
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])

            record = {
                "route": route,
                "date": date,
                "daytype": daytype,
                "rides": rides,
            }
            records.append(record)
    print(
        "Memory Use in dictionary: Current %d, Peak %d"
        % tracemalloc.get_traced_memory()
    )
    tracemalloc.stop()
    return records


if __name__ == "__main__":
    import tracemalloc

    rows = read_rides_as_tuples("Data/ctabus.csv")
    rows = read_rides_as_class_instance("Data/ctabus.csv")
    rows = read_rides_as_dictionary("Data/ctabus.csv")
    rows = read_rides_as_named_tuple("Data/ctabus.csv")
    rows = read_rides_as_class_with_slots("Data/ctabus.csv")
