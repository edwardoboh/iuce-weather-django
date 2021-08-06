# IUCE Weather Station Backend Django App

This is the backend app for the IUCE Weather station.
Click [here](https://iuce-weather.herokuapp.com/sensor/) to view deployed app on Heroku.

Check repository for frontend React App or click [here](https://iuce.herokuapp.com/)
to view the deployed frontend React app on Heroku.

## Weather Station Platform

Web platform to gather data and to display the current state of the weather station. Built using JavaScript and Python.

The web platform is made up of two parts;

1. A frontend user interface to display the last measured value of temperature, pressure, light intensity and humidity.
2. A Backend web server which receives data from the weather station device through API calls, send the last measured device readings to the frontend user interface for display and stores all received data to a database.
3. A database server which receives and stores all device readings from the web server. The data is stored either for download in a CSV format or for training machine learning algorithm to make predictions.

The Frontend user interface is to be built using ReactJS, a frontend JavaScript framework for building web applications. This user interface would contain:

1. A login page for authenticating the user of the platform.
2. A dashboard page which displays the latest sensor readings from the device, gotten from the server.
3. A charts page showing the device readings over a period of time in a chart. One for temperature, one for pressure, light intensity and humidity. All charts in a single page.
4. Lastly, a functionality to download these readings in a CSV format.

The Backend server is to be built with NodeJS, a JavaScript framework for developing backend web servers. The server functions both as a Webhook for receiving sensor readings from the weather station and as an API responding to the frontend&#39;s request for last sensor reading.

**(Optional: The Backend webserver also contains a machine learning model already trained using the recorded data from the weather station during the information gathering phase. This already trained model is used to make predictions on future data using Python together with a supervised machine learning algorithm)**

The Database to be used is a NoSQL database which stores all data from the weather station as a collection of documents in a BLOB (Binary Large Object) format.
