import logging
from django.contrib import messages
from pymongo import MongoClient
from django.shortcuts import render
from django.http import HttpResponse
from matplotlib.animation import FuncAnimation
import matplotlib
from math import sqrt, log
import array as arr
import math
from math import sqrt, log
import string
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from sympy import symbols, sympify
import re


logger = logging.getLogger(__name__)

# from F_Table import F_Table
# from T_Table import T_Table, mechanismName

# Put the logging info within your django view

CONNECTION_STRING = 'mongodb+srv://shwetashaw597:RahulShaw@user.gwvyi.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(CONNECTION_STRING, connect=False)
db = client['kineticsData']
collection = db['data']


equation = "x**2,x+(1-x)*math.log(1-x),1-(2/3)*x-(1-x)**(2/3),(1-(1-x)**(1/3))**2,x,1-(1-x)**(1/2),1-(1-x)**(1/3),(-math.log(1-x))**(2/3),(-math.log(1-x))**(1/2),(-math.log(1-x))**(1/3),(-math.log(1-x))**(1/4),x**(1/2),x**(1/3),x**(1/4),-math.log(1-x),(1-x)**(-1/2)-1,(1-x)**(-1)-1"
alphaEq = "x**(1/2),0,0,1-((1-(x**(1/2)))**3),x,1-((1-x)**2),1-((1-x)**3),1-math.exp(-(x**(3/2))),1-math.exp(-x**2),1-math.exp(-x**3),1-math.exp(-x**4),x**2,x**3,x**4,1-math.exp(-x),1-((1+x)**(-2)),1-((1+x)**(-1))"


T_Table = [[0.000, 1.000, 1.376, 1.963, 3.078, 6.314, 12.71, 31.82, 63.66, 318.31, 636.62],
           [0.000, 0.816, 1.061, 1.386, 1.886, 2.920,
            4.303, 6.965, 9.925, 22.327, 31.599],
           [0.000, 0.765, 0.978, 1.250, 1.638, 2.353,
            3.182, 4.541, 5.841, 10.215, 12.924],
           [0.000, 0.741, 0.941, 1.190, 1.533, 2.132,
               2.776, 3.747, 4.604, 7.173, 8.610],
           [0.000, 0.727, 0.920, 1.156, 1.476, 2.015,
               2.571, 3.365, 4.032, 5.893, 6.869],
           [0.000, 0.718, 0.906, 1.134, 1.440, 1.943,
               2.447, 3.143, 3.707, 5.208, 5.959],
           [0.000, 0.711, 0.896, 1.119, 1.415, 1.895,
               2.365, 2.998, 3.499, 4.785, 5.408],
           [0.000, 0.706, 0.889, 1.108, 1.397, 1.860,
               2.306, 2.896, 3.355, 4.501, 5.041],
           [0.000, 0.703, 0.883, 1.100, 1.383, 1.833,
               2.262, 2.821, 3.250, 4.297, 4.781],
           [0.000, 0.700, 0.879, 1.093, 1.372, 1.812,
               2.228, 2.764, 3.169, 4.144, 4.587],
           [0.000, 0.697, 0.876, 1.088, 1.363, 1.796,
               2.201, 2.718, 3.106, 4.025, 4.437],
           [0.000, 0.695, 0.873, 1.083, 1.356, 1.782,
               2.179, 2.681, 3.055, 3.930, 4.318],
           [0.000, 0.694, 0.870, 1.079, 1.350, 1.771,
               2.160, 2.650, 3.012, 3.852, 4.221],
           [0.000, 0.692, 0.868, 1.076, 1.345, 1.761,
               2.145, 2.624, 2.977, 3.787, 4.140],
           [0.000, 0.691, 0.866, 1.074, 1.341, 1.753,
               2.131, 2.602, 2.947, 3.733, 4.073],
           [0.000, 0.690, 0.865, 1.071, 1.337, 1.746,
               2.120, 2.583, 2.921, 3.686, 4.015],
           [0.000, 0.689, 0.863, 1.069, 1.333, 1.740,
               2.110, 2.567, 2.898, 3.646, 3.965],
           [0.000, 0.688, 0.862, 1.067, 1.330, 1.734,
               2.101, 2.552, 2.878, 3.610, 3.922],
           [0.000, 0.688, 0.861, 1.066, 1.328, 1.729,
               2.093, 2.539, 2.861, 3.579, 3.883],
           [0.000, 0.687, 0.860, 1.064, 1.325, 1.725,
               2.086, 2.528, 2.845, 3.552, 3.850],
           [0.000, 0.686, 0.859, 1.063, 1.323, 1.721,
               2.080, 2.518, 2.831, 3.527, 3.819],
           [0.000, 0.686, 0.858, 1.061, 1.321, 1.717,
               2.074, 2.508, 2.819, 3.505, 3.792],
           [0.000, 0.685, 0.858, 1.060, 1.319, 1.714,
               2.069, 2.500, 2.807, 3.485, 3.768],
           [0.000, 0.685, 0.857, 1.059, 1.318, 1.711,
               2.064, 2.492, 2.797, 3.467, 3.745],
           [0.000, 0.684, 0.856, 1.058, 1.316, 1.708,
               2.060, 2.485, 2.787, 3.450, 3.725],
           [0.000, 0.684, 0.856, 1.058, 1.315, 1.706,
               2.056, 2.479, 2.779, 3.435, 3.707],
           [0.000, 0.684, 0.855, 1.057, 1.314, 1.703,
               2.052, 2.473, 2.771, 3.421, 3.690],
           [0.000, 0.683, 0.855, 1.056, 1.313, 1.701,
               2.048, 2.467, 2.763, 3.408, 3.674],
           [0.000, 0.683, 0.854, 1.055, 1.311, 1.699,
               2.045, 2.462, 2.756, 3.396, 3.659],
           [0.000, 0.683, 0.854, 1.055, 1.310, 1.697,
               2.042, 2.457, 2.750, 3.385, 3.646],
           [0.000, 0.681, 0.851, 1.050, 1.303, 1.684,
               2.021, 2.423, 2.704, 3.307, 3.551],
           [0.000, 0.679, 0.848, 1.045, 1.296, 1.671,
               2.000, 2.390, 2.660, 3.232, 3.460],
           [0.000, 0.678, 0.846, 1.043, 1.292, 1.664,
               1.990, 2.374, 2.639, 3.195, 3.416],
           [0.000, 0.677, 0.845, 1.042, 1.290, 1.660,
               1.984, 2.364, 2.626, 3.174, 3.390],
           [0.000, 0.675, 0.842, 1.037, 1.282, 1.646, 1.962, 2.330, 2.581, 3.098, 3.300]]


mechanismName = ["Parabolic", "Valensi Barrier", "Ginstling Brounsthein", "Zander", "Linear Growth",
                 "Cylindrical", "Spherical", "Avrami Erofeev", "Avrami Erofeev", "Avrami Erofeev",
                 "Avrami Erofeev", "Mampel Power", "Mampel Power", "Mampel Power", "First Order Reaction", "One and Half Order", "Second Order"]


F_Table = [[161.4476, 199.5000, 215.7073, 224.5832, 230.1619, 233.9860, 236.7684, 238.8827, 240.5433, 241.8817, 243.9060, 245.9499,	248.0131, 249.0518, 250.0951, 251.1432, 252.1957, 253.2529, 254.3144],
           [18.5128, 19.0000,	19.1643,	19.2468,	19.2964,	19.3295,	19.3532,	19.3710,	19.3848,	19.3959,
            19.4125,	19.4291,	19.4458,	19.4541,	19.4624,	19.4707,	19.4791,	19.4874,	19.4957],
           [10.1280, 9.5521,	9.2766,	9.1172,	9.0135,	8.9406,	8.8867,	8.8452,	8.8123,	8.7855,
            8.7446,	8.7029,	8.6602,	8.6385,	8.6166,	8.5944,	8.5720,	8.5494,	8.5264],
           [7.7086, 6.9443,	6.5914,	6.3882,	6.2561,	6.1631,	6.0942,	6.0410,	5.9988,	5.9644,
               5.9117,	5.8578,	5.8025,	5.7744,	5.7459,	5.7170,	5.6877,	5.6581,	5.6281],
           [6.6079, 5.7861,	5.4095,	5.1922,	5.0503,	4.9503,	4.8759,	4.8183,	4.7725,	4.7351,
               4.6777,	4.6188,	4.5581,	4.5272,	4.4957,	4.4638,	4.4314,	4.3985,	4.365],
           [5.9874, 5.1433,	4.7571,	4.5337,	4.3874,	4.2839,	4.2067,	4.1468,	4.0990,	4.0600,
               3.9999,	3.9381,	3.8742,	3.8415,	3.8082,	3.7743,	3.7398,	3.7047,	3.6689],
           [5.5914, 4.7374,	4.3468,	4.1203,	3.9715,	3.8660,	3.7870,	3.7257,	3.6767,	3.6365,
               3.5747,	3.5107,	3.4445,	3.4105,	3.3758,	3.3404,	3.3043,	3.2674,	3.2298],
           [5.3177, 4.4590,	4.0662,	3.8379,	3.6875,	3.5806,	3.5005,	3.4381,	3.3881,	3.3472,
               3.2839,	3.2184,	3.1503,	3.1152,	3.0794,	3.0428,	3.0053,	2.9669,	2.9276],
           [5.1174, 4.2565,	3.8625,	3.6331,	3.4817,	3.3738,	3.2927,	3.2296,	3.1789,	3.1373,
               3.0729,	3.0061,	2.9365,	2.9005,	2.8637,	2.8259,	2.7872,	2.7475,	2.7067],
           [4.9646, 4.1028,	3.7083,	3.4780,	3.3258,	3.2172,	3.1355,	3.0717,	3.0204,	2.9782,
               2.9130,	2.8450,	2.7740,	2.7372,	2.6996,	2.6609,	2.6211,	2.5801,	2.537],
           [4.8443, 3.9823,	3.5874,	3.3567,	3.2039,	3.0946,	3.0123,	2.9480,	2.8962,	2.8536,
               2.7876,	2.7186,	2.6464,	2.6090,	2.5705,	2.5309,	2.4901,	2.4480,	2.4045],
           [4.7472, 3.8853,	3.4903,	3.2592,	3.1059,	2.9961,	2.9134,	2.8486,	2.7964,	2.7534,
               2.6866,	2.6169,	2.5436,	2.5055,	2.4663,	2.4259,	2.3842,	2.3410,	2.2962],
           [4.6672, 3.8056,	3.4105,	3.1791,	3.0254,	2.9153,	2.8321,	2.7669,	2.7144,	2.6710,
               2.6037,	2.5331,	2.4589,	2.4202,	2.3803,	2.3392,	2.2966,	2.2524,	2.2064],
           [4.6001, 3.7389,	3.3439,	3.1122,	2.9582,	2.8477,	2.7642,	2.6987,	2.6458,	2.6022,
               2.5342,	2.4630,	2.3879,	2.3487,	2.3082,	2.2664,	2.2229,	2.1778,	2.1307],
           [4.5431, 3.6823,	3.2874,	3.0556,	2.9013,	2.7905,	2.7066,	2.6408,	2.5876,	2.5437,
               2.4753,	2.4034,	2.3275,	2.2878,	2.2468,	2.2043,	2.1601,	2.1141,	2.065],
           [4.4940, 3.6337,	3.2389,	3.0069,	2.8524,	2.7413,	2.6572,	2.5911,	2.5377,	2.4935,
               2.4247,	2.3522,	2.2756,	2.2354,	2.1938,	2.1507,	2.1058,	2.0589,	2.0096],
           [4.4513, 3.5915,	3.1968,	2.9647,	2.8100,	2.6987,	2.6143,	2.5480,	2.4943,	2.4499,
               2.3807,	2.3077,	2.2304,	2.1898,	2.1477,	2.1040,	2.0584,	2.0107,	1.9604],
           [4.4139, 3.5546,	3.1599,	2.9277,	2.7729,	2.6613,	2.5767,	2.5102,	2.4563,	2.4117,
               2.3421,	2.2686,	2.1906,	2.1497,	2.1071,	2.0629,	2.0166,	1.9681,	1.9168],
           [4.3807, 3.5219,	3.1274,	2.8951,	2.7401,	2.6283,	2.5435,	2.4768,	2.4227,	2.3779,
               2.3080,	2.2341,	2.1555,	2.1141,	2.0712,	2.0264,	1.9795,	1.9302,	1.8780],
           [4.3512, 3.4928,	3.0984,	2.8661,	2.7109,	2.5990,	2.5140,	2.4471,	2.3928,	2.3479,
               2.2776,	2.2033,	2.1242,	2.0825,	2.0391,	1.9938,	1.9464,	1.8963,	1.843],
           [4.3248, 3.4668,	3.0725,	2.8401,	2.6848,	2.5727,	2.4876,	2.4205,	2.3660,	2.3210,
               2.2504,	2.1757,	2.0960,	2.0540,	2.0102,	1.9645,	1.9165,	1.8657,	1.8117],
           [4.3009, 3.4434,	3.0491,	2.8167,	2.6613,	2.5491,	2.4638,	2.3965,	2.3419,	2.2967,
               2.2258,	2.1508,	2.0707,	2.0283,	1.9842,	1.9380,	1.8894,	1.8380,	1.7831],
           [4.2793, 3.4221,	3.0280,	2.7955,	2.6400,	2.5277,	2.4422,	2.3748,	2.3201,	2.2747,
               2.2036,	2.1282,	2.0476,	2.0050,	1.9605,	1.9139,	1.8648,	1.8128,	1.7570],
           [4.2597, 3.4028,	3.0088,	2.7763,	2.6207,	2.5082,	2.4226,	2.3551,	2.3002,	2.2547,
               2.1834,	2.1077,	2.0267,	1.9838,	1.9390,	1.8920,	1.8424,	1.7896,	1.7330],
           [4.2417, 3.3852,	2.9912,	2.7587,	2.6030,	2.4904,	2.4047,	2.3371,	2.2821,	2.2365,
               2.1649,	2.0889,	2.0075,	1.9643,	1.9192,	1.8718,	1.8217,	1.7684,	1.711],
           [4.2252, 3.3690,	2.9752,	2.7426,	2.5868,	2.4741,	2.3883,	2.3205,	2.2655,	2.2197,
               2.1479,	2.0716,	1.9898,	1.9464,	1.9010,	1.8533,	1.8027,	1.7488,	1.6906],
           [4.2100, 3.3541,	2.9604,	2.7278,	2.5719,	2.4591,	2.3732,	2.3053,	2.2501,	2.2043,
               2.1323,	2.0558,	1.9736,	1.9299,	1.8842,	1.8361,	1.7851,	1.7306,	1.6717],
           [4.1960, 3.3404,	2.9467,	2.7141,	2.5581,	2.4453,	2.3593,	2.2913,	2.2360,	2.1900,
               2.1179,	2.0411,	1.9586,	1.9147,	1.8687,	1.8203,	1.7689,	1.7138,	1.6541],
           [4.1830, 3.3277,	2.9340,	2.7014,	2.5454,	2.4324,	2.3463,	2.2783,	2.2229,	2.1768,
               2.1045,	2.0275,	1.9446,	1.9005,	1.8543,	1.8055,	1.7537,	1.6981,	1.6376],
           [4.1709, 3.3158,	2.9223,	2.6896,	2.5336,	2.4205,	2.3343,	2.2662,	2.2107,	2.1646,
               2.0921,	2.0148,	1.9317,	1.8874,	1.8409,	1.7918,	1.7396,	1.6835,	1.622],
           [4.0847, 3.2317,	2.8387,	2.6060,	2.4495,	2.3359,	2.2490,	2.1802,	2.1240,	2.0772,
               2.0035,	1.9245,	1.8389,	1.7929,	1.7444,	1.6928,	1.6373,	1.5766,	1.5089],
           [4.0012, 3.1504,	2.7581,	2.5252,	2.3683,	2.2541,	2.1665,	2.0970,	2.0401,	1.9926,
               1.9174,	1.8364,	1.7480,	1.7001,	1.6491,	1.5943,	1.5343,	1.4673,	1.3893],
           [3.9201, 3.0718,	2.6802,	2.4472,	2.2899,	2.1750,	2.0868,	2.0164,	1.9588,	1.9105,
               1.8337,	1.7505,	1.6587,	1.6084,	1.5543,	1.4952,	1.4290,	1.3519,	1.2539],
           [3.8415, 2.9957,	2.6049,	2.3719,	2.2141,	2.0986,	2.0096,	1.9384,	1.8799,	1.8307,	1.7522,	1.6664,	1.5705,	1.5173,	1.4591,	1.3940,	1.3180,	1.2214,	1.0000]]


def getMechNumber(tVal, fVal, remEq, size):

    for row in range(0, 17):
        if remEq[row] == False:
            tVal[row] = 10000
            fVal[row] = 10000

    df = size + size - 2 - 1

    for row in range(0, 17):
        if (tVal[row] > T_Table[df][6]):
            tVal[row] = 10000

        if (fVal[row] > F_Table[size-2][size-2]):
            fVal[row] = 10000

    diff = 100000
    mechNumber = -1

    for row in range(0, 17):
        if tVal[row] < 10000 and fVal[row] < 10000 and (fVal[row]-tVal[row]) < diff:
            mechNumber = row
            diff = fVal[row]-tVal[row]

    return mechNumber+1


def getValidMech(maxR, eq, remEq, coRelationCof):

    for row in range(0, 17):
        if maxR < coRelationCof[row]:
            maxR = coRelationCof[row]

    maxRCount = 0
    for row in range(0, 17):
        if maxR == coRelationCof[row]:
            maxRCount = maxRCount+1
            eq.append(row)

    for row in range(0, maxRCount):
        if eq[row] >= 0 and eq[row] <= 3:
            for col in range(0, 4):
                remEq[col] = True
        elif eq[row] >= 4 and eq[row] <= 6:
            for col in range(4, 7):
                remEq[col] = True
        elif eq[row] >= 7 and eq[row] <= 10:
            for col in range(7, 11):
                remEq[col] = True
        elif eq[row] >= 11 and eq[row] <= 13:
            for col in range(11, 14):
                remEq[col] = True
        else:
            for col in range(14, 17):
                remEq[col] = True

    return (maxRCount)


def calculationOfTest(modifiedAlpha, size, alpha, tVal, fVal):

    for row in range(0, 17):
        sumOfModifiedAlpha = 0
        sumOfAlpha = 0

        for col in range(0, size):
            sumOfAlpha = sumOfAlpha + alpha[col]
            sumOfModifiedAlpha = sumOfModifiedAlpha + modifiedAlpha[col][row]

        meanOfAlpha = sumOfAlpha/size
        meanOfModifiedAlpha = sumOfModifiedAlpha/size

        avgOfAlpha = 0.0
        avgOfModifiedAlpha = 0.0

        for col in range(0, size):
            avgOfAlpha = avgOfAlpha + \
                ((alpha[col]-meanOfAlpha)*(alpha[col]-meanOfAlpha))

            avgOfModifiedAlpha = avgOfModifiedAlpha + \
                ((modifiedAlpha[col][row]-meanOfModifiedAlpha)
                 * (modifiedAlpha[col][row]-meanOfModifiedAlpha))

        # F test calculation
        fval = avgOfModifiedAlpha/avgOfAlpha
        if fval < 1 and fval != 0:
            fval = 1/fval
        fVal.append(round(fval, 5))

        # T test calculation
        dof = (2*size)-2

        variance = ((size-1)*(avgOfAlpha + avgOfModifiedAlpha))/(dof*size)

        sd = math.sqrt(abs(variance))

        tval = abs((meanOfAlpha-meanOfModifiedAlpha)/(sd*math.sqrt(2/size)))
        tVal.append(round(tval, 5))


def modifiedAlphaUsingNewtonMethod(fx, f1x, size, alpha, modifiedAlpha):

    for row in range(0, size):
        x = alpha[row]
        cond = True
        while cond == True:
            fxVal = eval(fx)
            f1xVal = eval(f1x)
            x1 = x-(fxVal/f1xVal)
            if abs(x1-x) < 0.00005:
                cond = False
            else:
                x = x1

        modifiedAlpha[row][1] = round(abs(x), 5)


def calculationOfModifiedAlpha(modifiedGAlpha, modifiedAlpha, size, alpha):
    equations = [str(x) for x in alphaEq.split(',')]
    for row in range(0, 17):

        for col in range(0, size):
            x = modifiedGAlpha[row][col]
            val = eval(equations[row])
            val = abs(val)
            modifiedAlpha[col][row] = round(val, 5)

    fx = "1-((2/3)*x)-((1-x)**(2/3))"
    f1x = "-(2/3)-(2/3)*((1-x)**(-1/3))"
    modifiedAlphaUsingNewtonMethod(fx, f1x, size, alpha, modifiedAlpha)
    fx = "x+(1-x)*math.log(1-x)"
    f1x = "-math.log(1-x)"
    modifiedAlphaUsingNewtonMethod(fx, f1x, size, alpha, modifiedAlpha)


def calculationOfModifiedGAlpha(gAlpha, modifiedGAlpha, timePeriods, regressionEq, size):

    for row in range(0, 17):
        for col in range(0, size):
            x = timePeriods[col]
            val = eval(regressionEq[row])
            modifiedGAlpha[row][col] = abs(round(val, 5))


def getSlope(ind, gAlpha, timePeriods, size):
    sumX = 0
    sumY = 0
    sumXY = 0
    sumX2 = 0
    for col in range(0, size):
        sumX = sumX + timePeriods[col]
        sumY = sumY + gAlpha[ind][col]
        sumXY = sumXY + (gAlpha[ind][col]*timePeriods[col])
        sumX2 = sumX2 + (timePeriods[col]*timePeriods[col])

    slope = (size*sumXY - (sumX * sumY))/(size*sumX2 - (sumX * sumX))

    return slope


def calculationOfLeastRegLine(gAlpha, timePeriods, regressionEq, size):

    for row in range(0, 17):
        slope = getSlope(row, gAlpha, timePeriods, size)
        meanY = int(sum(gAlpha[row])/size)
        meanX = int(sum(timePeriods)/size)

        const = meanY - (slope * meanX)

        eq = ""
        c = "{:.5f}".format(const)
        eq += c
        s = "{:.5f}".format(slope)
        if (s[0] != '-'):
            eq += '+'

        eq += s
        eq += '*x'
        regressionEq.append(eq)


def calculationOfCorelationCoeff(gAlpha, timePeriods, coRelationCof, size):

    sumTime = 0
    sumGalpha = 0
    for row in range(0, 17):
        for col in range(0, size):
            sumGalpha = sumGalpha + gAlpha[row][col]
            sumTime = sumTime + timePeriods[col]

        meanGalpha = sumGalpha/size
        meanTime = sumTime/size
        sumX = 0.0
        sumXY = 0.0
        sumY = 0.0
        for col in range(0, size):
            sumXY = sumXY + ((gAlpha[row][col]-meanGalpha)
                             * (timePeriods[col]-meanTime))
            sumY = sumY + ((gAlpha[row][col]-meanGalpha)
                           * (gAlpha[row][col]-meanGalpha))
            sumX = sumX + ((timePeriods[col]-meanTime)
                           * (timePeriods[col]-meanTime))

        sumVal = math.sqrt(sumX*sumY)

        if sumVal != 0:
            r = round((sumXY/sumVal), 2)
            coRelationCof.append(r)

        else:
            r = round(sumXY, 2)
            coRelationCof.append(r)


def calculationOfGAlpha(gAlpha, alpha, size):
    equations = [str(x) for x in equation.split(',')]
    for row in range(0, 17):
        for col in range(0, size):
            try:
                x = alpha[col]
                val = eval(equations[row])
                gAlpha[row][col] = round(abs(val), 5)
            except ValueError:
                gAlpha[row][col] = 0


def calculationOfAlpha(finalWeights, timePeriods, alpha, initialWeight):
    for item in finalWeights:
        alphaVal = float(abs((initialWeight-item)/initialWeight))
        alpha.append(round(alphaVal, 5))


def dataAnalysisHelper(sizeOfData, initialWeightOfData, finalWeightsOfData, timePeriodsofData, G_Alpha):
    # Taking Inputs
    initialWeight = float(initialWeightOfData)
    size = int(sizeOfData)
    finalWeights = []
    timePeriods = []
    alpha = []
    coRelationCof = []
    regressionEq = []
    tVal = []
    fVal = []

    finalWeights = [float(x) for x in finalWeightsOfData.split(',')]
    # finalList = [line.split(',') for line in finalWeightsOfData.readlines()]
    # for i in range(0, size):
    #     ele = finalList[0][i]
    #     finalWeights.append(float(ele))

    timePeriods = [int(x) for x in timePeriodsofData.split(',')]
    # timeList = [line.split(',') for line in timePeriodsofData.readlines()]
    # for i in range(0, size):
    #     ele = timeList[0][i]
    #     timePeriods.append(float(ele))

    # 1. Calculation of alpha
    calculationOfAlpha(finalWeights, timePeriods, alpha, initialWeight)

    # 2. Calculation of GAlpha
    gAlpha = [[0 for i in range(size)] for j in range(17)]
    calculationOfGAlpha(gAlpha, alpha, size)

    # 3. Calculation of corelation coefficient
    calculationOfCorelationCoeff(gAlpha, timePeriods, coRelationCof, size)

    # 4. Function to find the least regression line
    calculationOfLeastRegLine(gAlpha, timePeriods, regressionEq, size)

    # 5. Function to find modified GAlpha
    modifiedGAlpha = [[0 for i in range(size)] for j in range(17)]
    calculationOfModifiedGAlpha(
        gAlpha, modifiedGAlpha, timePeriods, regressionEq, size)

    # 6. Function to find modified Alpha
    modifiedAlpha = [[0 for i in range(17)] for j in range(size)]
    calculationOfModifiedAlpha(modifiedGAlpha, modifiedAlpha, size, alpha)

    # 6. Function to find number of mechanisms for which we will proceed further
    maxR = 0
    eq = []
    remEq = [False] * 17
    df = size + size - 2 - 1
    maxRCount = getValidMech(maxR, eq, remEq, coRelationCof)

    # 7. Function to find T Distribution  and F Distribution value
    calculationOfTest(modifiedAlpha, size, alpha, tVal, fVal)

    # 8. find Prevaling Mechanism
    count = 0
    mechNumber = -1
    for i in range(0, 17):
        if coRelationCof[i] == 1:
            count = count+1
            mechNumber = i+1

    if count != 1:
        mechNumber = getMechNumber(tVal, fVal, remEq, size)

        G_Alpha = gAlpha[mechNumber]
        print(mechNumber)

    return mechNumber


def dataAnalysis(request):
    return render(request, "analysis.html")


def Analysis(request):

    if request.method == "GET":
        reaction = request.GET.get("reaction")
        temperature = request.GET.get("temp")
        reactionData = collection.find()
        finalWeights = []
        MechNumber = 0
        G_Alpha = []
        timePeriods = []

        check = False

        for item in reactionData:
            if item["reaction"] == reaction and item["temperature"] == temperature:
                check = True
                size = item["size"]
                initialWeight = item["initialWeight"]
                finalWeights = item["finalWeights"]
                timePeriods = item["timePeriods"]
                G_Alpha = item["G_Alpha"]
                MechNumber = item["MechNumber"]
                break

        if check == True:
            if MechNumber != 0:

                context = {'mech': MechNumber}
                return render(request, "analysisResult.html", context)
            else:
                MechNumber = dataAnalysisHelper(
                    size, initialWeight, finalWeights, timePeriods, G_Alpha)
                filter = {'reaction': reaction, 'temperature': temperature}
                newValues = {
                    "$set": {"G_Alpha": G_Alpha, "MechNumber": MechNumber}}
                collection.update_one(filter, newValues)
                context = {'mech': MechNumber}
                return render(request, "analysis.html", context)

        else:
            context = {'mech': 0}
            return render(request, "analysis.html", context)

