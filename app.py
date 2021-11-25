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
  comando = "SELECT idt_conhecimento, nme_conhecimento, dta_conhecimento, desc_conhecimento FROM tb_conhecimentos ORDER BY nme_conhecimento;"

  cs = mysql.consultar(comando, ())
  conhecimentos = ""
  for [idt, nme, dta, desc] in cs:
        conhecimentos += '<div class="col-md-4 mt-3 mb-3">'
        conhecimentos += '<div class="card p-3">'
        conhecimentos += '<div class="d-flex flex-row mb-3">'
        conhecimentos += '<div class="d-flex flex-column ml-2">'
        conhecimentos += f'<h5>{nme}</h5>'
        conhecimentos += '</div>'
        conhecimentos += '</div>'
        conhecimentos += f'<h6>{desc}</h6>'
        conhecimentos += '<div class="d-flex justify-content-between install mt-3">'
        conhecimentos += f'<span>Data de aquisição: {dta}</span>'
        conhecimentos += '<span class="text-primary">'
        conhecimentos += '<i class="fa fa-angle-right"></i>'
        conhecimentos += '</span>'
        conhecimentos += '</div></div></div>'
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

@app.route('/alterar', methods=['GET', 'POST'])
def alterar():
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

app.run()
  
