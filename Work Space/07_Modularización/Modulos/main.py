#### Una forma de importar....
print ("========== Una forma de importar un modulo ============ ")
import febonacci

febonacci.fibo(100)

print(febonacci.fibo2(100))


print ("========== Otra forma de importar un modulo ============ ")
#### otra  forma de importar....
from febonacci import fibo, fibo2

fibo(100)

print(fibo2(100))


print ("========== Otra forma de importar un modulo ============ ")
from febonacci import *
fibo(500)


print ("========== Otra forma de importar un modulo con as f ============ ")
import febonacci as f
f.fibo(100)

print(f.fibo2(100))


print ("========== Otra forma de importar un modulo con from ============ ")

from febonacci import fibo as f1
from febonacci import fibo2 as f2
f1(100)

print(f2(100))

print ("===========Import Sys=====================")
import sys


print ("===========Vamos a ver la fucnión dir=====================")
import febonacci

print (dir(febonacci))

print ("===========Vamos a ver importando modulo sys=====================")
import sys

print (dir(sys))


print ("===========Vamos a ver importando modulo builtins=====================")
import builtins

print (dir(sys))







