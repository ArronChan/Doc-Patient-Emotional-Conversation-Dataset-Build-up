1. 截取对话视频，命名格式为 **S<u>XX</u>E<u>XX</u>-<u>XX</u>.mp4**

   ​							表示：第几季-哪一集-序号

   如第一季第一集的第二个片段，则命名为：

   ​		S01E01-02.mp4

   注意！个位数的话，**0一定要加上**

2.  将所有截取视频都放在./video内

3. 在终端中运行

   ```python
   python create.py
   ```

   即开始进行每个视频的处理，结果存放在./output中

4. 打开每个视频的人脸截取结果     ./output/xxxx/chopFace

   选取**患者**情绪表现**最强烈**的**10-20**帧表情，复制到./output/xxxx/keyExpFrame

5. 在./output/xxxx/conversation.txt中写入视频对话内容：

   格式为：

   P: xxxxxxx

   D: xxxxxxx

   注意！':'为英文冒号，冒号后面有一个空格