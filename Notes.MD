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

	**duck-typing**
	
		readability MATTERS

		classes and objects should do what they say they do

Class definitions:

	use 'class' keyword

	capitalize name of chear class (i.e. use CamelCase)

	use 'self' to refer to an instance's own, unique data
	
	'self-reference'

		'self.method()' to call methods on same object
		
		'self.attribute' to access instance-specific data

	start each emember function's argument list with 'self'

		def my_function(self,.....)

	inheritance
		
		class Joker(Card)
	
		can call all of parent's method

		child can overwrite methods if want

		check if object belongs to a specificed class 'isinstance()'

	__init__()

		super().__init__() to call base class's __init__() method
	
		**always call super class when inheriting**

		class Joker(Card):

[magic methods help](http://www.python-course.eu/python3_magic_methods.php)

**common magic methods**


	* __init__ 	constructor

	* __str__	 	defin behaor for str(obj)
	
	* __repr__ 	define behavior for repr(obj)
	
	* __len__ 	return number of elementds in object

	* __call__ 	call instance like a function

	* __iter__ 	returns an iterable

 
assert to test preconditions



		

##Tips
	start ipython like this for matplotlib: **ipython --pylab**

##To Review at night

[@property](https://www.blog.pythonlibrary.org/2014/01/20/python-201-properties/)

update slides

[_ and __](https://dbader.org/blog/meaning-of-underscores-in-python)


## 01.03 - SQL

**Relational Database Management Systems (RDBMS)**
	
	store data in multiple related tables

	Entity Relationship Diagram (ERD)
		
		Show table informatio visually
		
	De facto standard for storing data for a long time
	
		e.g. Oracle, MySQL, SQL Server, Postgres
		
	Terminology:
		
		**Schema** defines strucure of tables and databases
		
**SQL**

	Data Scientist - most important is to extract information
	
	101: SELECT and FROM e.g. SELECT * FROM
	
	SQL is declarative language unlike Python which is imperative. Meaning, SQL we tell it what we want NOT 'how'.
	
	whitespace and capitalization don't matter though convention is ALL CAPS for keywords
	
	Best to break up lines eg:
	
			SELECT
			
				column1,
				
				column2
			
			FROM
			
				my_table;
				
### Advanced SQL

**ALIAS**
	NOT in WHERE or HAVING
	
	Does work in GROUP BY

**SELECT DISTINCT**

	Can do more than one SELECT DISTINCT, but will do distinct combos of all items in select
	
**Multiple JOIN**

	SELECT ...
	
	FROM purchases AS p
	LEFT OUTER JOIN customers AS c ON p.cust_id = c.cust_id
	LEFT......
	
**datetime**
		tmstmp
	2017-07-19 12:00:00
	
	DATE(tmstmp) returns date
	MIN(tmstmp)	returns minute
				
	
## 01.04 - Jupyter and Pandas

psycopg2 - used to interface

[10 minutes to pandas](http://pandas.pydata.org/pandas-docs/stable/10min.html)



**5 steps to general workflow in psycopg2**

	1. Open connection
	
	2. Create a cursor object
	
	3. Use the cursor to execute SQL queries
	
	4. Commit SQL actions
	
	5. Close the cursor and connection

**Example**

	import psycopg2
	
	conn = psycopg2.connect(dbname='election_data', user'ewellinger', host='localthost'
	
		host can be used to connect to remote datatbases
	
	cur = conn.cursor()
	
		**cursor** is the control structure that enables traversal over the records
			
			executes queries to fetch data
			
			handles transactions with SQL database
			
			returned as generator
			
	query = '''SELECT headline
					FROM articles
					WHERE ....	;'''
	
	cur.execute(query)
	
	ways to fetch:
		
		cur.fetchone() - returns the next result
		
		cur.next()
		
		cur.fetchmany(n)
		
		cur.fetchall()
		
		for res in cur - iterates over results
		
	*if given root access* create new_user that only has read only access
	
	make mistake on query do **conn.rollback()**
	
	Then close it up!
	
		cur.close()
		
		conn.close()

**CAREER SERVICES**

	Q1 - Personal Branding
	
	Q2 - Networking
	
	Q3 - Job Search Strategy
	
	Q4 - Interviews
	
	Q5 - Post Grad
	
	Avoid 'student' typecast
	
	At platte park 11-2pm on Thursdays
	
	Capstones sponsored by company are most successful capstones
	
**Slack**
	
		Used for internal communication. Now industry standard.
		
		Join local organizations and can network within local channels
		
		Joine #colorado-events in slack

**Tips**

	info on any dataset in python - print dir
		
	
## 01.05 - Plotting:

#### Week 1 Review Questions

1. Compare and contrast functional and object oriented programming paradigms.  Then discuss the the 3 pillars of OOP and how they relate to Python.

	''in a fight between a bear and an alligator, terrain determines the outcome''
	
	
	
	**P_I_E**
		
		Polymorphism - many shapes
		
		Inheritance - Vehicle -> car, bike, truck
		
		Encapsulation - Class, method ...Abstraction -> away the details that we don't need to see
	

	**OOP**
		
		Data to be acted upon
		
		Central activity is composing and extending objects to new nethods
	
	
	**Functional**
		
		Data loosley coupled to write new functios

2. What are some distinguishing characteristics of the Python programming
language?

		OOP
		
		Interpretive vs compiled
		
		Data Structures - tuples in lists, lists in dictionaries
		
		Huge library of modules
		
		Open source
		
		Loosely typed 
		
		Flexibility
		
		Indentation increases readability - '''code is read more than it is written'''

3. What are some differences between Python 2 and Python 3?  Why was Python 3
developed?

		range - list python 2, generator python 3 (xrange creates list)

4. List major data structures in Python.  Which data structure(s) would you use to
in each of the following situations, and why:

  * Unchanging sales records
  		
  		* Tuple 	

  * A customer database where changing information, such as address, email,
  and purchases are associated with a given customer name.
  
  		* Dictionary

  * Driving waypoint locations between arbitrary points A and B.
  		
  		* List of tuples  	

  * The unique words used in a text corpus.
  		
  		* Sets - key is unique 	

  * A search engine that returns results quickly for a given search term.
  
  		* Dictionary 



5. Write a one line list comprehension to perform the following matrix
multiplication (A dot product B).  Describe how it works. How would you check
it with NumPy?

[[math for j in range(len(B[0]))] for i in range(len(A))]

```python
    A = [ [ 2, 4], [ 1, 7], [-1, 8] ]

    B = [ [3, 2, -5, 6],  [1, -3, 4, 8] ]
```

6. Use datatable 'customers' below, write a SQL query to....

| cust_id | cust_name | current_city | hometown |
|:----------:|:------------:|:----------:|:-----------:|
| 1 | Amanda | Atlanta | Raleigh |
| 2 | Brittany | Denver | New York |
| 3 | Charles | Paris | Raleigh |
| 4 | David | San Diego | Los Angeles |
| 5 | Elizabeth | Atlanta | London |
| 6 | Greg | Denver | Atlanta |
| 7 | Maria | Raleigh | New York |
| 8 | Sarah | New York | Raleigh |
| 9 | Thomas | Atlanta | Raleigh |

  A) return all pairs of customers that live in the same city.
  
  	SELECT a.current_city,
  		string_agg(DISTINCT b.cust_name, ',') as cust_Pair
  	FROM customers AS a, customers AS b
  	WHERE a.currenty_city = b.current_city
  	GROUP BY a.current_city
  	HAVING STRING_AGG(distinct B.cust_name, ',') LIKE '%,%';
  	
  	SELECT
  		t1
  		
  	
  	
  	 	
  B) return the pair of cities that customers move between most often (in either direction).
  
### Plotting

As Data Scientist need to be able to communicate data and relationships.

'''x = 45'''

**Figure class, axes class, then some classes inside of Axes**

	'''
	
	import matplotlib.pyplot as plt	
	plt.figure(figsize=(8,6))	
	ax = plt.add_subplot(1,1,1)	
	...	
	ax.set_title(’foo’)	
	ax.set_ylabel(’y’)	
	ax.set_xlabel(’x’)	
	plt.savefig(’foo.png’,dpi=400)
	
	in Jupyter notebe %matplotlib inline
	
	'''
	
**super helpful**
	
	get documentation 'pydoc numpy.array'
	
	matplotlib.org - plotting commands summary
	
	matplotlib.org - gallery of loads and loads of plots
	
	seaborn.pydata.org - gallery...."........"........
	
ax1 = fig.add_subplot(221) - rows, columns, handle
ax1 = fig.add_subplot(2,2,1) - same

axes objects ('ax') are object we are playing with and moving around

#WEEK 2: PROBABILITY AND STATISTICS



## 02.01 - PROBABILITY

**Links**
[Probability Cheat Sheet](http://pytolearn.csd.auth.gr/d1-hyptest/11/distros.html)

[Probability visualized!](http://students.brown.edu/seeing-theory/index.html)

[scipy intro](https://oneau.wordpress.com/2011/02/28/simple-statistics-with-scipy/)

[probability theory intro](https://github.com/benjamineverett/immersive_notes/blob/master/docs/02_01_reading_review_prob_theory.pdf)

[use mathmatical formulas in markdown](http://csrgxtu.github.io/2015/03/20/Writing-Mathematic-Fomulars-in-Markdown/)

[stats short course](https://galvanizeopensource.github.io/stats-shortcourse/)

[Different probablity distributions examples](https://www.utdallas.edu/~scniu/OPRE-6301/documents/Important_Probability_Distributions.pdf)

[Solutions for the day](

[slides](

[pdf, cdf, ppf](http://pytolearn.csd.auth.gr/d1-hyptest/11/distros.html)

X ∼ Bernoulli(p) (where 0 ≤ p ≤ 1): one if a coin with heads probability p comes up heads, zero otherwise.
	
\\[p(x) = p\\] 
	
	if p = 1
	
\\[1 − p\\] 

	if p = 0

X ∼ Binomial(n, p) (where 0 ≤ p ≤ 1): the number of heads in n independent flips of a coin with heads probability p.
	
\\[p(x) = \binom{n}{x}\\]
	
\\[\binom{p}{x}(1-p)(n-x)\\]

X ∼ Geometric(p) (where p > 0): the number of flips of a coin with heads probability p until the first heads.

\\[p(x) = p(1 − p)x−1\\]

X ∼ P oisson(λ) (where λ > 0): a probability distribution over the nonnegative integers used for modeling the frequency of rare events.
p(x) = e
−λ λ
x
x!

\\[P(B|A) = \frac{P(A,B)}{P(A)} = \frac{P(A|B)P(B)}{P(A)}\\]
\\[P(B) = P(B|A)P(B) + P(B^\mathsf{c}|A)P(B^\mathsf{c})\\]



**To KNOW:**

	Is distribution discrete or continuous?
	
	What is an example of how I'd use the distribution

**Questions to Ask:**

	Are my data discrete or continuous?
	
	Are my data symmetric?
	
	What limits are there on possible values for my data?
	
	How likely are extreme values in my data?
	
	Would my data reasonably look like a random sample from this distribution?


##02.02 - Sampling & Estimation

**Slides**
[Distribution and Parmeter Estimation](https://github.com/benjamineverett/immersive_notes/blob/master/docs/02_02_Distribution_and_Parameter_Estimation.pdf)
[Sampling - Afternoon](https://github.com/benjamineverett/immersive_notes/blob/master/docs/02_02_Sampling.pdf)

[**Jupyter Notebooks**](https://github.com/benjamineverett/immersive_notes/tree/master/JupyterNotebooks/02_02_Sampling_Estimation)

[**Solutions**](https://github.com/gSchool/dsi-solns-g49/tree/master/estimation-sampling)

**Readings**
	
[intro to bootstrap](https://www.youtube.com/watch?v=_nhgHjdLE-I)
	
[Central Limit Theorem (CLT) explained](https://www.khanacademy.org/math/statistics-probability/sampling-distributions-library/sample-means/v/central-limit-theorem)
	
[Maximum Liklihood estimator (MLE) explained](https://www.youtube.com/watch?v=I_dhPETvll8)

**Bootstrap Mean**

	1. Take random samples from a population
	2. Take random samples from those random samples
	3. Take random samples many times over...say 1000
	4. Use this to mean, variance, etc


**Central Limit Theorem**

	Sum of out comes of sample size n taken x amount of times.
	
	n = 4
	x = 100
	
	I'm taking 4 samples from my data, and I'm doing it 100 times.
	


**Estimation Intro**

	Want to use sample of population because we cannot sample entire population
	
	Model will have inaccuracies.
	
	We'd like to be as accurate as possible (of course!)
	


**Method of Moments**

Assume a distribution(Poisson, Bernoulli Binomial, Gaussian)
	
Compute the relevant [moments](https://en.wikipedia.org/wiki/Moment_(mathematics)) from the data (mean and variance)

Use moments to plot

See this [jupyter notebook](



**Maximum Likelihood Estimation**

Likelikhood of what? The sample data, given the distribution parameter(s)

\\[If P(X|\theta_{1}) > P(X|\theta_{2})\\]

Then evidence supports theta 1 over theta 2



**Maximum a Posteriori (MAP)**

Use Baye's theorem



**Kernel Density Estimation (KDE)**

What if our data does not match a known distribution




**Bootstrapping**

Take a sample that is representative of the population

Random sampling is often not as random as we'd like.

Bootstrap Sampling Method:

	1. Start with your dataset of size n
	2. Sample from your dataset with replacement to create 1 bootstrap sample of size n
3. Repeat B times. Each bootstrap sample can then be used as a separate dataset for estimation and model fitting


##_02.03 - Hypothesis Testing_

**Links**
(PDF, CDF, PPF, SF)[http://pytolearn.csd.auth.gr/d1-hyptest/11/distros.html]

(Seeing Theory)[http://students.brown.edu/seeing-theory/index.html]

[Latex Formating Symobols - Cheat Sheet](

[Repo](https://github.com/benjamineverett/dsi-ab-testing)

[Z vs. T Statistic](https://www.youtube.com/watch?v=5ABpqVSx33I)

[Hypothesis Testing](https://www.youtube.com/watch?v=-FtlH4svqx4)

**Z-Statistic V t-statistic**


\\[z-statistic=\frac{\overline{x} - \mu_\overline{x}}{\sigma_\overline{x}}\\]

\\[\sigma_\overline{x}=\frac{\sigma}{\sqrt{n}}\\]

use z-stat when n > 30

use t-stat when n < 30

**Hypothesis Testing Steps**



1. Set up null hypothesis - \\[H_0:\\]

2. Set up alternative hypothesis - \\[H_1:\\]

3. Assume null is true. Then we can say, if probability we got results we did is very very small we can reject null hypothesis


Ex. Testing drug response time on 100 rats. Mean response for non-injected rats is 1.2 seconds. Mean of 100 rats injected is 1.05 seconds with sample standard deviation of 0.5 seconds. Is drug affecting response time?

Large sample size, so can assume sample standard deviation:
\\[\sigma_\overline{x}=\frac{0.5}{\sqrt{100}}\\]
\\[\sigma_\overline{x}=0.05\\]
\\[z =\frac{1.2 - 1.05}{0.05}\\]
\\[z=3\\]

\\[z-stat = .9987 \therefore reject..H_0!\\]

**scipy distributions**

	dist = stats.poisson(lambda)
		dist.pdf
		dist.rvs
			.
			.
			.
			.

\\[Z=\frac{\overline{X}-\mu}{\frac{\sigma}{\sqrt{n}}}\\]

**Estimation vs Hypothesis Testing**

We don't say null is true, we state whether we can reject the null

1. State the null(H0) and the alternative (H1) hypothese
2. Choose level of significance (alpha)
3. Choose a statistical test and find the test statistic
4. Draw conclusions
	1. Reject H0 in favor of H1
	2. Fail to reject H0 

**One tailed vs two tailed**

Type 1 - False positive - reject null and it is actually true
Type 2 - Failing to rejet H0 when it is false


Proportions - Comparing proportions is a 1 vs. 0 test
Means - anywhere on a distribution

**t-tests (use Welchs T-test for 2 samples!)**

using scipy returns tuple (t-stat, p-value)

**Example**

H0 - men_heights <= women_heights
H1 - men > women

Bonferroni Correction = # of comparisons is n choose k


##02.04 - Power Analysis and Bayesian Stats

Type I error - False Positive - Alpha Error - Reject H0 when H0 is true - Specificity
	
Type II error - False Negative - Beta Error - Do not reject H0 when H0 is false - Sensitivity

**Power:**

\\[Power = 1 - \beta\\]

Power levels of 80-90% considered effective

|  |  Test  |  Test    |
|-------|:------:|--------:|
| Test  |   D+          |     D-  |
|   T+  | CORRECT   | **Type II** |
| T-	  | **Type I** | CORRECT|


![Helpful Graph](https://github.com/benjamineverett/immersive_notes/blob/master/Screen%20Shot%202017-07-27%20at%208.11.54%20AM.png)
 
 **Think Curve:**
 
 to right of threshhold (alpha) is True positive and False Positive
 
 to left is True negative False negative
 
 As move to right of alpha:
 
 decreased sensitivity
 increased specificity

**Bayes Rule in Statistics**

\\[P(\theta|data) = \frac{P(data|\theta) * P(\theta)}{P(data)}\\]


**Main objective**

Define Power
Factors that influence Power
Intro to R

\\[1-\beta = \phi[Z_\frac{a}{2} + \frac{\mu_1 - \mu_0}{\sigma}\sqrt{n}]\\]

W/I baysian stats use Monte Carlo method often


##02.05 - Multi Armed Bandit

A prior with a beta creates a posterior with a beta

\\[P(y|\theta) \infity p(\theta|y)[(\theta)\\]


Goal of multi armed bandit is to maximize rewards or alternatively minimize regret

UCB1 - choose whichever bandit has the largest value

softmax = choose the bandit randomly in properotion to its estimated value




###**Tips/Tricks:**
	
**format string for floating points**
	
	1. {:,2f}.format(my_int)
	
	2. {:20,2f}.format(my_int) <- adds white space ahead of int so that two numbers can line up
		E.g.
			      123,456,000.98 <- with #2
			345,453,2123,9894.98

File under “stupid Python tricks”: You can use a semicolon to combine statements in series [on a single line.](https://docs.python.org/3/reference/compound_stmts.html)





**SATURDAY**

	Review probability distributions and how to identify which distribution to use
	
	Review different ways to use z-score and t-statistic
	
	Review functional programming in R
	
	Update Talent
	
	check blog on switching industries
	
	
	
	





	



