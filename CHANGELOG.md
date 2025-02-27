# 更新日志

*日志使用 [Simple Changelog 汉化版](https://github.com/NiButCrazy/simple-changelog-Chinese) 生成*

## [0.1.0 正式版] - 2025-01-29
### 新增内容
- 为棋盘各行为添加了音效
- 添加了 重新开始游戏 的 按钮
- 添加了 显示回合 的信息 UI

### 作出更改
- 将军 时鼠标悬浮会变成紫色地图块，更加易于辨别
- 把游戏结束时的提示框改成了游戏内自己的选择UI

### 修复错误
- 修复了 Timer 类在调用嵌套 then 时会导致回调函数变成 None 的 BUG
- 修复了棋子死亡后忘记从 chess_dict 及时删除的 BUG
- 修复了兵在吃掉位于地图边缘的王时会触发“升变”的 BUG
- 修复了兵在“升变”后可以无视回合随便跑的BUG
- 修复了兵在“升变”时选择 UI 内的棋子图像并没有变成对应的棋子颜色的 BUG

### 不推荐使用功能
- 联机功能还在开发中，以后电子阳痿了再开发


## [0.0.7-Beta] - 2025-01-28
### 新增内容
- 为游戏添加了回合制
- 新增“兵升变”的 UI 和 “王车移位”的逻辑与功能
- 添加选择ui函数

### 修复错误
- 修复了马不能准确识别空白地图块的BUG
- 修复了棋子死亡后该位置的其他棋子被识别为空地图块
- 修复了 Timer 类 的回调函数会死循环的BUG

### 文档变化
- 修改了部分游戏规则


## [0.0.6-Beta] - 2025-01-27
### 新增内容
- 添加了兵的“路过吃兵”、“兵的升变（差个选择UI）”
- 添加了棋子移动的动画，并实现了“吃”这个功能

### 作出更改
- 更改了地图块的边框的显示的逻辑与方法

### 修复错误
- 修复了 UIChildrenList 类添加 node_parent 时添加成自己的BUG
- 修复了地图块激活时会无视路径上棋子的 BUG


## [0.0.5-Beta] - 2025-01-26
### 新增内容
- gameMap 函数添加了地图方块的激活特效
- 添加了鼠标处于激活地图块上时，会有相应的地图块背景色以加强显示效果

### 作出更改
- 鼠标右键现在只能在空白处右键才能取消棋子的选中状态，并且右键棋子无法选中棋子

### 修复错误
- 修复了鼠标在进出棋子与激活地图块时会抽搐的问题

### 文档变化
- 添加了“ 规则说明.txt”

### 不推荐使用功能
- 兵的逻辑代码忘记做了，先别使用该类


## [0.0.4-Beta] - 2025-01-25
### 新增内容
- 是的，我终于为棋盘添加了所有棋子以及类模块文件
- 为 GameMap 添加了 [选择、清除] 等相应特效函数

### 作出更改
- 改变了部分模块的导入逻辑，防止产生循环套娃导入的现象
- 把黑色棋子图片添加了白色描边，不会两眼一黑了

### 不推荐使用功能
- 棋子单独的功能判定还未做


## [0.0.3-Beta] - 2025-01-25
### 新增内容
- 添加了 gameMap、basicChess、binChess 三个模块
- 为 uiBase 模块添加 Group 类，方便对子节点的管理

### 作出更改
- 把 gameScene 里 的 create_map 功能集成进 gameMap 里面去
- 现在 UIBase 类 支持绘制透明背景 UI


## [0.0.2] - 2025-01-23
### 新增内容
- 添加了一块棋盘地图绘制功能

### 修复错误
- 修复了信息昵称更改后无法及时更新的问题
- 修复了绝大多数的功能，使其能正常工作

### 文档变化
- .gitignore 文件更新

### 不推荐使用功能
- 不推荐游玩游戏，因为啥都没写


## [0.0.2-Beta] - 2025-01-22
### 新增内容
- 创建了基础的UI框架

### 作出更改
- 更改了部分不合理的逻辑

### 文档变化
- 完善了 REEADME.md 内容

### 不推荐使用功能
- 不推荐使用任何功能，因为啥都没做完


## [0.0.1-Beta] - 2025-01-22
### 新增内容
- 初始化项目结构