g = 9.80665
#g=1
r=16.59/100
r_delta=0.05/100
t_experimental=[[32.03,29.08,30.25],[2,2,2]]
t_max=[32.03,2]
t_min=[29.08,1]
t=[]
t_delta=[]
pi=3.1415926
for i in range(len(t_experimental)):
    temp=0
    # print(sum(t_experimental[i])/len(t_experimental[i]))
    t.append(sum(t_experimental[i])/len(t_experimental[i]))
    t_delta.append((t_max[i]-t_min[i])/2+0.02)
n=50
m_experimental=[8.4/g,2]
m_max=[8.5/g,2]
m_min=[8.3/g,1]
m=[469.84/1000,1] #weight
m_delta=[]
for i in range(len(m_experimental)):
    print(m_max[i],m_min[i],(m_max[i]+m_min[i])/2)
    m.append((m_max[i]+m_min[i])/2)
    m_delta.append((m_max[i]-m_min[i])/2)
w=[]
w_delta=[]
for i in m_experimental:
    print('m',i,i*g)
    w.append(i*g)
for i in m_delta:
    w_delta.append(i*g)
f=[]
f_delta=[]

for i in range(len(m_experimental)):
    f.append(4*pi**2*m[i]*r*n**2/t[i]**2)
    f_delta.append((r_delta/r+2*t_delta[i]/t[i])*f[i])
print("t",t)
for i in range(len(f)):
    print(i+1,"f",f[i],"f_delta",f_delta[i],"f_min",(f[i]-f_delta[i]),"f_max",
          (f[i]+f_delta[i]),)
    print("w",w[i],"w_delta",w_delta[i],"w min",(w[i]-w_delta[i]),"w max",(w[i]+w_delta[i]))
# print("f",f,"f_delta",f_delta)
# print("w",w,"w_delta",w_delta)

print('m',m,m_delta)
print("r",r)

