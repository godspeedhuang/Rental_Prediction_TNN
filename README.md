# 台南市區租屋估價平台
- [專案說明](#專案說明)
- [資料說明](#資料說明)
- [操作說明](#操作說明)
- [技術說明](#技術說明)
- [專案結構](#專案結構)
- [貢獻者](#貢獻者)
- [其他](#其他)

## 專案說明
此專案為成功大學 **大數據分析與資料探勘課程** 之期末報告，專題發想從大學生的角度切入，想找到合適又符合預算的出租房屋是一件相當困難的事情，因此本專題將挑選台南市區中的七個行政區，篩選出約50個條件的特徵值，利用機器學習模型預測該條件下之合理租金範圍，並將該模型部署於租金預測平台網站上，期望能降低租屋市場的資訊不對等與不透明，同時給予出租及承租雙方相對客觀的估價系統，以供作參考，操作頁面可參考以下連結。

- [網站Demo影片](https://www.youtube.com/watch?v=3swbfVjmSXA)
## 資料說明
資料集來自[開放台灣民間租屋資料](https://rentalhouse.g0v.ddio.io/)，租屋資料來源為591租屋網，資料時間為2021年01至05月份，地區為台南市東區、中西區、北區、南區、安平區、安南區及永康區之租屋資料，總有效筆數15,994筆。

## 操作說明
### 網頁版面簡介
![網頁簡介](/images/web_demo.png)
- **STEP 1. 選擇模型**
    - 線性迴歸(LinearRegression)
    - 隨機迴歸森林(RandomForest)
    - 極限梯度提升法(XGBoost)
- **STEP 2. 輸入參數**
    - 輸入欲出租/承租之房屋各項參數
- **STEP 3. 點擊估價按鈕進行估價**
- **STPE 4. 顯示估價結果**
- 互動式地圖版面
    - 會顯示選取的里別所在之實際區域

## 技術說明
- 網頁技術
   - 本平台為增加網站即時互動性，使用`Python Dash框架`進行前後端撰寫，Dash是一個建立在Flask、Plotly.js以及React.js基礎上的高效簡潔框架，是建立互動式資料視覺化網站應用的利器，並將訓練好的模型部署在後端程式，可根據前端網頁模型的選擇不同，呼叫不同的模型進行預測結果的計算，最後考量金錢成本問題將網站部署於免費的雲平台heroku上。
- 機器學習模型
  - 使用`多元線性迴歸`、`隨機迴歸森林`和`XGBoost`三種模型為主進行資料訓練，下表為各項模型參數與表現整理

| 使用模型 | 設定條件 | R-Square | MAE | 採用
| :------- | :------- | -------: | -------: | :-------: |
| 多元線性迴歸    | 無限定    | **0.47** | 140.50 | v |
|     | Lasso Regression    | 0.32 | 140.41 |
| 隨機迴歸森林    | n_estimators=**200**<br>max_depth=5| 0.47 | 139.98 |
|     | n_estimators=**1000**<br>max_depth=5| **0.47**| 140.12 |  v |
| XGBoost    | Odjective=reg:squarederror<br>n_estimators=**200**<br>colsample_bytree=0.3<br>learning_rate=0.1<br>max_depth=5<br>alpha=10    | 0.73 | 110.66 |
|     | Odjective=reg:squarederror<br>n_estimators=**1000**<br>colsample_bytree=0.3<br>learning_rate=0.1<br>max_depth=5<br>alpha=10    | **0.87**| 95.10 |  v |

## 專案結構
主要有三個子資料夾，分別存放`資料前處理(preprocess/)`、`模型訓練過程(training/)`及`模型成果(model/)`之相關檔案，其餘如下所示。
```
Rental_Prediction_TNN/
    ├─ preprocess/        // 原始資料前處理
    |   ├─ rawdata/
    |   |   ├─ 2021Q1-deduplicated.csv   
    |   |   ├─ 202104-deduplicated.csv
    |   |   └─ 202105-deduplicated.csv         
    |   ├─ 編碼表/
    |   |   └─ 編碼表.___.csv 
    |   ├─ 前處理後租金資料.csv
    |   ├─ preprocess.ipynb                 
    |   ├─ preprocess2.ipynb
    |   └─ ...    
    ├─ trainging/        // 模型訓練
    |   ├─ rentdata.csv
    |   └─ training.ipynb
    ├─ models/           // 模型成果
    |   ├─ linearregression2.pickle
    |   ├─ rd10002.pickle    
    |   └─ xgb10002.pickle
    ├─ web_map/           // 互動式地圖
    |   ├─ map_test.html
    |   └─ vill.geojson
    ├─ main.py           // 主程式
    ├─ func.py           // 函數集
    ├─ requirements.txt          
    ├─ runtime.txt
    ├─ Procfile
    ├─ images/        
    └─ README.md    
```


## 貢獻者
- 黃軒柏
- 郭亭琳
- 王弘旻

## 其他資料
- [專案簡報](https://ncku365-my.sharepoint.com/:p:/g/personal/f24076182_ncku_edu_tw/EdRMI2NjZ1ZMtGLyPz1MUGwBTS4qnmdI1wXoGJGtbFkftA?e=ciIIHM)
- [專案報告書](https://ncku365-my.sharepoint.com/:w:/g/personal/f24076182_ncku_edu_tw/EUR0cFsBotZDtzxgZd8f2dEBfPQEpzd5Zv9EVU_a7jSTTg?e=OgwM4Y)
