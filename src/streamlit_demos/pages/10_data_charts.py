"""Data & charts: show tables, edit them, and draw charts.

Demonstrates: st.dataframe, st.data_editor, st.table, st.bar_chart,
st.line_chart, st.area_chart, st.scatter_chart, st.map, and CSV upload with
st.file_uploader + pandas.

The sample data is data/sales.csv (generated, fictional).
"""

import numpy as np
import pandas as pd
import streamlit as st

from utils import load_sales

st.title("📊 Data & charts")

sales = load_sales()  # cached helper from utils.py

# ---------- 1. Showing tables ----------
st.header("1. Tables")

# TRY THIS: click a column header to sort; hover a table to search/download it.
st.subheader("st.dataframe (interactive)")
st.dataframe(sales, height=250, hide_index=True)

st.subheader("st.table (static)")
st.table(sales.head(5))
st.caption("Idea: dataframe = scrollable and sortable; table = a fixed picture.")

# ---------- 2. Editable table ----------
st.header("2. Editable table")

# TRY THIS: double-click a cell to edit it, or add a row at the bottom.
editable = sales.head(5)[["region", "product", "units"]]
edited = st.data_editor(editable, num_rows="dynamic", key="data_editor", hide_index=True)
st.write("Total units after your edits:", int(edited["units"].sum()))
st.caption("Idea: data_editor RETURNS the edited DataFrame so you can use it.")

# ---------- 3. Charts ----------
st.header("3. Charts")

# TRY THIS: pick other regions to filter every chart below.
regions = st.multiselect(
    "Regions", sorted(sales["region"].unique()), default=["North", "South"], key="chart_regions"
)
filtered = sales[sales["region"].isin(regions)]

by_product = filtered.groupby("product")["revenue"].sum()
by_month = filtered.set_index("date").resample("MS")["revenue"].sum()

tab_bar, tab_line, tab_area, tab_scatter = st.tabs(["Bar", "Line", "Area", "Scatter"])
with tab_bar:
    st.bar_chart(by_product)
with tab_line:
    st.line_chart(by_month)
with tab_area:
    st.area_chart(by_month)
with tab_scatter:
    st.scatter_chart(filtered, x="units", y="revenue", color="product")
st.caption("Idea: pass a DataFrame or Series and Streamlit picks sensible axes.")

# ---------- 4. Map ----------
st.header("4. Map")

# st.map needs 'lat' and 'lon' columns. We scatter random points around Paris.
rng = np.random.default_rng(0)
points = pd.DataFrame(
    {"lat": 48.85 + rng.normal(0, 0.02, 40), "lon": 2.35 + rng.normal(0, 0.02, 40)}
)
# TRY THIS: drag and zoom the map.
st.map(points)
st.caption("Idea: any DataFrame with lat/lon columns becomes a map.")

# ---------- 5. CSV upload ----------
st.header("5. Upload your own CSV")

# TRY THIS: upload data/sales.csv (or any CSV) to see it parsed with pandas.
csv_file = st.file_uploader("Choose a CSV file", type="csv", key="data_csv")
if csv_file is not None:
    uploaded = pd.read_csv(csv_file)
    st.write(f"{len(uploaded)} rows, {len(uploaded.columns)} columns")
    st.dataframe(uploaded.head(20))
    st.write("Summary statistics:")
    st.dataframe(uploaded.describe())
else:
    st.info("Upload a CSV to preview it here.")
st.caption("Idea: file_uploader gives a file object that pandas can read directly.")
