"""
This is an Python implementation of a DEPOSIT Collector
It handles data under the SmartCampus format. eg. {"n":"TEST","v":"12","t":"1455610331"}
Default port: 8000

Part of DEPOSIT framework: https://github.com/ace-design/DEPOSIT
"""
from flask import Flask, json, request
app = Flask(__name__)
PORT = 8000		#Change the default port here
@app.route('/')
def api_root():
    return '<h3>DEPOSIT Collector</h3><p>It works! Values under the SmartCampus format must be sent on /collect</p><p>This project is part of the <a href="https://github.com/ace-design/DEPOSIT" target="_blank">DEPOSIT framework</a></p>'

@app.route('/collect', methods = ['POST'])
def collect():
    # Get the parsed contents of the form data
    app.logger.debug("JSON received...")
    app.logger.debug(request.json)

    if request.json:
    	print(request)
    	return 'Value posted with success'
    else:
    	return "No data received"

if __name__ == '__main__':
	print("DEPOSIT Collector")
	app.run(host="0.0.0.0", debug=True, port=PORT)