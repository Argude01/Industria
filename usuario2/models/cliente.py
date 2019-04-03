from odoo import models,api,fields

class cliente(models.Model):
    _name="fs.cliente"
    _description = "Clientes"

    nombre=fields.Char(string="Apellido")
    apellido=fields.Char(string="Apellido")
    fechaNac=fields.Date(string="Fecha de nacimiento")
    foto=fields.Binary(string="Foto")
    descripcion=fields.Text(string="Descripcion")