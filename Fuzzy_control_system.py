import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


value_PWM_x_serv = ctrl.Consequent(np.arange(-100, 101, 1), 'value_PWM_x_serv')
# value_PWM_y_serv = ctrl.Consequent(np.arange(-100, 101, 1), 'value_PWM_y_serv')

x_error = ctrl.Antecedent(np.arange(-200, 201, 1), 'x_error')
# y_error = ctrl.Antecedent(np.arange(-200, 201, 1), 'y_error')

value_PWM_x_serv['low'] = fuzz.trapmf(value_PWM_x_serv.universe, [-100,-100, -20, 0])
value_PWM_x_serv['medium'] = fuzz.trimf(value_PWM_x_serv.universe, [-20, 0, 20])
value_PWM_x_serv['high'] = fuzz.trapmf(value_PWM_x_serv.universe, [0, 20 ,100 ,100])
# value_PWM_x_serv.view()

# value_PWM_y_serv['low'] = fuzz.trapmf(value_PWM_y_serv.universe, [-100,-100, -20, 0])
# value_PWM_y_serv['medium'] = fuzz.trimf(value_PWM_y_serv.universe, [-20, 0, 20])
# value_PWM_y_serv['high'] = fuzz.trapmf(value_PWM_y_serv.universe, [0, 20 ,100 ,100])
# value_PWM_y_serv.view()

x_error['poor'] = fuzz.trapmf(x_error.universe, [-200,-200,-150, 0])
x_error['average'] = fuzz.trimf(x_error.universe, [-150, 0, 150])
x_error['good'] = fuzz.trapmf(x_error.universe, [0,150,200,200])
# x_error.view()

# y_error['poor'] = fuzz.trapmf(y_error.universe, [-200,-200,-150, 0])
# y_error['average'] = fuzz.trimf(y_error.universe, [-150, 0, 150])
# y_error['good'] = fuzz.trapmf(y_error.universe, [0,150,200,200])
# y_error.view()

# plt.show()

rule1_for_x = ctrl.Rule(x_error['poor'], value_PWM_x_serv['low'])
rule2_for_x = ctrl.Rule(x_error['average'], value_PWM_x_serv['medium'])
rule3_for_x = ctrl.Rule(x_error['good'], value_PWM_x_serv['high'])

# rule1_for_y = ctrl.Rule(y_error['poor'], value_PWM_y_serv['low'])
# rule2_for_y = ctrl.Rule(y_error['average'], value_PWM_y_serv['medium'])
# rule3_for_y = ctrl.Rule(y_error['good'], value_PWM_y_serv['high'])


value_x_ctrl = ctrl.ControlSystem([rule1_for_x, rule2_for_x, rule3_for_x]) #need fix this
# value_y_ctrl = ctrl.ControlSystem([rule1_for_y, rule2_for_y, rule3_for_y])


value_x = ctrl.ControlSystemSimulation(value_x_ctrl)
# value_y = ctrl.ControlSystemSimulation(value_y_ctrl)

value_x.input['x_error'] = 0

# value_y.input['y_error'] = 9.8


value_x.compute()
# value_y.compute()

print (value_x.output['value_PWM_x_serv'])
# print (value_y.output['servvalue_PWM_second_service'])

# value_PWM_x_serv.view()
# value_PWM_second_serv.view()
# y_error.view()

x_error.view(sim=value_x)
value_PWM_x_serv.view(sim=value_x)

plt.show()