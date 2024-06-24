from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def wait_for_loading_to_finish(driver):
    WebDriverWait(driver, 10).until(
        lambda d: "nprogress-busy" not in d.find_element(By.TAG_NAME, "html").get_attribute("class")
    )

def parsel_sorguyu_ac(ilce, mahalle, ada, parsel):
    # Chrome tarayıcısını başlatma ----NORMAL ÇALIŞTIRMA---
    driver = webdriver.Chrome()

    try:
        # Web sayfasını açma
        driver.get("https://parselsorgu.tkgm.gov.tr/")
        print("Parsel Sorgu açıldı")

        # "Kabul Ediyorum" butonuna tıklama
        kabul_butonu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "terms-ok"))
        )
        kabul_butonu.click()

        # "Kabul Ediyorum" butonundan sonra yüklenmenin bitmesini bekleyin
        wait_for_loading_to_finish(driver)

        # İl dropdown'unun yüklenmesini bekleyin
        il_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "province-select"))
        )
        select_il = Select(il_dropdown)
        select_il.select_by_visible_text("Muğla")

        # İl seçiminden sonra yüklenmenin bitmesini bekleyin
        wait_for_loading_to_finish(driver)

        # İlçe dropdown'unun yüklenmesini bekleyin
        ilce_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "district-select"))
        )
        select_ilce = Select(ilce_dropdown)
        select_ilce.select_by_visible_text(ilce)

        # İlçe seçiminden sonra yüklenmenin bitmesini bekleyin
        wait_for_loading_to_finish(driver)

        # Mahalle dropdown'unun yüklenmesini bekleyin
        mahalle_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "neighborhood-select"))
        )
        select_mahalle = Select(mahalle_dropdown)

        # Girilen mahalle adının ilk üç harfi ile eşleşen bir seçenek bulma
        for option in select_mahalle.options:
            if option.text[:3].lower() == mahalle[:3].lower():
                select_mahalle.select_by_visible_text(option.text)
                break

        # Mahalle seçiminden sonra yüklenmenin bitmesini bekleyin
        wait_for_loading_to_finish(driver)

        # Ada numarası girişi
        ada_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "block-input"))
        )
        ada_input.send_keys(ada)

        # Parsel numarası girişi
        parsel_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "parcel-input"))
        )
        parsel_input.send_keys(parsel)

        # Formu gönderme
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "administrative-query-btn"))
        )
        submit_button.click()

        # Sorgula butonuna bastıktan sonra yüklenmenin bitmesini bekleyin
        wait_for_loading_to_finish(driver)

        # Mesajı alacak olan span elementi
        span_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "span-message"))
        )

        # Span elementinin içeriğini al
        message = span_message.text.strip()

        # İçerik kontrolü ve mesaj yazdırma
        if message == "Kayıt Bulunamadı":
            print("Kayıt Bulunamadı")
        elif message == "Parsel bilgilerini görüntülemek için seçili parsele tıklayınız.":
            print("Parsel bilgilerini görüntülemek için seçili parsele tıklayınız.")



    finally:
        # Tarayıcıyı kapatma (gerekirse)
        # driver.quit()
        while True:
            continue
