from flask import redirect
import pandas as pd

from dtale.app import build_app
from dtale.views import startup

if __name__ == '__main__':
    app = build_app(reaper_on=False)

    @app.route("/hukuk")
    def create_df():
        file = "uploads/Hukuk.xlsx"
        df = pd.read_excel(file)
        print(df)
        instance = startup(data=df, ignore_duplicate=True)
        return redirect(f"/dtale/main/{instance._data_id}", code=302)

    @app.route("/")
    def hello_world():
        return 'Hi there, load data using <a href="/hukuk">Hukuk İncele</a>'

    app.run()