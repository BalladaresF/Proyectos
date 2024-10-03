/*
 * Aquí se maneja lo relacionado al árbol binario.
 */
package proyecto2;


/**
 *
 * @author Andres B
 */
public class Arbol {

    String Preorden="";
    String Inorden="";
    String Postorden="";
    StringBuilder DatosPreorden=new StringBuilder(Preorden);
    StringBuilder DatosInorden=new StringBuilder(Inorden);
    StringBuilder DatosPostorden=new StringBuilder(Postorden);
    
    String AddPreorden;
    String AddInorden;
    String AddPostorden;
    
    private Nodo raiz;
    public Arbol() {

    }

    public boolean EstaVacio(){
        return this.raiz==null;
    }
    
    public Nodo getRaiz(){
        return raiz;
    }
    
    public boolean EsHoja(Nodo n){
        return n.getIzquierda()==null && n.getDerecha()==null;
    }
    public boolean EsInterno(Nodo n){
        return !EsHoja(n);
    }
    
    //Aquí se busca en los elementos del árbol si existe algún número en cuestión.
    public boolean existe(int busqueda) {
        return existe(this.raiz, busqueda);
    }
    private boolean existe(Nodo n, int busqueda) {
        if (n == null) {
            return false;
        }
        if (n.getDato() == busqueda) {
            return true;
        } else if (busqueda < n.getDato()) {
            return existe(n.getIzquierda(), busqueda);
        } else {
            return existe(n.getDerecha(), busqueda);
        }
    }

    public void insertar(int dato) {
        if (this.raiz == null) {
            this.raiz = new Nodo(dato);
        } else {
            this.insertar(this.raiz, dato);
        }
    }

    private void insertar(Nodo padre, int dato) {
        if (dato > padre.getDato()) {
            if (padre.getDerecha() == null) {
                padre.setDerecha(new Nodo(dato));
            } else {
                this.insertar(padre.getDerecha(), dato);
            }
        } else {
            if (padre.getIzquierda() == null) {
                padre.setIzquierda(new Nodo(dato));
            } else {
                this.insertar(padre.getIzquierda(), dato);
            }
        }
    }

    //Métodos para obtener el preorden, inorden y postorden. Estos se han realizado recursivamente.
    private void preorden(Nodo n) {
        if (n != null) {
            AddPreorden=n.getDato()+ " ";
            DatosPreorden.append(AddPreorden);
            preorden(n.getIzquierda());
            preorden(n.getDerecha());
        }   
    }
    private void inorden(Nodo n) {
        if (n != null) {
            inorden(n.getIzquierda());
            AddInorden=n.getDato()+ " ";
            DatosInorden.append(AddInorden);
            inorden(n.getDerecha());
        }
    }
    private void postorden(Nodo n) {
        if (n != null) {
            postorden(n.getIzquierda());
            postorden(n.getDerecha());
            AddPostorden=n.getDato()+ " ";
            DatosPostorden.append(AddPostorden);
        }
    }

    //Aquí se consiguen en valores tipo String los distintos ordenamientos del árbol binario.
    public String preorden() {
        this.preorden(this.raiz);
        String Datos=DatosPreorden.toString();
        return Datos;
    }
    public String inorden() {
        this.inorden(this.raiz);
        String Datos=DatosInorden.toString();
        return Datos;
    }
    public String postorden() {
        this.postorden(this.raiz);
        String Datos=DatosPostorden.toString();
        return Datos;
    }
 
    //Aquí se manejan los métodos para borrar los datos en el árbol y los strings.
    public void VaciarStrings(){
        DatosPreorden.delete(0, DatosPreorden.length());
        DatosInorden.delete(0, DatosInorden.length());
        DatosPostorden.delete(0, DatosPostorden.length());
    }
    public void EliminarTodo(){
        this.raiz=null;
        DatosPreorden.delete(0, DatosPreorden.length());
        DatosInorden.delete(0, DatosInorden.length());
        DatosPostorden.delete(0, DatosPostorden.length());
    }
    
    //Aquí se cuentan los nodos recursivamente.
    public int CuentaNodos(Nodo n){
        int NumeroNodos=1;
        
        if(n.getIzquierda()!=null){
            NumeroNodos+=CuentaNodos(n.getIzquierda());
        }
        if(n.getDerecha()!=null){
            NumeroNodos+=CuentaNodos(n.getDerecha());
        }
        
        return NumeroNodos;
    }
    
    //Aquí se cuentan las hojas recursivamente.
    public int CuentaHojas(Arbol Arbol, Nodo n){
        int NumeroHojas=0;
        
        if (Arbol.EsHoja(n)){
            NumeroHojas=1;
        }else{
            if(n.getIzquierda()!=null){
            NumeroHojas+=CuentaHojas(Arbol, n.getIzquierda());
            }
            if(n.getDerecha()!=null){
               NumeroHojas+=CuentaHojas(Arbol, n.getDerecha());
            }
        }
        
        return NumeroHojas;
    }
    
    //Aquí se encuentra la altura de forma recursiva.
    public int Altura(Nodo n){
        int NumeroAltura=0;
        
        if(EsInterno(n)){
            if(n.getIzquierda()!=null){
                NumeroAltura=Math.max(NumeroAltura, Altura(n.getIzquierda()));  //Math.max se encarga de sacar el mayor de los 2 valores.
            }
            if(n.getDerecha()!=null){
                NumeroAltura=Math.max(NumeroAltura, Altura(n.getDerecha()));
            }
            NumeroAltura++;
        }
        
        return NumeroAltura;
    }
    
    //Aquí se busca el nodo mayor y el nodo menor. Este último es eliminado del árbol.
    public int BuscarMayor(){
        int mayor=raiz.getDato();
        Nodo nodo=raiz;
        
        while(nodo.getDerecha()!=null){
            nodo=nodo.getDerecha();
            mayor=nodo.getDato();
        }
        
        return mayor;
    }
    public int BuscarMenor(){
        int menor=raiz.getDato();
        Nodo nodo=raiz;
        
        while(nodo.getIzquierda()!=null){
            nodo=nodo.getIzquierda();
            menor=nodo.getDato();
        }

        return menor;
    }
    public void EliminarMenor(){
        
    }

}

//https://devs4j.com/2017/12/04/borrar-elementos-de-un-arbol-binario/

