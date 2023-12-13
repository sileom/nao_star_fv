import os
from distutils import command
from tkinter import messagebox

from ultralytics import YOLO
import PIL
import customtkinter
import pyttsx3
import torch
import cv2
from PIL import ImageFile

import tensorflow as tf
from tensorflow.lite.python.interpreter import Interpreter

import mediapipe as mp
from PIL import Image
from PIL import ImageTk
import zmq
from subprocess import run

import numpy as np
import cv2
import time
from tktooltip import ToolTip

# impedisce lo scalamento dello sfondo
customtkinter.deactivate_automatic_dpi_awareness()
# settaggi per lo stile della libreria customtkinter
customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("blue")


class App:

    def __init__(self):

        #self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        self.finestra = Finestra()
        self.frame_benvenuto = FrameBenvenuto(self.finestra)
        self.frame_menu = FrameMenu(self.finestra)
        self.frame_colloquio_iniziale = FrameColloquioIniziale(self.finestra)
        self.frame_touch_me = FrameTouchMe(self.finestra)
        self.frame_congedo = FrameCongedo(self.finestra)
        self.frame_balla = FrameBalla(self.finestra)
        self.frame_canta = FrameCanta(self.finestra)
        self.frame_motricita = FrameMotricita(self.finestra)
        self.frame_riepilogo_dati = FrameRiepilogoDati(self.finestra)
        self.frame_imitare_versi = FrameImitareVersi(self.finestra)
        self.frame_guarda = FrameGuarda(self.finestra)
        self.frame_registra = FrameRegistra(self.finestra)
        self.frame_fammi_vedere = FrameFammiVedere(self.finestra)
        # il client crea una socket_azioni e si collega al server di azioni sulla porta 5555
        self.context = zmq.Context()
        self.nome = ""
        self.socket_azioni = self.context.socket(zmq.REQ)
        self.socket_azioni.connect("tcp://localhost:5555")

    def get_socket_azioni(self):
        return self.socket_azioni



    def get_nome(self):
        print(self.nome)
        return self.nome


    def get_context(self):
        return self.context

    def get_frame_benvenuto(self):
        self.frame_menu.destroy()
        if not self.frame_benvenuto.winfo_exists():
            self.frame_benvenuto = FrameBenvenuto(self.finestra)
        self.frame_benvenuto.visualizza()

    def get_frame_menu(self, nome_bambino):
        if nome_bambino == "":
            messagebox.showinfo(title="info", message="Bisogna inserire un nome")
            return
        self.nome = nome_bambino
        self.frame_benvenuto.destroy()
        if not self.frame_menu.winfo_exists():
            self.frame_menu = FrameMenu(self.finestra)
        self.frame_menu.visualizza()

    def get_frame_colloquio_iniziale(self):
        self.frame_menu.destroy()
        if not self.frame_colloquio_iniziale.winfo_exists():
            self.frame_colloquio_iniziale = FrameColloquioIniziale(self.finestra)
        self.frame_colloquio_iniziale.visualizza()

    def get_frame_touch_me(self):
        self.frame_menu.destroy()
        if not self.frame_touch_me.winfo_exists():
            self.frame_touch_me = FrameTouchMe(self.finestra)
        self.frame_touch_me.visualizza()

    def get_frame_congedo(self):
        self.frame_menu.destroy()
        if not self.frame_congedo.winfo_exists():
            self.frame_congedo = FrameCongedo(self.finestra)
        self.frame_congedo.visualizza()

    def get_frame_balla(self):
        self.frame_menu.destroy()
        if self.frame_congedo.winfo_exists():
            self.frame_congedo.destroy()
        if not self.frame_balla.winfo_exists():
            self.frame_balla = FrameBalla(self.finestra)
        self.frame_balla.visualizza()

    def get_frame_canta(self):
        self.frame_menu.destroy()
        if not self.frame_canta.winfo_exists():
            self.frame_canta = FrameCanta(self.finestra)
        self.frame_canta.visualizza()

    def get_frame_motricita(self):
        self.frame_menu.destroy()
        if not self.frame_motricita.winfo_exists():
            self.frame_motricita = FrameMotricita(self.finestra)
        self.frame_motricita.visualizza()

    def get_frame_riepilogo_dati(self):
        self.frame_menu.destroy()
        if not self.frame_riepilogo_dati.winfo_exists():
            self.frame_riepilogo_dati = FrameRiepilogoDati(self.finestra)
        self.frame_riepilogo_dati.visualizza()

    def get_frame_registra(self):
        self.frame_menu.destroy()
        if not self.frame_registra.winfo_exists():
            self.frame_registra = FrameRegistra(self.finestra)
        self.frame_registra.visualizza()

    def get_frame_imitare_versi(self):
        self.frame_menu.destroy()
        if not self.frame_imitare_versi.winfo_exists():
            self.frame_imitare_versi = FrameImitareVersi(self.finestra)
        self.frame_imitare_versi.visualizza()

    def get_frame_guarda(self):
        self.frame_menu.destroy()
        if not self.frame_guarda.winfo_exists():
            self.frame_guarda = FrameGuarda(self.finestra)
        self.frame_guarda.visualizza()

    def get_frame_fammi_vedere(self):
        self.frame_menu.destroy()
        if not self.frame_fammi_vedere.winfo_exists():
            self.frame_fammi_vedere = FrameFammiVedere(self.finestra)
        self.frame_fammi_vedere.visualizza()

    def action_comeback(self, frame):
        frame.destroy()
        self.frame_menu = FrameMenu(self.finestra)
        self.frame_menu.visualizza()

    def run_app(self):
        self.finestra.visualizza()
        self.frame_benvenuto.visualizza()
        self.finestra.mainloop()


class Finestra(customtkinter.CTk):

    def __init__(self):
        super().__init__()


    def on_closing(self):
        instance = get_applicazione()
        socket_azioni = instance.get_socket_azioni()
        socket_azioni.send_string("chiudi")
        socket_azioni.close()
        self.destroy()

    def visualizza(self):
        self.state("zoomed")
        #self.attributes("-fullscreen", True)
        self.title("NAOAvatar Controller Pad")
        self.iconbitmap(r"immagini/favicon.ico")
        self.protocol("WM_DELETE_WINDOW", lambda: self.on_closing())


class FrameBenvenuto(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)



    def visualizza(self):

        def avviaMenu():
            socket_azioni = instance.get_socket_azioni()
            socket_azioni.send_string("Nome_" + entry_nome.get())
            risultato = socket_azioni.recv_string()
            print(risultato)
            instance.get_frame_menu(entry_nome.get())
            

        instance = get_applicazione()
        self.columnconfigure(0, weight=1, uniform='third')
        self.rowconfigure(0, weight=1, uniform='third')
        self.pack(expand=True, fill="both")
        self.configure(fg_color="transparent")
        # TODO: vedere come ridimensionare lo sfondo
        bg_image = customtkinter.CTkImage(Image.open("immagini/sfondo_benvenuto.jpg"),
                                          size=(instance.finestra.winfo_width(), instance.finestra.winfo_height()))
        bg_image_label = customtkinter.CTkLabel(self, text="", image=bg_image)
        bg_image_label.grid(row=0, column=0)

        frame_appoggio = customtkinter.CTkFrame(self, fg_color="#6CDACD")
        label = customtkinter.CTkLabel(frame_appoggio,
                                       text="Benvenuto,\ninserire i dati",
                                       font=("Georgia", 30, "bold"))
        label_nome = customtkinter.CTkLabel(frame_appoggio, text="Nome del bambino: ", font=("Georgia", 24))
        entry_nome = customtkinter.CTkEntry(frame_appoggio, font=("Georgia", 24), width=300)
        entry_nome.configure(placeholder_text="NOME")
        button_avvio = customtkinter.CTkButton(frame_appoggio, text="Inizio terapia", font=("Georgia", 24),
                                               command=avviaMenu)

        label_frase = customtkinter.CTkLabel(self, text="Progetto stella", fg_color="#DDF5F5",
                                             font=("Georgia", 40, "bold"))
        label_frase.grid(row=0, column=0, sticky="n", pady=150)

        label.pack(ipadx=20, ipady=20, anchor="center")
        label_nome.pack(pady=20)
        entry_nome.pack(pady=2)
        button_avvio.pack(pady=20, ipadx=5, ipady=5, anchor="center")
        frame_appoggio.grid(row=0, column=0, ipadx=25)


class FrameMenu(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.label_image1 = None
        self.volume = None

    def visualizza(self):

        def setVolume():
            self.volume = int(entry_volume.get())
            if(self.volume< 0 or self.volume >100):
                print("ciao")
                messagebox.showinfo(title="info", message="Bisogna inserire un valore di volume tra 0 e 100")
            else:
                socket_azioni = instance.get_socket_azioni()

                entry_volume.configure(placeholder_text=self.volume)
                socket_azioni.send_string("volume_"+str(self.volume))
                risultato = socket_azioni.recv_string()
                print(risultato)


        instance = get_applicazione()
        self.columnconfigure(0, weight=2, uniform='third')
        self.columnconfigure(1, weight=1, uniform='third')
        self.rowconfigure(0, weight=1, uniform='third')
        self.pack(expand=True, fill="both")
        self.configure(fg_color="#C1DEF5")

        bg_image = customtkinter.CTkImage(Image.open("immagini/sfondo_finestre.jpg"),
                                          size=(instance.finestra.winfo_width(), instance.finestra.winfo_height()))
        bg_image_label = customtkinter.CTkLabel(self, text="", image=bg_image)
        bg_image_label.grid(row=0, column=0, columnspan=2)

        frame_bottoni = customtkinter.CTkFrame(self, fg_color="#C1DEF5")
        frame_camere = customtkinter.CTkFrame(self, fg_color="transparent")

        # creazione dei bottoni
        font_bottoni = customtkinter.CTkFont(family="Georgia", size=15, weight="bold")
        button_colloquio_iniziale = customtkinter.CTkButton(frame_bottoni, text="Colloquio\niniziale",
                                                            font=font_bottoni, fg_color="#419797",
                                                            hover_color="#1F4747",
                                                            command=instance.get_frame_colloquio_iniziale)
        button_touch_me = customtkinter.CTkButton(frame_bottoni, text="Touch me", font=font_bottoni, fg_color="#5F6D67",
                                                  hover_color="#2F3734",
                                                  command=instance.get_frame_touch_me)
        button_congedo = customtkinter.CTkButton(frame_bottoni, text="Congedo", font=font_bottoni, fg_color="#419797",
                                                 hover_color="#1F4747",
                                                 command=instance.get_frame_congedo)
        button_balla = customtkinter.CTkButton(frame_bottoni, text="Balla", font=font_bottoni, fg_color="#5F6D67",
                                               hover_color="#2F3734",
                                               command=instance.get_frame_balla)
        button_canta = customtkinter.CTkButton(frame_bottoni, text="Canta", font=font_bottoni, fg_color="#5F6D67",
                                               hover_color="#2F3734",
                                               command=instance.get_frame_canta)
        button_motricita = customtkinter.CTkButton(frame_bottoni, text="Motricita'", font=font_bottoni,
                                                   fg_color="#5F6D67", hover_color="#2F3734",
                                                   command=instance.get_frame_motricita)
        button_imitare_versi = customtkinter.CTkButton(frame_bottoni, text="Imitare versi", font=font_bottoni,
                                                       fg_color="#62569F", hover_color="#302B4F",
                                                       command=instance.get_frame_imitare_versi)
        button_guarda = customtkinter.CTkButton(frame_bottoni, text="Guarda", font=font_bottoni,
                                                fg_color="#62569F", hover_color="#302B4F",command=instance.get_frame_guarda )
        button_fammi_vedere = customtkinter.CTkButton(frame_bottoni, text="Fammi vedere", font=font_bottoni,
                                                      fg_color="#62569F", hover_color="#302B4F", command= instance.get_frame_fammi_vedere)
        button_riepilogo_dati_bambino = customtkinter.CTkButton(frame_bottoni, text="Riepilogo\ndati",
                                                                font=font_bottoni, fg_color="#9F6756",
                                                                hover_color="#6A4539",
                                                                command=instance.get_frame_riepilogo_dati)
        button_registrare_frasi_terapista = customtkinter.CTkButton(frame_bottoni,
                                                                    text="Registrare frasi\ndel terapista",
                                                                    fg_color="#9F6756", hover_color="#6A4539",
                                                                    font=font_bottoni,command = instance.get_frame_registra)


        for x in range(3):
            frame_bottoni.columnconfigure(x, weight=1, uniform='third')

        for x in range(4):
            frame_bottoni.rowconfigure(x, weight=1, uniform='third')

        # immagini test nel frame delle telecamere

        image1 = customtkinter.CTkImage(Image.open("immagini/sfondo_finestre.jpg"), size=(300, 300))
        self.label_image1 = customtkinter.CTkLabel(frame_camere, image=image1, text="")

        label_volume = customtkinter.CTkLabel(frame_camere, text="Volume : ", font=("Georgia", 24))

       


        button_torna_al_menu = customtkinter.CTkButton(frame_camere, text="Indietro",
                                                       font=font_bottoni, command=instance.get_frame_benvenuto)
        entry_volume = customtkinter.CTkEntry(frame_camere, font=("Georgia", 24), width=200)
        entry_volume.configure(placeholder_text="50")
        button_volume = customtkinter.CTkButton(frame_camere, text="Imposta\nVolume",
                                                       font=font_bottoni,command = setVolume)
        button_colloquio_iniziale.grid(row=0, column=0, sticky="news", padx=50, pady=50)
        button_touch_me.grid(row=0, column=1, sticky="news", padx=50, pady=50)
        button_congedo.grid(row=0, column=2, sticky="news", padx=50, pady=50)
        button_balla.grid(row=1, column=0, sticky="news", padx=50, pady=50)
        button_canta.grid(row=1, column=1, sticky="news", padx=50, pady=50)
        button_motricita.grid(row=1, column=2, sticky="news", padx=50, pady=50)
        button_imitare_versi.grid(row=2, column=0, sticky="news", padx=50, pady=50)
        button_guarda.grid(row=2, column=1, sticky="news", padx=50, pady=50)
        button_fammi_vedere.grid(row=2, column=2, sticky="news", padx=50, pady=50)
        button_riepilogo_dati_bambino.grid(row=3, column=0, sticky="news", padx=50, pady=50)
        button_registrare_frasi_terapista.grid(row=3, column=2, sticky="news", padx=50, pady=50)


        self.label_image1.pack(expand=True)
        label_volume.pack(side="left", padx=10, pady=10)
        entry_volume.pack(side="left", pady=3)
        button_volume.pack(ipadx=20, ipady=20,pady=3)

        button_torna_al_menu.pack(ipadx=20, ipady=20, pady=20)
        frame_bottoni.grid(row=0, column=0, sticky="news", padx=50, pady=50)
        frame_camere.grid(row=0, column=1, sticky="news")
        

        def aggiorna_label():
            # oppure
            instance.socket_azioni.send_string("catturaimmagine_upper")
            im_dec = instance.socket_azioni.recv()
            im = cv2.imdecode(np.frombuffer(im_dec, np.uint8), cv2.IMREAD_COLOR)
            im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(im)
            ImageFile.LOAD_TRUNCATED_IMAGES = True
            try:
                image = customtkinter.CTkImage(im, size=(500, 500))
                self.label_image1.configure(image=image)
            except PIL.UnidentifiedImageError:
                pass
            self.label_image1.after(10, aggiorna_label)

        aggiorna_label()


class FrameColloquioIniziale(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

    def visualizza(self):

        def azione_primo_incontro():
            socket_azioni = instance.get_socket_azioni()
            socket_azioni.send_string("primo incontro")
            risultato = socket_azioni.recv_string()
            print(risultato)

        def azione_secondo_incontro():
            socket_azioni = instance.get_socket_azioni()
            socket_azioni.send_string("secondo incontro")
            risultato = socket_azioni.recv_string()
            print(risultato)

        def azione_bravo():
            socket_azioni = instance.get_socket_azioni()
            testo = "Bravo"
            socket_azioni.send_string("riproduci_" + testo)
            socket_azioni.recv_string()
            lista_esiti.append("Colloquio iniziale ok")
            lista_esiti_globale.append("Colloquio iniziale ok")

                    
        def riproduci_testo():
            socket_azioni = instance.get_socket_azioni()
            testo = entry_testo.get()
            socket_azioni.send_string("riproduci_" + testo)
            socket_azioni.recv_string()        

        instance = get_applicazione()
        self.pack(expand=True, fill="both")
        self.configure(fg_color="#DAF2F2")
        bg_image = customtkinter.CTkImage(Image.open("immagini/sfondo_finestre.jpg"),
                                          size=(instance.finestra.winfo_width(), instance.finestra.winfo_height()))
        bg_image_label = customtkinter.CTkLabel(self, text="", image=bg_image)
        bg_image_label.grid(row=0, column=0, columnspan=4, rowspan=3)

        for x in range(4):
            self.columnconfigure(x, weight=1, uniform='third')

        for x in range(3):
            self.rowconfigure(x, weight=1, uniform='third')

        label = customtkinter.CTkLabel(self, text="Colloquio\niniziale", font=("Georgia", 30, "bold"),
                                       fg_color="#DCF4F4")
        button_primo_incontro = customtkinter.CTkButton(self, text="Primo incontro", font=("Georgia", 22, "bold"),
                                                        fg_color="#419797", hover_color="#1F4747",
                                                        height=60, width=250, command=azione_primo_incontro)
        button_secondo_incontro = customtkinter.CTkButton(self, text="Secondo incontro", font=("Georgia", 22, "bold"),
                                                          fg_color="#419797", hover_color="#1F4747",
                                                          height=60, width=250, command=azione_secondo_incontro)
        button_menu_principale = customtkinter.CTkButton(self, text="Menu' principale", font=("Georgia", 22, "bold"),
                                                         bg_color="#CBEDEC",
                                                         command=lambda: instance.action_comeback(self))

        label.grid(row=0, column=1, columnspan=2)
        button_primo_incontro.grid(row=1, column=1)
        button_secondo_incontro.grid(row=1, column=2)
        button_menu_principale.grid(row=2, column=3, sticky="se", padx=50, pady=50, ipadx=25, ipady=25)

        button_bravo = customtkinter.CTkButton(self, text="Bravo", font=("Georgia", 22, "bold"),
                                            fg_color="#62569F", hover_color="#302B4F",
                                            command=azione_bravo)
        label_testo = customtkinter.CTkLabel(self, text="Inserisci testo", font=("Georgia", 22, "bold"))
        entry_testo = customtkinter.CTkEntry(self, font=("Georgia", 22), width=150,height=50)
        button_riproduci= customtkinter.CTkButton(self, text="Riproduci frase",
                                                       font=("Georgia", 22, "bold"),command = riproduci_testo)
        button_bravo.grid(row=2, column=2, sticky="s", padx=50, pady=50, ipadx=50, ipady=25)
        label_testo.grid(row=2, column=0, sticky="e", padx=50)
        entry_testo.grid(row=2, column=0, sticky="se", padx=10, pady=30, ipadx=30, ipady=25)
        button_riproduci.grid(row=2, column=1, sticky="s", padx=10, pady=50, ipadx=10, ipady=25)


class FrameTouchMe(customtkinter.CTkFrame):


    def __int__(self, master):
        super().__init__(master)


    def visualizza(self):

        def azione_touch_me_testa():
            socket_azioni = instance.get_socket_azioni()
            socket_azioni.send_string("tocca_lamiatesta")
            risultato = socket_azioni.recv_string()
            print(risultato)

        def azione_mano_destra():
                socket_azioni = instance.get_socket_azioni()
                socket_azioni.send_string("tocca_lamiamanodestra")
                risultato = socket_azioni.recv_string()
                print(risultato)

        def azione_mano_sinistra():
                socket_azioni = instance.get_socket_azioni()
                socket_azioni.send_string("tocca_lamiamanosinistra")
                risultato = socket_azioni.recv_string()
                print(risultato)
        def azione_piede_destro():
                socket_azioni = instance.get_socket_azioni()
                socket_azioni.send_string("tocca_ilmiopiededestro")
                risultato = socket_azioni.recv_string()
                print(risultato)
        def azione_piede_sinistro():
                socket_azioni = instance.get_socket_azioni()
                socket_azioni.send_string("tocca_ilmiopiedesinistro")
                risultato = socket_azioni.recv_string()
                print(risultato)
        def azione_bravo():
            socket_azioni = instance.get_socket_azioni()
            testo = "Bravo"
            socket_azioni.send_string("riproduci_" + testo)
            socket_azioni.recv_string()
            lista_esiti.append("TouchMe ok")
            lista_esiti_globale.append("TouchMe ok")

        def riproduci_testo():
            socket_azioni = instance.get_socket_azioni()
            testo = entry_testo.get()
            socket_azioni.send_string("riproduci_" + testo)
            socket_azioni.recv_string()

        instance = get_applicazione()
        self.pack(expand=True, fill="both")
        self.configure(fg_color="#DAF2F2")
        bg_image = customtkinter.CTkImage(Image.open("immagini/sfondo_finestre.jpg"),
                                          size=(instance.finestra.winfo_width(), instance.finestra.winfo_height()))
        bg_image_label = customtkinter.CTkLabel(self, text="", image=bg_image)
        bg_image_label.grid(row=0, column=0, columnspan=3, rowspan=4)
        for x in range(3):
            self.columnconfigure(x, weight=1, uniform='third')

        for x in range(4):
            self.rowconfigure(x, weight=1, uniform='third')

        label = customtkinter.CTkLabel(self, text="Touch\nMe", font=("Georgia", 30, "bold"))
        button_tocca_testa = customtkinter.CTkButton(self, text="Toccami la testa", font=("Georgia", 22, "bold"),
                                                     height=60, width=330, fg_color="#5F6D67", hover_color="#2F3734",
                                                     bg_color="#D9F1F1",command =azione_touch_me_testa)
        button_tocca_mano_destra = customtkinter.CTkButton(self, text="Toccami la mano destra",
                                                           height=60, width=330, fg_color="#5F6D67",
                                                           hover_color="#2F3734",
                                                           font=("Georgia", 22, "bold"),command =azione_mano_destra)
        button_tocca_mano_sinistra = customtkinter.CTkButton(self, text="Toccami la mano sinistra",
                                                             height=60, width=330, fg_color="#5F6D67",
                                                             hover_color="#2F3734",
                                                             font=("Georgia", 22, "bold"),command= azione_mano_sinistra)
        button_tocca_piede_destro = customtkinter.CTkButton(self, text="Toccami il piede destro",
                                                            height=60, width=330, fg_color="#5F6D67",
                                                            hover_color="#2F3734",
                                                            font=("Georgia", 22, "bold"),command= azione_piede_destro)
        button_tocca_piede_sinistro = customtkinter.CTkButton(self, text="Toccami il piede sinistro",
                                                              height=60, width=330, fg_color="#5F6D67",
                                                              hover_color="#2F3734",
                                                              font=("Georgia", 22, "bold"),command = azione_piede_sinistro)
        button_menu_principale = customtkinter.CTkButton(self, text="Menu' principale", font=("Georgia", 22, "bold"),
                                                         command=lambda: instance.action_comeback(self))
        label.grid(row=0, column=1)
        button_tocca_testa.grid(row=1, column=0, sticky="e")
        button_tocca_mano_sinistra.grid(row=1, column=1)
        button_tocca_mano_destra.grid(row=1, column=2, sticky="w")
        button_tocca_piede_sinistro.grid(row=2, column=0, sticky="e")
        button_tocca_piede_destro.grid(row=2, column=1)
        button_menu_principale.grid(row=3, column=2, sticky="se", padx=50, pady=50, ipadx=50, ipady=25)

        button_bravo = customtkinter.CTkButton(self, text="Bravo", font=("Georgia", 22, "bold"),
                                            fg_color="#62569F", hover_color="#302B4F",
                                            command=azione_bravo)
        label_testo = customtkinter.CTkLabel(self, text="Inserisci testo", font=("Georgia", 22, "bold"))
        entry_testo = customtkinter.CTkEntry(self, font=("Georgia", 22), width=150,height=50)
        button_riproduci= customtkinter.CTkButton(self, text="Riproduci frase",
                                                       font=("Georgia", 22, "bold"),command = riproduci_testo)
        button_bravo.grid(row=3, column=1, sticky="s", padx=50, pady=50, ipadx=50, ipady=25)
        label_testo.grid(row=3, column=0, sticky="nw", pady=50, padx=130)
        entry_testo.grid(row=3, column=0, sticky="sw", padx=100, pady=30, ipadx=30, ipady=25)
        button_riproduci.grid(row=3, column=0, sticky="se", padx=0, pady=50, ipadx=0, ipady=25)


class FrameCongedo(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

    def visualizza(self):

        def azione_congedo():
            socket_azioni = instance.get_socket_azioni()
            print(instance.get_nome())
            socket_azioni.send_string("Congedo_"+instance.get_nome())
            risultato = socket_azioni.recv_string()
            print(risultato)

        def azione_bravo():
            socket_azioni = instance.get_socket_azioni()
            testo = "Bravo"
            socket_azioni.send_string("riproduci_" + testo)
            socket_azioni.recv_string()
            lista_esiti.append("Congedo ok")
            lista_esiti_globale.append("Congedo ok")
                    
        def riproduci_testo():
            socket_azioni = instance.get_socket_azioni()
            testo = entry_testo.get()
            socket_azioni.send_string("riproduci_" + testo)
            socket_azioni.recv_string()


        instance = get_applicazione()
        self.pack(expand=True, fill="both")
        self.configure(fg_color="#DAF2F2")

        bg_image = customtkinter.CTkImage(Image.open("immagini/sfondo_finestre.jpg"),
                                          size=(instance.finestra.winfo_width(), instance.finestra.winfo_height()))
        bg_image_label = customtkinter.CTkLabel(self, text="", image=bg_image)
        bg_image_label.grid(row=0, column=0, columnspan=3, rowspan=3)

        for x in range(3):
            self.columnconfigure(x, weight=1, uniform='third')

        for x in range(3):
            self.rowconfigure(x, weight=1, uniform='third')

        label = customtkinter.CTkLabel(self, text="Congedo", font=("Georgia", 30, "bold"))
        button_balla = customtkinter.CTkButton(self, text="Balla", font=("Georgia", 22, "bold"),
                                               height=60, width=160, fg_color="#419797", hover_color="#1F4747",
                                               command=lambda: instance.get_frame_balla())
        button_saluta = customtkinter.CTkButton(self, text="Saluta", font=("Georgia", 22, "bold"),
                                                fg_color="#419797", hover_color="#1F4747",
                                                height=60, width=160, command=azione_congedo)
        button_menu_principale = customtkinter.CTkButton(self, text="Menu' principale", font=("Georgia", 22, "bold"),
                                                         command=lambda: instance.action_comeback(self))

        label.grid(row=0, column=1)
        button_balla.grid(row=1, column=0, sticky="e")
        button_saluta.grid(row=1, column=2, sticky="w")
        button_menu_principale.grid(row=2, column=2, sticky="se", padx=50, pady=50, ipadx=50, ipady=25)

        button_bravo = customtkinter.CTkButton(self, text="Bravo", font=("Georgia", 22, "bold"),
                                            fg_color="#62569F", hover_color="#302B4F",
                                            command=azione_bravo)
        label_testo = customtkinter.CTkLabel(self, text="Inserisci testo", font=("Georgia", 22, "bold"))
        entry_testo = customtkinter.CTkEntry(self, font=("Georgia", 22), width=150,height=50)
        button_riproduci= customtkinter.CTkButton(self, text="Riproduci frase",
                                                       font=("Georgia", 22, "bold"),command = riproduci_testo)
        button_bravo.grid(row=2, column=1, sticky="s", padx=50, pady=50, ipadx=50, ipady=25)
        label_testo.grid(row=2, column=0, sticky="nw", pady=120, padx=130)
        entry_testo.grid(row=2, column=0, sticky="sw", padx=100, pady=30, ipadx=30, ipady=25)
        button_riproduci.grid(row=2, column=0, sticky="se", padx=0, pady=50, ipadx=0, ipady=25)


class FrameBalla(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

    def visualizza(self):

        def azione_ballo_baby_shark():
            socket_azioni = instance.get_socket_azioni()
            socket_azioni.send_string("Ballo_BabyShark")
            risultato = socket_azioni.recv_string()
            print(risultato)

        def azione_ballo_mercoledi():
            socket_azioni = instance.get_socket_azioni()
            socket_azioni.send_string("Ballo_Mercoledi")
            risultato = socket_azioni.recv_string()
            print(risultato)

        def azione_ballo_whisky():
            socket_azioni = instance.get_socket_azioni()
            socket_azioni.send_string("Ballo_WhiskyIlRagnetto")
            risultato = socket_azioni.recv_string()
            print(risultato)

        def azione_stop():
            socket_azioni = instance.get_socket_azioni()
            socket_azioni.send_string("stop ballo")
            risultato = socket_azioni.recv_string()
            print(risultato)

        def riproduci_testo():
            socket_azioni = instance.get_socket_azioni()
            testo = entry_testo.get()
            socket_azioni.send_string("riproduci_" + testo)
            socket_azioni.recv_string()

        def azione_bravo():
            socket_azioni = instance.get_socket_azioni()
            testo = "Bravo"
            socket_azioni.send_string("riproduci_" + testo)
            socket_azioni.recv_string()
            lista_esiti.append("Ballo ok")
            lista_esiti_globale.append("Ballo ok")

        instance = get_applicazione()
        self.pack(expand=True, fill="both")
        self.configure(fg_color="#DAF2F2")

        bg_image = customtkinter.CTkImage(Image.open("immagini/sfondo_finestre.jpg"),
                                          size=(instance.finestra.winfo_width(), instance.finestra.winfo_height()))
        bg_image_label = customtkinter.CTkLabel(self, text="", image=bg_image)
        bg_image_label.grid(row=0, column=0, columnspan=3, rowspan=3)

        for x in range(3):
            self.columnconfigure(x, weight=1, uniform='third')

        for x in range(3):
            self.rowconfigure(x, weight=1, uniform='third')

        label = customtkinter.CTkLabel(self, text="Balla", font=("Georgia", 30, "bold"))
        button_ballo_1 = customtkinter.CTkButton(self, text="Baby shark", font=("Georgia", 22, "bold"),
                                                 fg_color="#5F6D67", hover_color="#2F3734",
                                                 height=60, width=210, command=azione_ballo_baby_shark)
        button_ballo_2 = customtkinter.CTkButton(self, text="Mercoledi'", font=("Georgia", 22, "bold"),
                                                 fg_color="#5F6D67", hover_color="#2F3734",
                                                 height=60, width=210, command=azione_ballo_mercoledi)
        button_ballo_3 = customtkinter.CTkButton(self, text="Whisky il ragnetto", font=("Georgia", 22, "bold"),
                                                 fg_color="#5F6D67", hover_color="#2F3734",
                                                 height=60, width=210, command=azione_ballo_whisky)
        button_menu_principale = customtkinter.CTkButton(self, text="Menu' principale", font=("Georgia", 22, "bold"),
                                                         command=lambda: instance.action_comeback(self))
        button_pausa = customtkinter.CTkButton(self, text="Stop", font=("Georgia", 22, "bold"),
                                               fg_color="#B71528", hover_color="#6E0D18", command=azione_stop)

        label.grid(row=0, column=1)
        button_ballo_1.grid(row=1, column=0, sticky="e")
        button_ballo_2.grid(row=1, column=1)
        button_ballo_3.grid(row=1, column=2, sticky="w")
        button_pausa.grid(row=2, column=1, sticky="s", padx=50, pady=50, ipadx=25, ipady=25)
        button_menu_principale.grid(row=2, column=2, sticky="se", padx=50, pady=50, ipadx=50, ipady=25)

        button_bravo = customtkinter.CTkButton(self, text="Bravo", font=("Georgia", 22, "bold"),
                                            fg_color="#62569F", hover_color="#302B4F",
                                            command=azione_bravo)
        label_testo = customtkinter.CTkLabel(self, text="Inserisci testo", font=("Georgia", 22, "bold"))
        entry_testo = customtkinter.CTkEntry(self, font=("Georgia", 22), width=150,height=50)
        button_riproduci= customtkinter.CTkButton(self, text="Riproduci frase",
                                                       font=("Georgia", 22, "bold"),command = riproduci_testo)
        button_bravo.grid(row=2, column=1, sticky="s", padx=50, pady=50, ipadx=50, ipady=25)
        label_testo.grid(row=2, column=0, sticky="nw", pady=120, padx=130)
        entry_testo.grid(row=2, column=0, sticky="sw", padx=100, pady=30, ipadx=30, ipady=25)
        button_riproduci.grid(row=2, column=0, sticky="se", padx=0, pady=50, ipadx=0, ipady=25)
        button_pausa.grid(row=2, column=2, sticky="sw", padx=0, pady=50, ipadx=0, ipady=25)


class FrameCanta(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

    def visualizza(self):

        def azione_canzone_baby_shark():
            socket_azioni = instance.get_socket_azioni()
            socket_azioni.send_string("Audio_BabyShark")
            risultato = socket_azioni.recv_string()
            print(risultato)

        def azione_canzone_coccodrillo():
            socket_azioni = instance.get_socket_azioni()
            socket_azioni.send_string("Audio_IlCoccodrilloComeFa")
            risultato = socket_azioni.recv_string()
            print(risultato)

        def azione_canzone_vecchia_fattoria():
            socket_azioni = instance.get_socket_azioni()
            socket_azioni.send_string("Audio_NellaVecchiaFattoria")
            risultato = socket_azioni.recv_string()
            print(risultato)

        def azione_stop_audio():
            socket_azioni = instance.get_socket_azioni()
            socket_azioni.send_string("stop_audio")
            risultato = socket_azioni.recv_string()
            print(risultato)

        def azione_bravo():
            socket_azioni = instance.get_socket_azioni()
            testo = "Bravo"
            socket_azioni.send_string("riproduci_" + testo)
            socket_azioni.recv_string()
            lista_esiti.append("Canta ok")
            lista_esiti_globale.append("Canta ok")
                    
        def riproduci_testo():
            socket_azioni = instance.get_socket_azioni()
            testo = entry_testo.get()
            socket_azioni.send_string("riproduci_" + testo)
            socket_azioni.recv_string()

        instance = get_applicazione()
        self.pack(expand=True, fill="both")
        self.configure(fg_color="#DAF2F2")

        bg_image = customtkinter.CTkImage(Image.open("immagini/sfondo_finestre.jpg"),
                                          size=(instance.finestra.winfo_width(), instance.finestra.winfo_height()))
        bg_image_label = customtkinter.CTkLabel(self, text="", image=bg_image)
        bg_image_label.grid(row=0, column=0, columnspan=3, rowspan=3)

        for x in range(3):
            self.columnconfigure(x, weight=1, uniform='third')

        for x in range(3):
            self.rowconfigure(x, weight=1, uniform='third')

        label = customtkinter.CTkLabel(self, text="Canta", font=("Georgia", 30, "bold"))
        button_canzone_1 = customtkinter.CTkButton(self, text="Baby shark", font=("Georgia", 22, "bold"),
                                                   fg_color="#5F6D67", hover_color="#2F3734",
                                                   height=60, width=210, command=azione_canzone_baby_shark)
        button_canzone_2 = customtkinter.CTkButton(self, text="Coccodrillo\ncome fa", font=("Georgia", 22, "bold"),
                                                   fg_color="#5F6D67", hover_color="#2F3734",
                                                   height=60, width=210, command=azione_canzone_coccodrillo)
        button_canzone_3 = customtkinter.CTkButton(self, text="Nella vecchia\nfattoria", font=("Georgia", 22, "bold"),
                                                   fg_color="#5F6D67", hover_color="#2F3734",
                                                   height=60, width=210, command=azione_canzone_vecchia_fattoria)
        button_menu_principale = customtkinter.CTkButton(self, text="Menu' principale", font=("Georgia", 22, "bold"),
                                                         command=lambda: instance.action_comeback(self))
        button_pausa = customtkinter.CTkButton(self, text="Stop", font=("Georgia", 22, "bold"),
                                               fg_color="#B71528", hover_color="#6E0D18", command=azione_stop_audio)

        label.grid(row=0, column=1)
        button_canzone_1.grid(row=1, column=0, sticky="e")
        button_canzone_2.grid(row=1, column=1)
        button_canzone_3.grid(row=1, column=2, sticky="w")
        button_pausa.grid(row=2, column=1, sticky="s", padx=50, pady=50, ipadx=25, ipady=25)
        button_menu_principale.grid(row=2, column=2, sticky="se", padx=50, pady=50, ipadx=50, ipady=25)

        button_bravo = customtkinter.CTkButton(self, text="Bravo", font=("Georgia", 22, "bold"),
                                            fg_color="#62569F", hover_color="#302B4F",
                                            command=azione_bravo)
        label_testo = customtkinter.CTkLabel(self, text="Inserisci testo", font=("Georgia", 22, "bold"))
        entry_testo = customtkinter.CTkEntry(self, font=("Georgia", 22), width=150,height=50)
        button_riproduci= customtkinter.CTkButton(self, text="Riproduci frase",
                                                       font=("Georgia", 22, "bold"),command = riproduci_testo)
        button_bravo.grid(row=2, column=1, sticky="s", padx=50, pady=50, ipadx=50, ipady=25)
        label_testo.grid(row=2, column=0, sticky="nw", pady=120, padx=130)
        entry_testo.grid(row=2, column=0, sticky="sw", padx=100, pady=30, ipadx=30, ipady=25)
        button_riproduci.grid(row=2, column=0, sticky="se", padx=0, pady=50, ipadx=0, ipady=25)
        button_pausa.grid(row=2, column=2, sticky="sw", padx=0, pady=50, ipadx=0, ipady=25)


class FrameMotricita(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

    def visualizza(self):

        def azione_seduto():
            socket_azioni = instance.get_socket_azioni()
            socket_azioni.send_string("seduto")
            risultato = socket_azioni.recv_string()
            print(risultato)

        def azione_in_piedi():
            socket_azioni = instance.get_socket_azioni()
            socket_azioni.send_string("in piedi")
            risultato = socket_azioni.recv_string()
            print(risultato)

        def azione_una_gamba():
            socket_azioni = instance.get_socket_azioni()
            socket_azioni.send_string("su una gamba")
            risultato = socket_azioni.recv_string()
            print(risultato)

        def azione_bravo():
            socket_azioni = instance.get_socket_azioni()
            testo = "Bravo"
            socket_azioni.send_string("riproduci_" + testo)
            socket_azioni.recv_string()
            lista_esiti.append("Motricita' ok")
            lista_esiti_globale.append("Motricita' ok")
                    
        def riproduci_testo():
            socket_azioni = instance.get_socket_azioni()
            testo = entry_testo.get()
            socket_azioni.send_string("riproduci_" + testo)
            socket_azioni.recv_string()


        instance = get_applicazione()
        self.pack(expand=True, fill="both")
        self.configure(fg_color="#DAF2F2")

        bg_image = customtkinter.CTkImage(Image.open("immagini/sfondo_finestre.jpg"),
                                          size=(instance.finestra.winfo_width(), instance.finestra.winfo_height()))
        bg_image_label = customtkinter.CTkLabel(self, text="", image=bg_image)
        bg_image_label.grid(row=0, column=0, columnspan=3, rowspan=3)

        for x in range(3):
            self.columnconfigure(x, weight=1, uniform='third')

        for x in range(3):
            self.rowconfigure(x, weight=1, uniform='third')

        label = customtkinter.CTkLabel(self, text="Motricita'", font=("Georgia", 30, "bold"))
        button_siediti = customtkinter.CTkButton(self, text="Siediti", font=("Georgia", 22, "bold"), width=220,
                                                 fg_color="#5F6D67", hover_color="#2F3734",
                                                 height=75, command=azione_seduto)
        button_in_piedi = customtkinter.CTkButton(self, text="In piedi", font=("Georgia", 22, "bold"), width=220,
                                                  fg_color="#5F6D67", hover_color="#2F3734",
                                                  height=75, command=azione_in_piedi)
        button_su_una_gamba = customtkinter.CTkButton(self, text="Su una gamba", font=("Georgia", 22, "bold"),
                                                      fg_color="#5F6D67", hover_color="#2F3734",
                                                      width=220, height=75, command=azione_una_gamba)
        button_menu_principale = customtkinter.CTkButton(self, text="Menu' principale", font=("Georgia", 22, "bold"),
                                                         command=lambda: instance.action_comeback(self))

        label.grid(row=0, column=1)
        button_siediti.grid(row=1, column=0, sticky="e")
        button_in_piedi.grid(row=1, column=1)
        button_su_una_gamba.grid(row=1, column=2, sticky="w")
        button_menu_principale.grid(row=2, column=2, sticky="se", padx=50, pady=50, ipadx=50, ipady=25)

        button_bravo = customtkinter.CTkButton(self, text="Bravo", font=("Georgia", 22, "bold"),
                                            fg_color="#62569F", hover_color="#302B4F",
                                            command=azione_bravo)
        label_testo = customtkinter.CTkLabel(self, text="Inserisci testo", font=("Georgia", 22, "bold"))
        entry_testo = customtkinter.CTkEntry(self, font=("Georgia", 22), width=150,height=50)
        button_riproduci= customtkinter.CTkButton(self, text="Riproduci frase",
                                                       font=("Georgia", 22, "bold"),command = riproduci_testo)
        button_pausa = customtkinter.CTkButton(self, text="Stop", font=("Georgia", 22, "bold"),
                                               fg_color="#B71528", hover_color="#6E0D18", command=azione_stop)
        button_bravo.grid(row=2, column=1, sticky="s", padx=50, pady=50, ipadx=50, ipady=25)
        label_testo.grid(row=2, column=0, sticky="nw", pady=120, padx=130)
        entry_testo.grid(row=2, column=0, sticky="sw", padx=100, pady=30, ipadx=30, ipady=25)
        button_riproduci.grid(row=2, column=0, sticky="se", padx=0, pady=50, ipadx=0, ipady=25)
        #button_pausa.grid(row=2, column=2, sticky="sw", padx=0, pady=50, ipadx=0, ipady=25)


class FrameRiepilogoDati(customtkinter.CTkFrame):

    def __int__(self, master):
        super().__init__(master)

    def visualizza(self):
        instance = get_applicazione()
        self.pack(expand=True, fill="both")
        self.configure(fg_color="#DAF2F2")

        bg_image = customtkinter.CTkImage(Image.open("immagini/sfondo_finestre.jpg"),
                                          size=(instance.finestra.winfo_width(), instance.finestra.winfo_height()))
        bg_image_label = customtkinter.CTkLabel(self, text="", image=bg_image)
        bg_image_label.grid(row=0, column=0, columnspan=3, rowspan=3)

        for x in range(3):
            self.columnconfigure(x, weight=1, uniform='third')

        for x in range(3):
            self.rowconfigure(x, weight=1, uniform='third')

        frame_appoggio = customtkinter.CTkFrame(self)
        frame_appoggio.configure(fg_color="transparent")

        label = customtkinter.CTkLabel(self, text="Riepilogo\ndati", font=("Georgia", 30, "bold"))
        label_nome = customtkinter.CTkLabel(frame_appoggio, text="Nome: " + instance.get_nome() , font=("Georgia", 20))
        label_esiti = customtkinter.CTkLabel(frame_appoggio, text="Esiti della terapia: ", font=("Georgia", 20))
        box_esiti = customtkinter.CTkTextbox(frame_appoggio, width=500, height=190, font=("Georgia", 18))
        lista_esiti = ["esito1", "esito2"] # modifica
        print(lista_esiti_globale)
        for esito in lista_esiti:
            box_esiti.insert("insert", esito + "\n")
        button_menu_principale = customtkinter.CTkButton(self, text="Menu' principale", font=("Georgia", 22, "bold"),
                                                         command=lambda: instance.action_comeback(self))

        label.grid(row=0, column=1)
        frame_appoggio.grid(row=1, column=1, sticky="news")
        label_nome.pack(pady=15)
        label_esiti.pack(pady=5)
        box_esiti.pack()
        button_menu_principale.grid(row=2, column=2, sticky="se", padx=50, pady=50, ipadx=50, ipady=25)

class FrameRegistra(customtkinter.CTkFrame):

    def __int__(self, master):
        super().__init__(master)

    def visualizza(self):

        def riproduci_testo():
            socket_azioni = instance.get_socket_azioni()
            testo = entry_testo.get()
            socket_azioni.send_string("riproduci_" + testo)
            socket_azioni.recv_string()

        instance = get_applicazione()
        self.pack(expand=True, fill="both")
        self.configure(fg_color="#DAF2F2")

        bg_image = customtkinter.CTkImage(Image.open("immagini/sfondo_finestre.jpg"),
                                          size=(instance.finestra.winfo_width(), instance.finestra.winfo_height()))
        bg_image_label = customtkinter.CTkLabel(self, text="", image=bg_image)
        bg_image_label.grid(row=0, column=0, columnspan=3, rowspan=3)

        for x in range(2):
            self.columnconfigure(x, weight=1, uniform='third')

        for x in range(3):
            self.rowconfigure(x, weight=1, uniform='third')

        frame_appoggio = customtkinter.CTkFrame(self)
        frame_appoggio.configure(fg_color="transparent")

        label = customtkinter.CTkLabel(self, text="Inserisci testo", font=("Georgia", 30, "bold"))
        entry_testo = customtkinter.CTkEntry(frame_appoggio, font=("Georgia", 24), width=400,height=400)
        entry_testo.configure(placeholder_text="Inserisci frase da riprodurre")
        button_riproduci= customtkinter.CTkButton(frame_appoggio, text="Riproduci frase",
                                                       font=("Georgia", 22, "bold"),width=300,height=100,command = riproduci_testo)

        
        

        button_menu_principale = customtkinter.CTkButton(self, text="Menu' principale", font=("Georgia", 22, "bold"),
                                                         command=lambda: instance.action_comeback(self))


        label.grid(row=0, column=1)
        entry_testo.grid(row= 0,column=1)
        button_riproduci.grid(row = 0,column=2,columnspan=2)
        
        frame_appoggio.grid(row=1, column=1, sticky="news")
        
        button_menu_principale.grid(row=2, column=2, sticky="se", padx=50, pady=50, ipadx=50, ipady=25)


class FrameImitareVersi(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.label_boundy_box = None
        self.label = None
        self.versi = {}
        with open("model/labels.txt", 'r') as f:
            self.labels = [line.strip() for line in f.readlines()]
        self.interpreter = Interpreter(model_path="model/detect.tflite")
        self.interpreter.allocate_tensors() 
        self.verso = ""
        self.scegli_verso = False
        self.output_versi =  cv2.VideoWriter('versi.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (320,240))
        self.stop_acquisizione = False;

    def visualizza(self):

        def bravo():
            instance.socket_azioni.send_string("riproduci_"+self.verso)
            r = instance.socket_azioni.recv()

            instance.socket_azioni.send_string("riproduci_Bravo!")
            r = instance.socket_azioni.recv()

        def sbagliato():
            instance.socket_azioni.send_string("riproduci_No")
            r = instance.socket_azioni.recv()

        def tornaIndietro():
            self.output_versi.release()
            instance.action_comeback(self)

        def azione_ok():
            self.scegli_verso = True


        def get_verso():
            print("suono")
            socket_azioni = instance.get_socket_azioni()
            verso_da_inviare = self.verso.split(":")[0]
            socket_azioni.send_string("Classe_" + verso_da_inviare)
            socket_azioni.recv_string()
            self.stop_acquisizione = False
            self.scegli_verso = False
            print("riprendi")
            self.versi = {}
            self.label_boundy_box.after(10, aggiorna_label)


        def aggiorna_label():
            if(not (self.stop_acquisizione)):
             try:
                instance.socket_azioni.send_string("catturaimmagine_lower")
                im_dec = instance.socket_azioni.recv()
                im = cv2.imdecode(np.frombuffer(im_dec, np.uint8), cv2.IMREAD_COLOR)
                im = cv2.flip(im,1)
                #im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
                imH, imW, _ = im.shape 
                input_details = self.interpreter.get_input_details()
                output_details = self.interpreter.get_output_details()
                height = input_details[0]['shape'][1]
                width = input_details[0]['shape'][2]
                image_resized = cv2.resize(im, (width, height))
                input_data = np.expand_dims(image_resized, axis=0)
                mean = np.mean(input_data)
                std = np.std(input_data)

                input_data = (np.float32(input_data) - mean) / std

                self.interpreter.set_tensor(input_details[0]['index'],input_data)
                self.interpreter.invoke()
                
      
                boxes = self.interpreter.get_tensor(output_details[1]['index'])[0] 
                classes = self.interpreter.get_tensor(output_details[3]['index'])[0] 
                scores = self.interpreter.get_tensor(output_details[0]['index'])[0] 
                detections = []
                min_conf = 0.2
                for i in range(len(scores)):
                  if ((scores[i].any() > min_conf) and (scores[i].any() <= 1.0)):
                      
                      object_name = self.labels[int(classes[i])]
                      if (scores[i] *100) > min_conf*100 and "sfondo" not in object_name:
                        ymin = int(max(1,(boxes[i][0] * imH)))
                        xmin = int(max(1,(boxes[i][1] * imW)))
                        ymax = int(min(imH,(boxes[i][2] * imH)))
                        xmax = int(min(imW,(boxes[i][3] * imW)))
                        
                        cv2.rectangle(im, (xmin,ymin), (xmax,ymax), (10, 255, 0), 2)

                        label = '%s: %d%%' % (object_name, int(scores[i]*100)) 
                        labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2) 
                        label_ymin = max(ymin, labelSize[1] + 10) 
                        cv2.rectangle(im, (xmin, label_ymin-labelSize[1]-10), (xmin+labelSize[0], label_ymin+baseLine-10), (255, 255, 255), cv2.FILLED) 
                        cv2.putText(im, label, (xmin, label_ymin-7), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2) 

                        detections.append([object_name, scores[i], xmin, ymin, xmax, ymax])
                        self.verso = label
                        label_split = label.split(":")
                        key = label_split[0]

                        if key in self.versi:
                            self.versi[key] += 1*scores[i]
                        else:
                            self.versi[key] = 0
                        self.verso = max(self.versi, key=self.versi.get)
                        self.label.configure(text = "verso " + self.verso)
                        self.label.grid(row=0 , column= 2)
                  self.output_versi.write(im)
                  if self.scegli_verso == True:
                        
                        self.verso = max(self.versi, key=self.versi.get)
                        self.stop_acquisizione = True
                        print("ho stoppato ")


                im = Image.fromarray((cv2.cvtColor(im,cv2.COLOR_BGR2RGB)))
                image_yolo = customtkinter.CTkImage(im, size=(900, 700))
                self.label_boundy_box.configure(image=image_yolo)


             except PIL.UnidentifiedImageError:
                pass
             self.label_boundy_box.after(10, aggiorna_label)
            else:
                get_verso();



        instance = get_applicazione()
        self.pack(expand=True, fill="both")
        self.configure(fg_color="#DAF2F2")

        bg_image = customtkinter.CTkImage(Image.open("immagini/sfondo_finestre.jpg"),
                                          size=(instance.finestra.winfo_width(), instance.finestra.winfo_height()))
        bg_image_label = customtkinter.CTkLabel(self, text="", image=bg_image)
        bg_image_label.grid(row=0, column=0, columnspan=4, rowspan=5)

        for x in range(3):
            self.columnconfigure(x, weight=1, uniform='third')

        for x in range(5):
            self.rowconfigure(x, weight=1, uniform='third')

        image1 = customtkinter.CTkImage(Image.open("immagini/sfondo_finestre.jpg"), size=(900, 700))
        self.label_boundy_box = customtkinter.CTkLabel(self, text="", image=image1)
        button_ok = customtkinter.CTkButton(self, text="Ok", font=("Georgia", 22, "bold"), width=220,
                                            fg_color="#62569F", hover_color="#302B4F", height=75,
                                            command=azione_ok)
        button_menu_principale = customtkinter.CTkButton(self, text="Menù principale", font=("Georgia", 22, "bold"),
                                                         width=220, height=75,
                                                         command=tornaIndietro)
        button_bravo = customtkinter.CTkButton(self, text="Bravo", font=("Georgia", 22, "bold"),
                                                         width=220, height=75,
                                                         command=bravo)
        button_no = customtkinter.CTkButton(self, text="Sbagliato", font=("Georgia", 22, "bold"),
                                                         width=220, height=75,
                                                         command=sbagliato)

        self.label_boundy_box.grid(row=0, column=0, columnspan=2, rowspan=5)

        self.label = customtkinter.CTkLabel(self, text="verso", font=("Georgia", 30, "bold"))

        button_ok.grid(row=1, column=2)
        button_bravo.grid(row=2,column=2)
        button_no.grid(row=3,column=2)
        button_menu_principale.grid(row=4, column=2)

        aggiorna_label()



class FrameGuarda(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.model = YOLO("model/yolov8s.pt")
        self.label_gaze = None
        self.parametro = 0
        self.stop = False
        self.sguardi = {}
        self.oggetti = {}
        self.label_plan = None
        self.OK = False
        self.output_sguardo = cv2.VideoWriter('sguardo.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (320,240))
        self.output_plan_view = cv2.VideoWriter('plan_view.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (640,480))
        self.output_detection = cv2.VideoWriter( 'detection.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (320,240))
        self.riprodotto = 0
        self.label_lower = None
        self.label = None
        self.label_sguardo = None
        self.salva_sguardo = False
        self.label_posizione_oggetto = None
        self.angle = 0
        self.stop_det = False
        self.inizio = 0
        mp_face_mesh = mp.solutions.face_mesh

        self.LEFT_EYE =[ 362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385,384, 398 ]
        self.RIGHT_EYE=[ 33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161 , 246 ] 
        self.LEFT_IRIS = [474,475, 476, 477]
        self.RIGHT_IRIS = [469, 470, 471, 472]

        self.face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5, min_tracking_confidence=0.5)


    def visualizza(self):

        def setOk():
            self.OK = True

        def tornaIndietro():
            self.output_sguardo.release()
            self.output_detection.release()
            self.sguardi= {}
            self.oggetti = {}
            self.output_plan_view.release()
            instance.socket_azioni.send_string("siediti")
            ris = instance.socket_azioni.recv()
            instance.action_comeback(self)

        def setParametro():
            print("cambio" + self.entry_parametro.get())
            self.parametro = int (self.entry_parametro.get())
            self.sguardi = {}

        def setStop():
            self.sguardi = {}

        def riproduci_testo():
            socket_azioni = instance.get_socket_azioni()
            testo = entry_testo.get()
            socket_azioni.send_string("riproduci_" + testo)
            socket_azioni.recv_string()


        def aggiorna_label():
            
            try:
                if(not(self.stop)):
                    instance.socket_azioni.send_string("catturaimmagine_lower")

                    im_low = instance.socket_azioni.recv()
                    posizione = 0.99
                    rgb_low = cv2.imdecode(np.frombuffer(im_low, np.uint8), cv2.IMREAD_COLOR)   

                    self.output_detection.write(cv2.cvtColor(rgb_low,cv2.COLOR_BGR2RGB)) 
                    rgb_low= cv2.cvtColor(rgb_low, cv2.COLOR_BGR2RGB)
                    altezza,larghezza,_= rgb_low.shape
                    print(altezza)
                    print(larghezza)
                    if(not self.stop_det):
                        results = self.model.predict(rgb_low)           
                        for result in results:                                         
                            boxes = result.boxes.cpu().numpy()                         
                            for box in boxes:                                          
                                r = box.xyxy[0].astype(int)

                                nome = result.names[int(box.cls[0])]    
                                print(nome)
                                if(nome == "sports ball"):
                                    posizione = (r[0]/larghezza)                   
                                    cv2.rectangle(rgb_low, r[:2], r[2:], (255, 255, 255), 2)   
                                    cv2.putText(rgb_low, nome, (r[0], r[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
                        if posizione < 0.25:
                            sguardo_verso = "sinistra"
                        elif posizione > 0.65 and not posizione == 0.99:
                            sguardo_verso = "destra"
                        elif posizione == 0.99:
                            sguardo_verso = "oggetto nondef"
                        else:
                            sguardo_verso = "centro"
                            
                        if sguardo_verso in self.oggetti and not sguardo_verso == "oggetto nondef":
                            self.oggetti[sguardo_verso] += 1
                        else:
                            self.oggetti[sguardo_verso] = 0
                        rgb_low = cv2.flip(rgb_low,1)

                        im3 = Image.fromarray(rgb_low)

                        image_lowe = customtkinter.CTkImage(im3, size=(600, 500))

                        self.label_lower.configure(image=image_lowe)

                        if self.oggetti[max(self.oggetti, key=self.oggetti.get)] >3 and self.riprodotto == 0 :
                            instance.socket_azioni.send_string("guarda_"+max(self.oggetti, key=self.oggetti.get))
                            r = instance.socket_azioni.recv()
                            self.riprodotto = 1
                        if self.riprodotto :
                            self.inizio = time.time()
                            self.stop_det = True
                            self.salva_sguardo = True

                    instance.socket_azioni.send_string("catturaimmagine_upper")
                    im_up = instance.socket_azioni.recv()
                    im = cv2.imdecode(np.frombuffer(im_up, np.uint8), cv2.IMREAD_COLOR)         
                    im = cv2.flip(im,1)       
                    rgb_frame = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
                    h, w,c = rgb_frame.shape
                    dst = cv2.imread("immagini/dest_2d.jpg")
                    dst = cv2.cvtColor(dst,cv2.COLOR_BGR2RGB)
                    distanza_x = 0
                    face_3d = []
                    face_2d = []

                    self.output_sguardo.write(cv2.cvtColor(rgb_frame,cv2.COLOR_BGR2RGB))

                    results = self.face_mesh.process(rgb_frame)

                    def draw_eye_line(frame, center, average_point):
                        cv2.line(frame, tuple(center), tuple(average_point), (0, 0, 255), 2)
                    

                    if results.multi_face_landmarks:
                        mesh_points = np.array(
                            [np.multiply([p.x, p.y], [w, h]).astype(int) for p in results.multi_face_landmarks[0].landmark]
                        )

                        (l_cx, l_cy), l_radius = cv2.minEnclosingCircle(mesh_points[self.LEFT_IRIS])
                        (r_cx, r_cy), r_radius = cv2.minEnclosingCircle(mesh_points[self.RIGHT_IRIS])

                        centro_sinistra = np.array([l_cx, l_cy], dtype=np.int32)
                        centro_destra = np.array([r_cx, r_cy], dtype=np.int32)

                        cv2.circle(rgb_frame, centro_sinistra, int(l_radius), (255, 0, 255), 1, cv2.LINE_AA)
                        cv2.circle(rgb_frame, centro_destra, int(r_radius), (255, 0, 255), 1, cv2.LINE_AA)

                        punti_occhio_sinistro = mesh_points[self.LEFT_EYE]
                        punti_occhio_destro = mesh_points[self.RIGHT_EYE]

                        bordi_sinistro = tuple(punti_occhio_sinistro[punti_occhio_sinistro[:, 0].argmin()]) + tuple(
                            punti_occhio_sinistro[punti_occhio_sinistro[:, 0].argmax()]
                        )
                        media_occhio_sinistro = (
                            (bordi_sinistro[0] + bordi_sinistro[2]) // 2,
                            (bordi_sinistro[1] + bordi_sinistro[3]) // 2,
                        )

                        bordi_destro = tuple(punti_occhio_destro[punti_occhio_destro[:, 0].argmin()]) + tuple(
                            punti_occhio_destro[punti_occhio_destro[:, 0].argmax()]
                        )
                        media_occhio_destro = (
                            (bordi_destro[0] + bordi_destro[2]) // 2,
                            (bordi_destro[1] + bordi_destro[3]) // 2,
                        )

                        draw_eye_line(rgb_frame, centro_destra, media_occhio_destro)
                        draw_eye_line(rgb_frame, centro_sinistra, media_occhio_sinistro)


                        distanza_x = (media_occhio_destro[0] - centro_destra[0]) + (media_occhio_sinistro[0] - centro_sinistra[0]) 
                        distanza_y = media_occhio_destro[1] - centro_destra[1] + (media_occhio_sinistro[1] - centro_sinistra[1])

                        for face_landmarks in results.multi_face_landmarks:
                            for idx, lm in enumerate(face_landmarks.landmark):
                                if idx == 33 or idx == 263 or idx == 1 or idx == 61 or idx ==291 or idx == 199:
                                    if idx == 1:
                                        nose_2d = (lm.x* w, lm.y*h)
                                        nose_3d = (lm.x*w,lm.y*h,lm.z *3000)
                                    x,y = int(lm.x*w), int(lm.y*h)
                                    face_2d.append([x,y])
                                    face_3d.append([x,y,lm.z])

                            face_2d = np.array(face_2d, dtype= np.float64)
                            face_3d = np.array(face_3d, dtype = np.float64)
                            
                            focal_length = 1*w
                            
                            cam_matrix = np.array([[focal_length, 0 , h/2],
                                                    [0,focal_length, w/2],
                                                    [0,0,1]])

                            dist_matrix = np.zeros((4,1),dtype=np.float64)
                            _,rot_vec,trans_vec = cv2.solvePnP(face_3d,face_2d,cam_matrix,dist_matrix)

                            rmat,jac = cv2.Rodrigues(rot_vec)
                            angoli,mtxR,mtxQ,Qx,Qy,Qz = cv2.RQDecomp3x3(rmat)
                                    
                            angolo_lunghezza = angoli[0]*360
                            angolo_larghezza = angoli[1]*360
                            z = angoli[2]*360

                            
                            nose_3d_proj, jacobian = cv2.projectPoints(nose_3d,rot_vec,trans_vec,cam_matrix,dist_matrix)

                            p1 = (int(nose_2d[0]), int(nose_2d[1]))
                            if abs(distanza_x) > 2:
                                p2 = (int(nose_2d[0]+angolo_larghezza - distanza_x *self.parametro), int(nose_2d[1]-angolo_lunghezza))
                            else:

                                p2 = (int(nose_2d[0]+angolo_larghezza), int(nose_2d[1] -angolo_lunghezza))
                            cv2.line(rgb_frame,p1,p2,(255,0,0),3)
                            
                            nose_dst = [315,104] 
                            eps = 0.01
                            x1_sguardo_frontale, y1_sguardo_frontale = nose_dst
                            x2_sguardo_frontale, y2_sguardo_frontale = nose_dst[0], nose_dst[1] + 400

                            x1_sguardo_finale, y1_sguardo_finale = nose_dst
                            x2_sguardo_finale = int(nose_dst[0] + (10 * angolo_larghezza - (distanza_x * self.parametro)))
                            y2_sguardo_finale = nose_dst[1] + 400

                            m_sguardo_frontale = (y2_sguardo_frontale - y1_sguardo_frontale) / (x2_sguardo_frontale - x1_sguardo_frontale+eps)
                            m_sguardo_finale = (y2_sguardo_finale - y1_sguardo_finale) / (x2_sguardo_finale - x1_sguardo_finale+eps)

                            angolo_rad = np.arctan(abs((m_sguardo_finale - m_sguardo_frontale) / (1 + m_sguardo_frontale * m_sguardo_finale)))
                            theta = np.degrees(angolo_rad)
                            if m_sguardo_frontale < m_sguardo_finale:
                                theta = -theta
                            
                            cv2.line(dst, nose_dst, (nose_dst[0], nose_dst[1]+400), (0, 255, 0), 3) 
                            cv2.line(dst, nose_dst, (int(nose_dst[0] + (10*angolo_larghezza-(distanza_x*self.parametro))), nose_dst[1]+400), (0, 255, 0), 3) 
                                        
                            if (400 - nose_dst[0] + (10*angolo_larghezza-(distanza_x*self.parametro))) > 0:
                                theta = -theta

                            self.angle = theta

                       
                    im = Image.fromarray(cv2.flip(rgb_frame,1))
                    self.output_plan_view.write(cv2.cvtColor(dst,cv2.COLOR_BGR2RGB))
                    image_waze = customtkinter.CTkImage(im, size=(600, 500))



                    key = "no"
                    if self.angle > 10:
                        key = "destra"
                    elif self.angle <-10:
                        key = "sinistra"
                    else:
                        key = "centro"

                    if key in self.sguardi and not key == "no" and self.salva_sguardo :
                        self.sguardi[key] += 1
                    else:
                        self.sguardi[key] = 0
                    print(self.sguardi)
                    if(not self.salva_sguardo):

                        self.label.configure(text = "sguardo non memorizzato")
                    else:

                        print(time.time() - self.inizio)
                        self.label.configure(text = "Sguardo: " +max(self.sguardi, key=self.sguardi.get))
                    print("IO")
                    print(self.sguardi[max(self.sguardi, key=self.sguardi.get)])
                    if(max(self.sguardi, key=self.sguardi.get)  == max(self.oggetti, key=self.oggetti.get)  and self.sguardi[max(self.sguardi, key=self.sguardi.get)] > 5 ):
                        instance.socket_azioni.send_string("riproduci_Bravo!")
                        ric = instance.socket_azioni.recv()
                        self.stop = True
                        tornaIndietro()
                    self.label_posizione_oggetto.configure(text = max(self.oggetti, key=self.oggetti.get))
                    #self.label_sguardo.configure(text = "direzione iride " + str(distanza_x))
                    self.label_gaze.configure(image=image_waze)
                    im2 = Image.fromarray(dst)
                    image_plan = customtkinter.CTkImage(im2, size=(600, 500))
                    self.label_plan.configure(image=image_plan)

                    self.label_gaze.after(10, aggiorna_label)


            except Exception as e:
                print(  e)
                pass
            



        
        tts = pyttsx3.init()
        voices = tts.getProperty('voices')
        tts.setProperty('voice', voices[0].id)  

        instance = get_applicazione()
        self.pack(expand=True, fill="both")
        self.configure(fg_color="#DAF2F2")

        bg_image = customtkinter.CTkImage(Image.open("immagini/sfondo_finestre.jpg"),
                                          size=(instance.finestra.winfo_width(), instance.finestra.winfo_height()))
        bg_image_label = customtkinter.CTkLabel(self, text="", image=bg_image)
        bg_image_label.grid(row=0, column=0, columnspan=5, rowspan=5)

        for x in range(5):
            self.columnconfigure(x, weight=1, uniform='third')

        for x in range(5):
            self.rowconfigure(x, weight=1, uniform='third')

        image1 = customtkinter.CTkImage(Image.open("immagini/sfondo_finestre.jpg"), size=(600, 500))
        self.label_gaze = customtkinter.CTkLabel(self, text="", image=image1)
        image2 = customtkinter.CTkImage(Image.open("immagini/dest_2d.jpg"), size=(600, 500))

        self.label_plan = customtkinter.CTkLabel(self, text="", image=image2)
        self.entry_parametro = customtkinter.CTkEntry(self,font=("Georgia", 24), width=300)
        self.button_parametro = customtkinter.CTkButton(self, text="sensibilità iride", font=("Georgia", 22, "bold"),
                                                         width=75, height=75,
                                                         command=setParametro)
        self.button_sguardo_scorretto = customtkinter.CTkButton(self, text="Sguardo scorretto_reset", font=("Georgia", 22, "bold"),
                                                         width=75, height=75,
                                                         command=setStop)
        self.button_sguardo_corretto = customtkinter.CTkButton(self, text="Sguardo corretto", font=("Georgia", 22, "bold"),
                                                         width=75, height=75,
                                                         command=setOk)
        image3 = customtkinter.CTkImage(Image.open("immagini/dest_2d.jpg"), size=(300, 300))
        self.label_lower = customtkinter.CTkLabel(self, text="", image=image3)
        self.label = customtkinter.CTkLabel(self, text="gradi", font=("Georgia", 30, "bold"))
        self.label.configure(text="30")
        self.label_posizione_oggetto = customtkinter.CTkLabel(self, text="gradi", font=("Georgia", 30, "bold"))
        #self.label_sguardo = customtkinter.CTkLabel(self, text="gradi", font=("Georgia", 30, "bold"))

        button_menu_principale = customtkinter.CTkButton(self, text="Menù principale", font=("Georgia", 22, "bold"),
                                                         width=220, height=75,
                                                         command=tornaIndietro)

        self.label_gaze.grid(row=0, column=0, columnspan=2, rowspan=2)
        self.label_lower.grid(row=2, column=0, columnspan=2, rowspan=2)

        self.label_plan.grid(row=1, column=2, columnspan=2, rowspan=2)
        self.label.grid(row=3,column=2)
        self.label_posizione_oggetto.grid(row=3,column=3)
        #self.label_sguardo.grid(row=3,column=4)
        self.entry_parametro.grid(row=4,column=1)
        self.button_sguardo_corretto.grid(row=3,column=4)
        self.button_parametro.grid(row=4,column=2)
        self.button_sguardo_scorretto.grid(row=4,column=3)
        button_menu_principale.grid(row=4, column=4)
        
        label_testo = customtkinter.CTkLabel(self, text="Inserisci testo", font=("Georgia", 22, "bold"))
        entry_testo = customtkinter.CTkEntry(self, font=("Georgia", 22), width=150,height=75)
        button_riproduci= customtkinter.CTkButton(self, text="Riproduci frase",
                                                       font=("Georgia", 22, "bold"),command = riproduci_testo)
        label_testo.grid(row=1, column=4, sticky="se", padx=70)
        entry_testo.grid(row=2, column=4, sticky="ne", padx=80)
        button_riproduci.grid(row=2, column=4, sticky="se", padx=50, pady=25, ipadx=10, ipady=25)

        aggiorna_label()


class FrameFammiVedere(customtkinter.CTkFrame):
    
    def __init__(self, master):
        super().__init__(master)
        self.label_boundy_box = None
        self.label = None
        self.versi = {}
        with open("model/labels.txt", 'r') as f:
            self.labels = [line.strip() for line in f.readlines()]
        self.interpreter = Interpreter(model_path="model/detect.tflite")
        self.interpreter.allocate_tensors() 
        self.verso = ""
        #self.scegli_verso = False
        self.output_versi =  cv2.VideoWriter('versi.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (320,240))
        self.stop_acquisizione = True;

    def visualizza(self):

        #def bravo():
        #    instance.socket_azioni.send_string("riproduci_"+self.verso)
        #    r = instance.socket_azioni.recv()
        #
        #    instance.socket_azioni.send_string("riproduci_Bravo!")
        #    r = instance.socket_azioni.recv()

        def tornaIndietro():
            self.output_versi.release()
            instance.action_comeback(self)

        def azione_vedi():
            self.versi = {}
            instance.socket_azioni.send_string("in piedi normale")
            r = instance.socket_azioni.recv()
            instance.socket_azioni.send_string("riproduci_Fammivederequalcosa")
            r = instance.socket_azioni.recv()
            self.stop_acquisizione = False


        def aggiorna_label():
            if(not (self.stop_acquisizione)):
             try:
                instance.socket_azioni.send_string("catturaimmagine_lower")
                im_dec = instance.socket_azioni.recv()
                im = cv2.imdecode(np.frombuffer(im_dec, np.uint8), cv2.IMREAD_COLOR)
                im = cv2.flip(im,1)
                #im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
                imH, imW, _ = im.shape 
                input_details = self.interpreter.get_input_details()
                output_details = self.interpreter.get_output_details()
                height = input_details[0]['shape'][1]
                width = input_details[0]['shape'][2]
                image_resized = cv2.resize(im, (width, height))
                input_data = np.expand_dims(image_resized, axis=0)
                mean = np.mean(input_data)
                std = np.std(input_data)

                input_data = (np.float32(input_data) - mean) / std

                self.interpreter.set_tensor(input_details[0]['index'],input_data)
                self.interpreter.invoke()
                
      
                boxes = self.interpreter.get_tensor(output_details[1]['index'])[0] 
                classes = self.interpreter.get_tensor(output_details[3]['index'])[0] 
                scores = self.interpreter.get_tensor(output_details[0]['index'])[0] 
                detections = []
                min_conf = 0.3
                for i in range(len(scores)):
                  if ((scores[i].any() > min_conf) and (scores[i].any() <= 1.0)):
                      
                      object_name = self.labels[int(classes[i])]
                      if (scores[i] *100) > min_conf*100 and "sfondo" not in object_name:
                        ymin = int(max(1,(boxes[i][0] * imH)))
                        xmin = int(max(1,(boxes[i][1] * imW)))
                        ymax = int(min(imH,(boxes[i][2] * imH)))
                        xmax = int(min(imW,(boxes[i][3] * imW)))
                        
                        cv2.rectangle(im, (xmin,ymin), (xmax,ymax), (10, 255, 0), 2)

                        label = '%s: %d%%' % (object_name, int(scores[i]*100)) 
                        labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2) 
                        label_ymin = max(ymin, labelSize[1] + 10) 
                        cv2.rectangle(im, (xmin, label_ymin-labelSize[1]-10), (xmin+labelSize[0], label_ymin+baseLine-10), (255, 255, 255), cv2.FILLED) 
                        cv2.putText(im, label, (xmin, label_ymin-7), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2) 

                        detections.append([object_name, scores[i], xmin, ymin, xmax, ymax])
                        self.verso = label
                        label_split = label.split(":")
                        key = label_split[0]

                        if key in self.versi:
                            self.versi[key] += 1*scores[i]
                        else:
                            self.versi[key] = 0
                        self.verso = max(self.versi, key=self.versi.get)
                        if self.versi[max(self.versi, key=self.versi.get)] > 5:
                            instance.socket_azioni.send_string("riproduci_"+self.verso)
                            r = instance.socket_azioni.recv()
                            self.stop_acquisizione = True
                            print("ho stoppato ")

                        self.label.configure(text = "Oggetto: " + self.verso)
                        self.label.grid(row=0 , column= 2)
                  self.output_versi.write(im)
                 


                im = Image.fromarray((cv2.cvtColor(im,cv2.COLOR_BGR2RGB)))
                image_yolo = customtkinter.CTkImage(im, size=(900, 700))
                self.label_boundy_box.configure(image=image_yolo)


             except PIL.UnidentifiedImageError:
                pass
            
            self.label_boundy_box.after(10, aggiorna_label)
            



        instance = get_applicazione()
        self.pack(expand=True, fill="both")
        self.configure(fg_color="#DAF2F2")

        bg_image = customtkinter.CTkImage(Image.open("immagini/sfondo_finestre.jpg"),
                                          size=(instance.finestra.winfo_width(), instance.finestra.winfo_height()))
        bg_image_label = customtkinter.CTkLabel(self, text="", image=bg_image)
        bg_image_label.grid(row=0, column=0, columnspan=4, rowspan=5)

        for x in range(3):
            self.columnconfigure(x, weight=1, uniform='third')

        for x in range(5):
            self.rowconfigure(x, weight=1, uniform='third')

        image1 = customtkinter.CTkImage(Image.open("immagini/sfondo_finestre.jpg"), size=(900, 700))
        self.label_boundy_box = customtkinter.CTkLabel(self, text="", image=image1)
        button_vedi = customtkinter.CTkButton(self, text="Vedi", font=("Georgia", 22, "bold"), width=220,
                                            fg_color="#62569F", hover_color="#302B4F", height=75,
                                            command=azione_vedi)
        button_menu_principale = customtkinter.CTkButton(self, text="Menù principale", font=("Georgia", 22, "bold"),
                                                         width=220, height=75,
                                                         command=tornaIndietro)
        

        self.label_boundy_box.grid(row=0, column=0, columnspan=2, rowspan=5)

        self.label = customtkinter.CTkLabel(self, text="verso", font=("Georgia", 30, "bold"))

        button_vedi.grid(row=1, column=2)
        button_menu_principale.grid(row=4, column=2)

        aggiorna_label()


applicazione = App()

global lista_esiti_globale
lista_esiti_globale = []


def get_applicazione():
    return applicazione



applicazione.run_app()
