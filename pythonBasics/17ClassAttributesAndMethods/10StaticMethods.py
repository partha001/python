class WeatherForcast():

    def __init__(self,temperatures) :
        self.temperatures = temperatures
    
    def inCelcius(self):
        return [self.convertFromFarenheitToCelcius(temp) for temp in self.temperatures]
        ## also note though convertFromFarenheitToCelcius is a static method still it can invoked w.r.t an instance or w.r.t to the class

    @staticmethod
    def convertFromFarenheitToCelcius(fahr):
        calculation = (5/9) * (fahr-32)
        return round(calculation,2)
    
wf = WeatherForcast([100,90,80,70])
print(wf.inCelcius()) #op: [37.78, 32.22, 26.67, 21.11]

#note the static method can be called w.r.t both instance as well as class . earlier we have called it w.r.t the instance from within inCelcius()
# now lets call it w.r.t the class
print(WeatherForcast.convertFromFarenheitToCelcius(100)) #op: 37.78

        
