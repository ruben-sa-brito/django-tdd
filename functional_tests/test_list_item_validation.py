from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        # Edith acessa a página inicial e aceidentalmente tenta submeter
        # um item vazio na lista. Ela tecla enter na caixa de entrada vazia

        # A página inicial é atualizada e há uma mensagem de erro informando 
        # que itens da lista não podem estar em branco

        # Ela tenta novamente com um texto para o item, e isso agora funciona

        # De forma perversa, ela agora decide submeter um segundo item em
        # branco na lista

        # Ela recebe um aviso semelhante na página na lista

        # E ela pode corrigir isso preenchendo o item com um texto

        self.fail('write me!')



