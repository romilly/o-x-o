# Ten minutes to RIDE

This is a short introductory guide to Dyalog APL's **RIDE** interface.

**RIDE** stands for Remote Integrated Development Environment.

When you code using Dyalog APL, you'll use two key software components.

1. *The APL interpreter* which executes APL code.
1. *A developer interface* which allows you to write code, invoke the interpreter and debug code when necessary.

Most new users develop using RIDE. Other interfaces are available, including an
[open source kernel](https://github.com/Dyalog/dyalog-jupyter-kernel)
for [jupyter notebooks](https://jupyter.org/), but RIDE is recommended
and is part of the default installation of Dyalog APL.

Dyalog's installation depends on the target environment.
[Windows]() users, [maxOS X]() users, [Linux users]() with Intel/AMD hardware and [Raspberry Pi]()
users will find information specific to their environment on the Dyalog website.

The links above are current as of December 2020 but are subject to change.

This short guide will help you get started with RIDE and APL after you have installed the appropriate software.

RIDE works the same way in all the environments listed above.

## Three ways to work

There are three common ways of using RIDE to connect you to the APL interpreter, They are determined by
the location of the GUI (Graphic User Interface) you interact with, and the location of the computer on
which APL is installed.

Here are the configurations:

1. *Local GUI, local Interpreter*. This is the configuration you use if you're using RIDE on the computer
   on which you installed APL.
1. *Local GUI, remote interpreter*. This allows a laptop user (for example) to interact with a server, or to interact
   with a Raspberry Pi that has no monitor, keyboard or mouse installed. RIDE needs to be installed on both computers,
   and the computers must be connected by a TCP network.
1. *Local access to a remote Desktop*, remote GUI, remote interpreter. This is essentially the same as 1. above.
   You'll be accessing the other computer using a protocol like *VNC* or *RDP* but this won't affect RIDE's operation.
   You'll need to configure RIDE for **local** use. 

## Starting RIDE

In each case you will start RIDE by clicking on the icon which was added during installation.

![Starting RIDE](im)





