import threading
import time


def feed_dog(food):
    print('Begin feeding the dog.')
    print(f"The dog is eating {food}.")
    time.sleep(5)
    print('Feeding the dog complete.')


def feed_cat(food):
    print('Begin feeding the cat.')
    print(f"The cat is eating {food}.")
    time.sleep(5)
    print('Feeding the cat complete.')


x = threading.Thread(target=feed_dog, args=("food",))
x.start()

y = threading.Thread(target=feed_cat, args=("food",))
y.start()

print(f"Total threads = {threading.activeCount()}")
