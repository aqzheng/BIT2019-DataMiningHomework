# 关联规则挖掘
        姓名：郑安庆 学号：3120181078
## 数据集选择
        Wine Reviews
## 运行环境及依赖
        python 3.6.3
        pandas、json
## 运行方法
        # convert data
        python process_data.py
        # run apriori algorithm
        python main.py

        # you need to modify the config.py files in your opinion
        '''
        data_path = "wine-reviews"
        data_file_list = ["winemag-data_first150k.csv","winemag-data-130k-v2.csv"]
        min_support = 0.25
        min_confidence = 0.5
        '''
## 文件结构

        BIT2019-DataMiningHomework/Homework-2/
         main.py
         process_data.py
         config.py
         --data                           # 数据目录
           --wine-reviews
             --winemag-data_first150k.csv
             --winemag-data-130k-v2
         --result                         # 结果目录
           --wine-reviews
             --winemag-data_first150k
               --processd.csv             # 经过process_data.py处理后的数据
               --freq_set.json            # 频繁项集结果
               --rules.json               # 关联规则结果
             --winemag-data-130k-v2
               --...
