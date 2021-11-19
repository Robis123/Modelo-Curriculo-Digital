from Utilitarios import bd, pathing
from flask import Flask, render_template, request

rota = pathing.Path()
app = Flask(__name__, template_folder=rota.templateWay(), static_folder=rota.staticWay())

"""
set FLASK_DEBUG=1
set FLASK_ENV=development
set FLASK_APP=modelagem_de_negocios.aplicacao.main.py
flask run
"""

@app.route('/')
def index():
  return render_template('CRUD.html')

@app.route('/incluir', methods=['POST'])
def incluir():

  nme = request.form['nme']
  dta = request.form['dta']
  tel = request.form['tel']

  mysql = bd.SQL("robis123", "Robson123", "curriculodigital")
  comando = "INSERT INTO tb_pessoa(nme_pessoa, dta_nasc_pessoa, tel_pessoa) VALUES (%s, %s, %s);"
  if mysql.executar(comando, [nme, dta, tel]):
      msg="Pessoa " + nme + " cadastrada com sucesso!"
  else:
      msg="Falha na inclusão de pessoa."

  return msg

@app.route('/buscar', methods=['POST'])
def buscar():


  parte = request.form['parte']

  mysql = bd.SQL("robis123", "Robson123", "curriculodigital")
  comando = "SELECT * FROM tb_pessoa WHERE nme_pessoa LIKE CONCAT('%', %s, '%') ORDER BY nme_pessoa;"
  cs=mysql.consultar(comando, [parte])
  print(cs)
  dados = cs.fetchone()
  if dados == None:
      saida = ""
  else:
      saida = str(dados[0]) + ',' + dados[1] + ',' + str(dados[2]) + ',' + dados[3]

  return saida


@app.route('/alterar', methods=['POST'])
def alterar():


  idt = request.form['idt']
  nme = request.form['nme']
  dta = request.form['dta']
  tel = request.form['tel']

 
  mysql = bd.SQL("robis123", "Robson123", "curriculodigital")
  comando = "UPDATE tb_pessoa SET nme_pessoa=%s, dta_nasc_pessoa=%s, tel_pessoa=%s WHERE idt_pessoa=%s;"
  if mysql.executar(comando, [nme, dta, tel, idt]):
      msg="Pessoa " + nme + " alterada com sucesso!"
  else:
      msg="Falha na alteração de pessoa."

  return msg


@app.route('/excluir', methods=['POST'])
def excluir():


  idt = request.form['idt']
  nme = request.form['nme']


  mysql = bd.SQL("robis123", "Robson123", "curriculodigital")
  comando = "DELETE FROM tb_pessoa WHERE idt_pessoa=%s;"
  if mysql.executar(comando, [idt]):
      msg="Pessoa " + nme + " excluida com sucesso!"
  else:
      msg="Falha na exclusão de pessoa."

  return msg


app.run()
