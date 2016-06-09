print('Initialising retracing_steps')

from pyb import Pin, ADC, Timer

# Key variables --------------------------------------------------
speed = 50 # standard driving speed


# Defining the motor modules--------------------------------------
A1 = Pin('Y9',Pin.OUT_PP) # motor A is on the RHS of the vehicle
A2 = Pin('Y10',Pin.OUT_PP)
motor1 = Pin('X1')

B1 = Pin('Y11',Pin.OUT_PP) # motor B is on the LHS of the vehicle
B2 = Pin('Y12',Pin.OUT_PP)
motor2 = Pin('X2')

tim = Timer(2, freq = 1000)
ch1 = tim.channel(1, Timer.PWM, pin = motor1)
ch2 = tim.channel(2, Timer.PWM, pin = motor2)

# Get Keypad commands via Bluetooth (based from Task 8)-----------------------------------
key = ('1', '2', '3', '4', 'U', 'D', 'L', 'R') 
uart = UART(6)
uart.init(9600, bits=8, parity=None, stop=2) 
while True: 
	while (uart.any()!=10): #wait we get 10 chars
		n=uart.any()   
	command = uart.read(10) #reading the ASCII code for when a button is pressed
	key_index = command[2]-ord('1') 
	if command[3]==ord('1'):
  		test = 'something is pressed'
  	#if U is pressed
  	if (key_index==4):
  		action = 'UP pressed'
  	#if D is pressed
  	if (key_index==5):
  		action = 'DOWN pressed'
  	#if L is pressed
  	if (key_index==6):
 	 	action = 'LEFT pressed'
  	#if R is pressed
  	if (key_index==7):
 	 	action = 'RIGHT pressed'
	else: 
	  	action = 'nothing pressed'
print ('Key ', test, '', action)



# ---------------------------------------------------------------

def stop():
	ch1.pulse_width_percent(0) # send a pulse of width 0% to motor A
	ch2.pulse_width_percent(0) # send a pulse of width 0% to motor B

def drive(speed): # Set direction to forward

	A1.high() # Motor A set forward
	A2.low()

	B1.low() # Motor B set forward
	B2.high()

	ch1.pulse_width_percent(speed) # send a pulse of width 'speed'% to motor A
	ch2.pulse_width_percent(speed) # send a pulse of width 'speed'% to motor B
