/*
 * Aquí se realizan todas las funciones del proyecto. En la pantalla, se muestran los tiempos realizados, la lista desordenada y la lista ordenada.
 */
package Clases;

import java.util.Random;

/**
 *
 * @author Andres B
 */
public final class Pantalla extends javax.swing.JFrame {
    //Variable original donde se almacenará la lista aleatoria:
    double[] Valores=new double [2000];             
    
    //Copias de la variable que serán ordenadas con los algoritmos:
    double[] CopiaUno=new double [2000];
    double[] CopiaDos=new double [2000];
    double[] CopiaTres=new double [2000];
    double[] CopiaCuatro=new double [2000];
    
    //Variables que almacenarán los tiempos de cada algoritmo:
    long TiempoUno;
    long TiempoDos;
    long TiempoTres;
    long TiempoCuatro;
    
    /**
     * Creates new form Pantalla
     */
    
    public Pantalla() {
        //Aquí se crean los valores aleatorios:
        for(int i=0; i<Valores.length; i++){
            Random Random=new Random();
            Valores[i]=Random.nextDouble();
            CopiaUno[i]=Valores[i];
            CopiaDos[i]=Valores[i];
            CopiaTres[i]=Valores[i];
            CopiaCuatro[i]=Valores[i];
        }
        
        //Aquí se ordenan por burbuja:
        long Inicio=System.nanoTime();
        Burbuja(CopiaUno);
        long Fin=System.nanoTime();
        TiempoUno=(Fin-Inicio);
        
        //Aquí se ordenan por inserción:
        Inicio=System.nanoTime();
        Insercion(CopiaDos);
        Fin=System.nanoTime();
        TiempoDos=(Fin-Inicio);
        
        //Aquí se ordenan por mezclas:
        Inicio=System.nanoTime();
        MezclasDividir(CopiaTres);
        Fin=System.nanoTime();
        TiempoTres=(Fin-Inicio);
        
        //Aquí se ordenan por rápido:
        Inicio=System.nanoTime();
        RapidoDetector(CopiaCuatro);
        Fin=System.nanoTime();
        TiempoCuatro=(Fin-Inicio);
        
        initComponents();
    }
    
        
        
    /**
     * This method is called from within the constructor to initialize the form. WARNING: Do NOT modify this code. The content of this method is always regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        ListaSinOrdenar = new java.awt.TextArea();
        ListaOrdenada = new java.awt.TextArea();
        Titulo = new javax.swing.JLabel();
        Titulo1 = new javax.swing.JLabel();
        Titulo2 = new javax.swing.JLabel();
        Etiqueta1 = new javax.swing.JLabel();
        Etiqueta2 = new javax.swing.JLabel();
        jScrollPane = new javax.swing.JScrollPane();
        TablaComparativa = new javax.swing.JTable();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Proyecto 1");

        jPanel1.setBackground(new java.awt.Color(0, 51, 51));

        ListaSinOrdenar.setEditable(false);
        for(int i=0; i<Valores.length; i++){
            String Datos=Double.toString(Valores[i]);
            ListaSinOrdenar.append(Datos+"\n");
        }
        ListaSinOrdenar.setFont(new java.awt.Font("Microsoft JhengHei", 0, 18)); // NOI18N

        ListaOrdenada.setEditable(false);
        //Debido a que el resultado es el mismo, se puede intercambiar CopiaUno con cualquiera de las copias
        for(int i=0; i<CopiaUno.length; i++){
            String Datos=Double.toString(CopiaUno[i]);
            ListaOrdenada.append(Datos+"\n");
        }
        ListaOrdenada.setFont(new java.awt.Font("Microsoft JhengHei", 0, 18)); // NOI18N

        Titulo.setFont(new java.awt.Font("Microsoft JhengHei", 0, 24)); // NOI18N
        Titulo.setForeground(new java.awt.Color(255, 255, 255));
        Titulo.setText("Algoritmos de ordenación");

        Titulo1.setFont(new java.awt.Font("Microsoft JhengHei", 0, 18)); // NOI18N
        Titulo1.setForeground(new java.awt.Color(255, 255, 255));
        Titulo1.setText("A continuación, se ordena una lista de 2000 valores usando");

        Titulo2.setFont(new java.awt.Font("Microsoft JhengHei", 0, 18)); // NOI18N
        Titulo2.setForeground(new java.awt.Color(255, 255, 255));
        Titulo2.setText("los siguientes algoritmos:");

        Etiqueta1.setFont(new java.awt.Font("Microsoft JhengHei", 0, 18)); // NOI18N
        Etiqueta1.setForeground(new java.awt.Color(255, 255, 255));
        Etiqueta1.setText("Lista sin ordenar:");

        Etiqueta2.setFont(new java.awt.Font("Microsoft JhengHei", 0, 18)); // NOI18N
        Etiqueta2.setForeground(new java.awt.Color(255, 255, 255));
        Etiqueta2.setText("Lista ordenada:");

        TablaComparativa.setFont(new java.awt.Font("Microsoft JhengHei", 0, 18)); // NOI18N
        TablaComparativa.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {"Burbuja", TiempoUno+" ns"},
                {"Inserción", TiempoDos+" ns"},
                {"Mezclas", TiempoTres+" ns"},
                {"Rápido", TiempoCuatro+" ns"}
            },
            new String [] {
                "Algoritmo", "Tiempo realizado (nanosegundos)"
            }
        ));
        jScrollPane.setViewportView(TablaComparativa);

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGap(68, 68, 68)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(Etiqueta1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addComponent(ListaSinOrdenar, javax.swing.GroupLayout.PREFERRED_SIZE, 240, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addGap(0, 0, Short.MAX_VALUE)))
                        .addGap(18, 18, 18)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(Etiqueta2, javax.swing.GroupLayout.PREFERRED_SIZE, 240, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(ListaOrdenada, javax.swing.GroupLayout.PREFERRED_SIZE, 240, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addContainerGap(67, Short.MAX_VALUE))
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(Titulo1)
                            .addComponent(Titulo2))
                        .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))))
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGap(176, 176, 176)
                .addComponent(Titulo)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(jScrollPane, javax.swing.GroupLayout.PREFERRED_SIZE, 400, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(111, 111, 111))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                .addGap(21, 21, 21)
                .addComponent(Titulo)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(Titulo1)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(Titulo2)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 35, Short.MAX_VALUE)
                .addComponent(jScrollPane, javax.swing.GroupLayout.PREFERRED_SIZE, 111, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(30, 30, 30)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(Etiqueta2)
                    .addComponent(Etiqueta1))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(ListaSinOrdenar, javax.swing.GroupLayout.PREFERRED_SIZE, 314, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(ListaOrdenada, javax.swing.GroupLayout.PREFERRED_SIZE, 314, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(46, 46, 46))
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(0, 6, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Pantalla.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Pantalla.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Pantalla.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Pantalla.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                
                new Pantalla().setVisible(true);
            }
        });
    }
    
    //Ordenamiento por burbuja:
    //Observaciones: Este es el más lento de todos, pero el más sencillo de programar.
    private void Burbuja(double[] Valores){
        double Aux;
        
        for (int i = 0; i < Valores.length - 1; i++) {
            for (int j = 0; j < Valores.length - i - 1; j++) {                                                              
                if (Valores[j+1] <Valores[j]) {
                    Aux = Valores[j+1];
                    Valores[j+1] = Valores[j];
                    Valores[j] = Aux;
                }
            }
        }
    }
    
    //Ordenamiento por inserción:
    //Observaciones: Este es usualmente más rápido que el de burbuja, pero en ocasiones es más lento.
    private void Insercion(double[] Valores){
        double Aux;
        
        for(int i=1; i<Valores.length; i++){
            Aux=Valores[i];
            for(int j=i-1; j>=0 && Valores[j]>Aux; j--){
                Valores[j+1]=Valores[j];
                Valores[j]=Aux;
            }
        }
    }
    
    //Ordenamiento por mezclas:
    //Observaciones: Este es mucho más rápido que los 2 anteriores, pero junto con el siguiente son los más complejos de programar.
    private void MezclasDividir(double[] Valores){   //esto es para llamar solo a Valores cuando se quiere ejecutar el método.
        MezclasDividir(Valores, Valores.length);
    }
    private void MezclasDividir(double[] Valores, int Cantidad){     //se encarga de dividir la lista.
        
        if (Cantidad < 2) {
            return;
        }
        
        int Mitad = Cantidad / 2;
        double[] Iquierda = new double[Mitad];
        double[] Derecha = new double[Cantidad - Mitad];

        System.arraycopy(Valores, 0, Iquierda, 0, Mitad);
        for (int i = Mitad; i < Cantidad; i++) {
            Derecha[i - Mitad] = Valores[i];
        }
        
        MezclasDividir(Iquierda, Mitad);
        MezclasDividir(Derecha, Cantidad - Mitad);

        MezclasOrdenamiento(Valores, Iquierda, Derecha, Mitad, Cantidad - Mitad);
    }
    
    private void MezclasOrdenamiento(double[] Valores, double[] Izquierda, double[] Derecha, int MitadUno, int MitadDos) {       //se encarga de ordenar y juntar las listas.
        int i = 0, j = 0, k = 0;
        
        while (i < MitadUno && j < MitadDos) {
            if (Izquierda[i] <= Derecha[j]) {
                Valores[k++] = Izquierda[i++];
            }
            else {
                Valores[k++] = Derecha[j++];
            }
        }
        
        while (i < MitadUno) {
            Valores[k++] = Izquierda[i++];
        }
        
        while (j < MitadDos) {
            Valores[k++] = Derecha[j++];
        }
    }
    
    //Ordenamiento rápido:
    //Observaciones: Este es usualmente el más rápido de los 4.
    private void RapidoDetector(double[] Valores){       //esto es para llamar solo a Valores cuando se quiere ejecutar el método.
        RapidoDetector(Valores, 0, Valores.length-1);
    }
    private void RapidoDetector(double[] Valores, int MitadUno, int MitadDos){       //se encarga de mover Izquierda y Derecha para detectar números por mover.
        if(MitadUno>=MitadDos){
            return;
        }
        
        double Pivote=Valores[MitadDos];    //el pivote puede ser cualquier elemento del arreglo. En este caso se eligió el último valor.
        
        int Izquierda=MitadUno;
        int Derecha=MitadDos;
        
        while(Izquierda<Derecha){
            while(Valores[Izquierda]<=Pivote && Izquierda<Derecha){
                Izquierda++;
            }
            while(Valores[Derecha]>=Pivote && Izquierda<Derecha){
                Derecha--;
            }
            RapidoOrdenamiento(Valores, Izquierda, Derecha);
        }
        RapidoOrdenamiento(Valores, Izquierda, MitadDos);
        
        RapidoDetector(Valores, MitadUno, Izquierda-1);
        RapidoDetector(Valores, Izquierda+1, MitadDos);
    }
    
    private void RapidoOrdenamiento(double[] Valores, int IndiceUno, int IndiceDos){     //se encarga de intercambiar los valores de los números a mover.
        double Aux=Valores[IndiceUno];
        Valores[IndiceUno]=Valores[IndiceDos];
        Valores[IndiceDos]=Aux;
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JLabel Etiqueta1;
    private javax.swing.JLabel Etiqueta2;
    private java.awt.TextArea ListaOrdenada;
    private java.awt.TextArea ListaSinOrdenar;
    private javax.swing.JTable TablaComparativa;
    private javax.swing.JLabel Titulo;
    private javax.swing.JLabel Titulo1;
    private javax.swing.JLabel Titulo2;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JScrollPane jScrollPane;
    // End of variables declaration//GEN-END:variables

}
//Videos complementarios:

//Video de burbuja: https://www.youtube.com/watch?v=NVuQWFYlXm8

//video de inserción: https://www.youtube.com/watch?v=O4iuk9VhqYs

//video de merge sort: https://www.youtube.com/watch?v=bOk35XmHPKs

//video de quicksort: https://www.youtube.com/watch?v=h8eyY7dIiN4

//medir el tiempo en nanosegundos: https://www.youtube.com/watch?v=IYjyioHHBBo