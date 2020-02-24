import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""Vorbereitungen, um der Datei zu arbeiten."""
# Pfad zur csv-Datei:
ibm_filepath = "WA_Fn-UseC_-HR-Employee-Attrition.csv"
# Lese das File in die Variable ibm_data
ibm_data = pd.read_csv(ibm_filepath)

print(ibm_data.describe())

# Das Alter hat einen Einfluss darauf, ob ein Angestellter/eine Angestellte kündigen wird
sns.swarmplot(x="Attrition", y='Age', hue="Gender", data=ibm_data)  # Den merken wir uns. alternativ mit EducationField

#Das Einkommen hat einen Einfluss darauf, ob Mitarbeiter kündigen im Hinblick auf Gender und Zufriedenheit
sns.catplot(y="MonthlyIncome", x="Attrition", hue="JobSatisfaction", data=ibm_data,
            kind="swarm")
sns.catplot(y="MonthlyIncome", x="Attrition", hue="Gender", data=ibm_data,
            kind="swarm")

# In wie vielen Firmen ein Angestellter vorher gearbeitet hat gibt Hinweise darauf, ob er/sie in diesem Unternehmen bleibt
sns.catplot(y="NumCompaniesWorked", x="Attrition",hue="Gender", data=ibm_data, kind="box")
sns.catplot(y="NumCompaniesWorked", x="Attrition", data=ibm_data, kind="box")

# Wie involviert ein Angestellter in den Beruf ist und seine Zufriedenheit mit dem Beruf  korrelieren
sns.lmplot(x="JobSatisfaction", y="JobInvolvement", hue="Attrition", data=ibm_data)

#An wie viele Fortbildungen ein Angestellter im letzten Jahr teilgenommen hat korreliert damit, wie viel Geld ein Angestellter verdient und damit, ob er kündigt

sns.lmplot(x="TrainingTimesLastYear", y="MonthlyIncome", data=ibm_data)

plt.show()
print("Fertig")
