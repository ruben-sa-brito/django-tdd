from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from .base import FunctionalTest
from selenium import webdriver

class NewVisitorTest(FunctionalTest):
    def test_can_start_a_list_and_retrive_it_later(self):
        #Edith ouviu falar de uma nova aplicação online interessante para
        #lista de tarefas. Ela decide verificar sua homepage
        self.browser.get(self.live_server_url)

        #Ela percebe que o título da página e o cabeçalho mencionam listas
        #tarefas (to-do)

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        #Ela é convidada a inserir um item de tarefa imediatamente
        inputbox = self.browser.find_element(By.ID, 'id_new_item') 
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #Ela digita "Buy peacock feathers" (comprar penas de pavão) em uma caixa
        #de texto (o hobby de Edith é fazer iscas para pesca com fly) 
        inputbox.send_keys('Buy peacock feathers')


        #Quando ela tecla enter, a página é atualizada, e agora a página lista
        #"1: buy peacock feathers" como um item em uma lista de tarefas
        inputbox.send_keys(Keys.ENTER)
        
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        
        #Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro
        #item. Ela insere "Use peacock feathers to make a fly" (Usar penas de pavão
        #para fazer um fly - Edith é bem metódica)
        inputbox = self.browser.find_element(By.ID, 'id_new_item') 
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        

        #A pagina é atualizada novamente e agora mostra os dois itens em sua lista
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Edith se pergunta se o site lembrará de sua lista. Então ela nota
        #que o site gerou um url único para ela -- há um pequeno
        #texto explicativo para isso.

        # Ela acessa esse URL - sua lista de tarefas continua lá

        #Satisfeita, ela volta a dormir

    def test_multiple_users_can_start_lists_at_different_url(self):
        # Edith inicia uma nova lista de tarefas
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # Ela percebe que sua lista tem um URL único
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # Agora um novo usuário, Francis, chega ao site.

        ## Usamos uma nova sessão de navegador para garantir que nenhuma informação
        ## de Edith está vindo de cookies etc

        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis acessa a página inicial. Não há nenhum sinal da lista de Edith

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis inicia uma nova lista inserindo um item novo. Ele
        # é menos interessante que Edith
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis obtém seu próprio URL exclusivo 
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Novamente, não há nehum sinal da lista de Edith
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)


