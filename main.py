from pyscript import document

def generate_names(e):
   
    first_names = ["Bea", "Carl", "Kenzo", "Gurleen", "Leona", "Simrandip", "Phoebe", "Calvin", "Sah-heon","Gano", "Rafael", "Sean", "Renzo", "Enriquez","Harmony", "Khloe", "Caleb", "Martina", "Ethan","Claire", "Miguel", "Jalainie", "Ivy", "Ramon", ]
    last_names = ["Vilale", "Rufo","Guia","Kaur",  "Abeleda", "Kaur", "Catimbang", "Garcia", "Choi", "Prince", "Paolo", "Cotioco", "Arce", "Alejandro","Yao", "Espina", "Arias", "Cajucom", "Rivera","Lim", "Sanchez", "Abdullah", "Zosa", "Santos"]

    
    output = "<ol>"

    
    for i in range(len(first_names)):
        output = output + "<li>" + last_names[i] + ", " + first_names[i] + "</li>"

    output = output + "</ol>"

   

    document.getElementById("playersList").innerHTML = output
