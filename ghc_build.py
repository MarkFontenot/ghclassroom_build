#!/home/mark/anaconda3/bin/python

# script to descend into each repo that has been cloned for a project
# and run cmake


# Imports

import os


# Params
baseFolder = '/home/mark/code/20S-3353/PA00 - Try It Out-02-04-2020-04-26-16'


if os.path.exists(baseFolder):
    print('Project path exists\n')
else:
    print('Can\'t open project path\n')


for filename in os.listdir(baseFolder):
    size = os.path.getsize(os.path.join(baseFolder, filename))
    print (filename)

