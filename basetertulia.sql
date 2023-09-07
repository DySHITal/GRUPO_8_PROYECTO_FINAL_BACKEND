create database tertulia;
use tertulia;

CREATE TABLE usuarios (
    id_usuario INT unsigned PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    alias varchar(50) not null,
    fechas_nacimiento date not null,
    correo VARCHAR(100) NOT NULL,
    contrasena VARCHAR(100) NOT NULL,
    avatar VARCHAR(100),
    estado BOOLEAN
)engine InnoDB;

CREATE TABLE servidor (
    id_servidor INT unsigned PRIMARY KEY AUTO_INCREMENT,
    nombre_servidor VARCHAR(50) NOT NULL,
    fecha_creacion date not null
)engine InnoDB;

alter table servidor
add descripcion varchar(1000);

CREATE TABLE usuario_servidor (
    id_usuario_servidor INT unsigned PRIMARY KEY AUTO_INCREMENT,
    usuario INT unsigned NOT NULL,
    servidor INT unsigned NOT NULL,
    constraint usuario_fk FOREIGN KEY (usuario) REFERENCES usuarios(id_usuario),
    constraint servidor_fk FOREIGN KEY (servidor) REFERENCES servidor(id_servidor) 
)engine InnoDB;

CREATE TABLE canales (
    id_canales INT unsigned PRIMARY KEY AUTO_INCREMENT,
    nombre_canal varchar(50) not null,
    id_servidor INT unsigned not null,
    FOREIGN KEY (id_servidor) REFERENCES servidor(id_servidor)
)engine InnoDB;

create table mensajes (
	id_mensaje int unsigned primary key auto_increment,
    mensaje varchar(1000),
    fecha_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    canal int unsigned not null, 
    constraint canal_fk foreign key (canal) references canales(id_canales)
    )engine InnoDB;
    
create table usuario_mensaje (
	id_usuario_mensaje int unsigned primary key auto_increment,
    id_usuario int unsigned not null,
    id_mensaje int unsigned not null, 
    foreign key (id_usuario) references usuarios(id_usuario),
    foreign key (id_mensaje) references mensajes(id_mensaje)
    )engine InnoDB;