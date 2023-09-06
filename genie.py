import json
import torch
from speak import talk
import datetime
from brain import NeuralNet
from listen import listen
from task import NonInputExecution,InputExecution
from NeuralNet import tokenize,bag_of_words
import random

def wishMe():
    hour = int(datetime.datetime.now().hour)
    time = datetime.datetime.now().strftime('%H : %M')
    if hour>=0 and hour<12:
        talk(f"Good Morning!,its  {time}")

    elif hour>=12 and hour<18:
        talk(f"Good Afternoon!,its {time}")

    else:
        talk(f"Good Evening!,its {time}")

    talk("I am  genie Sir. Please tell me how may I help you")
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open('intents.json','r') as json_data:
    intents = json.load(json_data)
FILE = "TrainData.pth"
data = torch.load(FILE)
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]
model = NeuralNet(input_size,hidden_size,output_size).to(device=device)
model.load_state_dict(model_state)
model.eval()
Name = "Genie"
def main():
    wishMe()
    a = 1
    while a == 1:
        try:
            sentence = listen()
            result = str(sentence)
            sentence = tokenize(sentence)
            x = bag_of_words(sentence,all_words)
            x = x.reshape(1,x.shape[0])
            x = torch.from_numpy(x).to(device)
            output = model(x)
            _,predicted = torch.max(output,dim=1)
            tag = tags[predicted.item()]
            probs = torch.softmax(output,dim=1)
            prob = probs[0][predicted.item()]
            if prob.item() > 0.75:
                for intent in intents["intents"]:
                    if tag == intent["tag"]:
                        reply = random.choice(intent["responses"])
                        sd = intent["tag"]
                        if "bye" in reply:
                            talk(reply)
                            a=0
                        elif "time" in sd:
                            NonInputExecution(sd)
                        elif "date" in sd:
                            NonInputExecution(sd)
                        elif "day" in sd:
                            NonInputExecution(sd)
                        elif "wikipedia" in sd:
                            InputExecution(sd,result)
                        elif "google" in sd:
                            InputExecution(sd,result)
                        elif "play" in sd:
                            InputExecution(sd,result)
                        elif "temperature" in sd:
                            InputExecution(sd,result)
                        elif "how to" in sd:
                            InputExecution(sd,result)
                        elif "news" in sd:
                            InputExecution(sd,result)
                        elif "where am i" in sd:
                            InputExecution(sd,result)
                        elif "joke" in sd:
                            InputExecution(sd,result)
                        elif "ip address" in sd:
                            InputExecution(sd,result)
                        elif "planet" in sd:
                            InputExecution(sd,result)
                        elif "remember" in sd:
                            InputExecution(sd,result)
                        elif "rememebered data" in sd:
                            InputExecution(sd,result)
                        elif "youtube search" in sd:
                            InputExecution(sd,result)
                        elif "download" in sd:
                            InputExecution(sd,result)
                        elif "speedtest" in sd:
                            InputExecution(sd,result)
                        elif "where-is" in sd:
                            InputExecution(sd,result)
                        elif "chrome" in sd:
                            InputExecution(sd,result)
                        elif "YouTubeAuto" in sd:
                            InputExecution(sd,result)
                        elif "WindowsAuto" in sd:
                            InputExecution(sd,result)
                        elif "open" in sd:
                            InputExecution(sd,result)
                        elif "website" in sd:
                            InputExecution(sd,result)
                        elif "close" in sd:
                            InputExecution(sd,result)
                        elif "WhatsappMsg" in sd:
                            InputExecution(sd,result)
                        elif "call" in sd:
                            InputExecution(sd,result)
                        elif "showchat" in sd:
                            InputExecution(sd,result)
                        elif "translate" in sd:
                            InputExecution(sd,result)
                        elif "table" in sd:
                            InputExecution(sd,result)
                        elif "nasa" in sd:
                            InputExecution(sd,result)
                        else:
                            talk(reply)
        except:
            pass

