#server that provides dictionary as a service
import routes
import cherrypy
from dictionary_controller import DictionaryController

def start_service():
	# create a controller object
	d_cont = DictionaryController()

	# set up dispatcher
	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	# connect /dictionary/ to dictionaryController's get_key method
	dispatcher.connect('dict_get_key', '/dictionary/:key', controller=d_cont, action='GET_KEY', conditions=dict(method=['GET']))

	dispatcher.connect('dict_put_key', '/dictionary/:key', controller=d_cont, action='PUT_KEY', conditions=dict(method=['PUT']))

	dispatcher.connect('dict_post_INDEX', '/dictionary/', controller=d_cont, action='POST_INDEX', conditions=dict(method=['POST']))

	dispatcher.connect('dict_delete_key', '/dictionary/:key', controller=d_cont, action='DELETE_KEY', conditions=dict(method=['DELETE']))

	dispatcher.connect('dict_get', '/dictionary/', controller=d_cont, action='GET_DICT', conditions=dict(method=['GET']))

	dispatcher.connect('dict_delete', '/dictionary/', controller=d_cont, action='DELETE_DICT', conditions=dict(method=['DELETE']))


#	dispatcher.connect('dict_delete', '/dictionary/', controller=d_cont, action='DELETE_DICT', conditions=dict(method=['DELETE']))

	# configure server
	conf = {
		'global': {
			'server.socket_host': 'localhost',	# or student04.cse.nd.edu
			'server.socket_port': 51034
				#port num is 5100 + MID so my MID 34 has port 51034
		},
		'/': {
			'request.dispatch': dispatcher, #object dispatcher
		}
	}	#end conf

	# update conf with cherrypy
	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)

	# start the server
	cherrypy.quickstart(app)

if __name__ == '__main__':
	start_service()
