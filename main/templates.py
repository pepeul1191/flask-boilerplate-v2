from .constants import constants

def load_css(csss):
  rpta = ''
  if len(csss) > 0:
    for css in csss:
      temp = '<link href="' + constants['static_url'] + css + '.css" rel="stylesheet"/>'
      rpta = rpta + temp
  return rpta

def load_js(jss):
  rpta = ''
  if len(jss) > 0:
    for js in jss:
      temp = '<script src="' + constants['static_url'] + js + '.js" type="text/javascript"></script>'
      rpta = rpta + temp
  return rpta
