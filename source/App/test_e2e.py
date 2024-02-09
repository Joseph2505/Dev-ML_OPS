from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestApp(unittest.TestCase):
    
  def setUp(self):
      self.service = Service(ChromeDriverManager().install())
      self.driver = webdriver.Chrome(service=self.service)
      self.driver.maximize_window()

  def tearDown(self):
      self.driver.quit()

  def test_prediction(self):
      self.driver.get("https://dev-mlops-dev.streamlit.app/")  # Mettez l'URL de votre application Streamlit ici
      
      # # Attendez que l'élément de slider Recency soit visible
      # recency_slider = WebDriverWait(self.driver, 30).until(
      #     EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Recency']"))
      # )
      # recency_slider.send_keys('50')

      # Répétez pour d'autres éléments de slider...

      # Attendre un peu pour que la prédiction se produise (le temps de la mise à jour de l'interface utilisateur)
      self.driver.implicitly_wait(5)

if __name__ == "__main__":
    unittest.main()
