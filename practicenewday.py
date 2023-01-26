class Crustaceo:
    def __init__(self, nome, patas, olhos ):
        self._nome = nome
        self.patas = patas
        self.olhos = olhos

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome


class Caranguejo(Crustaceo):
    def __init__(self, nome, patas, olhos, casco):
        super().__init__(nome, patas, olhos)
        self.casco = casco


class Camarao(Crustaceo):
    def __init__(self, nome, pata, olhos, barbatana):
        super().__init__(nome, pata, olhos)
        self.barbatana = barbatana

#######################################################################

jorge = Caranguejo('Jorge', 10, 2,'Não')

print(jorge._nome)
print(jorge.casco)