from sklearn.preprocessing import Imputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import custom_transformers

num_pipeline = Pipeline([
        ('imputer', Imputer(strategy = 'median')),
        ('attribs_adder', custom_transformers.CombinedAttributesAdder()),
        ('std_scaler', StandardScaler()),
    ])
