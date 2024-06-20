from time import sleep

for i in range(10, -1, -1):
    print(i)
    if i != 0:
        sleep(1)
        
print('KABOOOM!!!')
