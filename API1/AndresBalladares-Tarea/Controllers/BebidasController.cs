using AndresBalladares_Tarea.Models;
using AndresBalladares_Tarea.Services;
using Microsoft.AspNetCore.Mvc;

namespace AndresBalladares_Tarea.Controllers
{
    /*
     * En esta clase se llaman los procesos del servicio dentro de un try-catch.
     * Para observar la lógica de los procesos, ir a la clase BebidaServicio.
     */

    [ApiController]
    [Route("[controller]")]
    public class BebidasController : ControllerBase
    {
        private readonly IBebidaServicio BebidaServicio;

        public BebidasController(IBebidaServicio _BebidaServicio)
        {
            BebidaServicio = _BebidaServicio;
        }

        //Obtener lista de bebidas.
        [HttpGet("GetBebidas")]
        public async Task<ActionResult<IEnumerable<Bebida>>> GetBebidas()
        {
            try
            {
                var bebidas = await BebidaServicio.GetBebidas();
                return Ok(bebidas);
            }
            catch(Exception ex) 
            {
                return StatusCode(500, ex.Message);
            }
        }

        //Obtener bebida por ID.
        [HttpGet("GetBebida/{id}")]
        public async Task<ActionResult<Bebida>> GetBebida(int id)
        {
            try
            {
                var bebida = await BebidaServicio.GetBebida(id); 
                return Ok(bebida);
            }
            catch (KeyNotFoundException ex)
            {
                return NotFound(ex.Message);
            }
            catch (Exception ex)
            {
                return StatusCode(500, ex.Message);
            }
        }

        //Añadir una bebida.
        [HttpPost("AgregarBebida")]
        public async Task<ActionResult> AddBebida(Bebida bebida)
        {
            try
            {
                await BebidaServicio.AddBebida(bebida);
                return CreatedAtAction(nameof(GetBebida), new { id = bebida.ID }, bebida);
            }
            catch (ArgumentException ex)
            {
                return BadRequest(ex.Message);
            }
            catch (Exception ex)
            {
                return StatusCode(500, ex.Message);
            }
        }

        //Borrar una bebida por ID.
        [HttpDelete("BorrarBebida/{id}")]
        public async Task<ActionResult> DeleteBebida(int id)
        {
            try
            {
                await BebidaServicio.DeleteBebida(id);
                return NoContent();
            }
            catch (KeyNotFoundException ex)
            {
                return NotFound(ex.Message);
            }
            catch (Exception ex)
            {
                return StatusCode(500, ex.Message);
            }
        }

        //Actualizar una bebida por ID.
        [HttpPut("ActualizarBebida/{id}")]
        public async Task<ActionResult> UpdateBebida(int id, Bebida bebida)
        {
            try
            {
                await BebidaServicio.UpdateBebida(id, bebida);
                return NoContent();
            }
            catch (ArgumentException ex)
            {
                return BadRequest(ex.Message);
            }
            catch (KeyNotFoundException ex)
            {
                return NotFound(ex.Message);
            }
            catch (Exception ex)
            {
                return StatusCode(500, ex.Message);
            }
        }

        //Añadir un tipo de bebida a una bebida existente por ID.
        [HttpPost("AgregarTipoABebida/{id}/tipos")]
        public async Task<ActionResult> AddTipoDeBebida(int id, TipoBebida tipoDeBebida)
        {
            try
            {
                await BebidaServicio.AddTipoDeBebida(id, tipoDeBebida);
                var bebida = await BebidaServicio.GetBebida(id);
                return CreatedAtAction(nameof(GetBebida), new { id = bebida.ID }, bebida);
            }
            catch (ArgumentException ex)
            {
                return BadRequest(ex.Message);
            }
            catch (KeyNotFoundException ex)
            {
                return NotFound(ex.Message);
            }
            catch (Exception ex)
            {
                return StatusCode(500, ex.Message);
            }
        }

        //Eliminar un tipo de bebida de una bebida existente por ID.
        [HttpDelete("EliminarTipoABebida/{id}/tipos/{tipoId}")]
        public async Task<ActionResult> DeleteTipoDeBebida(int id, int tipoId)
        {
            try
            {
                await BebidaServicio.DeleteTipoDeBebida(id, tipoId);
                return NoContent();
            }
            catch (KeyNotFoundException ex)
            {
                return NotFound(ex.Message);
            }
            catch (Exception ex)
            {
                return StatusCode(500, ex.Message);
            }
        }

        //Actualizar un tipo de bebida de una bebida existente por ID.
        [HttpPut("ActualizarTipoABebida/{id}/tipos/{tipoId}")]
        public async Task<ActionResult> UpdateTipoDeBebida(int id, int tipoId, TipoBebida tipoDeBebida)
        {
            try
            {
                await BebidaServicio.UpdateTipoDeBebida(id, tipoId, tipoDeBebida);
                return NoContent();
            }
            catch (ArgumentException ex)
            {
                return BadRequest(ex.Message);
            }
            catch (KeyNotFoundException ex)
            {
                return NotFound(ex.Message);
            }
            catch (Exception ex)
            {
                return StatusCode(500, ex.Message);
            }
        }
    }
}

/*
 * Explicación de todos los returns:
 * NotFound: Respuesta HTTP 404. El recurso solicitado no pudo ser encontrado en el servidor.
 * BadRequest: Respuesta HTTP 400. Ocurrió un error en los datos enviados, usualmente porque la ID no coincide.
 * StatusCode: Respuesta HTTP 500. Ocurrió un error no controlado en el código.
 * NoContent: Respuesta HTTP 204. La solicitud fue exitosa, pero no se muestra el contenido.
 * CreatedAtAction: Respuesta HTTP 201. El recurso fue creado exitosamente y se muestra su ubicación.
 * Ok: Respuesta HTTP 200. La solicitud fue exitosa y se muestran lso datos solicitados.
 */
