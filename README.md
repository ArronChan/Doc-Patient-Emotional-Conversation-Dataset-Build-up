### 制作本数据集的目的：

收集影视剧中医患之间的对话片段，作为让虚拟人重演医生角色的参考材料。



### 环境要求

python 3.6

opencv-python



### 制作方法

1. 观看《实习医生格蕾》第二季至第十六季（可以从美剧天堂/极速之星下载），使用视频编辑软件（如pr等），从中截取医患间的情绪对话视频片段，要求：

   1. 尽量选取对话双方皆有正脸出镜的片段，避免面部遮挡/侧脸的片段
   2. 尽量选取情绪更强烈的对话片段
   3. 每段视频仅包括：患者发言-医生回复 两句话，一段交流较长的对话应分成多个视频

2. 截取对话视频，命名格式为 **S<u>XX</u>E<u>XX</u>-<u>XX</u>.mp4**，表示：第几季-哪一集-序号，存储格式为mp4

   如第一季第一集的第二个片段，则命名为：S01E01-02.mp4

   注意！个位数的话，**0一定要加上**

3. 打开终端，安装opencv-python

   ```python
   pip install opencv-python
   ```

4. 下载本repository：

   ```cmd
   git clone https://github.com/ArronChan/Doc-Patient-Emotional-Conversation-Dataset-Build-up.git
   ```

5. 将所有截取视频都放在./video内

6. 进入本repo，在终端中运行

   ```python
   python create.py
   ```

   即开始进行每个视频的处理，结果存放在./output中

7. 打开每个视频的人脸截取结果     ./output/xxxx/chopFace

   选取**患者**情绪表现**最强烈**的**10-20**帧表情，复制到./output/xxxx/keyExpFrame

8. 在./output/xxxx/conversation.txt中写入视频对话内容：

   格式为：

   ​		P: xxxxxxx

   ​		D: xxxxxxx

   注意！':'为英文冒号，且冒号后面有一个空格



### 预期数据量

​	约200组对话数据
