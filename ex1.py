import marimo

__generated_with = "0.10.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import pandas as pd
    import seaborn as sns
    return pd, sns


@app.cell
def _(pd):
    books = pd.read_json("books.json")
    books
    return (books,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
