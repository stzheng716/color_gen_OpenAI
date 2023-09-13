import openai
import json
from flask import Flask, render_template, request
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPEN_AI_API_KEY"]

app = Flask(__name__,
    template_folder='templates'
)

def get_colors(msg):
    prompt = f"""
    You are a color aplette generating assistant that responds to text prompts for color palettes with hexicodes
    You should genereate color palettes that fit hte theme, mood, or instructions in the prompt. 
    The palettes should be between 2 and 8 colors

    Q:Covert the following verbal descrition of of a color palette into a list of colors: summer
    A:["#EF9595","#EFB495","#EFD595", "#EBEF95"]

    Q:Covert the following verbal descrition of of a color palette into a list of colors: winter
    A:["#F5EFE7","#D8C4B6","#4F709C", "#213555"]

    Q:Covert the following verbal descrition of of a color palette into a list of colors: {msg}
    A:
    """

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
    )
    
    print("RESPONSE", response)
    colors = json.loads(response["choices"][0]["text"])
    return colors

@app.route("/palette", methods=["POST"])
def prompt_to_palette():
    query = request.form.get("query")
    colors = get_colors(query)
    return {"colors": colors}
    
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)