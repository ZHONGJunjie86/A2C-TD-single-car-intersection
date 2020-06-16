import numpy as np 
import os 
import random
def main():
    if(os.path.exists('D:/Software/GamaWorkspace/Python/python_AC_1.csv') == False or
       os.path.exists("D:/Software/GamaWorkspace/Python/python_AC_2.csv") == False): #
        data = []
        data.append(0)
        return data
    elif(os.stat("D:/Software/GamaWorkspace/Python/python_AC_1.csv").st_size == 0 or 
         os.stat("D:/Software/GamaWorkspace/Python/python_AC_2.csv").st_size == 0): #
        data = []
        data.append(0)
        return data
    else:
        try:
            if(random.random()>0.51):
                state = np.loadtxt("D:/Software/GamaWorkspace/Python/python_AC_1.csv", delimiter=",")  #D:/Software/GamaWorkspace/Python/from_python.csv
            else:
                state = np.loadtxt("D:/Software/GamaWorkspace/Python/python_AC_2.csv", delimiter=",")
            data = []
            data.append(0)
            if(state.size == 1):
                data.append(state)
                return data
            elif(state.size == 2):
                #data.append(state[0])
                #data.append(state[1])  直接传 state[0]类型错误
                a = float(state[0])
                b = float(state[1])
                return [a,b]        #data
            else:
                return data
        except(ValueError):
            data = []
            data.append(0)
            return data


if __name__ == '__main__':
    main()