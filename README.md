# Optimization Methods Lab Works

This repository contains laboratory works focused on solving the problem of minimizing unimodal and non-unimodal functions of one and many variables. The solutions are primarily implemented in Python, with methods ranging from classical to gradient-based techniques.

## Lab List

### Minimization of Unimodal and Non-unimodal Functions (One Variable)

| Lab | Title | Description |
| --- | ----- | ----------- |
| 1   | **Bisection Method** | Divides the interval in half to iteratively narrow down the minimum of a unimodal function. |
| 2   | **Golden Section Method** | Optimizes the search for the minimum by using the golden ratio to divide the interval. |
| 3   | **Newton's Method** | Uses the function's second derivative to converge rapidly to a local minimum. |
| 4   | **Cyclic Coordinate Descent** | Minimizes the function by iteratively optimizing each coordinate direction. |
| 5   | **Steepest Descent Method** | Moves in the direction of the steepest gradient to find the minimum. |

### Minimization of Unimodal and Non-unimodal Functions (Multiple Variables)

| Lab | Title | Description |
| --- | ----- | ----------- |
| 1   | **Conjugate Gradient Method** | An efficient method for solving large-scale problems, minimizing along conjugate directions. |
| 2   | **Newton's Method** | Extends the Newton approach to functions of many variables, using the Hessian matrix. |
| 3   | **DFP Method** | An update method for approximating the Hessian matrix in quasi-Newton optimization. |
| 4   | **Projected Gradient Method** | Ensures that the gradient steps stay within a feasible region using projection techniques. |
| 5   | **Sequential Unconstrained Minimization Methods** | Converts constrained optimization problems into a series of unconstrained ones. |

## Current Status

Currently, the repository contains only the first two laboratory works:
- **Bisection Method** (Lab 1 for one-variable functions)
- **Golden Section Method** (Lab 2 for one-variable functions)

The number of labs will increase as I complete more of them. Additionally, a comparison between the different optimization methods will be added in future updates.
