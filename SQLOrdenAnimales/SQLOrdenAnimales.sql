create database OrdenAnimales

use OrdenAnimales

------------------------------------------------------
--PARTE 1: creación de las tablas e inserción de datos.
------------------------------------------------------

create table Reino(
	IDReino varchar(30) primary key NOT NULL
)

create table Phylum(
	IDPhylum varchar(30) primary key NOT NULL,
	Reino varchar(30),
	CONSTRAINT fk_Reino FOREIGN KEY (Reino) REFERENCES Reino(IDReino) 
)

create table Clase(
	IDClase varchar(30) primary key NOT NULL,
	Phylum varchar(30),
	CONSTRAINT fk_Phylum FOREIGN KEY (Phylum) REFERENCES Phylum(IDPhylum) 
)

create table Orden(
	IDOrden varchar(30) primary key NOT NULL,
	Clase varchar(30),
	CONSTRAINT fk_Clase FOREIGN KEY (Clase) REFERENCES Clase(IDClase) 
)

create table Familia(
	IDFamilia varchar(30) primary key NOT NULL,
	Orden varchar(30),
	CONSTRAINT fk_Orden FOREIGN KEY (Orden) REFERENCES Orden(IDOrden)
)

create table Genero(
	IDGenero varchar(30) primary key NOT NULL,
	Familia varchar(30),
	CONSTRAINT fk_Familia FOREIGN KEY (Familia) REFERENCES Familia(IDFamilia)
)

create table Especie(
	IDEspecie varchar(30) primary key NOT NULL,
	Genero varchar(30),
	Nombre_Cientifico varchar(45) NOT NULL,
	Nombre_Comun varchar(45) NOT NULL,
	CONSTRAINT fk_Genero FOREIGN KEY (Genero) REFERENCES Genero(IDGenero)
)

--Si se desea eliminar las tablas, usar este código una vez:
--drop table Especie
--drop table Genero
--drop table Familia
--drop table Orden
--drop table Clase
--drop table Phylum
--drop table Reino


insert into Reino values 
	('Animal'),
	('Vegetal');

insert into Phylum values 
	('Chordata', 'Animal'),
	('Tracheophyta', 'Vegetal');

insert into Clase values 
	('Mammalia', 'Chordata'),
	('Angiosperma', 'Tracheophyta');

Insert into Orden values
	('Artiodactyla', 'Mammalia'),
	('Primate', 'Mammalia'),
	('Carnívora', 'Mammalia'),
	('Glumifloral', 'Angiosperma'),
	('Cetacea', 'Mammalia');

Insert into Familia values
	('Bovidae', 'Artiodactyla'),
	('Hominidae', 'Primate'),
	('Canidae', 'Carnívora'),
	('Felidae', 'Carnívora'),
	('Gramínea', 'Glumifloral'),
	('Balaenopteridae', 'Cetacea');

Insert into Genero values
	('Bos', 'Bovidae'),
	('Homo', 'Hominidae'),
	('Canis', 'Canidae'),
	('Felis', 'Felidae'),
	('Zea', 'Gramínea'),
	('Megaptera', 'Balaenopteridae');

Insert into Especie values
	('Taurus', 'Bos', 'Bos Taurus', 'Vaca'),
	('Sapiens', 'Homo', 'Homo Sapiens', 'Hombre/Mujer'),
	('Familiaris', 'Canis', 'Canis Familiaris', 'Perro'),
	('Silvestris', 'Felis', 'Felis Silvestris', 'Gato'),
	('Maíz', 'Zea', 'Zea Maíz', 'Maíz'),
	('Novaeangliae', 'Megaptera', 'Megaptera Novaeangliae', 'Ballena Jorobada');

--Si se desea eliminar los datos ingresados, usar este código una vez:
--delete from Especie;
--delete from Genero;
--delete from Familia;
--delete from Orden;
--delete from Clase;
--delete from Phylum;
--delete from Reino;

--------------------------------------------------------------------------
--PARTE 2: función para obtener un nombre y sacar el reino correspondiente.
--------------------------------------------------------------------------

--Para crear la función:
GO
create or alter function fnc_get_reino (@Nombre VARCHAR(30))
returns table
as 
	return
	select Reino.IDReino as Reino_Correspondiente from Especie
		inner join Genero on Especie.Genero=Genero.IDGenero
		inner join Familia on Genero.Familia=Familia.IDFamilia
		inner join Orden on Familia.Orden=Orden.IDOrden
		inner join Clase on Orden.Clase=Clase.IDClase
		inner join Phylum on Clase.Phylum=Phylum.IDPhylum
		inner join Reino on Phylum.Reino=Reino.IDReino
	where Nombre_Comun=@Nombre;
GO

--Para utilizar la función:
SELECT * FROM fnc_get_reino('Gato');

--------------------------------------------------
--PARTE 3: función para insertar un nuevo registro.
--------------------------------------------------

--Para crear el procedimiento:
GO
create or alter procedure sp_inserta_registro
	@Nombre_Comun varchar(30),
	@Nombre_Cientifico varchar(30),
	@Especie varchar(30),
	@Genero varchar(30),
	@Familia varchar(30),
	@Orden varchar(30),
	@Clase varchar(30),
	@Phylum varchar(30),
	@Reino varchar(30)
as
	if not exists(select * from Reino where IDReino=@Reino)
		insert into Reino (IDReino) values (@Reino);
	if not exists(select * from Phylum where IDPhylum=@Phylum)
		insert into Phylum (IDPhylum, Reino) values (@Phylum, @Reino);
	if not exists(select * from Clase where IDClase=@Clase)
		insert into Clase (IDClase, Phylum) values (@Clase, @Phylum);
	if not exists(select * from Orden where IDOrden=@Orden)
		insert into Orden (IDOrden, Clase) values (@Orden, @Clase);
	if not exists(select * from Familia where IDFamilia=@Familia)
		insert into Familia (IDFamilia, Orden) values (@Familia, @Orden);
	if not exists(select * from Genero where IDGenero=@Genero)
		insert into Genero (IDGenero, Familia) values (@Genero, @Familia);
	if not exists(select * from Especie where IDEspecie=@Especie)
		insert into Especie (IDEspecie, Genero, Nombre_Cientifico, Nombre_Comun) values (@Especie, @Genero, @Nombre_Cientifico, @Nombre_Comun);
GO

--Para utilizar el procedimiento:
exec sp_inserta_registro 'Ardilla gris', 
						 'Sciurus Aureogaster', 
						 'Aureogaster', 
						 'Sciurus', 
						 'Sciuridae', 
						 'Rodentia', 
						 'Mammalia', 
						 'Chordata', 
						 'Animal';

exec sp_inserta_registro 'Limonero', 
						 'Citrus x Limon', 
						 'Limon', 
						 'Citrus', 
						 'Rutaceae', 
						 'Sapindales', 
						 'Magnoliopsida', 
						 'Magnoliophyta', 
						 'Vegetal';

exec sp_inserta_registro 'Ameba', 
						 'Amoeba Agilis', 
						 'Agilis', 
						 'Amoeba', 
						 'Amoebidae', 
						 'Euamoebida', 
						 'Tubulinea', 
						 'Amoebozoa', 
						 'Protista';

--Para observar todos los registros ingresados:
select Reino.IDReino, Phylum.IDPhylum, Clase.IDClase, Orden.IDOrden, 
	Familia.IDFamilia, Genero.IDGenero, Especie.IDEspecie, 
	Especie.Nombre_Cientifico, Especie.Nombre_Comun from Especie 
		inner join Genero on Especie.Genero=Genero.IDGenero
		inner join Familia on Genero.Familia=Familia.IDFamilia
		inner join Orden on Familia.Orden=Orden.IDOrden
		inner join Clase on Orden.Clase=Clase.IDClase
		inner join Phylum on Clase.Phylum=Phylum.IDPhylum
		inner join Reino on Phylum.Reino=Reino.IDReino
		order by Nombre_Comun;
