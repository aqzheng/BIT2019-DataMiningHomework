# 数据探索性分析与数据预处理
        姓名：郑安庆 学号：3120181078
## 数据集选择
        Wine Reviews
        Oakland Crime Statistics 2011 to 2016
## 运行环境及依赖
        python 3.6.3
        pandas、scipy、matplotlib、sklearn
## 运行方法
        python main.py

        # you need to modify the config.py files in your opinion
        '''
        data1_path = "wine-reviews"
        data1_file_list = ["winemag-data_first150k.csv","winemag-data-130k-v2.csv"]

        data2_path = "oakland-crime-statistics-2011-to-2016"
        data2_file_list = ["records-for-2011.csv", "records-for-2012.csv", "records-for-2013.csv", "records-for-2014.csv", "records-for-2015.csv", "records-for-2016.csv"]
        '''
## 文件结构

        BIT2019-DataMiningHomework/Homework-1/
         main.py
         config.py
         --data                           # 数据目录
           --wine-reviews
             --winemag-data_first150k.csv
             --winemag-data-130k-v2
          --oakland-crime-statistics-2011-to-2016
             --...
         --result                         # 结果目录
           --wine-reviews
             --winemag-data_first150k
               --figure                   # 图片结果目录
                 --*_histogram.png
                 --*_qq.png
                 --*_box.png
               --nominal_attribute        # 标称属性结果目录
                 --*.txt
               --numeric_attribute        # 数值属性结果目录
                 --*.txt
               --strategy_1               # 缺失值填补结果1目录
                 --winemag-data_first150k.csv
                 --*_histogram.png
                 --*_qq.png
                 --*_box.png
               --strategy_2               # 缺失值填补结果2目录
                 --...
               --strategy_3               # 缺失值填补结果3目录
                 --...
               --strategy_4               # 缺失值填补结果4目录
                 --...
             --winemag-data-130k-v2
               --...
          --oakland-crime-statistics-2011-to-2016
            --...
