from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from datetime import datetime, timedelta

import skyscraper

app = Flask(__name__)
app.config['SECRET_KEY']="YeCqhrYGgBqrwH5XRHuj4XFBmY"

bootstrap = Bootstrap(app)


@app.route('/')
def home():
    
    DAYS_TO_GET = 7

    # raw outputs are just lists of shows
    sky_raw = skyscraper.get_shows(DAYS_TO_GET)
    cycling_raw = skyscraper.get_eurosport_cycling()

    # turn to an ordered dict of days
    tidied = skyscraper.tidy_shows(sky_raw + cycling_raw)
    
    start_date = datetime.now().strftime("%-d %b")
    end_date = (datetime.now() + timedelta(days=7)).strftime("%-d %b")
    
    by_game = skyscraper.get_by_game(tidied)
    return render_template('skyscraper.html', out=tidied,
                                          by_game=by_game, 
                                          start_date=start_date,
                                          end_date=end_date)


if __name__ == '__main__':
    app.run(debug=True)
