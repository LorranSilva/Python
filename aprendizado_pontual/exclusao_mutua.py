#! /usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Thread
from time import sleep

lock = 0  # Variável de travamento


class Processo(Thread):

    def __init__(self, p):
        Thread.__init__(self)
        self.p = p

    def run(self):
        global lock
        while True:
            if lock == 0:
                lock = 1
                print ("processo %d entrou na regiao critica" % self.p)
                lock = 0
                print ("processo saiu da regiao critica")
            else:
                sleep(60)  # delay de 60
            sleep(3)  # delay de 3 só pra deixar tudo mais emocionante =P.


p1 = Processo(0)
p2 = Processo(1)

p1.start()
p2.start()
