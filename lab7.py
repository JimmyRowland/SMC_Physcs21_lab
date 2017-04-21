#three significant digits
g = 9.80665
#part 1
force_average=1.969
integral_distance_force=2.62
h_start=0.509
h_end=1.09
m_hanging=0.2



h_delta=h_end-h_start
work_done_by_average_force=h_delta*force_average
comparison_workByForce_integral= work_done_by_average_force / integral_distance_force
change_in_potential_energy=m_hanging*g*h_delta
difference_work_potential=(work_done_by_average_force-change_in_potential_energy)/change_in_potential_energy
print("work_done_by_average_force",work_done_by_average_force,"comparison_workByForce_integral",comparison_workByForce_integral,'change_in_potential_energy',change_in_potential_energy,'difference_work_potential',difference_work_potential)



#part 2
s_delta=[0.1,0.2,0.43]
k_spring_constant=11.1
integral_work_by_hand=[0.042,0.211,0.997]


u_spring_potential=[]
difference_work_spring_2=[]
for i in range(len(s_delta)):
    u_spring_potential.append(k_spring_constant*s_delta[i]**2/2)
    difference_work_spring_2.append((integral_work_by_hand[i]-u_spring_potential[i])/u_spring_potential[i])
print("u_spring_potential",u_spring_potential,"difference_work_spring_2",difference_work_spring_2)


#part3



m_cart=1
m_sensor=1
v_final_horizontal=1
integral_push =1



m_cart_sensor=m_cart+m_sensor
k_delta=v_final_horizontal**2*m_cart_sensor/2
difference_work_kDelta=integral_push/k_delta
print("k_delta",k_delta,"difference_work_kDelta",difference_work_kDelta)


#part 4
t_cart_delta=0.5
w_cart=1
position=[0,0.054,0.108,0.162]
velocity=[0.243,0.291,0.340,0.387]
a_average=0.253


h_vertical=[]
potential_h=[]
k_cart=[]
e_mechanical_total=[]
difference_points_total=[]
sin_O=a_average/g

for i in range(len(position)):
    h_vertical.append(sin_O*position[i]*(-1))

for i in range(len(position)):
        h_vertical[i] -= h_vertical[3]
        potential_h.append(h_vertical[i] * m_cart * g)
        k_cart.append(velocity[i] ** 2 * m_cart / 2)
        e_mechanical_total.append(k_cart[i] + potential_h[i])
for i in range(len(position)):
    difference_points_total.append((e_mechanical_total[-3+i]-e_mechanical_total[-4+i])/e_mechanical_total[-3+i])
    print(e_mechanical_total[-3 + i], e_mechanical_total[-4 + i])
print('sin_O',sin_O)
print('h_vertical',h_vertical,'potential_h',potential_h)
print('k_cart',k_cart,'e_mechanical_total',e_mechanical_total)
print('difference_points_total',difference_points_total)
