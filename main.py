import pandas as pd

column_name = 'Goals'
l = []
def get_goals(filename, country):
 
    goals = pd.read_csv(filename)
    #g = goals.groupby(country).groups
    goals = goals[goals['Country'] == country]
    g = goals.shape[0]
    sum = goals[column_name].sum()
    print(sum)
    lst = l.append(g)
    lst = l.append(sum)
    
    tup = tuple(lst)
    
    return tup
    

goals = get_goals('getGoalsBasedOnCountry.csv', 'India')
print(goals)