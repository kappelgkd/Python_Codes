from selenium import webdriver
from time import sleep

# define a classe de automatizar o chrome
class chromeAuto:
    # método init para inicializar com os caminhos iniciais 
    def __init__(self):
        self.driver_path = ('chromedriver.exe')
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options = self.options
        )

    # método para acessar uma url especifica
    def acessarUrl(self, url):
        self.chrome.get(url)
    
    # método para fechar o navegador
    def sair(self):
        self.chrome.quit()
     
    # método para clicar em um botão da página
    def click_login(self, btn):
       # guarda o caminho encontrado na variável
        # vai tentar executar o comando.
        try:
            bt_login = self.chrome.find_element_by_link_text(btn)
        # em caso de erro
        except Exception as e:
            print('Erro: ', e)
         # faz o clique no caminho encontrado
        bt_login.click()
    

    
    def click_perfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > summary > img')
            perfil.click()


        except Exception as e:
            print('Erro ao clicar no menu', e)




    def faz_Login(self):
        # vai encontrar os campos de login, senha e o botão enter
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_name('password')
            bt_login = self.chrome.find_element_by_name('commit')
            # vai digitar o login, senha, aguardar 1s e clicar no enter
            input_login.send_keys('kappelgkd')
            input_password.send_keys('#Kappel1711')
            sleep(1)
            bt_login.click()

        
        except Exception as e:
            print('Erro ao fazer login: ', e)

    def click_LogOut(self):
        try:
            log_Out = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > details-menu > form > button')
            log_Out.click()

        except Exception as e:
            print('Erro ao fazer logOut.', e)
    

    # método para clicar em um link.
    def click_Link(self):
        try:
                link = self.chrome.find_element_by_xpath('//*[@id="glb-corpo"]/div[2]/div[1]/div[1]/div[1]/a/p')
                link.click()
        except Exception as e:
            print('Erro ao acessar link.', e)


    
    
if __name__== '__main__':
        chrome = chromeAuto()
        chrome.acessarUrl('http://www.github.com')
        chrome.faz_Login()
        sleep(5)
        chrome.sair()
