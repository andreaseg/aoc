import sys
import re
from enum import Enum

def part1(guard_events):
    guard_dict = dict()
    current_guard_id = -1
    awake_timestamp = 0
    for event in guard_events:
        if event.event_type == GuardEventType.BEGIN:
            current_guard_id = event.guard_id
            if current_guard_id not in guard_dict:
                guard_dict[current_guard_id] = 0
            awake_timestamp = event.get_minute()
        elif event.event_type == GuardEventType.WAKE_UP:
            guard_dict[current_guard_id] += event.get_minute() - awake_timestamp 
        elif event.event_type == GuardEventType.FALL_ASLEEP:
            awake_timestamp = event.get_minute() 
        else:
            raise ValueError('Invalid event type')
    (guard_id, asleep) = max(guard_dict.items(), key = lambda tup: tup[1])
    
    asleep_times = 60*[0]
    for event in list(filter(lambda g: g.guard_id == guard_id, guard_events)):
        if event.event_type == GuardEventType.BEGIN:
            awake_timestamp = event.get_minute()
        elif event.event_type == GuardEventType.WAKE_UP:
            for time in range(awake_timestamp, event.get_minute()):
                asleep_times[time] += 1
        elif event.event_type == GuardEventType.FALL_ASLEEP:
            awake_timestamp = event.get_minute()
        else:
            raise ValueError('Invalid event type')
    sleepiest_time = argmax(asleep_times)

    print("Sleepiest guard is %i, slept for a total of %i minutes, answer is %i" % (guard_id, asleep, (guard_id * sleepiest_time)))

def part2(guard_events):
    guard_dict = dict()

    time = 0
    current_guard_id = -1
    for event in guard_events:
        if event.event_type == GuardEventType.BEGIN:
            current_guard_id = event.guard_id
            if current_guard_id not in guard_dict:
                guard_dict[current_guard_id] = 60*[0]
            time = event.get_minute()
        elif event.event_type == GuardEventType.WAKE_UP:
            for t in range(time, event.get_minute()):
                guard_dict[current_guard_id][t] += 1
        elif event.event_type == GuardEventType.FALL_ASLEEP:
            time = event.get_minute()
        else:
            raise ValueError('Invalid event type')
    (guard_id, asleep_times) = max(guard_dict.items(), key = lambda tup: max(tup[1]))
    sleepiest_time = argmax(asleep_times)

    print("Sleepiest guard is %i, slept most at time %i, answer is %i" % (guard_id, sleepiest_time, (guard_id * sleepiest_time)))


def argmax(list):
    return max(range(len(list)), key=lambda i:list[i])

class GuardEventType(Enum):
    BEGIN = 1
    FALL_ASLEEP = 2
    WAKE_UP = 3
    UNKNOWN = 4

class GuardEvent:
    def __init__(self, guard_id: int, month: int, day: int, minute: int, event_type: GuardEventType):
        self.guard_id = guard_id
        self.time = (month, day, minute)
        self.event_type = event_type

    def get_minute(self):
        return self.time[2]

    def __repr__(self):
        return '< GuardEvent: %i >' % self.guard_id


def parse_events(event_list):
    event_list.sort()
    parsed_events = []
    time_reg = re.compile(r'\[\d+-(\d+)-(\d+)\s\d+:(\d+)\]\s(.*)')
    guard_reg = re.compile(r'(\d+)')
    guard_id = -1
    for line in event_list:
        matches = time_reg.match(line)
        month = int(matches.group(1))
        day = int(matches.group(2))
        minute = int(matches.group(3))
        message = matches.group(4)
        event_type = GuardEventType.UNKNOWN
        if message[0] == 'w':
            event_type = GuardEventType.WAKE_UP
        elif message[0] == 'f':
            event_type = GuardEventType.FALL_ASLEEP
        else:
            g_matches = guard_reg.search(message)
            guard_id = int(g_matches.group(1))
            event_type = GuardEventType.BEGIN
        parsed_events.append(GuardEvent(guard_id, month, day, minute, event_type))
    return parsed_events


def main():
    events = parse_events(sys.stdin.readlines())
    print("Part 1")
    part1(events)
    print("Part 2")
    part2(events)

if __name__ == '__main__':
    main()
