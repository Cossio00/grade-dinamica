import pdfplumber
from PyPDF2 import PdfReader


class Disciplina:
    def __init__(self, codigo_disciplina, chs, situacao, tipo): 
        self.codigo_disciplina = codigo_disciplina
        self.chs = chs
        self.situacao = situacao
        self.tipo = tipo        #tipo indica: 0 para obrigatoria, 1 para eletiva e 2 para facultativa
                
    def setCodigoDisciplina(self, codigo_disciplina):
        self.codigo_disciplina = codigo_disciplina
                
    def setChs(self, chs):
        self.chs = chs
    
    def setSituacao(self, situacao):
        self.situacao = situacao

    def setTipo(self, tipo):
        self.tipo = tipo
    
    def getCodigoDisciplina(self):
        return self.codigo_disciplina
    
    def getChs(self):
        return self.chs
                    
    def getSituacao(self):
        return self.situacao

    def getTipo(self):
        return self.tipo

#HISTORICO_ESCOLAR__GRADUACAO2021128
#HISTORICO_ESCOLAR__GRADUACAO1914004
#HISTORICO_ESCOLAR__GRADUACAO1624348
with pdfplumber.open("../../../../HISTORICO_ESCOLAR__GRADUACAO1624348.pdf") as pdf:
    disciplinas = []
    for page_number, page in enumerate(pdf.pages):

        tables = page.extract_tables()
        
        for table in tables:
            for row in table:
                if row[-1] == 'AP':
                    #print(row)
                    if(len(row) > 10):
                        disciplina = Disciplina(row[1], row[7], row[-1], 0)
                    else:
                        disciplina = Disciplina(row[1], row[2], row[-1], 0)
                    disciplinas.append(disciplina)
                    
        
    for disciplina in disciplinas:
        if "(E)" in disciplina.getCodigoDisciplina():
            disciplina.setTipo(1)
        if "(F)" in disciplina.getCodigoDisciplina():
            disciplina.setTipo(2)

    for disciplina in disciplinas:
        print(disciplina.getCodigoDisciplina(), disciplina.getTipo())