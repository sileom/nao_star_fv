# -*- coding: utf-8 -*-

import threading
import time
import os
import math
import datetime
import cv2
import numpy as np
import zmq
from naoqi import ALProxy
import qi
import shutil
import glob
from BalloBabyShark import BalloBabyShark
from BalloMercoledi import BalloMercoledi
from BalloWhisky import BalloWhisky
from UnaGamba import UnaGamba
from Saluti import Saluti

from PIL import Image

# from functools import cached_property


class Azioni:

    balloMercoledi = BalloMercoledi()
    balloBabyShark = BalloBabyShark()
    balloWhisky = BalloWhisky()
    unaGamba = UnaGamba()
    saluti = Saluti()

    def get_azione_incontro_uno(self):
        if (device == "robot"):
            self.ledProxy.setIntensity("LeftFaceLedsGreen", 0.1)
            self.ledProxy.setIntensity("LeftFaceLedsBlue", 0.1)
            self.ledProxy.setIntensity("LeftFaceLedsRed", 0.7)
            self.ledProxy.setIntensity("RightFaceLedsGreen", 0.1)
            self.ledProxy.setIntensity("RightFaceLedsBlue", 0.1)
            self.ledProxy.setIntensity("RightFaceLedsRed", 0.7)
        self.motion.wakeUp()
        self.animatedTextProxy.say("Ciao mi chiamo Stella ^start(   animations/Stand/Gestures/Me_1) e oggi giocheremo insieme e faremo tante attività ")
        
        self.animatedTextProxy.say("^start(animations/Stand/Gestures/Explain_10) Mi piacerebbe sapere come ti ^start(animations/Stand/Gestures/Explain_3) chiami e quanti anni hai.")
        time.sleep(1.8)
        self.animatedTextProxy.say("Io vengo da un pianeta ^start(animations/Stand/BodyTalk/BodyTalk_2) lontano e tu da dove vieni?")
        self.postureProxy.goToPosture("Crouch",0.3)

    def get_azione_incontro_due(self):

        if (device == "robot"):
            self.ledProxy.setIntensity("LeftFaceLedsGreen", 0.1)
            self.ledProxy.setIntensity("LeftFaceLedsBlue", 0.1)
            self.ledProxy.setIntensity("LeftFaceLedsRed", 0.7)
            self.ledProxy.setIntensity("RightFaceLedsGreen", 0.1)
            self.ledProxy.setIntensity("RightFaceLedsBlue", 0.1)
            self.ledProxy.setIntensity("RightFaceLedsRed", 0.7)
        self.postureProxy.goToPosture("Stand",0.3)
        self.animatedTextProxy.say("Ciao  ^start(   animations/Stand/Gestures/Hey_1) e bentornato")
        
        self.animatedTextProxy.say("^start(animations/Stand/Gestures/Explain_10) Hai voglia di giocare ancora ^start(animations/Stand/Gestures/Explain_3) e divertirti di nuovo con me ?")
        
        self.animatedTextProxy.say("Ricordi cosa abbiamo ^start(animations/Stand/BodyTalk/BodyTalk_2) fatto l'ultima volta?")


        self.postureProxy.goToPosture("Crouch",0.3)


    def riproduci_testo(self,messaggio):
        self.textProxy.say(messaggio)

    def get_azione_congedo(self,nome):
        self.postureProxy.goToPosture("Stand",0.3)
        self.ballo = self.saluti.get_movimento()
        if(not self.motion_source):
            interpolation_thread = threading.Thread(target=self.interpolazione_angoli)
            interpolation_thread.start()
            self.postureProxy.goToPosture("Crouch",0.3)
            self.motion_source = True
        print("Nome:")
        print(nome)
        self.animatedTextProxy.say("Ciao %s ci vediamo la prossima volta !" % nome)

    def get_azione_siediti(self):
        self.postureProxy.goToPosture("Crouch", 0.6)
        self.motion.setStiffnesses("Body", 0.0)

    def get_azione_siediti_motricita(self):
        self.animatedTextProxy.say("Fai come me")
        self.postureProxy.goToPosture("Crouch", 0.6)

    def get_azione_in_piedi(self):
        self.animatedTextProxy.say("Fai come me")
        self.postureProxy.goToPosture("Stand", 0.5)

    def get_azione_in_piedi_normale(self):
        self.postureProxy.goToPosture("Stand", 0.5)

        
    def get_azione_una_gamba(self):
        self.animatedTextProxy.say("Fai come me")
        self.postureProxy.goToPosture("Stand", 0.6)
        self.motion.angleInterpolationBezier(self.unaGamba.get_name(), self.unaGamba.get_time()
                                            , self.unaGamba.get_keys())


    def get_azione_stop_motricita(self):
        try:
            posture_proxy = ALProxy("ALRobotPosture", self._ip, self._port)
            print(self._ip)
            posture_proxy.goToPosture("Crouch", 0.6)
        except Exception as e:
            print("Could not create proxy to ALRobotPosture")
            print("Error was: ", e)

        

    def interpolazione_angoli(self):
        try:
            print("Sto ballando")
            i = 0
            step = len(self.ballo[self.ballo.keys()[0]][0])
            while (i < step and self.stop_ballo == False) :
                tempo = 0
                keys = list()
                for chiave in self.ballo.keys():
                    if(i > 0):
                        temp = self.ballo[chiave][0][i-1]
                        tempo = self.ballo[chiave][0][i] - temp
                    else :
                        tempo = self.ballo[chiave][0][i]
                    keys.append((self.ballo[chiave][1][i][0]))
                self.motion.setAngles(self.ballo.keys(),keys,0.3)
                time.sleep(tempo)
                tempo = 0
                keys = list()
                i = i+1
            self.stop_ballo = False

            self.motion_source = False
            self.stop_audio()
            self.postureProxy.goToPosture("Crouch", 0.3)
        except BaseException, err:
             print err
       

    def get_azione_stop_ballo(self):
        self.stop_ballo = True

    def get_ballo(self,nome_ballo):
        self.postureProxy.goToPosture("Stand", 0.6)
        if("Baby" in nome_ballo):
            self.ballo = self.balloBabyShark.get_ballo()
            self.riproduci_audio(nome_ballo)
            if(not self.motion_source):
                baby_thread = threading.Thread(target=self.interpolazione_angoli)
                baby_thread.start()
                self.motion_source = True
        if("Whisky" in nome_ballo):
            print("Whisky")
            self.ballo = self.balloWhisky.get_ballo()
            self.riproduci_audio(nome_ballo)
            if(not self.motion_source):
                whisky_thread = threading.Thread(target=self.interpolazione_angoli)
                whisky_thread.start()
                self.motion_source = True
        if("ercole" in nome_ballo):
            self.ballo = self.balloMercoledi.get_ballo()
            self.riproduci_audio(nome_ballo)
            if(not self.motion_source):
                mercoledi_thread = threading.Thread(target=self.interpolazione_angoli)
                mercoledi_thread.start()
                self.motion_source = True
        
        #if(not self.motion_source):
        #    interpolation_thread = threading.Thread(target=self.interpolazione_angoli)
        #    interpolation_thread.start()
        #    interpolation_thread.join()
        #    self.postureProxy.goToPosture("Crouch", 0.3)
        #    self.motion_source = True

    


    def get_azione_cattura_immagine(self):


        
        if (device == "robot"):
            result = self.video_device_upper.getImageRemote(self.upper)
            self.video_device_upper.releaseImage(self.upper)
            im = Image.frombytes("RGB", (result[0], result[1]), result[6])
            cvim = np.array(im)
            frame_enc = cv2.imencode(".jpg", cvim)[1].tobytes()
            self.output_upper.write(cvim)
            socket.send(frame_enc)
        else:
            
            ret,frame = self.upper.read()
            frame = cv2.resize(frame,(320,240))
            frame_enc = cv2.imencode(".jpg", frame)[1].tobytes()
            self.output_upper.write(frame)

            socket.send(frame_enc)

    def get_azione_cattura_immagine_lower(self):
        if (device == "robot"):
            result = self.video_device_lower.getImageRemote(self.lower)
            self.video_device_lower.releaseImage(self.lower)
            im = Image.frombytes("RGB", (result[0], result[1]), result[6])
            cvim = np.array(im)
            frame_enc = cv2.imencode(".jpg", cvim)[1].tobytes()
            self.output_lower.write(cvim)
            socket.send(frame_enc)
        else:
            
            ret,frame = self.lower.read()
            frame = cv2.resize(frame,(320,240))
            frame_enc = cv2.imencode(".jpg", frame)[1].tobytes()

            self.output_lower.write(frame)
            socket.send(frame_enc)


    def stop_audio(self):
        self.audioProxy.stop(self.id_song)
        self.audio_source = False
        
    def riproduci_audio(self, messaggio):
        path = os.path.join(os.getcwd(),"canzoni_pc", messaggio +".ogg")
        print(path)
        if (device == "robot"):
            if(not self.audio_source):
                self.ledProxy.setIntensity("LeftFaceLedsGreen", 0.5)
                self.ledProxy.setIntensity("LeftFaceLedsBlue", 0.1)
                self.ledProxy.setIntensity("LeftFaceLedsRed", 0.7)
                self.ledProxy.setIntensity("RightFaceLedsGreen", 0.5)
                self.ledProxy.setIntensity("RightFaceLedsBlue", 0.1)
                self.ledProxy.setIntensity("RightFaceLedsRed", 0.7)
                print(messaggio)
                self.id_song = self.audioProxy.post.playFile("/home/nao/canzoni/" + messaggio + ".ogg")
                self.audio_source=True
        else:
            if(not self.audio_source):
                self.id_song = self.audioProxy.post.playFile(path)
                self.audio_source=True
                
    def riproduci_verso(self, messaggio):
        path = os.path.join(os.getcwd(),"canzoni_pc", messaggio +".ogg")
        print(path)
        if (device == "robot"):
            self.animatedTextProxy.say("Ripeti con me")
            time.sleep(0.6)
            self.id_song = self.audioProxy.post.playFile("/home/nao/canzoni/" + messaggio + ".ogg")

        else:
            self.animatedTextProxy.say("Ripeti con me")
            time.sleep(0.6)
            self.id_song = self.audioProxy.post.playFile(path)

    def setVolume(self, volume):
        print(volume)
        self.volumeProxy.setOutputVolume(int(volume))
   

    def setNome(self, nome):
        print(nome)
        self.nome = nome
        data_ora_corrente = datetime.datetime.now()

        # Formatta la stringa della data e dell'orario nel formato desiderato
        formatted_datetime = data_ora_corrente.strftime("%Y-%m-%d_%H-%M-%S")

        # Crea la directory utilizzando il nome formattato
        nome_directory = "video_" + formatted_datetime + "_" + nome
        self.nome_cartella = nome_directory

        os.mkdir(nome_directory)

    def get_chiudi(self):
        self.output_lower.release()
        self.output_upper.release()
        files_mp4 = glob.glob("*.mp4")
        for file in files_mp4:
            print(file)
            shutil.move(file,self.nome_cartella )

    def guarda_thread(self):
        names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
        namesL = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand"]
        angle_right = [26.9, 27.5, -13.8, -22.1, 6.4, 0.02]
        angle_center =  [39.4, 3.3, 41.2, 33.4, -49.6, 0.02]
        angle_left = [39.4, -14.1, 71.0, 45.7, -49.2, 0.02]
        print(self.direzione)
        direzione = self.direzione
        if direzione == "destra":
            angle_rad = [math.radians(angle) for angle in angle_right]
            print(angle_rad)

            self.motion.setStiffnesses("Body", 1.0)
            self.motion.setAngles(names, angle_rad, 0.1)
            self.textProxy.say("Guarda la palla!")
        if direzione == "sinistra":
            angle_rad = [math.radians(angle) for angle in angle_left]

            self.motion.setStiffnesses("Body", 1.0)

            print(angle_rad)
            self.motion.setAngles(namesL, angle_rad, 0.1)
            
            self.textProxy.say("Guarda la palla!")
        if direzione == "centro":

            self.motion.setStiffnesses("Body", 1.0)
            angle_rad = [math.radians(angle) for angle in angle_center]
            self.motion.setAngles(names, angle_rad, 0.1)

            self.textProxy.say("Guarda la palla!")

    def guarda(self,direzione):
        self.direzione  = direzione
        guarda_thread = threading.Thread(target=self.guarda_thread)
        guarda_thread.start()
        
    def fammi_vedere(self):
        self.postureProxy.goToPosture("Stand", 0.6)
        if (device == "robot"):    
                self.animatedTextProxy.say("Fammi vedere qualcosa")
                self.motion.angleInterpolationBezier(self.bracciaAlzate.get_name(), self.bracciaAlzate.get_time()
                                            , self.bracciaAlzate.get_keys())
        else:
                self.animatedTextProxy.say("Fammi vedere qualcosa")
                self.motion.angleInterpolationBezier(self.bracciaAlzate.get_name(), self.bracciaAlzate.get_time()
                                            , self.bracciaAlzate.get_keys())        

    def touch_me(self, messaggio):
        #self.postureProxy.goToPosture("Stand",0.6)
        self.textProxy.say("tocca  " + messaggio)
        datoccare = messaggio
        testa = 0
        mano_sinistra = 0
        mano_destra = 0
        piede_destro = 0
        piede_sinistro = 0
        tempo_inizio = time.time()
        tempo_trascorso = 0.0
        while(testa == 0.0 and mano_sinistra == 0.0 and mano_destra == 0.0 and piede_destro == 0 and piede_sinistro == 0 and tempo_trascorso <100):
            tempo_trascorso = int( time.time() -tempo_inizio )
            testa = self.memoryProxy.getData("Device/SubDeviceList/Head/Touch/Front/Sensor/Value")
            testa = testa or self.memoryProxy.getData("Device/SubDeviceList/Head/Touch/Rear/Sensor/Value")
            testa = testa or self.memoryProxy.getData("Device/SubDeviceList/Head/Touch/Middle/Sensor/Value")
            mano_sinistra  = self.memoryProxy.getData("Device/SubDeviceList/LHand/Touch/Back/Sensor/Value")
            mano_destra  = self.memoryProxy.getData("Device/SubDeviceList/RHand/Touch/Back/Sensor/Value")
            piede_sinistro  = self.memoryProxy.getData("Device/SubDeviceList/LFoot/Bumper/Right/Sensor/Value")
            piede_sinistro  = piede_sinistro and self.memoryProxy.getData("Device/SubDeviceList/LFoot/Bumper/Right/Sensor/Value")
            piede_destro  = self.memoryProxy.getData("Device/SubDeviceList/RFoot/Bumper/Right/Sensor/Value")
            piede_destro  = piede_destro and self.memoryProxy.getData("Device/SubDeviceList/RFoot/Bumper/Right/Sensor/Value")

        if(testa == 1.0):
            toccato = "lamiatesta"
        if(mano_destra == 1.0):
            toccato = "lamiamanodestra"
        if(mano_sinistra == 1.0):
            toccato = "lamiamanosinistra"
        if(piede_sinistro == 1.0):
            toccato ="ilmiopiedesinistro"
        if(piede_destro == 1.0):
            toccato = "ilmiopiededestro"
        if(toccato == datoccare):
            self.textProxy.say("Bravo, hai toccato "+ messaggio)
        else:
            self.textProxy.say("Sbagliato, Hai toccato " + toccato)


        


    def __init__(self, ip, port):
        self.postureProxy = ALProxy("ALRobotPosture",ip,port)
        self.motion = ALProxy("ALMotion",ip,port)
        self.audioProxy = ALProxy("ALAudioPlayer",ip,port)
        self.animatedTextProxy = ALProxy("ALAnimatedSpeech",ip,port)
        self.textProxy = ALProxy("ALTextToSpeech",ip,port)
        self.memoryProxy = ALProxy("ALMemory", ip, port)
        resolution = 1 # 640x480 sceglie 1 per 320x240
        self.video_device_upper = ALProxy('ALVideoDevice',ip, port)
        self.video_device_lower = ALProxy('ALVideoDevice',ip, port)
        if(device == "PC"):
            self.upper = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            self.output_upper = cv2.VideoWriter('upper.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (320,240))
            self.output_lower = cv2.VideoWriter('lower.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (320, 240))

            self.lower = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        else:
            self.upper = self.video_device_upper.subscribeCamera(str(time.time()), 0, resolution, 13, 30)
            self.volumeProxy = ALProxy("ALAudioDevice",ip,port)
            self.volumeProxy.setOutputVolume(50)
            self.ledProxy = ALProxy("ALLeds", ip, port)
            resolution = 1
            self.lower = self.video_device_lower.subscribeCamera(str(time.time()), 1, resolution, 13, 30)

            self.output_upper = cv2.VideoWriter('upper.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (320, 240))
            self.output_lower = cv2.VideoWriter('lower.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (320, 240))
            

        self.id_song = None
        self.stop_ballo = False
        #life = ALProxy("ALAutonomousLife",ip,port)
        #life.setState("disabled")
        self.audio_source = False
        self.motion_source = False
        self.nome = ""
        self.ballo = ""
        self.direzione = ""
        self.nome_cartella = ""
        print("Azioni creato")

ip_robot = "nao.local"
#ip_robot = "desktop-gi62aj9.local."
port_robot = 9559
global device
if("desktop" in ip_robot):
    device = "PC"
else:
    device = "robot"

azioni = Azioni(ip_robot, port_robot)
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


# metodo per il controllo dell'azione richiesta dal client
def esegui_azione(message):
    # pass
    if message == "primo incontro":
        azioni.get_azione_incontro_uno()
        socket.send("Azione eseguita")
    elif "volume_" in message:
        azioni.setVolume(message.split("_")[1])
        socket.send("volume modificato")
    elif "Nome_" in message:

        nome_bambino = message.split("_")[1]
        azioni.setNome(nome_bambino)
        print(nome_bambino)
        socket.send("nome bimbo modificato")
    elif "Audio_" in message:
        azioni.riproduci_audio(message.split("_")[1])
        socket.send("Azione eseguita")
    elif "tocca_" in message:
        azioni.touch_me(message.split("_")[1])
        socket.send("Azione eseguita")
    elif "guarda_" in message:
        azioni.guarda(message.split("_")[1])
        socket.send("Azione eseguita")
    elif "riproduci_" in message:
        azioni.riproduci_testo(message.split("_")[1])
        socket.send("Azione eseguita")
    elif "Classe_" in message:
        azioni.riproduci_verso(message.split("_")[1])
        socket.send("Azione eseguita")
    elif "Ballo_" in message:
        nome_ballo = message.split("_")[1]
        azioni.get_ballo(nome_ballo)
        socket.send(nome_ballo)
    elif message == "secondo incontro":
        azioni.get_azione_incontro_due()
        socket.send("Azione eseguita")
    elif "catturaimmagine_" in message:
        camera = message.split("_")[1]
        if(camera == "upper"):
            azioni.get_azione_cattura_immagine()
        else:
            azioni.get_azione_cattura_immagine_lower()
    elif message == "seduto": # motricita
        azioni.get_azione_siediti_motricita()
        socket.send("Azione eseguita")
    elif message == "su una gamba":
        azioni.get_azione_una_gamba()
        socket.send("Azione eseguita")
    elif message == "in piedi":
        azioni.get_azione_in_piedi()
        socket.send("Azione eseguita")
    elif message == "in piedi normale":
        azioni.get_azione_in_piedi_normale()
        socket.send("Azione eseguita")
    elif message == "Stop_colloquio":
        azioni.get_azione_stop_colloqui()
        socket.send("Stop")
    elif message == "stop_audio":
        azioni.stop_audio()
        socket.send("Audio stoppato")
    elif message == "stop ballo":
        azioni.get_azione_stop_ballo()
        socket.send("Stop")
    elif message == "chiudi":
        azioni.get_chiudi()
        socket.send("Socket chiuso")

        socket.close()
        return "Socket chiuso"
    elif "Congedo_" in message: 
        azioni.get_azione_congedo(message.split("_")[1])
        socket.send("Riprodotto")
    elif "fammivedere_" in message:
        azioni.fammi_vedere()
        socket.send("fammi vedere")
    elif "siediti" in message:
        azioni.get_azione_siediti()
        socket.send("siediti")
    else:
        return "Errore"


while True:
    #  in attesa di una richiesta dal client per poterla eseguire
    stringa = socket.recv()
    risultato = esegui_azione(stringa)
    if risultato == "Socket chiuso":
        break
