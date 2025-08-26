"""
Потрібно розробити програму, яка імітує приймання та обробку заявок:
програма має автоматично генерувати нові заявки (ідентифіковані унікальним номером або іншими даними),
додавати їх до черги, а потім послідовно видаляти із черги для "обробки", імітуючи таким чином роботу сервісного центру.

З використанням черги Queue з модуля queue
"""

import multiprocessing
import random
import time
from queue import Queue
from faker import Faker
from colorama import Fore, Style

fake = Faker()

class Ticket:
    def __init__(self, title: str, request: str):
        self.title = title
        self.request = request
        self.id = hash(title + request)


def delay():
    """ Випадкова затримка між генерацією запитів (1-5 секунд) """
    time.sleep(random.uniform(1, 5))


def run_inf(callback, *args):
    """ Нескінченне виконання переданої функції із затримкою між виконаннями """
    while True:
        callback(*args)
        delay()


def generate_request(q: Queue):
    ticket = Ticket(
        title=' '.join(fake.words(nb=2)),
        request=fake.text(max_nb_chars=100),
    )
    q.put(ticket)
    print(f'{Fore.CYAN}Generated ticket: {ticket.id} - {ticket.title}{Fore.RESET}')

    return ticket


def process_request(q: Queue):
    if q.empty():
        print(f'{Fore.RED}Queue is empty{Fore.RESET}')
        return

    ticket = q.get()
    print(f'{Fore.GREEN}Processing ticket: {ticket.title}')
    print(Fore.LIGHTWHITE_EX + Style.DIM + ticket.request + Fore.RESET)

    delay()

    print(Fore.GREEN + Style.BRIGHT + 'Done' + Fore.RESET)

    return


if __name__ == '__main__':
    mq = multiprocessing.Queue()

    request_generator = multiprocessing.Process(target=run_inf, args=(generate_request, mq))
    request_processor = multiprocessing.Process(target=run_inf, args=(process_request, mq))

    request_generator.start()
    request_processor.start()

    try:
        request_generator.join()
        request_processor.join()
    except KeyboardInterrupt:
        print("\nПереривання роботи...")
        request_generator.terminate()
        request_processor.terminate()
