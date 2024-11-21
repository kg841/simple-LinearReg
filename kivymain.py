import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

def grafik(x1,x2,x3,x4,x5 , y1,y2,y3,y4,y5):
    import numpy as np
    import matplotlib.pyplot as plt


    # Sample data
    x = np.array([x1,x2,x3,x4,x5]).astype(np.float64)  # X Values
    y = np.array([y1,y2,y3,y4,y5]).astype(np.float64)  # Y Values


    # Doğrusal regresyon
    A = np.vstack([x, np.ones(len(x))]).T  
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]  # slope(m) and cut-off point(c)


    # R value calculation
    r = np.corrcoef(x, y)[0, 1]  
    print("R value :", r)



    # Plotting the graph
    plt.scatter(x, y, color='red', label='Datas')
    plt.plot(x, m*x + c, 'b-', label=f'y={m:.4f}x + {c:.4f} \n r =  {r} \n r Square = {r**2}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Linear Regression Graph')
    plt.legend()
    plt.grid()
    plt.show()

    # Linear equation
    print(f'The equation of a linear graph : y = {m:.4f}x + {c:.4f} ')
    
    r = np.corrcoef(x, y)[0, 1]  

    print("R value :", r)  

class MyGrid(Widget):
    x1 = ObjectProperty(None)
    x2 = ObjectProperty(None)
    x3 = ObjectProperty(None)
    x4 = ObjectProperty(None)
    x5 = ObjectProperty(None)

    y1 = ObjectProperty(None)
    y2 = ObjectProperty(None)
    y3 = ObjectProperty(None)
    y4 = ObjectProperty(None)
    y5 = ObjectProperty(None)


    def btn(self):
 
        print(float(self.x1.text),float(self.x2.text),float(self.x3.text),float(self.x4.text),float(self.x5.text),)
        print("*************************")
        print("*************************")
        
        print("*************************")
        grafik(float(self.x1.text),float(self.x2.text),float(self.x3.text),float(self.x4.text),float(self.x5.text),
               float(self.y1.text),float(self.y2.text),float(self.y3.text),float(self.y4.text),float(self.y5.text))


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()