# Chaos-Pendulum
Runnable simulation of a chaos pendulum or double-pendulum. By default the two lengths and two masses of 
the conjoined pendula are set equal. Gravity is reduced to ~0.41g. Due to rendering instability and other 
factors still being explored, the parameters of each pendulum as well as tending toward realistic gravity
display much greater system instability and sensitivity to intitial conditions than we would expect in 
the physical world. With that disclaimer and considerations taken, it does behave how one would expect.

# Python Dependencies & Software Used
Python 3.8.5, 
pygame 2.0.0, 
IDLE: Atom 1.53.0 x64 with package ide-python 1.6.2

# Downloading & Running
Download main, formular, and points. For now, gui isn't necessary, but it is a very early development of a 
GUI being designed to run the chaos pendulum suite from a graphical interface.

Windows users: 
Open windows terminal amd navigate to directory containing main.py, formular.py, and points.py via "cd" command. 
Typical/default Windows download location looks like "c:\users\<name>\downloads\". You can run it here or place 
elsewhere if desired(just know whereever you place it, you must navigate there in your terminal). Using command
"python main.py" and pressing enter, terminal should launch a new window with a rendered demonstration of a chaos
pendulum with default settings, and all these parameters are listed in the top pane of the window.

# Editing
If you would like to set your own parameters:
Unfortunately, the GUI isn't functioning yet so, using your preferred text editor(eg. Notepad++), directly modify
the values for mass, length, angles, etc in main.py. Do not modify formular.py or points.py.
