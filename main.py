
# Online Python - IDE, Editor, Compiler, Interpreter

def acepta(afd, w):
    estado=afd(["inicio"])
    rec=[estado]
    for s in w: 
        if s not in  afd["alfabeto"]:
            return false, rec
            
            if (estado,s) not in afd["delta"]:
                return false, rec
                
            estado=afd["delta"][(estado,s)]
            rec.append(estado)
            
            return (estado in afd["finales"]), rec
            
            def main(): 
                afd={
                    "alfabeto": {"a","b"},
                    "inicio":"q0",
                    "finales":{"q2"},
                    "delta":{
                        ("q0","a"):"q1",
                        ("q1","a"):"q1",
                        ("q2","b"):"q2"
                    }
                    
                }
                w=input("cadena (a,b):").strip()
                ok,rec=acepta(afd,w)
                print("recorrido:","->".join(rec))
                print("aceptada"if ok else "rechazada")
                
                if __name__=="__main__":
                    main()

