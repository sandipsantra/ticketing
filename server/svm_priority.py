import pickle
import priority_filter as pf
import pandas as pd
def predict_priority(clear_text):
    file_name=open(r"C:\Users\Ac37652\Desktop\server\count_vect_priority.pkl","rb")
    count_vect=pickle.load(file_name)
    file_name.close()
    file_name=open(r"C:\Users\Ac37652\Desktop\server\tf_transformer_priority.pkl","rb")
    tf_transformer=pickle.load(file_name)
    file_name.close()
    file_name=open(r"C:\Users\Ac37652\Desktop\server\svm_ticketing_priority.pkl","rb")
    svm_model_priority=pickle.load(file_name)
    file_name.close()
    count_vect = count_vect.transform([clear_text])
    tf_idf= tf_transformer.transform(count_vect)
    tf_idf_dense=pd.DataFrame(tf_idf.todense())
    class_text=svm_model_priority.predict(tf_idf_dense)
    class_value=str(class_text).strip('[]')
    priority=pf.filter_assignment_priority(class_value)
    return priority