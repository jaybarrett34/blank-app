# Lab 12: California Housing Predictor (+ Roulette)

Streamlit app with two pages in the top nav:

- **Housing Predictor**: random forest regression on the California housing dataset (`regression_model.joblib`).
- **Roulette**: a mock European roulette table. Drag chips onto the felt and spin. Play money only.

## Run it

Prerequisite: [uv](https://docs.astral.sh/uv/) (`curl -LsSf https://astral.sh/uv/install.sh | sh`).

```
uv sync                                  # install deps (Python 3.14)
uv run python train_model.py             # only if regression_model.joblib is missing
uv run streamlit run streamlit_app.py
```

`model.ipynb` contains the same training steps as `train_model.py` (select the `.venv` kernel).

## Layout

```
streamlit_app.py            entrypoint, sets up top navigation
app_pages/predictor.py      housing price predictor
app_pages/roulette.py       roulette page (hosts the HTML table)
app_pages/roulette_table.html  drag-and-drop table, runs in the browser
train_model.py              trains and saves regression_model.joblib
```
