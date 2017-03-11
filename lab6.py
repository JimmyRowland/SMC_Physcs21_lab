g = 9.80665
r=1
r_delta=0.1
t_experimental=[[2,2,2],[2,2,2]]
t_max=[2,2]
t_min=[1,1]
t=[]
t_delta=[]
pi=3.1415926
for i in range(len(t_experimental)):
    temp=0
    # print(sum(t_experimental[i])/len(t_experimental[i]))
    t.append(sum(t_experimental[i])/len(t_experimental[i]))
    t_delta.append((t_max[i]-t_min[i])/2)
n=50
m_experimental=[[1],[2]]
m_max=[2,2]
m_min=[1,1]
m=[]
m_delta=[]
for i in range(len(m_experimental)):
    m.append((m_max[i]+m_min[i])/2)
    m_delta.append((m_max[i]-m_min[i])/2)
w=[]
w_delta=[]
for i in m:
    w.append(i*g)
for i in m_delta:
    w_delta.append(i*g)
f=[]
f_delta=[]

for i in range(len(m_experimental)):
    f.append(4*pi**2*m[i]*r*n**2/t[i]**2)
    f_delta.append(r_delta/r+2*t_delta[i]/t[i])
print("t",t)
for i in range(len(f)):
    print(i+1,"f",f[i],"f_delta",f_delta[i],"f_min",(f[i]-f_delta[i])/2,"f_max",
          (f[i]+f_delta[i])/2,)
    print("w",w[i],"w_delta",w_delta[i],"w min",(w[i]-w_delta[i])/2,"w max",(w[i]+w_delta[i])/2)
# print("f",f,"f_delta",f_delta)
# print("w",w,"w_delta",w_delta)





