from Apartamento import Apartamento
from Torre import Torre

class Condominio:
    def __init__(self):
        self.lista_vagas = None  # Cabeça da Lista Encadeada
        self.fila_espera = []    # Fila (usando lista Python como FIFO)

    def adicionar_apartamento_fila(self, ap: Apartamento):
        """Adiciona um apartamento ao final da fila de espera."""
        ap.vaga = 0
        self.fila_espera.append(ap)
        print(f"Ap {ap.numero} entrou na fila de espera.")

    def atribuir_vaga(self, vaga_numero):
        """Retira o primeiro da fila e insere na lista encadeada ordenada."""
        if not self.fila_espera:
            print("Não há apartamentos na fila de espera.")
            return

        # FIFO: retira o primeiro que entrou
        ap = self.fila_espera.pop(0)
        ap.vaga = vaga_numero
        
        # Insere na Lista Encadeada (Ordenada por vaga)
        self._inserir_ordenado(ap)
        print(f"Ap {ap.numero} ocupou a vaga {vaga_numero}.")

    def _inserir_ordenado(self, novo_ap):
        """Lógica para manter a lista encadeada sempre em ordem de vaga."""
        if self.lista_vagas is None or novo_ap.vaga < self.lista_vagas.vaga:
            novo_ap.proximo = self.lista_vagas
            self.lista_vagas = novo_ap
            return

        atual = self.lista_vagas
        while atual.proximo and atual.proximo.vaga < novo_ap.vaga:
            atual = atual.proximo
        
        novo_ap.proximo = atual.proximo
        atual.proximo = novo_ap

    def imprimir_relatorios(self):
        print("\n--- RELATÓRIO DE VAGAS (LISTA ENCADEADA) ---")
        atual = self.lista_vagas
        if not atual: print("Nenhum apartamento com vaga.")
        while atual:
            atual.imprimir()
            atual = atual.proximo

        print("\n--- FILA DE ESPERA ---")
        if not self.fila_espera: print("Fila vazia.")
        for ap in self.fila_espera:
            ap.imprimir()

# Exemplo de execução
if __name__ == "__main__":
    t1 = Torre(1, "Residencial Sul", "Av. Borges de Medeiros, 500")
    
    condo = Condominio()
    
    # Criando apartamentos
    ap1 = Apartamento(10, "101", t1)
    ap2 = Apartamento(20, "202", t1)
    ap3 = Apartamento(30, "303", t1)
    
    # Colocando na fila
    condo.adicionar_apartamento_fila(ap1)
    condo.adicionar_apartamento_fila(ap2)
    condo.adicionar_apartamento_fila(ap3)
    
    # Atribuindo vagas de forma aleatória para testar a ordenação
    condo.atribuir_vaga(50)  # Ap 101 ganha vaga 50
    condo.atribuir_vaga(10)  # Ap 202 ganha vaga 10 (deve aparecer antes na lista)
    
    condo.imprimir_relatorios()