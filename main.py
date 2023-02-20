class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def verificarIntegridad(self):
        if (self.validateRegistros()):
            return "Auto original";
        return "Las piezas no son originales";
    

    def validateRegistros(self) :    
        if (self.registro != self.motor.registro) :
            return False;
        

        for asiento in self.asientos:
            if (asiento):
                return asiento.registro == self.registro;
            return  True;
        
        
    def cantidadAsientos(self):
        count = 0
        for asiento in self.asientos:
            if (isinstance(asiento, Asiento)):
                count+=1
        return count
    
class Motor :
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def asignarTipo(self, tipo) :
        if (self.validateTipo(tipo)) :
            self.tipo = tipo;
        
        print("Tipo not updated, invalid tipo")
    

    def validateTipo(self, tipo) :
        if (tipo != "electrico" and tipo != "gasolina") :
            return False
        
        return True
    

    def cambiarRegistro(self, registro):
        self.registro = registro;
    


class Asiento :
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color ) :
        if (self.validateColor(color)) :
            self.color = color;
        
        print("Color not updated, invalid color");
    

    def validateColor(self, color) :
        if (color != "rojo" and color != "verde" and color !=  "amarillo" and color !=  "negro" and color !=  "blanco") :
            return False;
        
        return True;
    
