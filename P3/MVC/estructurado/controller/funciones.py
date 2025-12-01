from tkinter import messagebox

def operaciones(n1,n2,signo):
    if signo=="+":
        ope=n1+n2
        tipo_ope="Suma"
    elif signo=="-":
        ope=n1-n2
        tipo_ope="Resta"
    elif signo=="x":
        ope=n1*n2
        tipo_ope="Multiplicacion"  
    elif signo=="/":
        ope=(n1/n2)
        tipo_ope="Divsion"

    messagebox.showinfo(title=tipo_ope,icon="info",message=f"{n1}{signo}{n2}={ope}")
    
