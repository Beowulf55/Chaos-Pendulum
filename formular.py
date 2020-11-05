import math


# ω = angular velocity
# θ = angle
# m = mass
# L = length
# g = gravity


def FirstAcceleration(θ1, θ2, m1, m2, L1, L2, g, ω1, ω2):
    numer1 = -g * (2 * m1 + m2) * math.sin(θ1)
    numer2 = -m2 * g * math.sin(θ1 - 2 * θ2)
    numer3 = -2 * math.sin(θ1-θ2)
    numer4 =  m2 * ((ω2 * ω2) * L2 + (ω1 * ω1) * L1 * math.cos(θ1-θ2))
    numer = numer1 + numer2 + (numer3 * numer4)
    denom = L1 * (2 * m1 + m2 - m2 * math.cos(2 * θ1 - 2 * θ2))

    return float(numer/denom)

def SecondAcceleration(θ1, θ2, m1, m2, L1, L2, g, ω1, ω2):
    numer1 = 2 * math.sin(θ1 - θ2)
    numer2 = (ω1 * ω1) * L1 * (m1 + m2) + g * (m1 + m2) * math.cos(θ1)
    numer3 = (ω2 * ω2) * L2 * m2 * math.cos(θ1-θ2)

    numer = numer1 * (numer2 + numer3)
    denom = L2 * (2 * m1 + m2 - m2 * math.cos(2 * θ1 - 2 * θ2))

    return float(numer/denom)
