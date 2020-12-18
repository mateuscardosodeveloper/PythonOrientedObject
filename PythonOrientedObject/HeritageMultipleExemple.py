#goal that's show you how Heritage multiple it works
#and how use Mixins
class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self): #if you comment this method will have process MRO - explaned bellow
      print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Arroba: #exemple that Mixin, not need to be Estanciado.
    def __str__(self):#Mixin can be called in any class, without needing any requirements
        return f'@ {self.nome}'# this are work if not must 'format' before

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Arroba):# Mixin being called
    pass

joao = Junior('Joao')
joao.busca_perguntas_sem_resposta()
joao.mostrar_tarefas()

luan = Pleno('Luan')
luan.busca_cursos_do_mes()
luan.mostrar_tarefas()

mateus = Senior('blah blah')#exemple that's Mixins it work
print(mateus)

#MRO(Method Resolution Order) Following way = Pleno > Alura > Funcionario > Caelum > Funcionario
#but exist order hierarchy like Alura, and Caelum with show in class Pleno
#ending up Funcionario being in another hierarchy
