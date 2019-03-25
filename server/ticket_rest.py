
from flask import Flask
from flask import jsonify
from flask_restful import Resource,Api,request
from flask_cors import CORS,cross_origin
from sklearn import svm, datasets
import text_process as tp
import svm_assign as sa
import svm_priority as sp
import pandas as pd
app = Flask(__name__)
api = Api(app)
CORS(app)
class ticketing(Resource):
    @cross_origin(origin='*')
    def post(self):
        if(request.headers['Content-Type']=='text/plain'):
            input_text=request.data
            decode_text=input_text.decode('utf-8')
            clear_text=tp.text_processing(decode_text)
            assign_return=sa.predict_assign(clear_text)
            priority_return=sp.predict_priority(clear_text)
            return jsonify({'Assignment group':assign_return,'Priority':priority_return})
       
        
        elif(request.headers['Content-Type']=='application/json'):
            input_text=request.json
            decode_text=input_text['text']
            clear_text=tp.text_processing(decode_text)
            svm_model=svm_load.load_svm()
            assign_return=sa.predict_assign(clear_text)
            return jsonify({'Assignment group':assign_return,'Priority':priority_return})      
                    
        else:
            return "Media type not support"
        
api.add_resource(ticketing,'/ticketing/')
if __name__ == '__main__':
    app.run(host='127.0.0.1')
    