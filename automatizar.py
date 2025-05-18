from pickle import STRING

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
import os
from time import sleep


def automacao(str_url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Firefox(options=options) 
    links = []

    driver.get(str_url)

    path0 = "/html/body/div[1]/main/div/div/div/div[1]/section/div/ul/li"

    print("Abrindo CNN e pegando notícias")

    caminho_noticias = driver.find_elements(By.XPATH, path0)

    for i in range(len(caminho_noticias)):
        if i == 0:
            continue
        xpath_noticias = os.path.join(path0[0:-3], f"li[{i}]/a")

        try:
            link_noticias = driver.find_element(By.XPATH, xpath_noticias)
            link = link_noticias.get_attribute("href")

            links.append(link)

        except:
            continue

    print(f"Foram encontrados {len(links)} links")

    driver.quit()

    return links


def pegar_materias(lista_links):
    lista_titulos = []

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Firefox(options=options)

    for link in lista_links:
        driver.get(link)

        try:    
            xpath_titulo = "/html/body/div[1]/div[2]/div/main/article/header/h1"
            elemento_titulo = driver.find_element(By.XPATH, xpath_titulo)

            titulo = elemento_titulo.text
            lista_titulos.append(titulo)

        except TimeoutException:
            print("Tempo para carregar página de título superado, parando e indo para o próximo")
            driver.execute_script("window.stop()")
            sleep(2)
            continue
        except:
            continue

    driver.quit()
    return lista_links, lista_titulos


def pega_os_paragrafos(lista_links, lista_titulos):
    lista_final_noticias = []
    count = 0

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Firefox(options=options)

    for link, titulo in zip(lista_links, lista_titulos):
        lista_noticia_atual = []
        driver.get(link)

        lista_noticia_atual.append(lista_titulos[count])
        count += 1

        xpath_count_paragrafes = "/html/body/div[1]/div[2]/div/main/article/div[2]/p"
        elements_xpath_count_paragrafes = driver.find_elements(By.XPATH, xpath_count_paragrafes)

        count_paragrafos = len(elements_xpath_count_paragrafes) + 1

        for i in range(1, count_paragrafos):
            xpath_paragrafes = xpath_count_paragrafes + f"[{i}]"

            try:
                texto = driver.find_element(By.XPATH, xpath_paragrafes).text

                if texto in ["Leia também:", "LEIA TAMBÉM:"]:
                    print("Texto sem importância. Parando...")
                    break

                lista_noticia_atual.append(texto)
            except:
                print("Erro: elemento não encontrado")

        lista_final_noticias.append(lista_noticia_atual)

    driver.quit()
    return lista_final_noticias


def convert_str(lista_final_noticias):
    lista_final = ""
    for noticia in range(len(lista_final_noticias)):
        lista = "\n".join(lista_final_noticias[noticia])
        lista_final += lista
    return lista_final


def chamada(str_url):
    lista_links, lista_titulos = pegar_materias(automacao(str_url))
    saida = convert_str(pega_os_paragrafos(lista_links, lista_titulos))
    return saida
