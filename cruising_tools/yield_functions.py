#!/usr/bin/env python
import numpy as np


''' This module contains forestry functions that will calculate stem green
    tons for loblolly pine (pinus taeda) using models provided by Baldwin
    & Feduccia, and Borders, et al.
'''

def pmrc_lcp_tons(dbh, totHt, mTop=3.0):
    """Calculates the green tons (wood + bark) for loblolly pine in the
        Lower Coastal Plain region.
        Source: PMRC 1990, Univ. of Georgia, Borders et al.

        :param mTop: top merchantable diameter outside bark.
        :param totHt: total tree height.
        :param dbh: diameter outside bark at 4.5ft.
        :returns: volume in tons.        
    """
    # model parameters
    PARAM_A = 1.829983
    PARAM_B = 1.247669
    PARAM_C = 3.523107
    PARAM_D = 1.449947

    # model constants, and calculated exponents
    const1 = 0.0740959
    const2 = 0.123329
    exp1 = np.power(dbh, PARAM_A)
    exp2 = np.power(totHt, PARAM_B)
    exp3 = np.power(mTop, PARAM_C)
    exp4 = np.power(dbh, PARAM_D)

    # calculate and return green tons
    return ((const1 * exp1 * exp2) - (const2 * (exp3 / exp4) * 
        (totHt - 4.5))) / 2000


def pmrc_ucp_tons(dbh, totHt, mTop=3.0):
    """Calculates the green tons (wood + bark) for loblolly pine in the
        Upper Coastal Plain region.
        Source: PMRC 1990, Univ. of Georgia, Borders et al.

        :param mTop: top merchantable diameter outside bark.
        :param totHt: total tree height.
        :param dbh: diameter outside bark at 4.5ft.
        :returns: volume in tons.        
    """
    # model parameters
    PARAM_A = 1.917146
    PARAM_B= 1.038452
    PARAM_C = 3.589155
    PARAM_D = 1.413061

    # model constants, and calculated exponents
    const1 = 0.141534
    const2 = 0.0932063
    exp1 = np.power(dbh, PARAM_A)
    exp2 = np.power(totHt, PARAM_B)
    exp3 = np.power(mTop, PARAM_C)
    exp4 = np.power(dbh, PARAM_D)

    # calculate and return green tons
    return ((const1 * exp1 * exp2) - (const2 * (exp3 / exp4) * 
        (totHt - 4.5))) / 2000
    

def baldwin_stem_tons(dbh, totHt, age=15, thinned=True, top=3.0):
    """Calculates the total stem volume in tons for loblolly pine in the
       West Gulf Region.
       Source: USDA Southern Forest Experiment Station, Baldwin & Feduccia, 
       SO-236, 1987
    
       :param dbh: diameter outside bark at 4.5 feet.
       :param totHt: total height of the stem.
       :param age: tree age.
       :returns: volume in tons.
    """
    # model parameters
    PARAM_1 = -2.06033
    PARAM_2 = 1.93926
    PARAM_3 = 1.05077
    PARAM_4 = 0.000061
    
    # calculated exponents
    expr1 = np.log(dbh)
    expr2 = np.log(totHt)
    expr3 = np.power(age, 2)
    
    # check for thinned stands, thinning has influence on merchantable ratio
    if thinned:
        merch_ratio = baldwin_merch_ratio_thinned(dbh, top)
    else:
        merch_ratio = baldwin_merch_ratio_unthinned(dbh, top)

    # calculate green tons
    tons = math.exp(PARAM_1 + (PARAM_2 * expr1) + (PARAM_3 * expr2) + 
        (PARAM_4 * expr3)) / 2000
    
    # return product of tons and merchantable ratio
    return tons * merch_ratio
    

def baldwin_merch_ratio_unthinned(dbh, mTop=3.0):
    """Calculates the merchantable volume ratio for unthinned stands.
       This can be applied to various top diameters to determine the
       volume proportion for a particular part of the stem.  Simply subtract
       the two proportions.
       Source: USDA Southern Forest Experiment Station, Baldwin & Feduccia,
       SO-236, 1987
    
       :param dbh: diameter outside bark at 4.5 ft.
       :param mTop: merchantable top diameter outside bark.    
       :returns: volume in tons.    
    """
    # model parameters
    PARAM_1 = -1.153726
    PARAM_2 = 4.911545
    PARAM_3 = 4.723876
    
    # calculated exponents
    expr1 = np.power(mTop, PARAM_2)
    expr2 = np.power(dbh, PARAM_3)

    # return merchantable ratio
    return math.exp(PARAM_1 * (expr1 / expr2))


def baldwin_merch_ratio_thinned(dbh, mTop=3.0):
    """Calculates the merchantable volume ratio for thinned stands.
       This can be applied to various top diameters to determine the
       volume proportion for a particular part of the stem.  Simply subtract
       the two proportions.
       Source: USDA Southern Forest Experiment Station, Baldwin & Feduccia, 
       SO-236, 1987

       :param dbh: diameter outside bark at 4.5 ft.
       :param mTop: merchantable top diameter outside bark.    
       :returns: volume in tons.    
    """
    # model parameters
    PARAM_1 = -2.058914
    PARAM_2 = 5.124867
    PARAM_3 = 5.170415
    
    # calculated exponents
    expr1 = np.power(mTop, PARAM_2)
    expr2 = np.power(dbh, PARAM_3)

    # return merchantable ratio
    return math.exp(PARAM_1 * (expr1 / expr2))
