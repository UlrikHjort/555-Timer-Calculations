#!/usr/bin/python
########################################################################
#                                                                           
#                          555 Monostable Mode                                      
#                                                                           
#                         555_Monostable_Mode.py                                    
#                                                                           
#                                 MAIN                                      
#                                                                           
#                   Copyright (C) 1998 Ulrik Hoerlyk Hjort                   
#                                                                           
#  555 Monostable Mode is free software;  you can  redistribute it                          
#  and/or modify it under terms of the  GNU General Public License          
#  as published  by the Free Software  Foundation;  either version 2,       
#  or (at your option) any later version.                                   
#  555 Monostable Mode is distributed in the hope that it will be                           
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
# Calculate T = ln(3)* R * C
#
# Where:
#       T is time in seconds
#       R is resistance in Ohm
#       C is capacity  in Farad
#
#####################################
def calculate_T():

  r_val = float(r_entry.get())
  c_val = float(c_entry.get())

  val = 1.1 *r_val * c_val
  t_entry.delete(0, END)
  t_entry.insert(0, str(val))



######################################
#
# Calculate R = T/(ln(3)* C)
#
# Where:
#       T is time in seconds
#       R is resistance in Ohm
#       C is capacity  in Farad
#
#####################################
def calculate_R():

  t_val = float(t_entry.get())  
  c_val = float(c_entry.get())

  val = t_val /(1.1 * c_val)
  r_entry.delete(0, END)
  r_entry.insert(0, str(val))


######################################
#
# Calculate C = T/(ln(3)* R)
#
# Where:
#       T is time in seconds
#       R is resistance in Ohm
#       C is capacity  in Farad
#
#####################################
def calculate_C():

  t_val = float(t_entry.get())  
  r_val = float(r_entry.get())

  val = t_val / (1.1 * r_val)     
  c_entry.delete(0, END)
  c_entry.insert(0, str(val))  


##################################
#
# Reset input entries to 0.0
#
##################################
def reset():
   t_entry.delete(0, END)
   t_entry.insert(0, str(0.0))
   r_entry.delete(0, END)
   r_entry.insert(0, str(0.0))
   c_entry.delete(0, END)
   c_entry.insert(0, str(0.0))


root=Tk()

h_label = Label(root, text="555 Monostable Mode")
h_label.grid(row=0, column=1)


t_label = Label(root, text="T (Sec)")
t_label.grid(row=1)

t_entry = Entry(root)
t_entry.grid(row=1, column=1)


r_label = Label(root, text="R (Ohm)")
r_label.grid(row=2)

r_entry = Entry(root)
r_entry.grid(row=2, column=1)


c_label = Label(root, text="C (Farads)")
c_label.grid(row=3)

c_entry = Entry(root)
c_entry.grid(row=3, column=1)

reset();

button=Button(root, text="Calculate T", command=calculate_T).grid(row=1, column=3);
button=Button(root, text="Calculate R", command=calculate_R).grid(row=2, column=3);
button=Button(root, text="Calculate C", command=calculate_C).grid(row=3, column=3);
button=Button(root, text="reset", command=reset).grid(row=4,column=1);

root.mainloop()
