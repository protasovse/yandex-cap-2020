"""
## D. Поиск ломающего коммита

В Поиске Яндекса реализована так называемая политика «зелёного транка»: любой код,
попадающий в репозиторий, с некоторыми оговорками гарантированно не ломает сборку
и тесты.

Тесты, впрочем, бывают крайне сложными, и запускать их все на каждый коммит оказывается
нецелесообразно. Так что для особенно сложных случаев реализована следующая процедура:
тесты запускаются с некоторой регулярностью, а проверяется сразу набор коммитов.
Таким образом, в течение некоторого времени в транк может попасть n непроверенных коммитов,
среди которых как минимум один содержит ошибку.

В такой ситуации тестирующая система должна обнаружить номер m первого коммита,
сломавшего тесты. Этот номер обладает следующим свойством: все коммиты с номерами,
меньшими m, успешно проходят тесты, а коммиты с номерами, большими либо равными m,
тесты не проходят. В данной задаче гарантируется, что коммит с указанными свойствами
обязательно существует и является единственным.

В целях экономии ресурсов тестирующая система может проверять только один коммит за раз.
Вам требуется написать программу, которая будет определять номер m.

Эта задача немного необычна — в ней вам предстоит реализовать интерактивное взаимодействие
с тестирующей системой. Это означает, что вы можете делать запросы и получать ответы в
онлайн-режиме. Обратите внимание, что ввод/вывод в этой задаче — стандартный
(то есть с экрана на экран). После вывода очередного запроса обязательно используйте функции
очистки потока, чтобы часть вашего вывода не осталась в каком-нибудь буфере.
Например, на С++ надо использовать функцию fflush(stdout), на Java вызов System.out.flush(),
на Pascal flush(output) и stdout.flush() для языка Python.

Вы можете делать запросы к тестирующей системе. Каждый запрос — это вывод целого числа,
принадлежащего диапазону от 1 до n. В ответ тестирующая система вернёт один из двух
результатов:

    строка «1» (без кавычек), если коммит с соответствующим номером успешно проходит все тесты;
    строка «0» (без кавычек), если коммит с соответствующим номером не проходит тесты.

Если ваша программа в точности знает номер m, она должна вывести строку вида «! m», после чего завершить свою работу.

Вашей программе разрешается сделать не более 25 запросов. 
"""
import sys


def get_result(i: int) -> bool:
    sys.stdout.write(str(i) + "\n")
    sys.stdout.flush()
    res = not int(sys.stdin.readline())
    return res


hi = int(sys.stdin.readline())
lo = 1

while hi > lo + 1:
    mi = lo + (hi - lo) // 2
    if get_result(mi):
        hi = mi
    else:
        lo = mi

sys.stdout.write(f"! {lo if get_result(lo) else hi}\n")
