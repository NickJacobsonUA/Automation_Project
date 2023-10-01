class BasePage: # base page использует driver, и будет представлять собой класс от которого будут следоваться все остальные страницы
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # Далее нужно открыть конкретный url. Для этого нужно создать функцию open

    def open(self):
        self.driver.get(self.url)
