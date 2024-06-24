from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeOptions oluşturma ---- ARKAPLAN İÇİN -----
options = Options()
options.add_argument('--headless=new') # Tarayıcıyı arka planda çalıştırmak için
driver = webdriver.Chrome(options=options)

# Chrome tarayıcısını başlatma ----NORMAL ÇALIŞTIRMA---
# driver = webdriver.Chrome()

try:
    # Web sayfasını açma
    driver.get("https://belgenet.csb.gov.tr/edys-web/sistemeGiris.xhtml")

    # Butonun yüklenmesini beklemek için bir bekleme zamanlayıcısı ayarlayın
    wait = WebDriverWait(driver, 10)

    # Butonun tıklanabilir olmasını bekleyin (id="girisYapButtonKerb" olan buton)
    giris_button = wait.until(EC.element_to_be_clickable((By.ID, "girisYapButtonKerb")))

    # Butona tıklama
    giris_button.click()

    # Sistemin açılmasını bekleme
    wait.until(EC.url_to_be("https://belgenet.csb.gov.tr/edys-web/mainInbox.xhtml"))
    # Burada istediğiniz ek işlemleri yapabilirsiniz (örneğin, oturumu yönetmek veya başka sayfalara gitmek)
    # Örnek olarak, bir sonraki sayfaya geçiş için bekleyebilirsiniz:
    # wait.until(EC.url_to_be("https://belgenet.csb.gov.tr/sonraki_sayfa"))
    print("ÇALIŞIYOR")

finally:
    while True:
        continue

