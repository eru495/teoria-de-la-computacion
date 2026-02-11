
# Online Python - IDE, Editor, Compiler, Interpreter
class AutomataFinito:
    def __init__(self):
        self.estado_actual = 'q0'  
        self.estado_aceptacion = {'q3'} 
        
    def transicion(self, bit):
        if self.estado_actual == 'q0':
            if bit == '0':
                self.estado_actual = 'q1'
            elif bit == '1':
                self.estado_actual = 'q2'
            
        elif self.estado_actual == 'q1':
            if bit == '1':
                self.estado_actual = 'q3'  
            else:
                self.estado_actual = 'error'
        
        elif self.estado_actual == 'q2':
            if bit == '0' or bit == '1':
                self.estado_actual = 'q3'
            else:
                self.estado_actual = 'error'
        
        elif self.estado_actual == 'q3':
            if bit == '0':
                self.estado_actual = 'q1'
            elif bit == '1':
                self.estado_actual = 'q2'
            
        if self.estado_actual == 'error':
            return False  
            
        return True
        
    def evaluar(self, cadena):
        self.estado_actual = 'q0'  
        for bit in cadena:
            if not self.transicion(bit):
                return False
        return self.estado_actual in self.estado_aceptacion  
        
dfa = AutomataFinito()

pruebas = ["01", "10", "0111", "0011", "01010", "00"]

for p in pruebas:
    resultado = "aceptada" if dfa.evaluar(p) else "rechazada"
    print(f"cadena '{p}': {resultado}")

