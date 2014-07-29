from distutils.core import setup, Extension

neoscrypt_module = Extension('neoscrypt',
				sources = ['neoscryptmodule.c',
					   'neoscrypt.c'],
				include_dirs=['.'])

setup (name='neoscrypt',
	version = '1.0',
	description = 'Bindings for the Scrypt Proof Of Work used By Feathercoin',
	ext_modules = [neoscrypt_module])
