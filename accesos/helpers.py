from main.constants import constants

def index_css():
  switcher = {
    'desarrollo': [
      # libreria
      'bower_components/bootstrap/dist/css/bootstrap.min',
      'bower_components/font-awesome/css/font-awesome.min',
      'bower_components/swp-backbone/assets/css/constants',
      'bower_components/swp-backbone/assets/css/dashboard',
      'bower_components/swp-backbone/assets/css/table',
      'bower_components/swp-backbone/assets/css/autocomplete',
      # estilos
      'assets/css/constants',
      'assets/css/styles',
    ],
    'produccion': ['dist/accesos.min'],
  }
  return switcher.get(constants['ambiente_static'])

def index_js():
  switcher = {
    'desarrollo': [
      # libreria
      'bower_components/jquery/dist/jquery.min',
      'bower_components/bootstrap/dist/js/bootstrap.min',
      'bower_components/underscore/underscore-min',
      'bower_components/backbone/backbone-min',
      'bower_components/handlebars/handlebars.min',
      'bower_components/swp-backbone/layouts/application',
      'bower_components/swp-backbone/views/table',
      'bower_components/swp-backbone/views/modal',
      'bower_components/swp-backbone/views/upload',
      'bower_components/swp-backbone/views/autocomplete',
      # accesos mono
      'bower_components/swp-backbone/_accesos_mono/models/modulo',
      'bower_components/swp-backbone/_accesos_mono/models/subtitulo',
      'bower_components/swp-backbone/_accesos_mono/models/item',
      'bower_components/swp-backbone/_accesos_mono/models/permiso',
      'bower_components/swp-backbone/_accesos_mono/models/rol',
      'bower_components/swp-backbone/_accesos_mono/models/usuario',
      'bower_components/swp-backbone/_accesos_mono/models/estado_usuario',
      'bower_components/swp-backbone/_accesos_mono/collections/estado_usuario_collection',
      'bower_components/swp-backbone/_accesos_mono/collections/modulo_collection',
      'bower_components/swp-backbone/_accesos_mono/collections/subtitulo_collection',
      'bower_components/swp-backbone/_accesos_mono/collections/item_collection',
      'bower_components/swp-backbone/_accesos_mono/collections/permiso_collection',
      'bower_components/swp-backbone/_accesos_mono/collections/rol_collection',
      'bower_components/swp-backbone/_accesos_mono/collections/usuario_collection',
      'bower_components/swp-backbone/_accesos_mono/data/tabla_permiso_data',
      'bower_components/swp-backbone/_accesos_mono/data/modal_usuario_detalle_data',
      'bower_components/swp-backbone/_accesos_mono/data/modal_usuario_log_data',
      'bower_components/swp-backbone/_accesos_mono/data/modal_usuario_rol_permiso_data',
      'bower_components/swp-backbone/_accesos_mono/data/tabla_modulo_subtitulo_data',
      'bower_components/swp-backbone/_accesos_mono/data/tabla_subtitulo_item_data',
      'bower_components/swp-backbone/_accesos_mono/data/tabla_rol_data',
      'bower_components/swp-backbone/_accesos_mono/data/tabla_rol_permiso_data',
      'bower_components/swp-backbone/_accesos_mono/data/tabla_usuario_data',
      'bower_components/swp-backbone/_accesos_mono/data/tabla_usuario_rol_data',
      'bower_components/swp-backbone/_accesos_mono/data/tabla_usuario_permiso_data',
      'bower_components/swp-backbone/_accesos_mono/data/tabla_modulo_data',
      'bower_components/swp-backbone/_accesos_mono/views/modulo_view',
      'bower_components/swp-backbone/_accesos_mono/views/permiso_view',
      'bower_components/swp-backbone/_accesos_mono/views/rol_view',
      'bower_components/swp-backbone/_accesos_mono/views/usuario_view',
      'bower_components/swp-backbone/_accesos_mono/views/usuario_log_view',
      'bower_components/swp-backbone/_accesos_mono/views/usuario_detalle_view',
      'bower_components/swp-backbone/_accesos_mono/views/usuario_sistema_view',
      'bower_components/swp-backbone/_accesos_mono/views/usuario_rol_permiso_view',
      'bower_components/swp-backbone/_accesos_mono/routes/accesos',
    ],
    'produccion': [],
  }
  return switcher.get(constants['ambiente_static'])
