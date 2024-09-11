using AndresBalladares_Tarea.Models;

namespace AndresBalladares_Tarea.Services
{
    public interface IBebidaServicio
    {
        Task<IEnumerable<Bebida>> GetBebidas();
        Task<Bebida> GetBebida(int ID);
        Task AddBebida(Bebida bebida);
        Task DeleteBebida(int ID);
        //Task UpdateBebida (Bebida bebida); //Actualizar bebida sin ID.
        Task UpdateBebida(int ID, Bebida bebida);
        Task AddTipoDeBebida(int ID, TipoBebida tipoDeBebida);
        Task DeleteTipoDeBebida(int ID, int IDTipo);
        Task UpdateTipoDeBebida(int ID, int IDTipo, TipoBebida tipoDeBebida);
    }
}
