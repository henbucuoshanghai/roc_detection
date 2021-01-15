##### coding=utf-8
from evaluation import *
from https://github.com/FenHua/Eval_object_detection
cfg = {'file_dir': './','overlapRatio': 0.5,'cls': 2,'presicion': False,'recall': False,'threshold': 0.5,'FPPIW': False,'roc': False,'pr': False}


if __name__ == "__main__":
    # 参数设置
    dir = ['sample/prediction/', 'sample/test_annos/']  # 预测结果与ground truth结果
    overlapRatio = 0.3  # IoU大小
    threshold = 0.5  # float类型，由于预测结果中存在score值，此阈值决定当前结果的有效性
    cls = 2  # 数据类别的个数，包含背景
    precision = True  # 是否返回精度指标
    recall = True  # 是否返回recall指标
    FPPIW = True  # 是否返回 False Positive Per Image 和 False Positive Per Window
    roc = True  # 是否返回ROC评价指标
    pr = True  # 是否返回precision-recall曲线
    print ("Your Folder's path: {}".format(dir))
    print ("Overlap Ratio: {}".format(overlapRatio))
    print ("Threshold: {}".format(threshold))
    print ("Num of Categories: {}".format(cls))
    print ("Precision: {}".format(precision))
    print ("Recall: {}".format(recall))
    print ("FPPIW: {}".format(FPPIW))
    print("Calculating......")
    cfg['file_dir'] = dir
    cfg['overlapRatio'] = overlapRatio
    cfg['cls'] = cls
    cfg['precision'] = precision
    cfg['recall'] = recall
    cfg['threshold'] = threshold
    cfg['FPPIW'] = FPPIW
    cfg['roc'] = roc
    cfg['pr'] = pr
    eval = evaluation(cfg)
    eval.run()
