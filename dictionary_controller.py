import json
import cherrypy
import requests

#controller class with event handlers
class DictionaryController(object):
    def __init__(self):
        self.myd = dict() # empty dictionary

    # helper method
    def get_value(self, key):
        return self.myd[key]

    #event handlers
    def GET_KEY(self, key):
        # 1. set up a default response_json
        output_json = {'result': 'success'}
        try:    # 3 perform risky operations in try-except block
            #2. check/conver any i/p to the correct format
            key = str(key)
            value = self.get_value(key)
            if value is not None:
                output_json['key'] = key
                output_json['value'] = value
                # happy path
            else:
                output_json['result'] = 'error'
                output_json['message'] = 'key does not exist'
        except KeyError as ex:  # This is the same as the else statement immediately above
            output_json['result'] = 'error'
            output_json['message'] = 'issue with key argument' + str(ex)
        except Exception as ex:
            output_json['result'] = 'error'
            output_json['message'] = str(ex)
        return json.dumps(output_json)     # return the type of object that is expected


    def PUT_KEY(self, key):
        #print('entered PUT_KEY')
        # take info from key and message body and add it to the dictionary
        output_json = {'result': 'success'}
        key = str(key)
        #get body of message into data
        try:
            data_str = cherrypy.request.body.read()
            data_json = json.loads(data_str)    # this is the message body
            # TODO
            self.myd[key] = data_json['value']     # what I did with Prof. Kumar
            #print(self.myd)     # just for debugging
            # just for debugging
            #output_json['key'] = key
            #output_json['value'] = data_json['value']
        except Exception as ex:
            output_json['result'] = 'error'
            output_json['message'] = str(ex)
        return json.dumps(output_json)

    def POST_INDEX(self):
        print('entered POST_KEY')
        # take info from key and message body and add it to the dictionary
        output_json = {'result': 'success'}
        #get body of message into data
        try:
            data_str = cherrypy.request.body.read()
            data_json = json.loads(data_str)    # this is the message body
            #print(data_json)
            theKey = data_json['key']
            self.myd[theKey] = data_json['value']
            #self.myd['value'] = data_json['value']
            print(self.myd)
            #for debugging
            #output_json['key'] = self.myd['key']
            #output_json['value'] = self.myd['value']
        except Exception as ex:
            output_json['result'] = 'error'
            output_json['message'] = str(ex)
        print(self.myd)
        return json.dumps(output_json)

    def DELETE_KEY(self, key):
        print('entered delete key')
        print(self.myd)
        output_json = {'result': 'success'}
        print(output_json)
        print(key)
        #TODO
        try:
            key = str(key)
            value = self.get_value(key)     # why does it stop here??
            del self.myd[key]
            print(self.myd)
        except KeyError as ex:  # This is the same as the else statement immediately above
            output_json['result'] = 'error'
            output_json['message'] = str(ex)
        except Exception as ex:
            output_json['result'] = 'error'
            output_json['message'] = str(ex)
        return json.dumps(output_json)

    def GET_DICT(self):
        output_json = {'result': 'success'}
        entriesList = []
        try:    # 3 perform risky operations in try-except block
            #2. check/conver any i/p to the correct format
            #print('in try')
            #print(self.myd)
            for key, val in (self.myd).items():
                entriesList.append({'key': key, 'value': val})
            #print(entriesList)
            output_json['entries'] = entriesList
            #print(output_json)
        except KeyError as ex:  # This is the same as the else statement immediately above
            output_json['result'] = 'error'
            output_json['message'] = 'issue with key argument' + str(ex)
        except Exception as ex:
            output_json['result'] = 'error'
            output_json['message'] = str(ex)

        return json.dumps(output_json)     # return the type of object that is expected


    def DELETE_DICT(self):
        output_json = {'result': 'success'}
        print('entered DELETE_DICT')
        print(self.myd)
        try:
            (self.myd).clear()
            print(self.myd)
        except KeyError as ex:  # This is the same as the else statement immediately above
            output_json['result'] = 'error'
            output_json['message'] = 'issue with key argument' + str(ex)
        except Exception as ex:
            output_json['result'] = 'error'
            output_json['message'] = str(ex)

        return json.dumps(output_json)     # return the type of object that is expected
