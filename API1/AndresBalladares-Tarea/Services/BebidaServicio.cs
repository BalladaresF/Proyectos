using AndresBalladares_Tarea.Models;

namespace AndresBalladares_Tarea.Services
{
    //Los procesos realizados en el controlador se pueden observar aquí.
    
    public class BebidaServicio : IBebidaServicio
    {
        private readonly List<Bebida> _bebidas = new List<Bebida>();

        public bool BebidaExiste(int id)
        {
            return _bebidas.Any(b => b.ID == id);
        }

        public bool TipoDeBebidaExiste(int id, int tipoId)
        {
            var bebida = _bebidas.FirstOrDefault(b => b.ID == id);
            return bebida != null && bebida.TiposDeBebida.Any(t => t.IDTipo == tipoId);
        }

        public Task<IEnumerable<Bebida>> GetBebidas()
        {
            return Task.FromResult<IEnumerable<Bebida>>(_bebidas);
        }

        public Task<Bebida> GetBebida(int id)
        {
            var bebida = _bebidas.FirstOrDefault(b => b.ID == id); 
            if (bebida == null)
            {
                throw new KeyNotFoundException("Bebida no encontrada.");
            }
            return Task.FromResult(bebida);
        }

        public Task AddBebida(Bebida bebida)
        {
            if (BebidaExiste(bebida.ID))
            {
                throw new ArgumentException("Ya existe una bebida con el mismo ID.");
            }
            _bebidas.Add(bebida);
            return Task.CompletedTask;
        }

        public Task DeleteBebida(int id)
        {
            var bebida = _bebidas.FirstOrDefault(b => b.ID == id);
            if (bebida != null)
            {
                _bebidas.Remove(bebida);
            }
            else
            {
                throw new KeyNotFoundException("Bebida no encontrada.");
            }
            return Task.CompletedTask;
        }

        /* Actualizar bebida sin actualizar IDs. 
        public Task UpdateBebida (Bebida bebida)
        {
            var index = _bebidas.FindIndex (b => b.ID == bebida.ID);
            if (index != -1)
            {
                _bebidas[index] = bebida;
            }
            else
            {
                throw new KeyNotFoundException("Bebida no encontrada");
            }
            return Task.CompletedTask;
        }*/

        public Task UpdateBebida(int id, Bebida bebida)
        {
            if (!BebidaExiste(id))
            {
                throw new KeyNotFoundException("Bebida no encontrada.");
            }
            if (BebidaExiste(bebida.ID) && id != bebida.ID)
            {
                throw new ArgumentException("Ya existe una bebida con el mismo ID.");
            }

            DeleteBebida(id);
            AddBebida(bebida);
            return Task.CompletedTask;

        }

        public Task AddTipoDeBebida(int id, TipoBebida tipoDeBebida)
        {
            var bebida = _bebidas.FirstOrDefault(b => b.ID == id);
            if (bebida == null)
            {
                throw new KeyNotFoundException("Bebida no encontrada.");
            }

            if (TipoDeBebidaExiste(id, tipoDeBebida.IDTipo))
            {
                throw new ArgumentException("Ya existe un tipo de bebida con el mismo ID en esta bebida.");
            }

            bebida.TiposDeBebida.Add(tipoDeBebida);
            return Task.CompletedTask;
        }

        public Task DeleteTipoDeBebida(int id, int tipoId)
        {
            var bebida = _bebidas.FirstOrDefault(b => b.ID == id); 
            if (bebida == null)
            {
                throw new KeyNotFoundException("Bebida no encontrada.");
            }
            var tipoDeBebida = bebida.TiposDeBebida.FirstOrDefault(t => t.IDTipo == tipoId);
            if (tipoDeBebida == null)
            {
                throw new KeyNotFoundException("Tipo de bebida no encontrado.");
            }
            bebida.TiposDeBebida.Remove(tipoDeBebida);
            return Task.CompletedTask;
        }

        /* Actualizar tipo de bebida sin actualizar IDs.
        public Task UpdateTipoDeBebida(int id, int tipoId, TipoBebida tipoDeBebida)
        {
            var bebida = _bebidas.FirstOrDefault(b => b.ID == id);
            if (bebida == null)
            {
                throw new KeyNotFoundException("Bebida no encontrada");
            }
            var tipoExistente = bebida.TiposDeBebida.FirstOrDefault(t => t.IDTipo == tipoId); 
            if (tipoExistente == null)
            {
                throw new KeyNotFoundException("Tipo de bebida no encontrado");
            }
            tipoExistente.Descripcion = tipoDeBebida.Descripcion;
            return Task.CompletedTask;
        }*/

        public Task UpdateTipoDeBebida(int id, int tipoId, TipoBebida tipoDeBebida)
        {
            if (!BebidaExiste(id))
            {
                throw new KeyNotFoundException("Bebida no encontrada. ");
            }
            if (!TipoDeBebidaExiste(id, tipoId))
            {
                throw new KeyNotFoundException("Tipo de bebida no encontrado.");
            }
            if (TipoDeBebidaExiste(id, tipoDeBebida.IDTipo) && tipoId != tipoDeBebida.IDTipo)
            {
                throw new ArgumentException("Ya existe un tipo de bebida con el mismo ID en esta bebida.");
            }
            
            var bebida = _bebidas.FirstOrDefault(b => b.ID == id);
            var tipoExistente = bebida.TiposDeBebida.FirstOrDefault(t => t.IDTipo == tipoId);

            tipoExistente.IDTipo = tipoDeBebida.IDTipo;
            tipoExistente.Descripcion = tipoDeBebida.Descripcion;
            return Task.CompletedTask;
        }
    }
}
