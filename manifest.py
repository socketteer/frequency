from fractions import Fraction


def remainder_method(sampling_frequency, true_frequency):
    phase = true_frequency / sampling_frequency
    apparent = abs(phase - int(round(phase)))
    return apparent


def gcd_method(sampling_frequency, true_frequency):
    frac = Fraction(true_frequency / sampling_frequency)
    return sampling_frequency / float(frac.denominator)

