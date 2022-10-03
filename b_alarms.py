"""
Работа в большинстве IT-компаний имеет много преимуществ: нет дресс-кода, можно
иногда поработать удалённо, классные и умные коллеги и, конечно же, свободный
график! Однако свободный график и возможность работать удалённо требуют большой
силы воли.

Программист Алексей любит работать по ночам и не любит приходить на работу
поздно. Чтобы точно проснуться с утра, Алексей каждый вечер заводит
N будильников на своём телефоне. Каждый будильник устроен таким образом,
что он звонит каждые X минут с того момента времени, на который его завели.
Например, если будильник был заведён на момент времени ti, то он будет звонить
в моменты времени ti, ti+X, ti+2⋅X и так далее. При этом если какие-то два
будильника начинают звонить в один момент времени, то отображается только один
из них.

Известно, что прежде чем проснуться, Алексей каждое утро слушает ровно
K будильников, после чего просыпается. Определите момент времени,
когда Алексей проснётся.


## Формат ввода
Первая строка содержит три целых числа N, X и K (1≤N≤105, 1≤X,K≤109) —
количество будильников, периодичность звонков и количество будильников,
которое нужно отключить, чтобы Алексей проснулся.

Вторая строка содержит N целых чисел t1, t2, …, tN (1≤ti≤109) —
моменты времени на которые были заведены будильники.

## Формат вывода
Выведите одно число — момент времени, когда Алексей проснётся.
"""

import sys
from functools import lru_cache
from math import ceil, floor
from typing import Generator, Iterable


def remove_unnecessary_alarms(
    alarms: Iterable[int], delta: int
) -> Iterable[int]:
    """Только уникальные будильники."""
    modules = {}
    for start_time in sorted(alarms):
        module = start_time % delta
        if module not in modules:
            modules[module] = start_time
            yield start_time


@lru_cache(maxsize=None)
def sum_bells_for_alarms_in_time(
    alarms: Iterable[int],
    current_time: int,
    delta: int
) -> int:
    """Вычисляем количество звонков будильников на время current_time."""
    return sum(
        [
            max((current_time - alarm) // delta + 1, 0)
            for alarm in alarms
        ]
    )


def main(row1: str, row2: str):
    alarm_count, delta, need_bell_count = map(int, row1.split())
    alarms = map(int, row2.split())

    clean_alarms = tuple(remove_unnecessary_alarms(alarms, delta))

    l = min(clean_alarms)
    r = sys.maxsize

    while l + 1 < r:
        c = l + ((r - l) >> 1)
        if (
            sum_bells_for_alarms_in_time(clean_alarms, c, delta) >=
            need_bell_count
        ):
            r = c
        else:
            l = c

    if (
        sum_bells_for_alarms_in_time(clean_alarms, l, delta) == need_bell_count
    ):
        print(l)
    elif (
        sum_bells_for_alarms_in_time(clean_alarms, r, delta) == need_bell_count
    ):
        print(r)
    else:
        print(-1)


if __name__ == "__main__":
    row1 = sys.stdin.readline().strip()
    row2 = sys.stdin.readline().strip()
    main(row1, row2)
