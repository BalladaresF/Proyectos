/*
 * Aquí se manejan los nodos, que son usados por el árbol binario.
 */
package proyecto2;

/**
 *
 * @author Andres B
 */
public class Nodo {
    int dato;
    Nodo izquierda, derecha;

    public Nodo(int dato) {
        this.dato = dato;
        this.izquierda = this.derecha = null;
    }


    public int getDato() {
        return dato;
    }

    public Nodo getIzquierda() {
        return izquierda;
    }

    public void setIzquierda(Nodo izquierda) {
        this.izquierda = izquierda;
    }

    public Nodo getDerecha() {
        return derecha;
    }

    public void setDerecha(Nodo derecha) {
        this.derecha = derecha;
    }
    
    public Nodo EncontrarPredecesor(){
        if(this.getDerecha()==null){
            return this;
        }else{
            return this.getDerecha().EncontrarPredecesor();
        }
    }
    
    public Nodo EncontrarSucesor(){
        if(this.getIzquierda()==null){
            return this;
        }else{
            return this.getIzquierda().EncontrarSucesor();
        }
    }
    
    public Nodo Borrar(int Valor) {
        Nodo response = this;
        if (Valor < this.dato) {        
            this.izquierda = this.izquierda.Borrar(Valor);    
        }else if (Valor > this.dato) {
            this.derecha = this.derecha.Borrar(Valor);
        }else {
            if (this.izquierda != null && this.derecha != null) {
                Nodo temp = this;
                Nodo maxOfTheLeft = this.izquierda.EncontrarPredecesor();
                this.dato = maxOfTheLeft.getDato();
                temp.izquierda=temp.izquierda.Borrar(maxOfTheLeft.getDato());
            } else if (this.izquierda != null) {
                response = this.izquierda;
            } else if (this.derecha != null) {
                response = this.derecha;
            } else {
                response = null;
            }
        }
        return response;
    }

}
