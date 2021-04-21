## Condas virtual environments

**Creates a virtual environment envname for a given version (x.x) of python**
`> conda create -n envname python=x.x anaconda`

**Clone an existing environment**
`> conda create --clone cloned_env  --name name_of_clone`

**List the existing environments**
`> conda info --envs`

**Activates the environment envname**
`> conda activate envname`

**Launch Jupyter notebook within activated environment (assuming it's already installed)**
`(envname) > jupyter notebook`

**List the packages in the environment**
`> conda list`

**List revisions to the packages**
`> conda list --revisions`

**Revert to an earlier version xx of the environment**
`> conda install --revision xx`

**Deactivate the environment**
`> conda deactivate`

**Delete the environment**
`> conda env remove --name env_to_remove` 


## Bash virtual enviromments
(after installing using $ sudo -H pip install virtualenv)

**Creates a virtual environment envname in Python 3**
`$ python3 -m  virtualenv envname`

**activates the environment envname**
`$ source envname/bin/activate`

**Deactivate the environmnent**
`$ deactivate`

### Saving the requirements and later installing them

**Saving the requirements, the below generates a requirements file**
`$ pip freeze > requirements.txt` 

**install the requirements**
`$ pip install -r requirements.txt`


