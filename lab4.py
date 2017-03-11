g = 9.80665
time_interval=1/6
m_glider = 1
m_added_to_glider =[0,0,0,100,100,100,100,200,200,200]
m2=[]
m1=[]
for x in range(10):
    m1.append(x+12)
    m2.append(m_glider+m_added_to_glider[x])
print("m1",m1,"\nm2",m2)
t_delta = 1
s=[[0,0.5,3,7,15,99],[],[],[],[],[],[],[],[],[]]
s_delta=[[],[],[],[],[],[],[],[],[],[]]
v_average=[[],[],[],[],[],[],[],[],[],[]]
for u in range(len(s)):

    for i in range(len(s[u])):
        if i==0 or i ==len(s[u])-1:
            s_delta[u].append(0)
            v_average[u].append(0)
        else:
            s_delta[u].append(s[u][i+1]-s[u][i-1])
            v_average[u].append(s_delta[u][i]/2/t_delta)
for i in range(10):
    print("group",i+1,"s_delta:",s_delta[i],"\nv_average",v_average[i])
a_max=[]
a_min=[]
a=[]
a_delta=[]
for u in v_average:
    max=0
    min=100000
    temp =0
    for i in range(1,len(u)-1):
        temp=u[i]/i/t_delta
        if temp >max:
            max = temp
        if temp < min:
            min = temp
    a_max.append(max)
    a_min.append(min)
    a.append((max+min)/2)
    a_delta.append((max - min) / 2)

print('a_max:',a_max,'\na_min:',a_min,'\na:',a,'\na_delta:',a_delta)
a_theoretical=[]
for i in range(10):
    a_theoretical.append(m1[i]*g/(m1[i]+m2[i]))
print('a_theoretical',a_theoretical)
for i in range(10):
    print(i+1,"a error bar min", a[i]-a_delta[i],"a",a[i],"max",a[i]+a_delta[i])