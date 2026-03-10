#

matricula = 2026001
nome1 = "Ana"
telefone = "84-9887134-52"
#com dicionario
aluno = {
"matricula": 2026001,
"nome": "ana silva",
"telefone": "9999-8888"

}

print(aluno)

contato = {
"@camila": "camila",
"@Paola": "Paola",
"@Sheron": "Sheron",
"@Bruna" : "Bruna",
"joao": "joao"
}
print(contato)
print(type(contato))

#acesso direto ao dicionario
print(contato["@camila"])


#acesso seguro ao get()
print(contato.get("@paola"))
print(contato.get("@inexistente"))
print(contato.get("@inexistente", "não encontrado"))

print("original: ", contato) #acessando a lista original

contato["@giovanna"] = "Giovanna"
print("apos add: ", contato)

contato["@paola"] = "paola oliveira"
print("apos add: ", contato)

contato.update(
    {
        "@bruna": "Bruna Marquizine",
        "@camila": "camila"
    }
)

print("apos atualização: ", contato)

#pop: remove e retorna
removido = contato.pop("@sheron")
print(f"removido:" "{removido}")
print("apos o pop: ", contato)

#del remove sem retonar
del contato ["@paola"]
print("apos o del: ", contato)

#clear
copia = dict (contato)
contato.clear()
print("apos clear: ", contato)
print("cópia: ", copia)

print("número de contato: ", len(contato))

contato.pop("@camila")
print("apos remover um: ", len(contato))

#verificarexisteência
if "@joao" in contato:
    print(f"encontrado: {contato['joao']}")

if "@inexistente" in contato:
    print("existe")

else:
    print("não existe.")        

#dicionario vazio
vazio = {}

#dicionário com tipos mistos
dados = {
    "nome": "joão" , 
    "idade": 25,
    "altura":1.70,
    "ativo": True
}

print
("vazio: ", vazio)
print("vazio: ", dados)

