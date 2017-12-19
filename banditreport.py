#! /usr/bin/env python2

import os
import sys
import numpy as np
from pprint import pprint

# Function to randomize and report new numbers.
def jumble_slightly(array):
    noise = np.random.normal(1, 0.07, len(array))

    effort = np.ceil(noise * array)

    return effort

# Function to find out which file to open
def grab_excel_path(db_abs_path):
    files = os.path.listdir(db_abs_path)
    files_sorted = files.sort(key = lambda x: os.stat(os.path.join(db_abs_path, x)).st_mtime)
    f = files_sorted[0] # Take the last modified assignments file

    return f

# Function to pull from DropBox
def read_expected_effort(db_abs_path, yourname):
    try:
        assert os.path.exists(db_abs_path)
    except:
        print "ERROR: The Dropbox path you gave doesn't exist on your local machine..."

    excel_path = grab_excel_path(db_abs_path)

    exp_effort = pd.read_excel(excel_path, sheet_name=2)

    your_exp_effort = exp_effort[exp_effort['Unnamed: 0'] == yourname, :].dropna(axis=1, how='all')

    return your_exp_effort

# Function to push to google sheets

def main(db_abs_path, yourname):

    # Grab your expected effort
    your_exp_effort = read_expected_effort(db_abs_path)

    # Calculate your new effort values, which are totally valid
    new_effort = jumble_slightly(effort_array)

    # Put into dataframe
    new_effort_df = your_exp_effort.copy()
    new_effort_df.idx[1,:] = new_effort

    print "Here's how hard you worked last week. Good job!"
    pprint(new_effort_df)

if __name__=='__main__':
    main(sys.argv[1], sys.argv[2])
