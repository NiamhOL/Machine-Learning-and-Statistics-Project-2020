# Import python modules for use in web service
import flask as fl
import numpy as np
# Silence tensorflowstartup warnings. Code adapted from
# https://stackoverflow.com/a/65215118
from tensorflow import tensorflow
silence_tensorflow()
import tensorflow.keras as kr

# curl http://127.0.0.1:5000/api/number/5
@app.route('/api/number/<speed>')
def number(speed):
   s = float(speed)
   # get power from power curve model
   return {"power" : power_output(s)}

# # Add list route.
# @app.route('/api/list/<speeds>')
# def number_list():
#    return {"value": power_output(speeds)}

# Load Keras model from saved files "my_model.json" & "my_model.h5". Code adapted from
# https://machinelearningmastery.com/save-load-keras-deep-learning-models/
# load json and create model
json_file = open('my_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = kr.models.model_from_json(loaded_model_json)
# load weights into new model
model.load_weights("wind_power.h5")
#print("Loaded model from disk")

# Copy of variables and function from Project.ipynb
# Set normalisation factors
wsF = 25
poF = 120
# Function to predict power output based on inputted wind speeds
def power_output(windspeeds):
   """ Function to predict power output based on inputted wind speeds
      Acceptable inputs include numbers or a list of numbers
   """
   # Set the cut off wind speeds
   minWS, maxWS = 3, 24.5

   # If wind speed is inside the cut off levels
   if windspeeds > minWS and windspeeds < maxWS:
      ws = np.array([windspeeds])
      return round(model.predict(ws/wsF)[0][0]*poF, 3)
   else:
      #print("Error")
      return 0

# Function test
# print(power_output(10))

# Run in debug mode
if __name__ == "__main__":
   app.run(debug=True)