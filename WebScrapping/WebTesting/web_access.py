import re
import xlsxwriter


from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager


URL = "http://www.bolsa.es/"

class WebAccess:
    def __init__(self):
        self.browser = self._create_browser()
        self.go_home_page()

    def __del__(self):
        self.browser.close()

    def _create_browser(self):
        edgeOptions = webdriver.EdgeOptions()
        edgeOptions.use_chronium = True
        edgeOptions.add_argument("start-maximized")
        edgeOptions.add_argument("log-level-3")
        # edgeOptions.set_capability("platformName", "Windows 10")

        capabilities = edgeOptions.to_capabilities()
        # browser = webdriver.Edge(options=edgeOptions)
        browser = webdriver.Edge(options=edgeOptions, executable_path=EdgeChromiumDriverManager().install())
        # browser = webdriver.Remote(command_executor="http://192.168.0.13:4444", options=edgeOptions)
        browser.maximize_window()
        return browser

    def go_home_page(self):
        print("Going to home page")
        self.browser.get(URL)
        print("... page loaded succesfully")

    def login(self, username, password):
        print("Login into website")
        self.browser.find_element(By.ID, "user").send_keys(username)
        self.browser.find_element(By.ID, "pass").send_keys(password)
        self.browser.find_element(By.TYPE, "submit").click()
        print("... succesfully login")

    def get_fields_name(self):
        fields_name = self.browser.find_elements(By.XPATH, "//div[contains(@style, 'width:755px;height:234px;position:absolute;left:14px')]//span[contains(@style, 'top:18px;color:#999999;text-align:center;')]")
        return [field_name.text for field_name in fields_name]

    def display_fields_values(self):
        t_span = self.browser.find_elements(By.XPATH, "//span[contains(@style, 'position:absolute;left:0px')]")
        n_span = self.browser.find_elements(By.XPATH, "//span[contains(@style, 'position:absolute;left:90px')]")
        u_span = self.browser.find_elements(By.XPATH, "//span[contains(@style, 'position:absolute;left:270px')]")
        v_span = self.browser.find_elements(By.XPATH, "//span[contains(@style, 'position:absolute;left:420px')]")
        vl_span = self.browser.find_elements(By.XPATH, "//span[contains(@style, 'position:absolute;left:570px')]")
        
        workbook = xlsxwriter.Workbook('./results/bolsa.xlsx')
        worksheet = workbook.add_worksheet("bolsa")

        worksheet.write(0, 0, 'Ticker')
        worksheet.write(0, 1, 'Name')
        worksheet.write(0, 2, 'Last Transaction')
        worksheet.write(0, 3, 'Variation')
        worksheet.write(0, 4, 'Volume')

        row = 1
        col = 0

        print ("{:<25} {:<35} {:<25} {:<25} {:<25}".format('Ticker','Name', 'Last Transaction', 'Variation', 'Volume'))
        

        for ts, ns, us, vs, ls in zip(t_span, n_span, u_span, v_span, vl_span,):
            print ("{:<25} {:<35} {:<25} {:<25} {:<25}".format(ts.text, ns.text, us.text, vs.text, ls.text))
            
            worksheet.write(row, col, ts.text)
            worksheet.write(row, col + 1, ns.text)
            worksheet.write(row, col + 2, us.text)
            worksheet.write(row, col + 3, vs.text)
            worksheet.write(row, col + 4, ls.text)
            row += 1

        workbook.close()