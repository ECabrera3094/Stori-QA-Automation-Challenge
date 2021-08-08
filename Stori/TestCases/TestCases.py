from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from Locators.Locators import MyLocators


class MyTestCases():

    def __init__(self, driver):
        
        self.driver = driver
        self.XPath_suggessionClassExample = MyLocators.XPath_suggessionClassExample
        self.XPath_countrieMexico = MyLocators.XPath_countrieMexico
        self.XPath_option_2 = MyLocators.XPath_option_2
        self.XPath_option_3 = MyLocators.XPath_option_3
        self.XPath_switchWindowExample = MyLocators.XPath_switchWindowExample
        self.XPath_secondPopUp = MyLocators.XPath_secondPopUp
        self.XPath_30DaysMoneyBack = MyLocators.XPath_30DaysMoneyBack
        self.XPath_switchTabExample = MyLocators.XPath_switchTabExample
        self.XPath_ViewAllCourses = MyLocators.XPath_ViewAllCourses
        self.saveRootImage = MyLocators.saveRootImage
        self.XPath_switchToAlertExample = MyLocators.XPath_switchToAlertExample
        self.XPath_alertButton = MyLocators.XPath_alertButton
        self.XPath_confirmButton = MyLocators.XPath_confirmButton
        self.XPath_webTableExample = MyLocators.XPath_webTableExample
        self.XPath_webTableFixedHeader = MyLocators.XPath_webTableFixedHeader
        self.XPath_iFrame = MyLocators.XPath_iFrame
        self.XPath_iFrameMessage = MyLocators.XPath_iFrameMessage
        
    def Challenge(self):

        # ----- Autocomplete
        self.driver.find_element_by_xpath(self.XPath_suggessionClassExample).send_keys("ME")
        
        self.driver.implicitly_wait(5)

        self.driver.find_element_by_xpath(self.XPath_countrieMexico).click()

        # ----- DropDown
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, self.XPath_option_2))).click()
        
        self.driver.implicitly_wait(3)
        
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, self.XPath_option_3))).click()

        self.driver.implicitly_wait(3)

        # ----- PopUp
        main_page = self.driver.current_window_handle

        self.driver.find_element_by_xpath(self.XPath_switchWindowExample).click()

        self.driver.implicitly_wait(3)

        for popUp in self.driver.window_handles:
            if popUp != main_page:
                open_Window = popUp

        self.driver.switch_to.window(open_Window)

        self.driver.implicitly_wait(5)

        # ----- Second Popup
        try:
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.XPath_secondPopUp))).click()
        except TimeoutError as TOE:
            pass
        # ----- Text "30 Days"
        str_30DaysMoneyBack = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.XPath_30DaysMoneyBack)))
        
        if str_30DaysMoneyBack == False:
            self.driver.execute_script('browserstack_executor : {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Oops! Test Failed"}}')
            self.driver.close()
            self.driver.quit()
        else:
            pass
            
        # ----- Close PopUp and Return to the Main Window.
        self.driver.close()
        self.driver.switch_to.window(main_page)
        
        # ----- Switch Tab Example
        self.driver.find_element_by_xpath(self.XPath_switchTabExample).click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        
        button_viewAllCourses = self.driver.find_element_by_xpath(self.XPath_ViewAllCourses)

        action = ActionChains(self.driver)

        action.move_to_element(button_viewAllCourses).perform()

        self.driver.save_screenshot(self.saveRootImage)

        self.driver.switch_to.window(main_page)

        # ----- Switch To Alert
        self.driver.find_element_by_xpath(self.XPath_switchToAlertExample).send_keys("Stori Card")

        self.driver.find_element_by_xpath(self.XPath_alertButton).click()

        obj_1 = self.driver.switch_to.alert

        str_Message_1 = obj_1.text

        obj_1.accept()

        self.driver.implicitly_wait(3)

        self.driver.find_element_by_xpath(self.XPath_switchToAlertExample).send_keys("Stori Card")

        self.driver.find_element_by_xpath(self.XPath_confirmButton).click()

        obj_2 = self.driver.switch_to.alert

        str_Message_2 = obj_2.text

        obj_2.accept()

        print("Alert: {0}\nConfirm: {1}".format(str_Message_1, str_Message_2))

        # ----- Web Table Example
        rws = self.driver.find_elements_by_xpath(self.XPath_webTableExample)
        #cols = self.driver.find_elements_by_xpath("/html/body/div[3]/div[1]/fieldset/table/tbody/tr[1]/th")
        
        len_Rows = len(rws)

        list_priceOver25 = []

        int_Flag = 0

        for i in range(2, len_Rows):
            # Fila - Columna
            int_Price = self.driver.find_element_by_xpath("/html/body/div[3]/div[1]/fieldset/table/tbody/tr["+str(i)+"]/td[3]").text
            
            if int(int_Price) == 25:
                int_Flag += 1
                str_nameCourse = self.driver.find_element_by_xpath("/html/body/div[3]/div[1]/fieldset/table/tbody/tr["+str(i)+"]/td[2]").text
                list_priceOver25.append(str_nameCourse)

        print("Total de Cursos: {0}\nCursos: {1}".format(int_Flag, list_priceOver25))

        # ----- Web Table Fixed Header
        rws = self.driver.find_elements_by_xpath(self.XPath_webTableFixedHeader)
        
        len_Rows = len(rws)
        
        list_namesEmployees = []

        for i in range(1, len_Rows+1):
            # Fila - Columna
            str_nameEmployees = self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/fieldset[2]/div[1]/table/tbody/tr["+str(i)+"]/td[1]").text
            list_namesEmployees.append(str_nameEmployees)
        
        print("Tabla 2: {0}\nEmpleados: {1}".format(len_Rows, list_namesEmployees))

        # ----- iFrame Example
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.XPath_iFrame))

        str_iFrame = self.driver.find_element_by_xpath(self.XPath_iFrameMessage).text

        print("Texto iFrame: ", str_iFrame)

        self.driver.switch_to.default_content()