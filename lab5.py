g = 9.80665
time_interval=1/6
m_glider = 0
m_added_to_glider =[0.013]
m2=[0.2198]
m1=[0.013]
# for x in range(len(m_added_to_glider)):
#     m1.append(x+12)
#     m2.append(m_glider+m_added_to_glider[x])
print("m1",m1,"\nm2",m2)
t_delta = 1/6
s=[[0,2.69,6.56,11.78,18.41,26.5,35.92,46.81,59.10,70.41]]
s_delta=[[]]
v_average=[[]]
for x in range(len(s[0])):
    s[0][x]=s[0][x]/100
for u in range(len(s)):

    for i in range(len(s[u])):
        if i==0 or i ==len(s[u])-1:
            s_delta[u].append(0)
            v_average[u].append(0)
        else:
            s_delta[u].append(s[u][i+1]-s[u][i-1])
            v_average[u].append(s_delta[u][i]/2/t_delta)
for i in range(len(m_added_to_glider)):
    print("group",i+1,"s_delta:",s_delta[i],"\nv_average",v_average[i])
a_max=[]
a_min=[]
a=[]
a_delta=[]
for u in v_average:
    max=0
    min=100000
    temp =0
    for i in range(2,len(u)-1):
        temp=(u[i]-u[1])/(i-1)/t_delta
        if temp >max:
            max = temp
            print('max',u[i],u[i]-u[1],(i-1),temp)
        if temp < min:
            min = temp
            print('min', u[i], u[i] - u[1], (i - 1),temp    )
    a_max.append(max)
    a_min.append(min)
    a.append((max+min)/2)
    a_delta.append((max - min) / 2)

print('a_max:',a_max,'\na_min:',a_min,'\na:',a,'\na_delta:',a_delta)
a_theoretical=[]
for i in range(len(m_added_to_glider)):
    a_theoretical.append(m1[i]*g/(m1[i]+m2[i]))
print('a_theoretical',a_theoretical)
for i in range(len(m_added_to_glider)):
    print(i+1,"a error bar min", a[i]-a_delta[i],"a",a[i],"max",a[i]+a_delta[i])
print("uncertainty",(a[0]-a_theoretical[0])/a_theoretical[0])