# Define las columnas Bootstrap y sección para cada campo


class Design:
	checkbox = "checkbox"


estructura_campos = {
	'sucursal': {
		'Información Sucursal': {
			'fila_1': [
				{'field_name': 'estatus_sucursal', 'columna': 2, 'design': None},
				{'field_name': 'nombre_sucursal', 'columna': 4, 'design': None},
			],
			'fila_2': [
				{'field_name': 'domicilio_sucursal', 'columna': 4, 'design': None},
				{'field_name': 'telefono_sucursal', 'columna': 2, 'design': None},
				{'field_name': 'email_sucursal', 'columna': 4, 'design': None},
			],
			'fila_3': [
				{'field_name': 'ws_url', 'columna': 4, 'design': None},
				{'field_name': 'ws_token_acceso', 'columna': 4, 'design': None},
			],
		}
	},

	'cuenta_mutual': {
		'Información Cuenta Mutual': {
			'fila_1': [
				{'field_name': 'estatus_cuenta_mutual', 'columna': 2, 'design': None},
				{'field_name': 'id_sucursal', 'columna': 2, 'design': None},
				{'field_name': 'id_socio', 'columna': 2, 'design': None},
				{'field_name': 'cuenta', 'columna': 2, 'design': None},
				{'field_name': 'documento', 'columna': 2, 'design': None},
			],
			'fila_2': [
				{'field_name': 'id_sg_usuario', 'columna': 3, 'design': None},
				{'field_name': 'id_sg_cuenta', 'columna': 3, 'design': None},
				{'field_name': 'cvu', 'columna': 3, 'design': None},
				{'field_name': 'alias', 'columna': 3, 'design': None},
			],
			'fila_3': [
				{'field_name': 'id_user', 'columna': 4, 'design': None},
			],
			'fila_4': [
				{'field_name': 'razon_social', 'columna': 4, 'design': None},
				{'field_name': 'cuit', 'columna': 2, 'design': None},
				{'field_name': 'sexo', 'columna': 2, 'design': None},
				{'field_name': 'fecha_nacimiento', 'columna': 2, 'design': None},
			],
			'fila_5': [
				{'field_name': 'caracteristica_pais_telefono', 'columna': 2, 'design': None},
				{'field_name': 'codigo_area_telefono', 'columna': 2, 'design': None},
				{'field_name': 'numero_telefono', 'columna': 2, 'design': None},
			],
			'fila_6': [
				{'field_name': 'id_entidad_tipo_documento', 'columna': 4, 'design': None},
				{'field_name': 'id_tipo_persona', 'columna': 4, 'design': None},
				{'field_name': 'id_tipo_cuenta', 'columna': 4, 'design': None},
			],
		}
	},

	'sg_entidad_tipo_documento': {
		'Información Entidad Tipo Documento': {
			'fila_1': [
				{'field_name': 'estatus_sg_entidad_tipo_documento', 'columna': 2, 'design': None},
				{'field_name': 'nombre', 'columna': 4, 'design': None},
			],
			'fila_1': [{'field_name': 'estatus_sg_entidad_tipo_documento', 'columna': 2, 'design': None},],
			'fila_2': [{'field_name': 'id_sg_entidad_tipo_documento', 'columna': 4, 'design': None},],
			'fila_3': [{'field_name': 'nombre', 'columna': 4, 'design': None},],
		}
	},

	'sg_tipo_persona': {
		'Información Tipo Persona': {
			'fila_1': [{'field_name': 'estatus_sg_tipo_persona', 'columna': 2, 'design': None},],
			'fila_2': [{'field_name': 'id_sg_tipo_persona', 'columna': 4, 'design': None}],
			'fila_2': [{'field_name': 'tipo_persona', 'columna': 4, 'design': None},],
		}
	},

	'sg_tipo_cuenta': {
		'Información Tipo Cuenta': {
			'fila_1': [{'field_name': 'estatus_sg_tipo_cuenta', 'columna': 2, 'design': None},],
			'fila_2': [{'field_name': 'id_sg_tipo_cuenta', 'columna': 4, 'design': None},],
			'fila_3': [{'field_name': 'tipo_cuenta', 'columna': 4, 'design': None},],
		}
	},
}
