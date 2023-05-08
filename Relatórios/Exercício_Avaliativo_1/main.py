# Nome: Álvaro Lúcio Almeida Ribeiro 
# Matrícula: 163 
# Exercício Avaliativo 1 

from database import Database
from motoristaDAO import MotoristaDAO
from motoristaCLI import MotoristaCLI

db = Database(database="ExercicioAvaliativo", collection="Motoristas")
motoristaDao = MotoristaDAO(database=db)

motoristaCLI = MotoristaCLI(motoristaDao)
motoristaCLI.run()