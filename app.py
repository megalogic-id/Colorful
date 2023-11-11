import os
import re

from flask import Flask, flash, render_template, request

from palette import *

app = Flask(__name__)
app.secret_key = "supersecretkey"


def validate_hex_color(color):
    return re.match("^#(?:[0-9a-fA-F]{3}){1,2}$", color)


@app.route('/', methods=['GET', 'POST'])
def index():
    selected_color = "#88E399"
    all_palettes = {}
    if request.method == 'POST':
        selected_color = request.form.get('hex-color').strip()
        if not validate_hex_color(selected_color):
            flash("Invalid Hex color. Please use the format #RRGGBB or #RGB.")
        else:
            selected_color = selected_color
            all_palettes = {
                "Matching Gradient": matching_gradient(selected_color),
                "Spot Palette": spot_palette(selected_color),
                "Twisted Spot Palette": twisted_spot_palette(selected_color),
                "Classy Palette": classy_palette(selected_color),
                "Small Switch Palette": small_switch_palette(selected_color),
                "Complementary Colors": complementary_colors(selected_color),
                "Triadic Colors": triadic_colors(selected_color),
                "Analogous Colors": analogous_colors(selected_color),
            }
    return render_template('pages/index.html',
                           all_palettes=all_palettes,
                           selected_color=selected_color)


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("pages/500.html"), 500


if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 8080)))
