# Python-Kivy : graphing by using Least Squares Method 

This is a mobile application developed using **Kivy**. The app allows the user to input 5 x-values and 5 y-values, and then uses the **Least Squares Method** to calculate and display a linear regression graph based on the provided data.

## Features

- The user can input 5 x-values and 5 y-values.
- The application calculates a linear regression model using the Least Squares Method.
- A graph is displayed showing the linear model and how it fits the data points.
  
## Installation

### Requirements

The following libraries are required to run this application:

- Kivy
- NumPy
- Matplotlib

## Usage
Once the application starts, you will be prompted to enter 5 x-values and 5 y-values.

After entering the data, click on the Show Graph button.


<img src="https://github.com/kg841/simple-LinearReg/blob/main/app-photo.png"   width="550" >
The application will display a graph showing the best-fit linear model based on your data.

### Like :
![Figure](https://github.com/kg841/simple-LinearReg/blob/main/Figure.png)

## Technical Explanation
This application uses the Least Squares Method to perform linear regression on 5 given (x, y) data points. Below are the steps involved:

**Data Input :** The user provides 5 x-values and 5 y-values.

**Mathematical Model :** Using the Least Squares Method, the slope and intercept of the best-fit linear model are computed.


**Formula :**  𝑦=𝑚𝑥+𝑏

  _m:Slope_
  
  _b:Intercept_

**Graph Plotting :** The calculated linear model is plotted on the graph alongside the data points to visualize the fit.


