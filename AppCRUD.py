from Utilitarios import bd
from flask import Flask, render_template, request

app = Flask(__name__)

"""
set FLASK_DEBUG=1
set FLASK_ENV=development
set FLASK_APP=AppCRUD.py
flask run
"""

# URL: localhost:5000/formincluir
@app.route('/formincluir', methods=['POST'])
def formIncluir():
  return render_template('formIncluir.html')

@app.route('/incluir', methods=['POST'])
def incluir():
  # Recuperando dados do formulário de formIncluir()
  conhecimento = request.form['nme']

  # Incluindo dados no SGBD
  mysql = bd.SQL("root", "robson123", "curriculorobis")
  comando = "INSERT INTO tb_conhecimentos(nme_conhecimento) VALUES (%s);"
  if mysql.executar(comando, [conhecimento]):
      msg="Conhecimento " + conhecimento + " cadastrado com sucesso!"
  else:
      msg="Falha na inclusão de conhecimento."

  return msg


@app.route('/')
def menu():
  return render_template('menu.html')

@app.route('/crudCurriculo', methods=['GET', 'POST'])
def crudCurriculo():
  # Recuperando todos os modelos da base de dados
  mysql = bd.SQL("root", "robson123", "curriculorobis")
  comando = "SELECT idt_conhecimento, nme_conhecimento FROM tb_conhecimentos ORDER BY nme_conhecimento;"

  cs = mysql.consultar(comando, ())
  conhecimentos = ""
  for [idt, nme] in cs:
      conhecimentos += "<TR>"
      conhecimentos += f'<td>{nme}</td>'
      conhecimentos += f'<td><button class=\"btn\" id=\"excluir\" onclick=\"jsExcluir(\'{nme}\', ({idt}))\">Excluir</button></td>'
      conhecimentos += f'<td><button class=\"btn\" id=\"alterar\" onclick=\"jsExcluir(\'{nme}\', {idt})\">Alterar</button></td>'
      conhecimentos += "</TR>"

  cs.close()

  return render_template('crudCurriculo.html', conhecimentos=conhecimentos)



@app.route('/excluir', methods=['GET', 'POST'])
def excluir():
  # Recuperando dados do formulário de crudCurriculo()
  idt = int(request.form['idt'])
  nme = request.form['nme']

  # Excluindo dados no SGBD
  mysql = bd.SQL("root", "robson123", "curriculorobis")
  comando = "DELETE FROM tb_conhecimentos WHERE idt_conhecimento=%s;"

  if mysql.executar(comando, [idt]):
      msg=f"Conhecimento {nme} excluído com sucesso!"
  else:
      msg=f"Falha na exclusão do conhecimento {nme}."

  return msg
