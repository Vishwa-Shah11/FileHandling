import pandas as pd

column_name = 'Goals'
l = []

def get_goals(filename, country):
    """
    Get the count of players and their cumulative goals for this country

    Arguments:
        filename: string
        country: string
    Return: 
        result: tuple, (integer, integer)
    """
    goals = pd.read_csv(filename)
    #g = goals.groupby(country).groups
    goals = goals[goals['Country'] == country]
    g = goals.shape[0]
    sum = goals[column_name].sum()
    l.append(g)
    l.append(sum)
    tup = tuple(l)
    
    if (tup == (0,0)):
        tup = (-1,-1)
    
    return tup