import os
import pandas
import numpy as np

cols = ['walltime','advance','ghostfill','regrid','adapt',
            'adv_steps','adv_step2', 'mx', 'patch_comm', 'output', 'grids_proc',
            'memcopy_h2h','memcopy_h2d','memcopy_d2h']

    
dtypes = {'walltime': float,
          'advance': float,
          'ghostfill': float,
          'regrid': float,
          'adapt': float,
          'adv_steps': int,
          'adv_step2': int,
          'mx': int,
          'patch_comm': float,
          'output' : float,
          'grids_proc' : int,          
          'memcopy_h2h': float,
          'memcopy_h2d': float,
          'memcopy_d2h': float}    

def read_data(dir,device):
    fname = os.path.join('{:s}'.format(dir),'{:s}'.format(device),'results.out')
    df = pandas.read_table(fname,delim_whitespace=True)
    df.sort_values('p',inplace=True)

    f = '{:.2f}'.format
    fstr = {'p' : '{:3d}'.format,
            'walltime' : f,
            'advance' : f,
            'ghostfill' : f, 
            'patch_comm' : f,
            'regrid' : f, 
            'partition' : f,
            'adapt' : f,             
            'cfl' : f, 
            'grids_proc' : '{:4d}'.format, 
            'DOF/s' : '{:.1e}'.format,
            'Speedup': '{:.1f}'.format, 
            'Eff.' : '{:.1f}%'.format, 
            'output':'{:.1f}'.format,
            'memcopy_h2h' : '{:.2f}'.format, 
            'memcopy_d2h' : '{:.2f}'.format,
            'memcopy_h2d' : '{:.2f}'.format}

    return df,fstr
