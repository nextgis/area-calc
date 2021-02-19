import math

#WGS84 params
mSemiMajor = 6378137.0
mSemiMinor = 6356752.3142

M_PI = 3.14159265358979323846
a2 = mSemiMajor * mSemiMajor
#e2 = 1 - (a2 / (mSemiMinor * mSemiMinor)) - bad one from QGIS 2.x https://github.com/qgis/QGIS/commit/297dbe0786d30b7b05462c8dac49b51f13175a19
e2 = 1 - ((mSemiMinor * mSemiMinor) / a2)

m_TwoPI = M_PI + M_PI

e4 = e2 * e2
e6 = e4 * e2

m_AE = a2 * ( 1 - e2 )

m_QA = ( 2.0 / 3.0 ) * e2
m_QB = ( 3.0 / 5.0 ) * e4
m_QC = ( 4.0 / 7.0 ) * e6

m_QbarA = -1.0 - ( 2.0 / 3.0 ) * e2 - ( 3.0 / 5.0 ) * e4  - ( 4.0 / 7.0 ) * e6
m_QbarB = ( 2.0 / 9.0 ) * e2 + ( 2.0 / 5.0 ) * e4  + ( 4.0 / 7.0 ) * e6
m_QbarC = -1 * ( 3.0 / 25.0 ) * e4 - ( 12.0 / 35.0 ) * e6
m_QbarD = ( 4.0 / 49.0 ) * e6

def getQ(x):
  sinx = math.sin(x)
  sinx2 = sinx * sinx

  return sinx *( 1 + sinx2 *( m_QA + sinx2 *( m_QB + sinx2 * m_QC)))

m_Qp = getQ( M_PI / 2 )
m_E = 4 * M_PI * m_Qp * m_AE
if m_E < 0.0:
    m_E = -m_E

def DEG2RAD(x):
    return x*M_PI/180

def getQbar(x):
  cosx = math.cos(x)
  cosx2 = cosx * cosx

  return cosx *(m_QbarA + cosx2 *(m_QbarB + cosx2 *(m_QbarC + cosx2 * m_QbarD)))

def calculate_area(points):
    thresh = 1e-6
    area = 0.0

    x2 = DEG2RAD(points[-1][0])
    y2 = DEG2RAD(points[-1][1])
    Qbar2 = getQbar(y2)

    for pnt in points:
        x1 = x2
        y1 = y2
        Qbar1 = Qbar2

        x2 = DEG2RAD(pnt[0])
        y2 = DEG2RAD(pnt[1])
        Qbar2 = getQbar( y2 )

        if (x1 > x2):
            while (x1 - x2 > M_PI):
                x2 += m_TwoPI
        elif (x2 > x1):
            while (x2 - x1 > M_PI):
                x1 += m_TwoPI

        dx = x2 - x1
        dy = y2 - y1
        if abs(dy) > thresh:
            area = area + dx * (m_Qp - ( Qbar2 - Qbar1 ) / dy)
        else:
            area = area + dx * (m_Qp - getQ( ( y1 + y2 ) / 2.0 ))

    area = area * m_AE
    if ((area) < 0.0):
        area = -area

    if (area > m_E):
        area = m_E
    if (area > m_E / 2):
        area = m_E - area

    return area

def output_debug(area):
    with open('debug.csv','w') as f_debug:
        f_debug.write('param;value\n')
        f_debug.write('mSemiMajor' + ';' + str(mSemiMajor) + '\n')
        f_debug.write('mSemiMinor' + ';' + str(mSemiMinor) + '\n')
        f_debug.write('M_PI' + ';' + str(M_PI) + '\n')
        f_debug.write('a2' + ';' + str(a2) + '\n')
        f_debug.write('e2' + ';' + str(e2) + '\n')
        f_debug.write('m_TwoPI' + ';' + str(m_TwoPI) + '\n')
        f_debug.write('m_AE' + ';' + str(m_AE) + '\n')
        f_debug.write('e6' + ';' + str(e6) + '\n')
        f_debug.write('m_QA' + ';' + str(m_QA) + '\n')
        f_debug.write('m_QB' + ';' + str(m_QB) + '\n')
        f_debug.write('m_QC' + ';' + str(m_QC) + '\n')
        f_debug.write('m_QbarA' + ';' + str(m_QbarA) + '\n')
        f_debug.write('m_QbarB' + ';' + str(m_QbarB) + '\n')
        f_debug.write('m_QbarC' + ';' + str(m_QbarC) + '\n')
        f_debug.write('m_QbarD' + ';' + str(m_QbarD) + '\n')
        f_debug.write('m_Qp' + ';' + str(m_Qp) + '\n')
        f_debug.write('m_E' + ';' + str(m_E) + '\n')
        f_debug.write('area' + ';' + str(area) + '\n')

def test_data():
    p0 = [51.82, 63.8]
    p1 = [43.48, 55.62]
    p2 = [75.38, 59.13]
    p3 = [51.82, 63.8]

    points = [p0,p1,p2,p3]

    return points

def areacalc(points):
    area = calculate_area(points) #730215205638.4752 - correct result of calculation
    #output_debug(area)

    return area
    