__author__ = 'Mikael Foo'

import ComfortModelsClass

dumpmv = ComfortModelsClass.ComfortModels()
 #%relative air velocity (m/s)
 #%relative humidity (%) Used only this way to input humidity level
 #%metabolic rate (met)
 #%clothing (clo),0.5 typical indoor summer clothing
 #%external work, normally around 0 (met)

def comfpmv(self, ta, tr, vel, rh, met, clo, wme):


    comf = dumpmv.comfPMV(ta, tr, vel, rh, met, clo, wme)

    return comf[0]

def comfpmv_ppd(self, ta, tr, vel, rh, met, clo, wme):

    comf = dumpmv.comfPMV(ta, tr, vel, rh, met, clo, wme)
    return comf[1]


def comfPMVElevatedAirspeed_pmv(self, ta, tr, vel, rh, met, clo, wme):

    comf = dumpmv.comfPMVElevatedAirspeed(ta, tr, vel, rh, met, clo, wme)
    return comf[0]

def comfPMVElevatedAirspeed_ppd(self, ta, tr, vel, rh, met, clo, wme):

    comf = dumpmv.comfPMVElevatedAirspeed(ta, tr, vel, rh, met, clo, wme)
    return comf[1]



