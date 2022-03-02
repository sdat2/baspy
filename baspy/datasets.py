


### Set default dataset
__default_dataset = 'cmip5'



'''
Define information for each dataset to be indexed and used

    Standard elements (case sensitive):
        * 'Centre', 'Model', Var, Frequency, Experiment, CMOR, 
                Version (i.e., data version), RunID, StartDate-EndDate

    Notes:
    ../Version!latest/... means only use the 'latest' directory as the 
        Version (and ignore sister directories) during the 
        filewalk (i.e, default is to use the '*' wildcard)


'''

dataset_dictionaries = \
    { 

    'happi': 
    {'Root':'/gws/nopw/j04/bas_climate/data/happi',
    'DirStructure':'Raw_Derived/Centre/Model/Experiment/CMOR/Version/Frequency/SubModel/Var/RunID',
    'FilenameStructure':'Var_CMOR_Model_Experiment_ExperimentXXX_Version_RunID_StartDate-EndDate',
    'InclExtensions':['.nc', '.nc4'],
    'Cached':{'Experiment':['All-Hist','Plus15-Future','Plus20-Future']}},


    'cmip5': 
    {'Root':'/badc/cmip5/data/cmip5/output1',
    'DirStructure':'Centre/Model/Experiment/Frequency/SubModel/CMOR/RunID/Version!latest/Var',
    'FilenameStructure':'Var_CMOR_Model_Experiment_RunID_StartDate-EndDate',
    'dtypes': {"Experiment":"category", "Var":"category", "Model":"category", "CMOR":"category", 
                                "RunID":"category", "Centre":"category", "Frequency":"category", 
                                "SubModel":"category", "Version":"category", "StartDate":"int32", "EndDate":"int32"},
    'InclExtensions':['.nc', '.nc4'],
    'Cached': {'Experiment':['piControl','historical','rcp26','rcp45','rcp85'], 
                'Frequency':['mon']}},
    

    'cmip6': 
    {'Root':'/badc/cmip6/data/CMIP6',
    'DirStructure':'MIP/Centre/Model/Experiment/RunID/CMOR/Var/Grid/Version!latest',
    'FilenameStructure':'Var_CMOR_Model_Experiment_RunID_Grid_StartDate-EndDate',
    'dtypes': {"Experiment":"category", "Var":"category", "Model":"category", "CMOR":"category", 
                            "RunID":"category", "Centre":"category", "Grid":"category", 
                            "Version":"category", "StartDate":"int32", "EndDate":"int32"},
    'InclExtensions':['.nc', '.nc4'],
    'Cached': {}},
    

    'cmip5_all_versions': 
    {'Root':'/badc/cmip5/data/cmip5/output1',
    'DirStructure':'Centre/Model/Experiment/Frequency/SubModel/CMOR/RunID/Version/Var',
    'FilenameStructure':'Var_CMOR_Model_Experiment_RunID_StartDate-EndDate',
    'dtypes': {"Experiment":"category", "Var":"category", "Model":"category", "CMOR":"category", 
                                "RunID":"category", "Centre":"category", "Frequency":"category", 
                                "SubModel":"category", "Version":"category", "StartDate":"int32", "EndDate":"int32"},
    'InclExtensions':['.nc', '.nc4'],
    'Cached': {'Experiment':['piControl','historical','rcp26','rcp45','rcp85'], 
                'Frequency':['mon']}},

    }
