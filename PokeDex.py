from turtle import back
import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO


#create app window
window = tk.Tk()
window.geometry("500x700")
window.configure(bg='#fa6666') 
window.title("Python Pokedex")
window.config(padx=10, pady=10)
window.resizable(False,False) #This disables the user from resizing the window


def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img


    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_types.config(text=" - ".join([t for t in pokemon.types]).title())
   #Divide Height and Weights by 10 for accurate values vis Bulbapedia
    pokemon_height.config(text=f"{pokemon.height / 10}" + " m")
    pokemon_weight.config(text=f"{pokemon.weight / 10}" + " kilograms")
    
    


title_label = tk.Label(window, text="Python Pokedex")
title_label.config(font=("Ariel", 32))
title_label.config(background="#fa6666")
title_label.pack(padx=10, pady=10)

#load pokemon images and other attributes
pokemon_image = tk.Label(window)
pokemon_image.config(background="#fa6666")
pokemon_image.pack()

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Ariel", 15))
pokemon_information.config(background="#fa6666")
pokemon_information.pack(padx=10, pady=10)

pokemon_name = tk.Label(window)
pokemon_name.config(font=("Ariel", 15))
pokemon_name.config(background="#fa6666")
pokemon_name.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Ariel", 15))
pokemon_types.config(background="#fa6666")
pokemon_types.pack(padx=10, pady=10)

pokemon_height = tk.Label(window)
pokemon_height.config(font=("Ariel", 15))
pokemon_height.config(background="#fa6666")
pokemon_height.pack(padx=10, pady=10)

pokemon_weight = tk.Label(window)
pokemon_weight.config(font=("Ariel", 15))
pokemon_weight.config(background="#fa6666")
pokemon_weight.pack(padx=10, pady=10)



#Function to load Pokemon
label_id_name = tk.Label(window, text=" Enter ID (1-898) or Name: ")
label_id_name.config(font=("Arial", 20))
label_id_name.config(background="#fa6666")
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tk.Button(window, text = "Search...", command=load_pokemon)
btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)



window.mainloop(0)
