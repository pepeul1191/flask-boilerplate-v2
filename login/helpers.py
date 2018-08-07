from main.constants import constants

def index_css():
  switcher = {
    'desarrollo': [
      'bower_components/bootstrap/dist/css/bootstrap.min',
      'bower_components/font-awesome/css/font-awesome.min',
      'bower_components/swp-backbone/assets/css/constants',
      'bower_components/swp-backbone/assets/css/login',
      'assets/css/login',
    ],
    'produccion': ['dist/login.min'],
  }
  return switcher.get(constants['ambiente_static'])

def index_js():
  switcher = {
    'desarrollo': [
      #'dist/bundle',
    ],
    'produccion': [],
  }
  return switcher.get(constants['ambiente_static'])
