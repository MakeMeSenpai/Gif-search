from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract the query term from url using request.args.get()
    user_input = request.args.get('user_input')

    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'
    params = {"Key": "AAHE3B82O96Z", "q": user_input, "limit": 10}

    # TODO: Make an API call to Tenor using the 'requests' library. For 
    # reference on how to use Tenor, see: 
    # https://tenor.com/gifapi/documentation

    r = requests.get("https://api.tenor.com/v1/search", params)
    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object
    json_data = json.loads(r.content)
    # return json_data
    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
    gifs = json_data["results"]
    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

    return render_template('index.html', json_data=json_data, gifs=gifs)

if __name__ == '__main__':
    app.run(debug=True)
