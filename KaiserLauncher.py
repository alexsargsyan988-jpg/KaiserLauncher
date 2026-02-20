import tkinter as tk
import webview

def start():
    if selected_version.get() == "Minecraft 1.8.9":
        webview.create_window("My Browser", "https://client.eaglercraft.win/eagler-files/1.8/Main/index.html")
        webview.start()
    if selected_version.get() == "Classic":
        webview.create_window("My Browser", "https://classic.minecraft.net/")
        webview.start()
    if selected_version.get() == "Paper Edition":
        webview.create_window("My Browser", "https://turbowarp.org/10128407/fullscreen")
        webview.start()
    if selected_version.get() == "Minecraft 1.5.2":
        webview.create_window("My Browser", "https://client.eaglercraft.win/eagler-files/1.5.2/main/index.html")
        webview.start()
    if selected_version.get() == "Minecraft 1.21.1":
        webview.create_window("My Browser", "https://client.eaglercraft.win/eagler-files/modded/1.8/EaglyMC/index.html")
        webview.start()
    if selected_version.get() == "Minecraft 1.7.3":
        webview.create_window("My Browser", "https://client.eaglercraft.win/eagler-files/1.7.3/Main/index.html")
        webview.start()
    if selected_version.get() == "Minecraft 1.12.2":
        webview.create_window("My Browser", "https://client.eaglercraft.win/eagler-files/1.12/Main/index.html")
        webview.start()
    if selected_version.get() == "Minecraft Beta 1.3":
        webview.create_window("My Browser", "https://client.eaglercraft.win/eagler-files/b1.3/Main/index.html")
        webview.start()
    if selected_version.get() == "Minecraft For Extra  slow PCs":
        webview.create_window("My Browser", "https://turbowarp.org/50029544/fullscreen")
        webview.start()
def About():
    root = tk.Tk()
    root.title("About KaiserLauncher")
    root.geometry("500x300")
    root.configure(bg="gray")
    abel = tk.Label(root, text="KaiserLauncher", font=("Fixedsys", 16), bg="gray", fg="white")
    abel.place(x=20, y=20)
    abel = tk.Label(root, text="KaiserLauncher Version 0.2", font=("Fixedsys", 16), bg="gray", fg="white")
    abel.place(x=20, y=100)
    xabel = tk.Label(root, text="Made By 卐EINHEITSPAKT卐", font=("Fixedsys", 16), bg="gray", fg="white")
    xabel.place(x=20, y=150)





root = tk.Tk()
root.title("KaiserLauncher")  
root.geometry("500x300")
root.configure(bg="gray")




top = tk.Frame(root, bg="gray", width=500, height=100)
top.place(x=0, y=0)
bottom = tk.Frame(root, bg="#171717", width=500, height=100)
bottom.place(x=0, y=200)
text = tk.Text(root, width=60, height=5, font=("Fixedsys", 12), bg="lightgray")
text.place(x=10, y=100)
scrollbar = tk.Scrollbar(root, command=text.yview)
scrollbar.place(x=480, y=100, height=85)
text.config(yscrollcommand=scrollbar.set)
text.insert("end", "KaiserLauncher is a project made by 卐EINHEITSPAKT卐         " )
text.insert("end", "its main goal is to help people with old PCs play MC            " )
text.insert("end", "Thanks For Playing.            " )
text.config(fg="red")

label = tk.Label(root, text="KaiserLauncher", font=("Fixedsys", 16), bg="gray", fg="white")
label.place(x=20, y=20)

# Choice list (dropdown without extra imports)
selected_version = tk.StringVar(root)
selected_version.set("Minecraft 1.5.2")

dropdown = tk.OptionMenu(
    root,
    selected_version,
    "Minecraft 1.5.2",
    "Minecraft 1.8.9",
    "Minecraft 1.12.2",
    "Minecraft 1.21.1",
    "Minecraft 1.7.3",
    "Minecraft Beta 1.5",
    "InfDev",
    "Classic",
    "Minecraft For Extra  slow PCs",
    "Paper Edition"
)
dropdown.config(
    font=("Fixedsys", 12),
    bg="black",
    fg="white",
    activebackground="lime",
    activeforeground="white",
    highlightthickness=0
)
dropdown["menu"].config(bg="#171717", fg="white")
dropdown.place(x=200, y=20)

Gamepad = tk.StringVar(root)
Gamepad.set("Gamepad")
dropdowng= tk.OptionMenu(
    root,
    Gamepad,
    "Off",
    "On"
)
dropdowng.config(
    font=("Fixedsys", 12),
    bg="black",
    fg="white",
    activebackground="lime",
    activeforeground="white",
    highlightthickness=0
)
dropdowng["menu"].config(bg="#171717", fg="white")
dropdowng.place(x=200, y=65)



btn = tk.Button(root, text="Play",  command=start,
                font=("Fixedsys", 12), bg="black", fg="white",
                activebackground="lime", activeforeground="white",
                highlightthickness=0)

abtn = tk.Button(root, text="About",  command=About,
                font=("Fixedsys", 12), bg="black", fg="white",
                activebackground="lime", activeforeground="white",
                highlightthickness=0)



btn.place(x=225, y=250)
abtn.place(x=20, y=50)

root.mainloop()
