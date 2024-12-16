import pandas as pd
import plotly.express as px


file_path = '00001.csv'
data = pd.read_csv(file_path)


print(data.head())

required_columns = ["Cycle", "Re", "Rct"]
if not all(col in data.columns for col in required_columns):
    raise ValueError("Required columns are missing from the dataset.")


data = data[required_columns].dropna()


fig_re = px.line(
    data, 
    x="Cycle", 
    y="Re", 
    title="Electrolyte Resistance (Re) vs. Charge/Discharge Cycles",
    labels={"Cycle": "Cycle Count", "Re": "Electrolyte Resistance (Ohms)"},
    template="plotly_dark"
)


fig_rct = px.line(
    data, 
    x="Cycle", 
    y="Rct", 
    title="Charge Transfer Resistance (Rct) vs. Charge/Discharge Cycles",
    labels={"Cycle": "Cycle Count", "Rct": "Charge Transfer Resistance (Ohms)"},
    template="plotly_dark"
)


fig_re.show()
fig_rct.show()
