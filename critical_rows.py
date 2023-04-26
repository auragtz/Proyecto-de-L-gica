import pandas as pd

# Initialize an empty DataFrame to store the concatenated results of premises and conclusion
final_premises = pd.DataFrame()

nVariable = int(input("How many variables? "))
nPremises = int(input("How many variables (2-3)? note: don't count conclusion as a premise "))

for i in range(nPremises):
    print(f"Editing premise {i+1}")
    # ciclo parte II
    # final_column = pd.DataFrame(df.iloc[:, -1]
    # final_premises = pd.concat([final_premises, final_column], axis=1)

print("Editing conclusion")
# ciclo II
# conclusion= pd.DataFrame(df.iloc[:, -1])
# final_premises = pd.concat([final_premises, conclusion], axis=1)

print(final_premises)
# evaluate critical rows ---------------------------------

critical_rows = final_premises[final_premises['conclusion'] == True]

# Print the critical rows
print(critical_rows)
print()

if False in critical_rows.values:
    print("invalid")
else:
    print("valid")

'''
# Este es un ejemplo de como funciona el codigo de arriba
#Se necesita correr solo :)

import pandas as pd
final_premises = pd.DataFrame() # initialize an empty DataFrame to store the concatenated results

data = {'P': [True, True, True, True, False, False, False, False],
        'Q': [True, True, False, False, True, True, False, False],
        'R': [True, False, True, False, True, False, True, False]}
df = pd.DataFrame(data)

VarConclusion = {'conclusion': [True, True, True, True, False, False, False, False]}
conclusion = pd.DataFrame(VarConclusion)

# operations
df['P AND Q'] = df['P'] & df['Q']
final_column = pd.DataFrame(df.iloc[:, -1])
final_premises = pd.concat([final_premises, final_column], axis=1)

df['(P AND Q) AND R'] = df['P AND Q'] & df['R']
final_column = pd.DataFrame(df.iloc[:, -1])
final_premises = pd.concat([final_premises, final_column], axis=1)

final_premises = pd.concat([final_premises, conclusion], axis=1)

print(df)
print()
print(final_premises)

critical_rows = final_premises[final_premises['conclusion'] == True]

# Print the critical rows
print(critical_rows)
print()

if False in critical_rows.values:
    print("invalid")
else:
    print("valid")

'''
