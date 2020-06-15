import numpy as np
import pandas as pd


class organ(object):
    """This class includes all the necessary functions to calculate organized hossein module."""
    # def __init__(self,)

    def create_df(num_days):
        dti = pd.date_range(pd.Timestamp(pd.to_datetime('today').date()), periods=int(num_days*24*2), freq='0.5H')
        df = pd.DataFrame(index=dti)
        df['Date'] = df.index
        df.to_csv('df_initial' , index=False)
        df = pd.read_csv('df_initial')
        df['Date'] = list(map(pd.Timestamp , df['Date']))
        df.set_index('Date' , inplace=True)
        return df

    def update_task(df , kind, task,when, start, stop , scale):

        # kind = input('please specify whether your task is a Habbit or Project:')
        while kind != 'Habit' and kind != 'Project':
            print('{} is not an option.'.format(kind))
            kind = input('please specify whether your task is a Habbit or Project:')
        
        # task = input('please enter the Topic of your {}'.format(kind))
        if (kind+'s' , task) not in df.columns:
            df[(kind+'s',task)] = np.zeros(len(df))
            df.columns = pd.MultiIndex.from_tuples(df.columns)
        
        # start_of_task = input('When did you start '+task+'? (template: 01:30)') + ':00'
        # stop_of_task = input('When did you end '+task+'? (template: 01:30)') + ':00'
        start_of_task = start+ ':00'
        stop_of_task = stop + ':00'
        
        start_timestamp = pd.Timestamp(str(pd.Timestamp.today()+pd.Timedelta(str(when)+'D'))[:10]+' ' + start_of_task)
        stop_timestamp  = pd.Timestamp(str(pd.Timestamp.today()+pd.Timedelta(str(when)+'D'))[:10]+' ' + stop_of_task)
        
        df[(kind+'s',task)][start_timestamp:stop_timestamp - pd.Timedelta(hours=0.5)] = scale

        df['Date'] = df.index.astype('str')
        df.to_csv('timeline1' , index=False)
        df.drop('Date', axis=1,inplace=True)
        # df = pd.read_csv('df_init')
        # df['Date'] = list(map(pd.Timestamp , df['Date']))
        # df.set_index('Date' , inplace=True)
        # df.columns = pd.MultiIndex.from_tuples(df.columns)

        
        return df