# -*- coding: utf-8 -*-
import redlab as rl

print("------- einzelne Werte -------------------------")
print("16 Bit Value: " + str(rl.cbAIn(0,0,1)))
print("Voltage Value: " + str(rl.cbVIn(0,0,1)))
# print("------- Messreihe -------------------------")
# print("Messreihe: " + str(rl.cbAInScan(0,0,0,300,8000,1)))
# print("Messreihe: " + str(rl.cbVInScan(0,0,0,300,8000,1)))
# #print("Samplerate: " + str(rl.cbInScanRate(0,0,0,8000)))
# print("------- Ausgabe -------------------------")
# def get_in():
#     while(True):
#         in_put = input()
#         if in_put != "x":
#             rl.cbVOut(0,0,101,float(in_put))
#             print("Voltage Value: " + in_put)
#         elif in_put == "x":
#             break
    
    
# if __name__ == "__main__":
#     get_in()