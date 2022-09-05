import pickle
import os
import pandas as pd
import time
import numpy as np


start = time.time()
filePath = os.path.split(__file__)[0] 

#inputfile = filePath + '\\All_mother_0707.csv'
outputfile_DNN = filePath + '\\DNN.pickle'
outputfile_C45 = filePath + '\\C45.pickle'
outputfile_Extree = filePath + '\\Extree.pickle'
outputfile_XGB = filePath + '\\XGB.pickle'
outputfile_LGBM = filePath + '\\LGBM.pickle'
outputfile_CatBc = filePath + '\\CatBc.pickle'
#outputfile_result = filePath + '\\result.csv'
#print(outputfile_DNN)

def PredictResult(OI_c_p_N_1,Open_Interest_c_N_1,Open_Interest_p_N_1):
    #df = pd.read_csv(inputfile)
    #print(df)
    featureColumns = ['OI_c_p_N-1','Open_Interest_c_N-1','Open_Interest_p_N-1']
    data = [OI_c_p_N_1,Open_Interest_c_N_1,Open_Interest_p_N_1]
    data_reshape = np.array(np.reshape(data,(1,3)))
    feature_df = pd.DataFrame(data_reshape,columns=featureColumns)
    #print(feature_df)
    result_dict = {'DNN':[],'C45':[],'Extree':[],'XGB':[],'LGBM':[],'CatBc':[]}


    # DNN.pickle
    with open(outputfile_DNN,'rb') as fr:
        DNN = pickle.load(fr)    
    DNN_pred = DNN.predict(feature_df)
    result_dict['DNN'] = DNN_pred


    # C45.pickle
    with open(outputfile_C45,'rb') as fr:
        C45 = pickle.load(fr)    
    C45_pred = C45.predict(feature_df)
    result_dict['C45'] = C45_pred


    # Extree.pickle
    with open(outputfile_Extree,'rb') as fr:
        Extree = pickle.load(fr)    
    Extree_pred = Extree.predict(feature_df)
    result_dict['Extree'] = Extree_pred


    # XGB.pickle
    with open(outputfile_XGB,'rb') as fr:
        XGB = pickle.load(fr)    
    XGB_pred = XGB.predict(feature_df)
    result_dict['XGB'] = XGB_pred


    # LGBM.pickle
    with open(outputfile_LGBM,'rb') as fr:
        LGBM = pickle.load(fr)    
    LGBM_pred = LGBM.predict(feature_df)
    result_dict['LGBM'] = LGBM_pred


    # CatBc.pickle   ->  這邊要注意的是該數直出來的是2維陣列,要再轉成1維
    with open(outputfile_CatBc,'rb') as fr:
        CatBc = pickle.load(fr)    
    CatBc_pred = CatBc.predict(feature_df)
    #print(XGB_pred.shape)
    #print(LGBM_pred.shape)
    #print(CatBc_pred.shape)
    b = np.reshape(CatBc_pred,(len(feature_df),-1)) # 無法轉成1維陣列
    #print(b.shape)
    #print(b)   
    #print(len(CatBc_pred[3]))
    #print(len(CatBc_pred))

    tmp_ = []
    for i in range(len(CatBc_pred)):
        # print(CatBc_pred[i])
        # print(type(CatBc_pred[i]))
        # print(CatBc_pred[i][0])
        tmp_.append(CatBc_pred[i][0])

    tmp_np = np.array(tmp_)
    result_dict['CatBc'] = tmp_np


    print(result_dict)
    #result_df.to_csv(outputfile)


    end = time.time()
    print('運行秒數: {:2.1%}秒 '.format((end - start)/100))
    
    
    tmp_str = ''
    x = ''
    for item in ['DNN','C45','Extree','XGB','LGBM','CatBc']:    
        #tmp_str += item + '的預測結果為:' +  str((x = '預測此履約價格 \'小於\' 當週結算價格' if result[item][0] == 0 else '預測此履約價格 \'大於\' 當週結算價格')) + '\n'
        x = '預測此履約價格 \'小於\' 當週結算價格' if result_dict[item][0] == 0 else '預測此履約價格 \'大於\' 當週結算價格'
        tmp_str += item + '的預測結果為:' + x + '\n'
    #print(tmp_str)
    
    return tmp_str

