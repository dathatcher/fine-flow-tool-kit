import csv
import teamtopology as tt
import fineflowevaluation as fine
import flowratio as fr

BU_TeamFlow = {'Delivery Team 1':  ['Cloud Team', 'Compliance', 'Security'],
               'Delivery Team 2':  ['SRE','Compliance'],
               'Delivery Team 3':  ['Compliance'],
               'Cloud Team': ['Network', 'DBTeam','Security'],
               'Network':    ['WinTel DNS', 'Security'],
               'Security':   [],
               'DbTeam': ['Security'],
               'SRE':   [],
               'WinTel DNS':  [],
               'Compliance':  []
               }
ttopology = tt.findTopology(BU_TeamFlow)

print(ttopology.items())

BU_TeamFlowWithInteractions = {'Delivery Team 1':  [('Cloud Team','X'), ('Compliance','E'), ('Security','E')],
                               'Delivery Team 2':  [('SRE','X'), ('Compliance','E')],
                               'Delivery Team 3':  [('Compliance','E')],
                               'Cloud Team': [('Network','C'), ('DBTeam','E'),('Security','E')],
                               'Network':    [('WinTel DNS','E'), ('Security', 'E')],
                               'Security':   [],
                               'DbTeam': [('Security','E')],
                               'SRE':   [],
                               'WinTel DNS':  [],
                               'Compliance':  []
                               }

ttopology2 = fine.evaluate(BU_TeamFlowWithInteractions, flow=True,
                           imp=True, need=True, energy=True, resilience=True)

for key, value in ttopology2.items():
    print(f"Key: {key}")
    print(value)  # Assuming each record is a single value or a string representation
