from dnspython import dns.resolver

host = str(input("Digite o ip ou site para ser verificado:"))
res = resolver.Resolver()

resultado res.resolver(host, "A")

for info in resultado:
	print(info)