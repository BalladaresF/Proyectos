package listasenlazadas1;

public class Nodo {
    Object Valor;   //Object: variable que puede almacenar cualquier tipo de dato.
    Nodo Siguiente; //Puntero.
    
    public Nodo(Object Valor){  //constructor para llamar valores desde el main.
        this.Valor=Valor;
        this.Siguiente=null;
    }
    
    public Object ObtenerValor(){
        return Valor;
    }
    
    public void EnlazarSiguiente(Nodo n){
        Siguiente=n;
    }
    
    public Nodo ObtenerSiguiente(){
        return Siguiente;
    }
}
