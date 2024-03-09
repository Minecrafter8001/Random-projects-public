T='enable desktop notifcations? (y/n)'
S='https://'
R='enter url:'
N=None
I=input
F=print
D=True
A=False
from plyer import notification as J
import time as K,requests as U
B=I(R)
while B=='':B=I(R)
if B!='':
	if S not in B and'http://'not in B:B=S+B
O=D
L=I(T)
while L=='':L=I(T)
P=L.lower()
if P in{'n','no','f','false'}:O=A;F('desktop notifcations disabled')
elif P in{'y','yes','t','true'}:O=D;F('desktop notifcations enabled')
M='server checker'
G=A
H=A
C=D
while D:
	Q=U.get(B);E=Q.status_code;F(Q)
	if E>=200 and E<=300:
		if not C:J.notify(title=M,message='OK',app_icon=N,timeout=10);H=A;G=A;C=D;K.sleep(120)
		else:K.sleep(120)
	elif E>=500 and E<600:
		F('server side error');C=A
		if not G:J.notify(title=M,message='server down server error',app_icon=N,timeout=10)
		H=A;G=D;C=A
	elif E>=400 and E<500:
		C=A;F('client side error')
		if not H:J.notify(title=M,message='server down client error',app_icon=N,timeout=10);H=D;G=A;C=A
	if not C:K.sleep(30)