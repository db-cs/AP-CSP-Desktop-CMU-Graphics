# AP CSP Desktop CMU Graphics

The CMU desktop allows you to create graphics without the web editor found on CMU academy. It also allows you to utilize other Python libraries in your code. You can even make requests via the internet or even edit files on your machine. This is just a clone of what you can download at [Desktop CMU Graphics](https://academy.cs.cmu.edu/desktop) with some additional instructions for class. 

## Getting Started

Open the [`example.py`](./example.py) file and read through the code and comments. Then open terminal using `cmd+j` on the Macs. Type `python3 example.py` and hit enter. Your graphic should pop up in a new window. Now you can close it.

## Making Your Own

Once again in the terminal type the command `touch myFile.py`. This will create a new python script with the name `myFile`. Feel free to change the name to something you prefer. Now for the boilerplate code. In order to use the Desktop CMU Graphics library you need to import the code. Then you can write like normal. Finally, you'll need to incude a command to get the library to run.

```python
from cmu_graphics import *

# Your code here

cmu_graphics.run()
```

Remeber that you have the [Docs + Colors](https://academy.cs.cmu.edu/docs) available online to remind yourself of the various shapes and colors available.

You can run it like you did with the example, but now you'd use `python3 myFile.py` instead. Each time you make a change to your code you need to save your changes. You can use the keyboard shortcut `cmd+s` on the Macs. Then you'll need to rerun your code to see the changes. In terminal you can use the up arrow to reload previous commands to save from having to retype it. There is also a cool play button at the top of the editor that you can use if you don't want to use the terminal.

## Incremental and Iterative Development

Unlike the CMU academy, you don't have multiple tasks to demonstrate iterative development. Professionals use version control systems to record changes to their program. On the Macs we have a program called Git that records these changes. Learning Git is an essential skill if you have interest in working in software development. I have a cheatsheet to help you with these commands, but here are the basics.

First you need to configure a few settings:

```bash
git config --global user.name "Type Your Name Here"
git config --global user.email "Type Your Email Here"
```

These set it up so your activity is signed correctly and you are recorded as the author of the changes.

Next each time you have made a change that you want to lock-in you need to commit it to the Git repository. This takes place in 3 steps:

```bash
git status # Checks what changes have been made
git add file.py # Adds changes in the specified file
git commit -m 'Message describing change' # Commits the change to the repository
```

Now you can check for previous changes using Git log:

```bash
git log
```

This is the way you save incremental changes. So once you have finished an iteration, you need to take it using a version number.

```bash
git tag -a v1.0 -m 'Version 1 of My Graphics'
```

This uses the typical pattern of version numbers. You can view the various tags details using the following command:

```bash
git tag # Shows all the tags
git show 1.0 # Shows the details for a specific tag
```

## Looking Under the Hood

All the code for the library is included in the folder [`cmu_graphics`](./cmu_graphics). Feel free to explore but be sure you do not change anything.
