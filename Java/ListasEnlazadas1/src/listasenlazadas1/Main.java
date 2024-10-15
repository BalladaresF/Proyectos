package listasenlazadas1;


public class Main {

    public static void main(String[] args) {
        //PARTE 1:
        Nodo Primer=new Nodo("Ejemplo");
        Nodo Segundo=new Nodo(45);
        Nodo Tercer=new Nodo("Tercer");
        //Hasta este punto, no están enlazados.
        
        Primer.EnlazarSiguiente(Segundo);                   //se enlaza 1 con 2.
        Primer.ObtenerSiguiente().EnlazarSiguiente(Tercer); //se enlaza 2 con 3.
        
        System.out.println(Primer.ObtenerSiguiente().ObtenerSiguiente().ObtenerValor());    //imprime el tercer valor a partir del primero.
        
        //PARTE 2:
        ListaEnlazada Lista=new ListaEnlazada(); 
        System.out.println("\nVacía: "+Lista.Vacia());
        
        Lista.AñadirPrimero(6);
        Lista.AñadirPrimero(5);
        Lista.AñadirPrimero(4);
        Lista.AñadirPrimero(3);
        Lista.AñadirPrimero(2);
        Lista.AñadirPrimero(1);      //todo se añade en el index 0. Es decir, el primer elemento será 1 y el último será 6.
        
        
        System.out.println("Primer elemento: "+Lista.Obtener(0));
        System.out.println("Último elemento: "+Lista.Obtener(Lista.Size()-1));
        System.out.println("Index 2: "+Lista.Obtener(2));
        
        System.out.println("Vacía: "+Lista.Vacia());
        System.out.println("Tamaño: "+Lista.Size());
        
        //PARTE 3:
        Lista.EliminarPrimero();
        System.out.println("\nPrimer elemento: "+Lista.Obtener(0));
        System.out.println("Tamaño: "+Lista.Size());
        
        Lista.Eliminar(2);
        System.out.println("\nPrimer elemento: "+Lista.Obtener(0));
        System.out.println("Index 2: "+Lista.Obtener(2));
        System.out.println("Tamaño: "+Lista.Size());
        
        Lista.Cortar(2);
        System.out.println("\nPrimer elemento: "+Lista.Obtener(0));
        System.out.println("Último elemento: "+Lista.Obtener(Lista.Size()-1));
        System.out.println("Tamaño: "+Lista.Size());
    }
}
