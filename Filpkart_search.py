import unittest
from selenium.webdriver import Chrome
import _csv


class Testsearch(unittest.TestCase):
    def setUp(self):
        self.driver=Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.flipkart.com")
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.close()

    def search_for_Device_rating(self):
        self.driver.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']").click()
        self.driver.find_element_by_name('q').send_keys("iphone")
#Get the deice name based on price
        n=self.driver.find_elements_by_xpath("//*[text()='₹51,999']//preceding::a[@class='s1Q9rs']")
        device_details = []
        for i in range(0, len(n)):
            e1 = n[i].text
            device_details.append(e1)
        print(device_details)
#Get the rating name based  price
        r = self.driver.find_elements_by_xpath("//*[text()='₹51,999']//preceding::span[@class='_2_R_DZ']")
        rating = []
        for i in range(0, len(r)):
            e2 = r[i].text
            rating.append(e2)
        print(rating)

        new = zip(device_details, rating)
        my_dict= dict(new)
        print(my_dict)

# Wirting into CSV file
        with open('mycsv.csv', 'w', newline='')as f:
            fieldnames = ['Deive_name','Rating']
            thewriter = _csv.DictWriter(f, fieldnames=fieldnames)
            thewriter.writerrow(my_dict)
