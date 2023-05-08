# ---------------------------------------------------------------------------- #
#                         Álvaro Lúcio Almeida Ribeiro                         #
#                           Engenharia de Software                             #
#                               Matricula 163                                  #
# ---------------------------------------------------------------------------- #

# -------------------------------- Relatório 1 ------------------------------- #

# ----------------------------- Classe professor ----------------------------- #

class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self):
        return(f"O professor, {self.nome} está ministrando uma aula sobre {aula.assunto}")


# ------------------------------- Classe Aluno ------------------------------- #

class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        return (f"O aluno, {self.nome} está presente.")


# -------------------------------- Classe Aula ------------------------------- #

class Aula:
    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []

    def adicionar_aluno(self, aluno):
        aluno.presenca()
        self.alunos.append(aluno)

    def listar_presenca(self):
        Ordenandoaux = []
        for aluno in self.alunos:
            Ordenandoaux.append(aluno.presenca())
        AlunosAux = "\n".join(Ordenandoaux)
        return f"Presença na aula sobre {self.assunto}, ministrada pelo professor {professor.nome}:\n{AlunosAux}\n"

# -------------------------------- Classe Main ------------------------------- #

professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.listar_presenca())