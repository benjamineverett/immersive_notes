# Assignment: Working with Command Lines

## Objectives
You will be using commands to create, move and rename files and directories.

If you have never used a Terminal before, follow the guided steps in [assignment_2_command_line_sample.md](assignment_2_command_line_sample.md). This will show you the commands you need to type to create directory, move them, copy files and delete them.

If you are somewhat familiar with a Terminal, figure out the right command lines to achieve the action items described below. The command lines, in the order you typed them, should be placed in the YOUR ANSWER placeholder.

A [cheatsheet](../resources/command_line_basics.md) is available to help you.

_______________________________________

## Questions

Do not use finder, just stay in the Terminal

1. Make a `testing_directory` on your Desktop.
2. Inside this directory, make a `code` directory, a `data` directory, a `raw_data` directory and a `test` directory.
3. Enter the `testing_directory` and create a `readme.md` file and a `do_not_readme.md` file with Atom.
4. Create a `simple_script.py` in the `test` directory with Atom, add the following text: `print('Hello World!')`.
5. Place the `raw_data` directory inside the `data` directory.
6. Get the new path to the `raw_data` directory.
7. Move the `simple_script.py` inside the `code` directory.
8. Rename the python script `hello_world.py`.
9. Delete the `do_not_readme.md` file.

To check your work, you can run `$ tree` in the `testing_directory`. Your output should look like this.

```
├── code
│   └── hello_word.py
├── data
│   └── raw_data
├── readme.md
└── test
```
_______________________________________

## Answers
Please indicate the commands necessary to execute steps 1-9.

YOUR ANSWER:
1. cd desktop

  mkdir testing_directory
2. cd testing_directory

    mkdir code

    mkdir data

    mkdir raw_data

    mkdir test
3. touch readme.md

    touch do_not_readme.md
4. touch test/simple_script.py

    open test/simple_script.py

    (changed preferences so that .py files open in Atom. Edited script in Atom)
5. mv raw_data data

6. cd data

    cd raw_data

    `pwd`: /Users/benjaminreverett/desktop/testing_directory/data/raw_data

    cd ../..
7. mv simple_script.py code

8. mv code/simple_script.py code/hello_world.py

9. rm -i do_not_readme.md
10.

```
Benjamin-R-Everett-Mac-Book-Air:testing_directory benjaminreverett$ tree
.
├── code
│   └── hello_world.py
├── data
│   └── raw_data
├── readme.md
└── test

4 directories, 2 files
Benjamin-R-Everett-Mac-Book-Air:testing_directory benjaminreverett$
```




________
