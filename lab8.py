from math import *
import statistics
import pandas
M_big=240*0.001
m_small=65.9*0.001
g = 9.80665
l=29.46*0.01
angle=[25.03,24.63,25.03,24.82,25.01,23.2,24.78,23.53,23.32,25.51]
h=[]
for i in range(len(angle)):
    h.append(l*(1-cos(radians(angle[i]))))
print('h',h)
h_mean=sum(h)/len(h)
print('h_mean',h_mean)

v_method1=[]
for i in range(len(angle)):
    v_method1.append((1+M_big/m_small)*sqrt(2*g*h[i]))
print('v_method1',v_method1)

v_method1_mean=sum(v_method1)/len(v_method1)
print('v_method1_mean',v_method1_mean)

v_method1_uncertainty=(max(v_method1)-min(v_method1))*2/(max(v_method1)+min(v_method1))
print('v_method1_uncertainty',v_method1_uncertainty)


H_big=81.86*0.01
R_big=[130.62,130.23,133.19,135.73,125.71,130.43,130.21,131.69,129.32,131.73]
for i in range(len(R_big)):
    R_big[i]/=100


v_method3=[]
for i in range(len(R_big)):
    v_method3.append(R_big[i]*sqrt(g/2/H_big))
print('v_method3',v_method3)
v_method3_mean=sum(v_method3)/len(v_method3)
print('v_method3_mean',v_method3_mean)


v_method3_uncertainty=(max(v_method3)-min(v_method3))*2/(max(v_method3)+min(v_method3))
print('v_method3_uncertainty',v_method3_uncertainty)




v_method1_SD=statistics.stdev(v_method1)
v_method3_SD=statistics.stdev(v_method3)
h_SD=statistics.stdev(h)
print('v_method1_SD',v_method1_SD)
print('v_method3_SD',v_method3_SD)
print("error bar 1",v_method1_mean-v_method1_mean*v_method1_uncertainty,v_method1_mean,v_method1_mean+v_method1_mean*v_method1_uncertainty)
print("error bar 3",v_method3_mean-v_method3_mean*v_method3_uncertainty,v_method3_mean,v_method3_mean+v_method3_mean*v_method3_uncertainty)
print("error bar 1",v_method1_mean-v_method1_SD,v_method1_mean,v_method1_mean+v_method1_SD)
print("error bar 3",v_method3_mean-v_method3_SD,v_method3_mean,v_method3_mean+v_method3_SD)

# print(sin(radians(30)))
# print(radians(180))
# dic={}
# dic['angle']=angle
# dic['h method1']=h
# dic['v_method1']=v_method1
# dic["Range"]=R_big
# dic['v_method3']=v_method3
# df=pandas.DataFrame(dic)
# df.to_csv('test.cvs')
# print(df)
