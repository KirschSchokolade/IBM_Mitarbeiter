import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pydotplus
import io


def ibm_tree_builder(splitsize, test_size):
    """Vorbereitugnen um mit der Datei zu arbeiten"""
    # Pfad zur CSV-Datei
    ibm_filepath = "WA_Fn-UseC_-HR-Employee-Attrition.csv"
    # Lese das File in die Variable ibm_data
    ibm_data = pd.read_csv(ibm_filepath)

    # splitten des Datensatzes 80% für training, 20% für test.
    train, test = train_test_split(ibm_data, test_size=test_size)
    print("Trainingsgröße: {}, Testgröße_ {}".format(len(train), len(test)))  # Ausgabe der Setgrößen

    # Definiert, wie fein der Baum gesplittet werden soll. => zu fein und man bekommt ein Overfitting.
    c = DecisionTreeClassifier(min_samples_split=splitsize)

    # Welche Variablen im Baum verwendet werden sollen.

    numerical_features = ["Age", "DistanceFromHome", "Education", "JobInvolvement", "JobSatisfaction",
                          "MonthlyIncome", "NumCompaniesWorked",
                          "TotalWorkingYears", "TrainingTimesLastYear", "WorkLifeBalance", "YearsAtCompany",
                          "YearsSinceLastPromotion", "YearsWithCurrManager"]

    # Festlegen der Trainingsdaten
    x_train = train[numerical_features]
    y_train = train["Attrition"]

    x_test = train[numerical_features]
    y_test = train["Attrition"]

    # Baum bauen
    ibm_data_decision_tree = c.fit(x_train, y_train)

    # Baum in Datei speichern
    outputfile = io.StringIO()
    export_graphviz(ibm_data_decision_tree, out_file=outputfile, feature_names=numerical_features)
    pydotplus.graph_from_dot_data(outputfile.getvalue()).write_png("./tree.png")

    prediction_of_accuracy = c.predict(x_test)
    # berechnen der Testgenauigkeit:
    score = accuracy_score(y_test, prediction_of_accuracy) * 100
    # Ausgabe der Genauigkeit auf eine Steller hinter dem Komma gerundet.
    print("Genauigkeit durch einen decision tree: ", round(score, 1), "%")


# Je kleiner der übergebene Wert, desto höher wird die Vorhersagegenauigkeit des Baums.
# Wenn der Wert zu klein gewählt wird, besteht die Gefahr des Overfittings.
ibm_tree_builder(200, 0.2)
