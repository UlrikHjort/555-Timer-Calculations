#!/usr/bin/python
########################################################################
#                                                                           
#                          555 Astable Mode                                      
#                                                                           
#                         555_Astable_Mode.py                                    
#                                                                           
#                                 MAIN                                      
#                                                                           
#                   Copyright (C) 1998 Ulrik Hoerlyk Hjort                   
#                                                                           
#  555 Astable Mode is free software;  you can  redistribute it                          
#  and/or modify it under terms of the  GNU General Public License          
#  as published  by the Free Software  Foundation;  either version 2,       
#  or (at your option) any later version.                                   
#  555 Astable Mode is distributed in the hope that it will be                           
#  useful, but WITHOUT ANY WARRANTY;  without even the  implied warranty    
#  of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                  
#  See the GNU General Public License for  more details.                    
#  You should have  received  a copy of the GNU General                     
#  Public License  distributed with Yolk.  If not, write  to  the  Free     
#  Software Foundation,  51  Franklin  Street,  Fifth  Floor, Boston,       
#  MA 02110 - 1301, USA.                                                    
########################################################################                                                                          

from Tkinter import *




######################################
#
# Calculate:
#        T1 = 0.693 *(R1 + R2) * C
#
#        T2 = 0.693 * R2 * C
#
#        T TOTAL = 0.693 * (R1 + (2.0 * R2)) * C 
#
#        FREQUENCY = 1.44 / ((R1 + (2.0 * R2)) * C)
#
#        DUTY = 100.0 - ((100.0 * R2)/(R1+(2.0*R2)))
#
# Where:
#       T is time in seconds
#       R is resistance in Ohm
#       C is capacity  in Farad
#
#####################################
def calculate():

    r1 = float(r1_entry.get())
    r2 = float(r2_entry.get())
    c  = float(c_entry.get())

    t1 = 0.693 *(r1 + r2) * c
    t2 = 0.693 * r2 * c
    t_total = 0.693 * (r1 + (2.0 * r2)) * c
    freq = 1.44 / ((r1 + (2.0 * r2)) * c)
    duty = 100.0 - ((100.0 * r2)/(r1+(2.0*r2)))

    t1_var.set("T1 = " + str(t1) + " s")
    t2_var.set("T2 = " + str(t2) + " s")
    t_total_var.set("T total period = " + str(t_total) + " s");
    freq_var.set("Frequency = " + str(freq) + " Hz");
    duty_var.set("Duty = " + str(duty) + " % High");

##################################
#
# Reset input entries to 0.0
#
##################################
def reset():
   r1_entry.delete(0, END)
   r1_entry.insert(0, str(0.0))
   r2_entry.delete(0, END)
   r2_entry.insert(0, str(0.0))
   c_entry.delete(0, END)
   c_entry.insert(0, str(0.0))

   t1_var.set("T1 = --- s");
   t2_var.set("T2 = --- s");
   t_total_var.set("T total period = --- s");
   freq_var.set("Frequency =  --- Hz");
   duty_var.set("Duty =  --- % High");


root=Tk()

h_label = Label(root, text="555 Astable Mode")
h_label.grid(row=0, column=1)


r1_label = Label(root, text="R1 (Ohm)")
r1_label.grid(row=2)

r1_entry = Entry(root)
r1_entry.grid(row=2, column=1)

r2_label = Label(root, text="R2 (Ohm)")
r2_label.grid(row=3)

r2_entry = Entry(root)
r2_entry.grid(row=3, column=1)


c_label = Label(root, text="C (Farads)")
c_label.grid(row=4)

c_entry = Entry(root)
c_entry.grid(row=4, column=1)


t1_var = StringVar()

t1_label = Label(root, textvariable=t1_var)
t1_label.grid(row=5)

t2_var = StringVar()

t2_label = Label(root, textvariable=t2_var)
t2_label.grid(row=6)

t_total_var = StringVar()
t_total_label = Label(root, textvariable=t_total_var)
t_total_label.grid(row=7)

freq_var = StringVar()

freq_label = Label(root, textvariable=freq_var)
freq_label.grid(row=8)


duty_var = StringVar()

duty_label = Label(root, textvariable=duty_var)
duty_label.grid(row=9)

reset();

button=Button(root, text="Calculate", command=calculate).grid(row=10, column=1);
button=Button(root, text="reset", command=reset).grid(row=10,column=2);

root.mainloop()
