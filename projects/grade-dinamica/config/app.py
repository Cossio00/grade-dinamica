from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pdfplumber
import os

app = Flask(__name__, static_folder='../', static_url_path='')  # raiz do projeto
CORS(app)

class Disciplina:
    def __init__(self, codigo, nome, chs, situacao, tipo): 
        self.codigo = codigo
        self.nome = nome
        self.chs = chs
        self.situacao = situacao
        self.tipo = tipo

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "chs": self.chs,
            "situacao": self.situacao,
            "tipo": self.tipo
        }

    def getCodigo(self):
        return self.codigo

    def getNome(self):
        return self.nome

    def getChs(self):
        return self.chs

    def getSituacao(self):
        return self.situacao
    
    def getTipo(self):
        return self.tipo
        
    def setCodigo(self, codigo):
        self.codigo = codigo

    def setNome(self, nome):
        self.nome = nome

    def setChs(self, chs):
        self.chs = chs

    def setSituacao(self, situacao):
        self.situacao = situacao

    def setTipo(self, tipo):
        self.tipo = tipo

@app.route("/")
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/upload", methods=["POST"])
def processar_pdf():
    if 'file' not in request.files:
        return jsonify({"erro": "Nenhum arquivo enviado"}), 400

    file = request.files['file']
    disciplinas = []

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    if row and row[-1] == 'AP':
                        codigo, nome = row[1].split(" - ")
                        if len(row) > 10:
                            disciplina = Disciplina(codigo, nome, row[7], row[-1], 0)
                        else:
                            disciplina = Disciplina(codigo, nome, row[2], row[-1], 0)
                        disciplinas.append(disciplina)

    for d in disciplinas:
        if "(E)" in d.getNome():
            d.setTipo(1)
        elif "(F)" in d.getNome():
            d.setTipo(2)

    return jsonify([d.to_dict() for d in disciplinas])

if __name__ == "__main__":
    app.run(debug=True)
