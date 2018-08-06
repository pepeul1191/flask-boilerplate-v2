#!/usr/bin/env python
# -*- coding: utf-8 -*-
from main.application import app

if __name__ == '__main__':
	#app.secret_key = constants['key']
	app.run(debug=True, host='0.0.0.0', port=3000)
