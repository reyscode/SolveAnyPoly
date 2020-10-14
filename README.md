# SolveAnyPoly

Solve polynomial of any degree using Newton's method and Synthetic division.

<img src="/images/graph-1.png" width=50% /><img src="/images/8-rev.png" width=50% />



## Setup

```bash
git clone https://github.com/reyscode/SolveAnyPoly
cd SolveAnyPoly/
pip install -r requirements.txt
```

## Usage

```bash
python3 solve_any_poly.py
```

```console
Enter Coefficients of Equation (comma separated):1,-9,26,-24
[2, 3, 4]
```


## How to contribute

- This project can be extended to solve equations with non-linear terms like sine, cosine, and exponential, by making use of Taylor series expansion
- Implementation of Finite Difference Method for derivative calculation, to remove sympy dependency
- Explore Secant method as a replacement for Newton's
