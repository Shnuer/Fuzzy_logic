import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


value_PWM_first_serv = ctrl.Antecedent(np.arange(0, 1000, 1), 'value_PWM_first_serv')
value_PWM_second_serv = ctrl.Antecedent(np.arange(0, 1000, 1), 'servvalue_PWM_second_service')

x_error = ctrl.Consequent(np.arange(0, 641, 1), 'x_error')
y_error = ctrl.Consequent(np.arange(0, 481, 1), 'y_error')

# value_PWM_first_serv['low'] = fuzz.trapmf(tip.universe, [0, 0, 13])
# value_PWM_first_serv['medium'] = fuzz.trapmf(tip.universe, [0, 13, 25])
# value_PWM_first_serv['high'] = fuzz.trapmf(tip.universe, [13, 25, 25])

value_PWM_first_serv['low'] = fuzz.trimf(value_PWM_first_serv.universe, [0, 0, 500])
value_PWM_first_serv['medium'] = fuzz.trimf(value_PWM_first_serv.universe, [0, 500, 1000])
value_PWM_first_serv['high'] = fuzz.trimf(value_PWM_first_serv.universe, [500, 1000, 1000])

value_PWM_second_serv['low'] = fuzz.trimf(value_PWM_second_serv.universe, [0, 0, 500])
value_PWM_second_serv['medium'] = fuzz.trimf(value_PWM_second_serv.universe, [0, 500, 1000])
value_PWM_second_serv['high'] = fuzz.trimf(value_PWM_second_serv.universe, [500, 1000, 1000])

x_error['poor'] = fuzz.trimf(x_error.universe, [0, 0, 320])
x_error['average'] = fuzz.trimf(x_error.universe, [0, 320, 640])
x_error['good'] = fuzz.trimf(x_error.universe, [320, 640, 640])

y_error['poor'] = fuzz.trimf(y_error.universe, [0, 0, 240])
y_error['average'] = fuzz.trimf(y_error.universe, [0, 240, 480])
y_error['good'] = fuzz.trimf(y_error.universe, [240, 480, 480])


rule1_for_x = ctrl.Rule(x_error['poor'], value_PWM_first_serv['low'])
rule2_for_x = ctrl.Rule(x_error['average'], value_PWM_first_serv['medium'])
rule3_for_x = ctrl.Rule(x_error['good'], value_PWM_first_serv['high'])

rule1_for_y = ctrl.Rule(y_error['poor'], value_PWM_second_serv['low'])
rule2_for_y = ctrl.Rule(y_error['average'], value_PWM_second_serv['medium'])
rule3_for_y = ctrl.Rule(y_error['good'], value_PWM_second_serv['high'])


value_x_ctrl = ctrl.ControlSystem([rule1_for_x, rule2_for_x, rule3_for_x]) #need fix this
value_y_ctrl = ctrl.ControlSystem([rule1_for_y, rule2_for_y, rule3_for_y])


value_x = ctrl.ControlSystemSimulation(value_x_ctrl)
value_y = ctrl.ControlSystemSimulation(value_y_ctrl)

value_x.input['x_error'] = 6.5

value_y.input['y_error'] = 9.8


value_x.compute()
value_y.compute()

print (value_x.output['value_PWM_first_serv'])
print (value_y.output['servvalue_PWM_second_service'])






value_PWM_first_serv.view()
value_PWM_second_serv.view()
x_error.view()
y_error.view()

plt.show()