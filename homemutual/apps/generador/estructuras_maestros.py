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

	'socio': {
		'Información Cuenta Socio': {
			'fila_1': [
				{'field_name': 'estatus_socio', 'columna': 2, 'design': None},
				{'field_name': 'tipo_cuenta', 'columna': 2, 'design': None},
				{'field_name': 'cuenta_socio', 'columna': 2, 'design': None},
				{'field_name': 'id_sucursal', 'columna': 4, 'design': None},
			],
			'fila_2': [
				{'field_name': 'nombre_socio', 'columna': 4, 'design': None},
				{'field_name': 'telefono_socio', 'columna': 2, 'design': None},
				{'field_name': 'email_socio', 'columna': 4, 'design': None},
			],
			'fila_3': [
				{'field_name': 'id_user', 'columna': 4, 'design': None},
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
				{'field_name': 'id_sg_account', 'columna': 4, 'design': None},
				{'field_name': 'cvu', 'columna': 4, 'design': None},
				{'field_name': 'alias', 'columna': 4, 'design': None},
			],
			'fila_3': [
				{'field_name': 'id_user', 'columna': 4, 'design': None},
			],
		}
	},

}
