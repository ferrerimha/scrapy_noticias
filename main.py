import automatizar
import tela

if __name__ == "__main__":
    noticias = automatizar.chamada("https://www.cnnbrasil.com.br/tecnologia/")
    dsplay = tela.Tela("1366x768", "Noticias Tech")
    dsplay.create_display(noticias)