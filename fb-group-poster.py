from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Konfigurasi akun dan grup

GROUP_URL = "https://www.facebook.com/groups/262280437314039/"
POST_MESSAGE = (
    "https://id.shp.ee/cLDLdo2\n\n"
    "Yang butuh VPS Forex bisa sampai 3 MT4.\n"
    "Harga promo 50rb-an buat 1 tahun.\n"
    "Gass co Shopee!"
)

# Inisialisasi browser
## # local windows
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(r"--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
chrome_options.add_argument("--profile-directory=Default")

## # local MacOS
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--user-data-dir=/Users/herdy/Downloads/fb/chrome-profile-selenium")
# chrome_options.add_argument("--profile-directory=Default")


while True:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(GROUP_URL)

    wait = WebDriverWait(driver, 30)
    buat_postingan_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".xkjl1po > .x1lliihq"))
    )
    buat_postingan_btn.click()

    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "._5rpu"))
    )
    input_postingan = driver.find_element(By.CSS_SELECTOR, "._5rpu")
    input_postingan.click()
    input_postingan.send_keys(POST_MESSAGE)

    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".x1l90r2v:nth-child(3) > .x9f619 > .x9f619 > .x1i10hfl > .x1ja2u2z"))
    )
    driver.find_element(By.CSS_SELECTOR, ".x1l90r2v:nth-child(3) > .x9f619 > .x9f619 > .x1i10hfl > .x1ja2u2z").click()
    time.sleep(random.randint(5, 10))  # Tunggu antara 5 hingga 10 detik

    driver.quit()  # Tutup browser sebelum menunggu 1 jam
    print("Berhasil posting. Menunggu 1 jam untuk posting berikutnya...")
    time.sleep(3600)  # Tunggu 1 jam sebelum posting berikutnya