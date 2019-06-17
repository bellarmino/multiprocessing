import math
from multiprocessing import Process, Value


def mprocess_func(num, ini, fim, exit):
    num_float = float(num)
    for i in range(int(ini), int(fim)):
        if exit.value==1: return
        if (num_float / i).is_integer():
            exit.value = 1
            return
    return


def check_prime(num):
    sqrt_num = math.sqrt(num)
    meio_num = int(sqrt_num / 2)
    if meio_num <= 2:
        meio_num = 3
    #Shared memory
    smem = Value('i', 0)

    # Primeiro grupo de verificação
    p1 = Process(target=mprocess_func, args=(num, 2, meio_num, smem))
    p1.start()
    # Segundo grupo de verificação
    p2 = Process(target=mprocess_func, args=(num, meio_num, int(sqrt_num)+1, smem))
    p2.start()

    p1.join()
    p2.join()

    if smem.value==1:
        return False
    else:
        return True

if __name__ == "__main__":

    print(check_prime(10000019))