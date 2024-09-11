namespace AndresBalladares_Tarea.Models
{
    public class Bebida
    {
        public int ID { get; set; }
        public string Descripcion { get; set; }
        public string tamaño { get; set; }
        public string PaisOrigen {  get; set; }
        public List<TipoBebida> TiposDeBebida { get; set; } = new List<TipoBebida>(); //Valores: ID, Descripción.
    }
}
