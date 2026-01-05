#script care schimba numele fisierelor
import os

path = r"A:FILME\Community S04"

for nume_fisier in os.listdir(path):
    i=nume_fisier.find("1080")
    if i!=-1:
        nume_nou=nume_fisier[:i-1] + os.path.splitext(nume_fisier)[1]
        p_vechi=os.path.join(path,nume_fisier)
        p_nou=os.path.join(path,nume_nou)
        os.rename(p_vechi,p_nou)
        print(f"Am redenumit :{nume_fisier} cu :{nume_nou}!")