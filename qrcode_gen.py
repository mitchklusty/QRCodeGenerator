import qrcode
import sys
data = ''
if len(sys.argv) < 2:
	data = input("String to encode: ")
else:
	for i in range(1, len(sys.argv)):
		data += sys.argv[i] + ' '
	data.rstrip()
print(data)
img = qrcode.make(data)  
img.save(f'new_qrcode.png')