from werkzeug.utils import redirect
from Utilitarios import bd
from flask import Flask, render_template, request

app = Flask(__name__)

"""
set FLASK_DEBUG=1
set FLASK_ENV=development
set FLASK_APP=AppCRUD.py
flask run
"""


@app.route('/incluir', methods=['POST'])
def incluir():
  # Recuperando dados do formulário de formIncluir()
  conhecimento = request.form['nme']
  desc = request.form['desc']
  data = request.form['dta']

  # Incluindo dados no SGBD
  mysql = bd.SQL("root", "robson123", "curriculorobis")
  comando = "INSERT INTO tb_conhecimentos(nme_conhecimento, dta_conhecimento, desc_conhecimento) VALUES (%s, %s, %s);"
  if mysql.executar(comando, [conhecimento, data, desc]):
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
  comando = "SELECT idt_conhecimento, nme_conhecimento, dta_conhecimento, desc_conhecimento FROM tb_conhecimentos ORDER BY idt_conhecimento;"

  cs = mysql.consultar(comando, ())
  conhecimentos = cs.fetchall()
  

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

@app.route('/formAlterar', methods=['GET', 'POST'])
def pagalterar():
  idt = int(request.form['idt'])
  mysql = bd.SQL("root", "robson123", "curriculorobis")
  comando = "SELECT * FROM tb_conhecimentos WHERE idt_conhecimento=%s;"

  cs = mysql.consultar(comando, [idt])
  listaConhecimento = cs.fetchone()
  return render_template("formAlterar.html", listaConhecimento=listaConhecimento)

@app.route('/alterar', methods=['GET', 'POST'])
def alterar():
  idt = int(request.form['idt'])
  nme = request.form['inputNome']
  desc = request.form['inputDesc']
  dta = request.form['inputData']
  # Excluindo dados no SGBD
  mysql = bd.SQL("root", "robson123", "curriculorobis")
  comando = "UPDATE tb_conhecimentos SET nme_conhecimento = %s, dta_conhecimento = %s, desc_conhecimento = %s WHERE idt_conhecimento = %s "

  mysql.executar(comando, [nme, dta, desc, idt])
     

  return redirect("/crudCurriculo")

app.run()
  
