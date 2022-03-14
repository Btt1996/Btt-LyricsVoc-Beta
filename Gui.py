
from lyricsByModules import song , res,artist ,MyA,Myproj,datenow
from gtts import gTTS
import os
import tkinter as tk
from google_images_search import GoogleImagesSearch


gis = GoogleImagesSearch(MyA, Myproj)
imgdata=song+" "+artist+" album"
with GoogleImagesSearch(MyA, Myproj) as gis:
     _search_params = {
         'q': imgdata
               }
     
     gis.search(search_params=_search_params,path_to_dir="\Images")


root = tk.Tk()

text1 = tk.Text(root, height=20, width=30)

text1.insert(tk.END, '\n')


text1.pack(side=tk.LEFT)

text2 = tk.Text(root, height=30, width=55)
scroll = tk.Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color',
                    foreground='#476042',
                    font=('Tempus Sans ITC', 12, 'bold'))
text2.tag_bind('follow',
               '<1>',
               lambda e, t=text2: t.insert(tk.END, "Not now, maybe later!"))
text2.insert(tk.END,song+" by "+artist+"\n", 'big')
quote = res
text2.insert(tk.END, quote, 'color')
text2.insert(tk.END, 'follow-up\n', 'follow')
text2.pack(side=tk.LEFT)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()


with open("lyrics of "+song+" by "+artist+".txt", "w") as outfile:
     print("attendez pour avoir "+artist+" de "+song)  
     outfile.write(res) 

myobj = gTTS(text="ok your Lyrics for "+song+" by "+artist+"have been saved succesfully", lang="en", slow=False)
myobj.save("ok.mp3")
os.system("mpg321 ok.mp3")

