from unittest import result
from PredictWithPickle_module import PredictResult
import pandas as pd
import numpy as np



result = PredictResult(-23810,1849,25659)
#PredictResult(-23810,1849,25659)
#PredictResult(7726,18395,10669)
#PredictResult(14960,17884,2924)
#PredictResult(11334,11969,635)
#PredictResult(4154,4156,2)
#PredictResult(512,512,0)

print(result['DNN'][0])
print('DNN的預測解果為:' + str(result['DNN'][0]))

'''
featureColumns = ['OI_c_p_N-1','Open_Interest_c_N-1','Open_Interest_p_N-1']
data_ = np.array(np.reshape([23810,1849,25659],(1,3)))
print(data_)
feature_df = pd.DataFrame(data_,columns=featureColumns)
print(feature_df)
'''



# 在 Flask 裡面只要載入 PredictWithPickle_module.py (from PredictWithPickle_module import PredictResult) 就能使用裡面的函式(PredictResult

# 結果會得出各個預測模型並放置於dict中, 再從中解出來顯示再網頁上即可, pickle_test_0712.py 為示範載入程式

