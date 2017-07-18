# Precourse Resources:

[SQL guide](https://github.com/benjamineverett/precourse/blob/master/Chapter_3_SQL/resources/create_sql_table.md)

	* create table
	* insert values

[linear algrebra simple review](https://github.com/benjamineverett/precourse/tree/master/Chapter_2_Linear_Algebra)

[terminal cheat sheet](https://github.com/benjamineverett/immersive_notes/blob/master/docs/terminal_cheat_sheet.txt)

[psql terminal commands](https://github.com/benjamineverett/immersive_notes/blob/master/docs/psql_commands.png)

[markdown cheat sheet](https://github.com/benjamineverett/immersive_notes/blob/master/docs/markdown_cheatsheet.pdf)

[ipython cheat sheet](https://github.com/benjamineverett/immersive_notes/blob/master/docs/iPythonCheatSheet.svg)

[numpy cheat sheet](https://github.com/benjamineverett/immersive_notes/blob/master/docs/Numpy_Python_Cheat_Sheet.pdf)



	

# Week 1: 
## 01.01

[Git How-To](https://github.com/benjamineverett/immersive_notes/blob/master/docs/lecture_01_01_python_intro.pdf)

[intro to python](https://github.com/benjamineverett/immersive_notes/blob/master/docs/lecture_01_01_python_intro.pdf)
	
	* anaconda
		* conda create
		* source activate
	* data types
	* data structures
	
[style guide](http://legacy.python.org/dev/peps/pep-0008/), [python code style](http://python-guide-pt-br.readthedocs.io/en/latest/writing/style/)

	* style guide
	* interesting notes on 'pythonic' way of coding

[timeit examples](https://github.com/benjamineverett/immersive_notes/blob/master/docs/01_01_timeit_examples.ipynb)

[data structures](https://github.com/benjamineverett/immersive_notes/blob/master/docs/01_01_data_structures.ipynb)

	* list comprehension
	* filtering list comprehension
	* lamba
	* map
	* zip
	* examples on lists, tuples, and sets

[python fundamentals](https://github.com/benjamineverett/precourse/blob/master/Chapter_1_Python_Syntax/resources/python.md)

	* generators
	* looping tools
	* list comprehensions
	* lambda functions
	* sets and dictionaries
	* mutable vs immutable
	* permutations and combinations
	* file I/O
	* exception handling
	* counter and defaultdict (default dict)

	
### General Notes:

imperative vs. declarative:
	
	imperative says how we are going for the result. Declarative seeks solutions (e.g. R)

interpreted instead of compiled:

	has reapid REPL(Read-Evaluate-Print-Loop)

Python is a general purpose programming language. R came out of a statistics background.

Uses for:

	tuple - for values that are not going to change use a tuple

	list - if value needs to be updated, changed, etc, use a list

	dictionary - if need quick recall use a dictionary

### Tips:

reveal hidden files in terminal: -a

## 01.02 - **Object Oriented Programming**

Classes - **a container of functions related to an idea**

	creates separation of concerns
	
	allows to test small snippet of code and move on
	
	Very important reasons to use:
	
		converse intelligently with software engineers
	
		use libaries which have OO design
	
		make own code more usable

Thinking OO

	class is a user-defined type i.e. an entity with data and actions
		
		on par with float, str, etc
		

	methods (in Python, also technically a class 'attribute')
		
		operations you can perfrom on an instance of the class e.g. sum(object)

	E.g.
		Class = bikes
			
			object = mountain bike
			
			object = road bike
			
			object = tricycle
		
		Class = car
		
			object = sports car
		
			object = sedan

		However, could do
		
		Class = things with wheels
		
			object = car
		
			object = bike

	Hallmarks

		encapsulation - requires code to namipualte an object's internal state, indrectly, only through method calls

		Really Good Idea to pgroam this way regardless of language:

			write a class to manage a resource

			bundle the resource as part of the class state

			only access the resource via well-defined

		Python does not enforce encapsulation
			
			begin with underscore to indicate not to mess - _do_not_touch_me

	**Polymorphism** - treat multiple objects the same if they support same interface
		
		'lap water'

			can do on cat or dog

		
		

	
	



