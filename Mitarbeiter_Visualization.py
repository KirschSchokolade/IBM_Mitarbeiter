import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""Vorbereitungen, um der Datei zu arbeiten."""
# Pfad zur csv-Datei:
ibm_filepath = "WA_Fn-UseC_-HR-Employee-Attrition.csv"
# Lese das File in die Variable ibm_data
ibm_data = pd.read_csv(ibm_filepath)

print(ibm_data.describe())

# Das Alter hat einen Einfluss darauf, ob ein Angestellter/eine Angestellte kündigen
sns.swarmplot(x="Attrition", y='Age', hue="Gender", data=ibm_data)  # Den merken wir uns. alternativ mit EducationField

# Das Einkommen hat einen Einfluss darauf, ob ein Angestellter/eine Angestellte kündigen
sns.catplot(y="MonthlyIncome", x="Attrition", hue="JobSatisfaction", data=ibm_data,
            kind="swarm")
sns.catplot(y="MonthlyIncome", x="Attrition", hue="Gender", data=ibm_data,
            kind="swarm")

# In wie vielen Firmen ein Angestellter/eine Angestellte vorher gearbeitet hat gibt Hinweise, ob sie in diesem Unternehmen bleibt.
sns.catplot(y="NumCompaniesWorked", x="Attrition",hue="Gender", data=ibm_data, kind="box")
sns.catplot(y="NumCompaniesWorked", x="Attrition", data=ibm_data, kind="box")

# Wie involviert ein Angestellter/eine Angestellte in den Beruf ist und wie zufrieden ein Angestellter/eine
# Angestellte mit diesem ist korrelieren.
sns.lmplot(x="JobSatisfaction", y="JobInvolvement", hue="Attrition", data=ibm_data)

# Wie viele Fortbildungen ein Angestellter/eine Angestellte in letzten Jahr gemacht hat korreliert damit,
# wie viel Geld ein Angestellter/eine Angestellte in seinem/ihrem Beruf verdient und darum damit, ob er/sie kündigt.
sns.lmplot(x="TrainingTimesLastYear", y="MonthlyIncome", data=ibm_data)

plt.show()
print("Fertig")
