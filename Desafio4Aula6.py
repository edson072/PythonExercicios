infor = input('Digite algo!')
print('O tipo primitivo desse dado é' , type(infor))
print('Esse dado só tem espaços?', infor.isspace())
print('Esse dado é um número?', infor.isnumeric())
print('Esse dado é alfabético?', infor.isalpha())
print('Esse dado é alfanumérico?', infor.isalnum())
print('Esse dado está em maiúsculas?', infor.isupper())
print('Esse dado está em letras minúsculas?',infor.islower())
print('Esse dado está capitalizado?', infor.istitle())