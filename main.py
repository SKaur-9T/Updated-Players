from pyscript import document

def generate_names(e):
   
    first_names = ["Leona", "Simrandip", "Phoebe", "Calvin", "Sah-hoen","Gano", "Rafael", "Sean", "Renzo", "Enriquez","Harmony", "Khloe", "Caleb", "Martina", "Ethan","Claire", "Miguel", "Jalainie", "Ivy", "Ramon"]
    last_names = ["Abeleda", "Kaur", "Catimbang", "Garcia", "Choi", "Prince", "Paolo", "Cotioco", "Arce", "Alejandro","Yao", "Espina", "Arias", "Cajucom", "Rivera","Lim", "Sanchez", "Abdullah", "Zosa", "Santos"]

    
    output = "<ol>"

    
    for i in range(len(first_names)):
        output = output + "<li>" + last_names[i] + ", " + first_names[i] + "</li>"

    output = output + "</ol>"

   
    document.getElementById("playersList").innerHTML = output