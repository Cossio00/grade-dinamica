import pdfplumber
from PyPDF2 import PdfReader


class Disciplina:
    def __init__(self, ano_sem, codigo_disciplina, chs, media, faltas, situacao):
        self.ano_sem = ano_sem        
        self.codigo_disciplina = codigo_disciplina
        self.chs = chs
        self.media = media
        self.faltas = faltas
        self.situacao = situacao
        
    def setAnoSem(self, ano_sem):
        self.ano_sem = ano_sem
        
    def setCodigoDisciplina(self, codigo_disciplina):
        self.codigo_disciplina = codigo_disciplina
                
    def setChs(self, chs):
        self.chs = chs

    def setMedia(self, media):
        self.media = media

    def setFaltas(self, faltas):
        self.faltas = faltas
    
    def setSituacao(self, situacao):
        self.situacao = situacao

    def getAnoSem(self):
        return self.ano_sem
    
    def getCodigoDisciplina(self):
        return self.codigo_disciplina
    
    def getChs(self):
        return self.chs
    
    def getMedia(self):
        return self.media

    def getFaltas(self):
        return self.faltas
                
    def getSituacao(self):
        return self.situacao
        
with pdfplumber.open("../../../../HISTORICO_ESCOLAR__GRADUACAO1914004.pdf") as pdf:
    disciplinas = []
    for page_number, page in enumerate(pdf.pages):

        tables = page.extract_tables()
        
        for table in tables:
            for row in table:
                if row[-1] == 'AP':
                    disciplina = Disciplina(row[0], row[1], row[2], row[3], row[4], row[-1])
                    disciplinas.append(disciplina)
                    
            
