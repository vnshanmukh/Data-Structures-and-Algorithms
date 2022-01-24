def caesarCipherEncryptor(string, key):
	res = []
	a=""
	for i in string:
        res.append(ord(i) + key)

	for i in res:
        while i > 122 :
       		i = 96 + i % 122
        a+=chr(i)
	return a
	
