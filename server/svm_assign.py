import pickle
import assignment as asg
import pandas as pd
def predict_assign(clear_text):
    file_name=open(r"C:\Users\Ac37652\Desktop\server\count_vect.pkl","rb")
    count_vect=pickle.load(file_name)
    file_name.close()
    file_name=open(r"C:\Users\Ac37652\Desktop\server\tf_transformer.pkl","rb")
    tf_transformer=pickle.load(file_name)
    file_name.close()
    file_name=open(r"C:\Users\Ac37652\Desktop\server\svm_ticketing.pkl","rb")
    svm_model=pickle.load(file_name)
    file_name.close()
    count_vect = count_vect.transform([clear_text])
    tf_idf= tf_transformer.transform(count_vect)
    tf_idf_dense=pd.DataFrame(tf_idf.todense())
    class_text=svm_model.predict(tf_idf_dense)
    class_value=str(class_text).strip('[]')
    assign_group=asg.filter_assignment(class_value)
    return assign_group