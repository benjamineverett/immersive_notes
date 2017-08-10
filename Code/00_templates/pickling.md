## Pickling Objects

Let's say we have a model like the following:

```python
class MyModel(object):
    def fit(self):
        pass

    def predict(self):
        return random.choice([True, False])


def get_data(datafile):
    ....
    return X, y
```

We don't necessarily want to retrain this model every time we want to predict because this could take a long time.  Instead, we can pickle our model after training like so:

```python
import random
import cPickle as pickle


# Let's look at training a model and then saving the resulting model
X, y = get_data('data/train.json')
model = MyModel()
model.fit(X, y)
with open('model.pkl', 'w') as f:
    pickle.dump(model, f)
```

Now we can easily load in this pickled model and use it to predict without having to retrain!  (**NOTE**: You can run into issues if packages are updated since the model was pickled.  e.g. you train your model using a particular version of `sklearn` and then later update it and try and read in the pickled model)

```python
# Now we can read this model in without having to retrain!
with open('model.pkl') as f:
    model = pickle.load(f)

model.predict(...)
```


## Pickling DataFrames

When working in `pandas` it is extremely easy to pickle our DataFrame to use later on.  But why would we do this when we could easily just save our DataFrame as a CSV and load that in later?  

The issue is that we may need to do processing every time we read this CSV in such as parsing datetimes into the pandas datetime object.  Since we are pickling the DataFrame, we no longer have to worry about recomputing that date parsing.

```python
import pandas as pd
import numpy as np

def clean_df(df):
    pass

# Read in our DataFrame
df = pd.read_csv('my_awesome_csv.csv')

# Do your data cleaning which is potentially very time intensive
clean_df(df)

# Pickle the resulting DataFrame
df.to_pickle('my_dataframe.pkl')
```

We can now read in this pickled DataFrame like so:

```python
df = pd.read_pickle('my_dataframe.pkl')
```


## Saving compressed NumPy Arrays

We can also do this when we have many `NumPy` Arrays that we need to save for accessing later.

```python
# We can save numpy vectors to a compressed dictionary
a = np.arange(1000)
b = np.arange(1000)
file_name = 'numpy_dict.rpz'
args = {'a': a, 'b': b}
np.savez_compressed(file_name, **args)
```

Now when we would like to access these arrays, we simply use `np.load` to load in the compressed file and access the resulting object like a dictionary:

```python
# And read them in
npz = np.load(file_name)
a = npz['a']
```
