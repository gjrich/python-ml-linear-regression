# python-ml-linear-regression

> Why Do We Square Residuals in Linear Regression?

Exploring simple linear regression using Python (and PyShiny)

## Explore the PyShiny Playground

We use the Shiny for Python (PyShiny) online playground to explore. 

- PyShiny https://shiny.posit.co/py/
- Playground https://shinylive.io/py/examples/
- Plotly Example: https://shinylive.io/py/examples/#plotly

Go to the Plotly Example at the link above. 
Notice there are two code files:

- app.py (visible tab)
- requirements.txt (background tab)

Click the run arrow to see the current chart.

We can use PyShiny to explore linear regression using Python. 

## Example 1: Random Linear Regression

Go to the PyShiny Playground. 
Run the [Plotly Example](https://shinylive.io/py/examples/#plotly).

For this example, we need to edit one file:

 - We'll replace the code in the app.py in the Playground with our **app_random.py** code.

### app.py

This Repo: Click on app_random.py above. Select all the code (CTRL A if Windows or CMD A if Mac). 
Copy the code to your clipboard (CTRL C if Windows, or CMD C if Mac). 

Browser: Click in the Playgroud app.py tab. Select all the code in the app.py playground example (CTRL A if Windows or CMD A if Mac). 
Paste the code from your clipboard (app_random.py as shown in this repo) into app.py in the Playground (CTRL V if Windows, or CMD V if Mac).
Verify the code copied correctly. 

Click the run arrow (▶) to see the updated app. 

## Example 2: Comparing Linear Regression Options

Go to the PyShiny Playground. 
Run the [Plotly Example](https://shinylive.io/py/examples/#plotly).

For this example, we need three files:

- We'll replace the code in the app.py in the Playground with our **app.py** code.
- We'll edit the **reqirements.txt** file to add more packages.
- We'll add another file named **utils.py** that has some linear regression code.

### app.py

This Repo: Click on app.py above. Select all the code (CTRL A if Windows or CMD A if Mac). 
Copy the code to your clipboard (CTRL C if Windows, or CMD C if Mac). 

Browser: Click in the Playground app.py tab. Select all the code in the app.py playground example (CTRL A if Windows or CMD A if Mac). 
Paste the code from your clipboard (app.py as shown in this repo) into app.py in the Playground (CTRL V if Windows, or CMD V if Mac).
Verify the code copied correctly.

### requirements.txt

This Repo: Click on requirements.txt above. Select all the code. 
Copy the code to your clipboard.

Browser: Click in the Playground requirements.txt tab. Select all the requirements.txt code in the playground example. 
Paste the code from your clipboard (requirements.txt as shown in this repo) into requirements.txt in the Playground.
Verify the code copied correctly.

### utils.py

This Repo: Click on utils.py above. Select all the code.
Copy the code to your clipboard.

Browser: Click in the Playground code window. Add a new code file. Name the file exactly **utils.py**. Spelling and capitalization should be exact. 
Paste the code from your clipboard (utils.py as shown in this repo) into your new utils.py file in the Playground.
Verify the code copied correctly.

Click the run arrow (▶) to see the updated app. 

## Links to the Apps Running in Shinylive

Example 1: Random Linear Regression

- [app](https://shinylive.io/py/app/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMAYjvocaeYYB0IaACASRlWIBOZTgAUohANZQA5nADOnAGIBLAXLLsWW7Y3abR2MgAtSnAMpkoEACZQB1zgBllAIwF3so8VNlz2yvkFhdxtiGH9AoU51KDJldWVCPwgAMwEwzjJsVGUIaU4A-ijndTxOABUAV1QAGzg9DlEa4jIazxTBAvI4d0I4gDc4TkIjOzJkwqDOWpa2jDgAD1QBeQUoBVQFiKLhGdbsDGl3VCMAfWIXACs4PrWFaWJ2NIy9uaO0M4vLuQxTlOVpJUVgVIsIVICVg0uCJsGYjLlPKhvDJ5E90jBovCIAdFstViCdpxKspOJw0Rk5FjsAB3ZTWWTjAlTFY2HqnV7YKE6bksfQAETg-wgQwA4s0XFAapwAGp2ZRQFx1ZI8lW6CD6MxwYRyMJDXKoSrCfpyhVKsmNbgQQg1SrWIa2SyZbJDLHjdjSZSDCCnCCVGDs4i5caILrCAC8nAArAAGd2eyinOTNVBDEMpZqxTgRgBMGFjeXj3qDPUIcFQwjTGfDnAAjLn8x6vT7A3I4ImyA5K8RMxGa3muarVfzBbkhopKla4qRlYOh+rGgKhUMoJwUhO+spTGRiJxZML3BROCvW8JiClOAsyp4HSv+EHlRUjEMke54BQ1Jw7UvMk-OMaBPKipDNA8AKJUrYOM0hCSm0ZS5HIdJDMY8SruuU7zl+u6UD0sRtjeAb3gAFL6-p3uQcghkGZRJsQKZdrEcHdAIpblvRZBlBALZtuo1hsQAlJwAC0AB8FTVHUwAlGQwDpt2ZAALplFJMlVvJ8mIOwpKkgA5LpIrYQeQyXpw16xLegbkZwtLGEe0QpoQyj-HAkGjnYnArDUsSbhAlLKKgR42JwnHxHAGC6dpDRaZwXCasIxhDCE1gUnAzmrp0KzLMQ1iVA5LjKDUyhZJpWmJWEGCts5hHRnxxWkrV0WcPp+64bZBXqJwZ7uVYSUYgsf6SpU8icC4WrUilECcNGAUODW9ULKcbVkCGymybE8lZpwwClTAGDbYRAkdAInCnF0XV5HAxF+gR5F8fJ9X1VwTU4YeK6LR157Ba2-U2kN4G5PkK4ilA4EIVYn7xGQAEuIa3kPY+wFcQUCilkxqV2MQE4OFN1lGLZMQ2HYDh2v08roe9QVce21j1Z9bbGj9FFOBDKlyetEZbd1ZXSMDchyFVHGUzxB2dCduRnbIl2kRZ4y3fdE1aVwADCkqEJUnmHvFwyCCscj8DY-0md9g0KBKEEdRNmsFcKblwAAjpUXmmJ4EYwH1ADUw2cB7tP1dgC0Q8tzOrQpG3ADRKacAAVBeXuhiWZbCN7iOHReAshadABefmEfNi1p62pz08bsvy3VpcNQASlqQIW7+e7PalfXdYbRdDestlkOJSE7tSowUIMR3QTUNQKMhChrpOsPlysncCBNucQ1e-vqAOs7csO36azCcIIpwACiSw6woACq3CaGvPJQpwx9fVvsJUkSyhYCi5zlnzAlviYDjbtEWo-khhU6jmmJM-WQr9xiETiK0OAYZWBgGcNbI6VcjirG8k0FocCarzi4DfIYICjA1n2pwT+WVMg7msPEWoUBPDHhuKQawgk6iDClE+KAFC8icEIkYbMAl9BiF5qdY8kMDYUGHgbXuiRcYkIcGNIkEF2D4OzIROBAAhYkNRhA43MJYOICQkheEkCiTBV9cGPywEQ6RZDwa608jQ6YdgZDHFxoRVAWDoTrAUGLMGKRBLqAAhwwiK5DowFiBQBwfj-puKsSQGAeVhSZEWMIZuWiMZHX1IaI29RfRP1QIRFIcDFYY3IOTEQ0tGYgEbAmEi11xgAF9jHznPhfHQG9RycAAGScCrqyI6Ihmj7E4IrUYQgmnNK0A0dgAABFkdoBDsn6W0dgmE5DQTIO+eZLQiEiSUACIEcANLl3CpwRcbSgloTQcYTMM8a5rHQQM8EezwrFThsrYeHUgSoUnluHc9dDLvKOn1N6zdPBvU6q3ZIUUFh5xMm9CMvzcKnHwmRCBlTvTVORXIMoqLEzJjgFiwspxizMQTvipstMqZYKinDFQwgrZwDcisFBvM0EwCynAKUqL-kx2BZwRaEKtLhzxXHYl5YNoxF0XEJIGA6V2FOIyo+3kc7QuwItSlWkXkrBaiuYU1JpgLM8Cs0JPRhjDOEM8DEqTPxmXqv8fIEZNjlVWe+ZR5dIVhihYvc0UUorYDDCqz19UoqeRGiPMMIBtILG0iGbSAANbSZRtLYCjZwbSABNbStSyiBq0lAuoYZ8nwNckguATKEKmAFKyzhZhcUhhAIKxAGAADMKRM08CYixJanAQBEo7Q25ttSapgCwS8lWasWqa3lag0wdK5EGzejEvET4fJTyilwKus8Jquzdi4NKR16UjBjmLTWgKIb1Uncy0g-t4ns0FVHGOHse0J13Ye+ei07rzlXYMzVL09WzBBW0v6HCHV0qISQHykMcrbiOtIjAcNTGa1tY8tY1hrCnEhuIC6H8tRfzhvwzxtdgJwF1TO2RhBv2pR-mwhwhUrGaxGGMG1AIMBUbQ70C6wHRw53dcqsM56y3ejpXxDAN5gDRnksO8ua7q5z3-jsiEQwvg3Dij3PucAB7DBgqPeE49zmkDPdJiatqwCZvACBBAyAVj21UHAeA5EMBkAWGQfARBSAUCoMgJEBNkgcnYMZ+SQA)
- [editor](https://shinylive.io/py/editor/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMAYjvocaeYYB0IaACASRlWIBOZTgAUohANZQA5nADOnAGIBLAXLLsWW7Y3abR2MgAtSnAMpkoEACZQB1zgBllAIwF3so8VNlz2yvkFhdxtiGH9AoU51KDJldWVCPwgAMwEwzjJsVGUIaU4A-ijndTxOABUAV1QAGzg9DlEa4jIazxTBAvI4d0I4gDc4TkIjOzJkwqDOWpa2jDgAD1QBeQUoBVQFiKLhGdbsDGl3VCMAfWIXACs4PrWFaWJ2NIy9uaO0M4vLuQxTlOVpJUVgVIsIVICVg0uCJsGYjLlPKhvDJ5E90jBovCIAdFstViCdpxKspOJw0Rk5FjsAB3ZTWWTjAlTFY2HqnV7YKE6bksfQAETg-wgQwA4s0XFAapwAGp2ZRQFx1ZI8lW6CD6MxwYRyMJDXKoSrCfpyhVKsmNbgQQg1SrWIa2SyZbJDLHjdjSZSDCCnCCVGDs4i5caILrCAC8nAArAAGd2eyinOTNVBDEMpZqxTgRgBMGFjeXj3qDPUIcFQwjTGfDnAAjLn8x6vT7A3I4ImyA5K8RMxGa3muarVfzBbkhopKla4qRlYOh+rGgKhUMoJwUhO+spTGRiJxZML3BROCvW8JiClOAsyp4HSv+EHlRUjEMke54BQ1Jw7UvMk-OMaBPKipDNA8AKJUrYOM0hCSm0ZS5HIdJDMY8SruuU7zl+u6UD0sRtjeAb3gAFL6-p3uQcghkGZRJsQKZdrEcHdAIpblvRZBlBALZtuo1hsQAlJwAC0AB8FTVHUwAlGQwDpt2ZAALplFJMlVvJ8mIOwpKkgA5LpIrYQeQyXpw16xLegbkZwtLGEe0QpoQyj-HAkGjnYnArDUsSbhAlLKKgR42JwnHxHAGC6dpDRaZwXCasIxhDCE1gUnAzmrp0KzLMQ1iVA5LjKDUyhZJpWmJWEGCts5hHRnxxWkrV0WcPp+64bZBXqJwZ7uVYSUYgsf6SpU8icC4WrUilECcNGAUODW9ULKcbVkCGymybE8lZpwwClTAGDbYRAkdAInCnF0XV5HAxF+gR5F8fJ9X1VwTU4YeK6LR157Ba2-U2kN4G5PkK4ilA4EIVYn7xGQAEuIa3kPY+wFcQUCilkxqV2MQE4OFN1lGLZMQ2HYDh2v08roe9QVce21j1Z9bbGj9FFOBDKlyetEZbd1ZXSMDchyFVHGUzxB2dCduRnbIl2kRZ4y3fdE1aVwADCkqEJUnmHvFwyCCscj8DY-0md9g0KBKEEdRNmsFcKblwAAjpUXmmJ4EYwH1ADUw2cB7tP1dgC0Q8tzOrQpG3ADRKacAAVBeXuhiWZbCN7iOHReAshadABefmEfNi1p62pz08bsvy3VpcNQASlqQIW7+e7PalfXdYbRdDestlkOJSE7tSowUIMR3QTUNQKMhChrpOsPlysncCBNucQ1e-vqAOs7csO36azCcIIpwACiSw6woACq3CaGvPJQpwx9fVvsJUkSyhYCi5zlnzAlviYDjbtEWo-khhU6jmmJM-WQr9xiETiK0OAYZWBgGcNbI6VcjirG8k0FocCarzi4DfIYICjA1n2pwT+WVMg7msPEWoUBPDHhuKQawgk6iDClE+KAFC8icEIkYbMAl9BiF5qdY8kMDYUGHgbXuiRcYkIcGNIkEF2D4OzIROBAAhYkNRhA43MJYOICQkheEkCiTBV9cGPywEQ6RZDwa608jQ6YdgZDHFxoRVAWDoTrAUGLMGKRBLqAAhwwiK5DowFiBQBwfj-puKsSQGAeVhSZEWMIZuWiMZHX1IaI29RfRP1QIRFIcDFYY3IOTEQ0tGYgEbAmEi11xgAF9jHznPhfHQG9RycAAGScCrqyI6Ihmj7E4IrUYQgmnNK0A0dgAABFkdoBDsn6W0dgmE5DQTIO+eZLQiEiSUACIEcANLl3CpwRcbSgloTQcYTMM8a5rHQQM8EezwrFThsrYeHUgSoUnluHc9dDLvKOn1N6zdPBvU6q3ZIUUFh5xMm9CMvzcKnHwmRCBlTvTVORXIMoqLEzJjgFiwspxizMQTvipstMqZYKinDFQwgrZwDcisFBvM0EwCynAKUqL-kx2BZwRaEKtLhzxXHYl5YNoxF0XEJIGA6V2FOIyo+3kc7QuwItSlWkXkrBaiuYU1JpgLM8Cs0JPRhjDOEM8DEqTPxmXqv8fIEZNjlVWe+ZR5dIVhihYvc0UUorYDDCqz19UoqeRGiPMMIBtILG0iGbSAANbSZRtLYCjZwbSABNbStSyiBq0lAuoYZ8nwNckguATKEKmAFKyzhZhcUhhAIKxAGAADMKRM08CYixJanAQBEo7Q25ttSapgCwS8lWasWqa3lag0wdK5EGzejEvET4fJTyilwKus8Jquzdi4NKR16UjBjmLTWgKIb1Uncy0g-t4ns0FVHGOHse0J13Ye+ei07rzlXYMzVL09WzBBW0v6HCHV0qISQHykMcrbiOtIjAcNTGa1tY8tY1hrCnEhuIC6H8tRfzhvwzxtdgJwF1TO2RhBv2pR-mwhwhUrGaxGGMG1AIMBUbQ70C6wHRw53dcqsM56y3ejpXxDAN5gDRnksO8ua7q5z3-jsiEQwvg3Dij3PucAB7DBgqPeE49zmkDPdJiatqwCZvACBBAyAVj21UHAeA5EMBkAWGQfARBSAUCoMgJEBNkgcnYMZ+SQA)

Example 2: Comparing Linear Regression Options

- [app]()
- [editor]()

## Acknowledgements

Many thanks to the creators, contributors, and maintainors for making these powerful tools available for free: 

- Python
- PyShiny
- GitHub
- pandas
- plotly
- numpy
- scipy
- statsmodels
- scikit-learn

## Screenshot Example 1

![Example 1](images/example1.png)

## Screenshot Example 2

![Example 2](images/example2.png)
