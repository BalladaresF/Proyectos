
package listasenlazadas1;

public class ListaEnlazada {
    Nodo Cabeza;
    int Size;
    
    public ListaEnlazada(){
        Cabeza=null;
        Size=0;
    }
    
    public void AñadirPrimero(Object obj){  //añadirá un primer elemento.
        if(Cabeza==null){
            Cabeza=new Nodo(obj);
        }
        else{
            Nodo temp=Cabeza;
            Nodo Nuevo=new Nodo(obj);
            Nuevo.EnlazarSiguiente(temp);
            Cabeza=Nuevo;
        }
        Size++;
    }
    
    public Object Obtener(int Index){   //Obtendrá el elemento que se solicite.
        int Contador=0;
        Nodo Temporal=Cabeza;
        while(Contador<Index){
            Temporal=Temporal.ObtenerSiguiente();
            Contador++;
        }
        return Temporal.ObtenerValor();
    }
    
    public void EliminarPrimero(){
        Cabeza=Cabeza.ObtenerSiguiente();
        Size--;
    }
    
    public void Eliminar(int Index){
        if(Index==0){
            Cabeza=Cabeza.ObtenerSiguiente();
        }
        else{
            int Contador=0;
            Nodo Temporal=Cabeza;

            while(Contador<Index-1){
                Temporal=Temporal.ObtenerSiguiente();
                Contador++;
            }
            Temporal.EnlazarSiguiente(Temporal.ObtenerSiguiente().ObtenerSiguiente()); 
        }
        Size--;
    }
    
    public void Cortar(int Index){  //todo lo que va después del Index desaparece.
        int Contador=0;
        Nodo Temporal=Cabeza;
        while(Contador<Index-1){
            Temporal=Temporal.ObtenerSiguiente();
            Contador++;
        }
        Temporal.EnlazarSiguiente(null);
        Size=Index;
    }
    
    public int Size(){
        return Size;
    }
    
    public boolean Vacia(){
        return(Cabeza==null);   //devolverá true o false.
    }
}
