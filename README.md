# SudokuSolver
解数独游戏的AI

## 使用方法
1. 将题目用json表示，具体格式参考`sudokyjsons/example.json`文件; 或者另一种格式也可以，参考`sudokyjsons/example2.json`文件
2. 调用程序求解：`python SudokuSolver.py -f sudokujsons/example.json` 后面的json名改为自己的文件名


## 更新日志
+ 2022-05-08: 加入对多结果题目的支持，现在可以输出所有结果