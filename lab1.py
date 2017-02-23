import math
m = 65.89
D_meter_stick = 1.89
D_vernier_caliper = 1.91
h_meter_stick = 3.17
h_vernier_caliper = 3.26
# instrumental uncertainty iu
meter_stick_iu = 0.05
vernier_caliper_iu = 0.005
double_pan_balance_iu = 0.02
# estimated uncertainty eu
meter_stick_D_eu = 0
meter_stick_h_eu = 0
vernier_caliper_D_eu = 0
vernier_caliper_h_eu = 0
double_pan_balance_eu = 0
# total uncertainty tu
dD_meter_stick = meter_stick_D_eu + meter_stick_iu
dh_meter_stick = meter_stick_iu + meter_stick_h_eu
dD_vernier_caliper = vernier_caliper_D_eu + vernier_caliper_iu
dh_vernier_caliper = vernier_caliper_iu + vernier_caliper_h_eu
dm = double_pan_balance_eu + double_pan_balance_iu
# density
p_meter_stick = 4*m/(math.pi*D_meter_stick*D_meter_stick*h_meter_stick)
p_vernier_caliper = 4*m/(math.pi*D_vernier_caliper*D_vernier_caliper*h_vernier_caliper)
dp_meter_stick = p_meter_stick*(dm/m+2*dD_meter_stick/D_meter_stick+dh_meter_stick/h_meter_stick)
dp_vernier_caliper = p_vernier_caliper*(dm/m+2*dD_vernier_caliper/D_vernier_caliper+dh_vernier_caliper/h_vernier_caliper)
print("meter stick m={} D={} h={} p={} dp={} range={}--{}".format(m,D_meter_stick,h_meter_stick,p_meter_stick,
                                                                 dp_meter_stick,p_meter_stick-dp_meter_stick,
                                                                 p_meter_stick+dp_meter_stick))
print("vernier_caliper m={} D={} h={} p={} dp={} range={}--{}".format(m, D_vernier_caliper, h_vernier_caliper, p_vernier_caliper,
                                                                     dp_vernier_caliper, p_vernier_caliper - dp_vernier_caliper,
                                                                     p_vernier_caliper + dp_vernier_caliper))
print(dm/m,dD_vernier_caliper/D_vernier_caliper,dh_vernier_caliper/h_vernier_caliper)
