# INTERNAL
import os
# EXTERNAL
import pandas as pd
# LOCAL

#--------------------------------------------------------------------------------

class ProcessData:

    def __init__(self,path):
        self.path = path
        # Check if path url exists
        # Read the data
        self.df = pd.read_csv(path)
        self.columns = self.df.columns
        self.shape = self.df.shape
    
    def _generate_report(self):
        pass

    def _imputation(self):
        # Impute missing values
        pass
    

