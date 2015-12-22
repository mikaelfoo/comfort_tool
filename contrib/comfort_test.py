__author__ = 'Mikael Foo'

import ComfortModelsClass

dumpmv = ComfortModelsClass.ComfortModels()
def comfpmv(self, ta, tr, vel, rh, met, clo, wme):
 #%relative air velocity (m/s)
 #%relative humidity (%) Used only this way to input humidity level
 #%metabolic rate (met)
 #%clothing (clo),0.5 typical indoor summer clothing
 #%external work, normally around 0 (met)

    return dumpmv.comfPMV(ta, tr, vel, rh, met, clo, wme)


def comfPMVElevatedAirspeed(self, ta, tr, vel, rh, met, clo, wme):


    return dumpmv.comfPMVElevatedAirspeed(ta, tr, vel, rh, met, clo, wme)



