def kelvintofahrenheit(temperature):
    assert(temperature>=0),"colder than absolute zero!"
    return(temperature-273)*1.8)+32
try:
    print (Kelvintofahrenhiet(273))
    print (int(kelvintofahrenhiet(505.78)))
    print (Kelvintofahrenhiet(-5))
except:
    print("negative values given for conversions")

