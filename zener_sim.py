# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 17:11:53 2022

@author: jason
"""

import circuitUtils

utils = circuitUtils.CircuitUtils()

print("---------------------------- Zener Diode Simulation ------------------------\n")
while (True):
    try:
        
        V_s = float(input("Enter a value for source voltage: "))
        R_s = float(input("Enter a value for source series resistance: "))
        
        V_z = -1 * float(input("Enter the specified Zener voltage: "))       #spec voltage in volts, will be given
        maxPower = float(input("Enter the max allowable power absorption: "))    #spec power rating in watts
        
        R_min = round((abs(V_z) * R_s)/(V_s - abs(V_z)), 3)
        R_max = round(abs(V_z) / (((V_s - abs(V_z))/R_s) - (maxPower / abs(V_z))), 3)
        
        if (R_max < 0):
            R_max = "No max"
        
        output = []
        
        R_load = float(input('Enter a value for the load resistor: '))
        
        R_eq = R_load + R_s
        
        if (R_load == 0):      #to avoid division by zero
            R_load == 0.000000000000000000000000001
            
        V_k = utils.voltageDivider(V_s, R_eq, R_load)
        V_d = -1 * V_k   
        
        if (V_d > V_z):     #ie, R_l isn't high enough (not enough equipment turned on)
        
            i_s = V_s/R_eq
            V_load = i_s * R_load
        
            output.append("\n----------------------- Begin Simulation -------------------------")
            output.append("Source Voltage: " + str(V_s) + " volts")
            output.append("Series Resistance: " + str(R_s) + " ohms")
            output.append("Series Current: " + str(i_s))
            output.append("Zener Voltage: " + str(V_z) + " volts")
            output.append("Power Rating: " + str(maxPower) + " watts")
            output.append('\nLoad Resistor Value: ' + str(R_load) + ' ohms')
            output.append("R_load min: " + str(R_min) + " ohms")
            output.append("R_load max: " + str(R_max) + " ohms\n")
        
            output.append("*** Zener is reverse-biased open ***\n")
            
            output.append("Load resistor voltage V_Rl = {0} volts".format(round(V_load, 3)))
            output.append("Load resistor current i_l= {0} amps".format(round(i_s, 3)))
            output.append("Zener diode voltage V_z = {0} volts".format(round(abs(V_z), 3)))
            output.append("Zener diode current i_z = {0} amps".format(0))    
            output.append("Power absorbed by Zener diode = {0} watts".format(0))
            
        elif (V_d <= V_z):  # Zener activation threshold is reached
    
            V_load = abs(V_z)
            i_s = (V_s - abs(V_z))/R_s
            i_load = V_load / R_load
            i_z = i_s - i_load
            power = i_z * abs(V_z)
        
            output.append("\n----------------------- Begin Simulation -------------------------")
            output.append("Source Voltage: " + str(V_s) + " volts")
            output.append("Series Resistance: " + str(R_s) + " ohms")
            output.append("Series Current: " + str(i_s))
            output.append("Zener Voltage: " + str(V_z) + " volts")
            output.append("Power Rating: " + str(maxPower) + " watts")
            output.append('\nLoad Resistor Value: ' + str(R_load) + ' ohms')
            output.append("R_load min: " + str(R_min) + " ohms")
            output.append("R_load max: " + str(R_max) + " ohms\n") 
        
            output.append("*** Zener is reverse-biased conducting ***\n")
        
            output.append("Load resistor voltage V_Rl = {0} volts".format(round(V_load, 3)))
            output.append("Load resistor current i_l= {0} amps".format(round(i_load, 3)))
            output.append("Zener diode voltage V_z = {0} volts".format(round(abs(V_z), 3)))
            output.append("Zener diode current i_z = {0} amps".format(round(i_z, 3)))
            output.append("Power absorbed by Zener diode = {0} watts".format(round(power, 3)))
            
            V_s_min = round(abs(((V_z * R_s) + (V_z * R_load))/R_load), 3)
            V_s_max = round(abs(((V_z + ((R_load * maxPower)/V_z)) * (R_s / R_load)) + V_z), 3)
            
            output.append("\n****************************************************************\n")
            output.append("For the given maximum power absorption of " + str(maxPower) + " watts,")
            output.append("the allowable range forsource voltage is:")
            output.append("Minimum Source Voltage: " + str(V_s_min) + " volts")
            output.append("Maximum Source Voltage: " + str(V_s_max) + " volts")
            output.append("\n****************************************************************\n")
            
            if (power > maxPower):
                output.append("***** Power absorbed by Zener diode exceeds the maximum allowable!!! *****")
        output.append("----------------------- End of Simulation ----------------------\n")
        
        for line in output:
            print(line)
            
        print("Enter another set of value or press Ctrl+c at any time to end the simulation\n")
        
        # option = input("Output to file?  <y , n>: ")
        
        # if option == "y":
        #     filename = input("Enter file prefix: ")
            
        #     filename = filename + str(".txt")
        #     f = open(filename, "w")
            
        #     for line in output:
        #         f.write(line + str("\n"))
        #     f.close()
                
            # print(str(filename) + " written successfully")
    except:
        KeyboardInterrupt
        break
print("Program Ending")
                            
