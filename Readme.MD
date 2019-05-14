# Flask - Matplotlib

This repository contain a simple flask app where user can input two lists of numbers and the app will return the graphic that was made using matplotlib module.

## Update 1
Following the instructions from this link:

https://technovechno.com/creating-graphs-in-python-using-matplotlib-flask-framework-pythonanywhere/

I try to create another version of the app named app1.py, which can render html file that contains the graphic that we have made.

### Note:
When I run this app I always get this warning message in my terminal

```bash
WARNING: QApplication was not created in the main() thread.
```    

So I used this line of code to change the backend that is used by matplotlib. Feel free to turn off this code, to know if the error also happens in your computer or not.

```python 
import matplotlib 
matplotlib.use('agg')
```

More information about this can be found in the documentation
https://matplotlib.org/tutorials/introductory/usage.html#backends