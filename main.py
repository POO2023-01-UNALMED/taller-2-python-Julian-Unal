class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados = cantidadCreados

    def verificarIntegridad(self):
        if (validateRegistros()):
            return "Auto original";
        return "Las piezas no son originales";
    

    def validateRegistros(self) :    
        if (self.registro != self.motor.registro) :
            return false;
        

        for asiento in self.asientos:
            if (asiento != null):
                return asiento.registro == self.registro;
            return  true;
        
        
    def cantidadAsientos(self):
        return true
    
class Motor :
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def asignarTipo(self, tipo) :
        if (validateTipo(tipo)) :
            self.tipo = tipo;
        
        print("Tipo not updated, invalid tipo")
    

    def validateTipo(self, tipo) :
        if (tipo != "electrico" & tipo != "gasolina") :
            return false
        
        return true
    

    def cambiarRegistro(registro):
        self.registro = registro;
    


class Asiento :

    color;
    precio;
    registro;

    def cambiarColor(self, color ) :
        if (validateColor(color)) :
            self.color = color;
        
        print("Color not updated, invalid color");
    

    def validateColor(self, color) :
        if (color != "rojo" & color != "verde" & color !=  "amarillo" & color !=  "negro" & color !=  "blanco") :
            return false;
        
        return true;
    
