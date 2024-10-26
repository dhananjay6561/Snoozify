# app.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import tensorflow as tf
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the model
model = tf.keras.models.load_model('chatbot_model.h5')

# Example function to process user input
def process_input(user_input):
    # Here, you'll process the input as per your model's requirements
    # For demonstration, let's say we just convert it to a numpy array
    # You will replace this with actual preprocessing logic
    input_array
