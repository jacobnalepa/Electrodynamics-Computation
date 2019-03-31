# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 16:17:35 2019

@author: jacob
"""

#This program calculates the scalar potential everywhere in space for three
#spherical charge distributions.

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#Coefficients for a hallow sphere with a potential on its surface defined by
#sqrt(cos(theta/2))
A0 = 4/5
A1 = 4/15
A2 = -4/39
A3 = 196/3315
A4 = -44/1105
A5 = 484/16529
A6 = -836/36975

#Defines a meshgrid for variables r and theta
theta = np.linspace(0, np.pi, 100)
r1 = np.linspace(0, 1, 100)
r2 = np.linspace(1, 2, 100)
r3 = np.linspace(2, 3, 100)
R1, T = np.meshgrid(r1, theta)
R2, T = np.meshgrid(r2, theta)
R3, T = np.meshgrid(r3, theta)

#Legendre polynomials
P0 = 1
P1 = np.cos(T)
P2 = (0.5*(3.*np.cos(T)**2-1))
P3 = (0.5*(5*np.cos(T)**3-3*np.cos(T)))
P4 = (0.125*(35*np.cos(T)**4-30*np.cos(T)**2+3))
P5 = (0.125*(63*np.cos(T)**5-70*np.cos(T)**3+15*np.cos(T)))
P6 = (0.0625*(231*np.cos(T)**6-315*np.cos(T)**4+105*np.cos(T)**2-5))
P7 = (0.0625*(429*np.cos(T)**7-693*np.cos(T)**5+315*np.cos(T)**3-35*np.cos(T)))
P8 = (.0078125*(6435*np.cos(T)**8-12012*np.cos(T)**6+6930*np.cos(T)**4-1260*np.cos(T)**2+35))
P9 = .0078125*(12155*np.cos(T)**9-25740*np.cos(T)**7+18018*np.cos(T)**5-4620*np.cos(T)**3+315*np.cos(T))
P10 = .00390625*(46189*np.cos(T)**10-109395*np.cos(T)**8+90090*np.cos(T)**6-30030*np.cos(T)**4+3465*np.cos(T)**2-63)
P11 = .00390625*(88179*np.cos(T)**11-230945*np.cos(T)**9+218790*np.cos(T)**7-90090*np.cos(T)**5+15015*np.cos(T)**3-693*np.cos(T))
P12 = (1/1024)*(676039*np.cos(T)**12-1939938*np.cos(T)**10+2078505*np.cos(T)**8-1021020*np.cos(T)**6+225225*np.cos(T)**4-18018)
P13 = (1/1024)*(1300075*np.cos(T)**13-4056234*np.cos(T)**11+4849845*np.cos(T)**9-2771340*np.cos(T)**7+765765*np.cos(T)**5-90090*np.cos(T)**3+3003*np.cos(T))

#Calculates the potential inside (ZA1) and outside (ZA2) the sphere
ZA1 = A0*P0+A1*R1*P1+A2*R1**2*P2+A3*R1**3*P3+A4*R1**4*P4+A5*R1**5*P5+A6*R1**6*P6
ZA2 = A0*(1/R2)*P0+A1*(1/R2)**2*P1+A2*(1/R2)**3*P2+A3*(1/R2)**4*P3+A4*(1/R2)**5*P4+A5*(1/R2)**6*P5+A6*(1/R2)**7*P6

#Converts r,theta into x,y
X1,Y1 = R1*np.cos(T), R1*np.sin(T)
X2, Y2 = R2*np.cos(T), R2*np.sin(T)
X3, Y3 = R3*np.cos(T), R3*np.sin(T)

#Plots the potential
fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X1, Y1, ZA1, cmap=plt.cm.YlGnBu_r)
ax.plot_surface(X2, Y2, ZA2, cmap=plt.cm.YlGnBu_r)

#labels the plot
ax.set_title(r'$\Phi$ from question 1')
ax.set_xlabel(r'rcos($\theta$)')
ax.set_ylabel(r'rsin($\theta$)')
ax.set_zlabel(r'$\Phi$')

#Coefficients for a hallow sphere with a surface charge density defined by
#cosh(cos(theta))
B0 = np.sinh(1)
B1 = 0
B2 = (1/2)*(np.e-7/np.e)
B3 = 0
B4 = (1/2)*(36*np.e-266/np.e)
B5 = 0
B6 = (1/2)*(3655*np.e-27007/np.e)

#Calculates the potential inside (ZB1) and outside (ZB2) the sphere
ZB1 = B0*P0+B1*R1*P1+B2*R1**2*P2+B3*R1**3*P3+B4*R1**4*P4+B5*R1**5*P5+B6*R1**6*P6
ZB2 = B0*(1/R2)*P0+B1*(1/R2)**2*P1+B2*(1/R2)**3*P2+B3*(1/R2)**4*P3+B4*(1/R2)**5*P4+B5*(1/R2)**6*P5+B6*(1/R2)**7*P6

#Plots the potential
fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X1, Y1, ZB1, cmap=plt.cm.YlGnBu_r)
ax.plot_surface(X2, Y2, ZB2, cmap=plt.cm.YlGnBu_r)

#labels the plot
ax.set_title(r'$\Phi$ from question 2')
ax.set_xlabel(r'rcos($\theta$)')
ax.set_ylabel(r'rsin($\theta$)')
ax.set_zlabel(r'$\Phi$')

#Coefficients for a hallow sphere of radius 1 with a potential V from theta=0
#to theta=pi/2 and potential zero from theta=pi/2 to theta=pi
C0 = 1/2
C1 = 3/4
C2 = 0
C3 = -7/16
C4 = 0
C5 = 11/32
C6 = 0
C7 = -75/256
C8 = 0
C9 = 133/512
C10 = 0
C11 = -483/2048
C12 = 0
C13 = 891/4096

#Coefficients for a hallow sphere of radius 2 with a potential 0 from theta=0
#to theta=pi/2 and potential V from theta=pi/2 to theta=pi
D0 = 1/2
D1 = -3/4
D2 = 0
D3 = 7/16
D4 = 0
D5 = -11/32
D6 = 0
D7 = 75/256
D8 = 0
D9 = -133/512
D10 = 0
D11 = 483/2048
D12 = 0
D13 = -891/4096

#Calculates the potential inside (ZC1) and outside (ZC2) the sphere of radius 1
#Calculates the potential inside (ZD1) and outside (ZD2) the sphere of radius 2
#Calculates the total potential between the two spheres
ZC1 = C0*R1*P0+C1*R1**2*P1+C2*R1**3*P2+C3*R1**4*P3+C4*R1**5*P4+C5*R1**6*P5+C6*R1**7*P6+C7*R1**8*P7+C8*R1**9*P8+C9*R1**10*P9+C10*R1**11*P10+C11*R1**12*P11+C12*R1**13*P12+C13*R1**14*P13
ZC2 = C0*(1/R2)*P0+C1*(1/R2)**2*P1+C2*(1/R2)**3*P2+C3*(1/R2)**4*P3+C4*(1/R2)**5*P4+C5*(1/R2)**6*P5+C6*(1/R2)**7*P6+C7*(1/R2)**8*P7+C8*(1/R2)**9*P8+C9*(1/R2)**10*P9+C10*(1/R2)**11*P10+C11*(1/R2)**12*P11+C12*(1/R2)**13*P12+C13*(1/R2)**14*P13
ZD1 = D0*P0+D1*(R2/2)*P1+D2*(R2/2)**2*P2+D3*(R2/2)**3*P3+D4*(R2/2)**4*P4+D5*(R2/2)**5*P5+D6*(R2/2)**6*P6+D7*(R2/2)**7*P7+D8*(R2/2)**8*P8+D9*(R2/2)**9*P9+D10*(R2/2)**10*P10+D11*(R2/2)**11*P11+D12*(R2/2)**12*P12+D13*(R2/2)**13*P13
ZD2 = D0*(2/R3)*P0+D1*(2/R3)**2*P1+D2*(2/R3)**3*P2+D3*(2/R3)**4*P3+D4*(2/R3)**5*P4+D5*(2/R3)**6*P5+D6*(2/R3)**7*P6+D7*(2/R3)**8*P7+D8*(2/R3)**9*P8+D9*(2/R3)**10*P9+D10*(2/R3)**11*P10+D11*(2/R3)**12*P11+D12*(2/R3)**13*P12+D13*(2/R3)**14*P13
Ztotal = ZC2+ZD1

#Plots the potential between the sphere of radius 1 and radius 2
fig = plt.figure(3)
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X2, Y2, Ztotal, cmap=plt.cm.YlGnBu_r)

#labels the plot
ax.set_title(r'$\Phi$ from question 3')
ax.set_xlabel(r'rcos($\theta$)')
ax.set_ylabel(r'rsin($\theta$)')
ax.set_zlabel(r'$\Phi$')

#fig = plt.figure(4)
#ax = fig.add_subplot(111, projection='3d')
#ax.plot_surface(X2, Y2, ZD1, cmap=plt.cm.YlGnBu_r)
#ax.plot_surface(X3, Y3, ZD2, cmap=plt.cm.YlGnBu_r)

#ax.set_title(r'$\Phi$ from question 3')
#ax.set_xlabel(r'rcos($\theta$)')
#ax.set_ylabel(r'rsin($\theta$)')