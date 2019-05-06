# python_zxing
echo "# python_zxing" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/lizhihua0625/python_zxing.git
git push -u origin master

或者

git remote add origin https://github.com/lizhihua0625/python_zxing.git
git push -u origin master

不废话，直接来说 我的目的是解析二维码

https://github.com/zxing/zxing  是基于这个的

我有试过window7下面，python3.6 成功
java version "1.8.0_181"
Java(TM) SE Runtime Environment (build 1.8.0_181-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.181-b13, mixed mode)

但是相同的环境，window10 解析二维码失败
centos7 也是解析失败，但是整了好久，找朋友帮忙，终于搞定啦，比较麻烦，学习下吧
openjdk version "1.8.0_212"
OpenJDK Runtime Environment (build 1.8.0_212-b04)
OpenJDK 64-Bit Server VM (build 25.212-b04, mixed mode)

Apache Maven 3.2.5 (12a6b3acb947671f09b81f49094c53f426d8cea1; 2014-12-14T12:29:23-05:00)
Maven home: /usr/local/maven3
Java version: 1.8.0_212, vendor: Oracle Corporation
Java home: /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.212.b04-0.el7_6.x86_64/jre
Default locale: en_US, platform encoding: UTF-8
OS name: "linux", version: "5.0.8-1.el7.elrepo.x86_64", arch: "amd64", family: "unix"

代码里面改了些东西，还是需要注意的

git clone https://github.com/zxing/zxing.git
cd zxing-master
mvn install
cd core
wget http://central.maven.org/maven2/com/google/zxing/core/2.2/core-2.2.jar
mv core-2.2.jar core.jar # Rename
mvn install
cd zxing-master/javase
wget http://central.maven.org/maven2/com/google/zxing/javase/2.2/javase-2.2.jar 
mv javase-2.2.jar javase.jar # Rename
mvn install
git clone git://github.com/oostendo/python-zxing.git

这些步骤，经走下来，我测试通过的，是如此

mvn install -Dmaven.test.skip=true   #需要执行这个
可能是环境的问题，我还改了Swap
[root@fantastic-hat-2 local]# free -h
              total        used        free      shared  buff/cache   available
Mem:           1.0G        305M         68M        952K        626M        527M
Swap:          2.2G        532M        1.7G

可能不需要这么大，但是请参考自己改一下，比较好
请参考
https://blog.csdn.net/zhbzhbzhbbaby/article/details/80810721

具体改了哪里，我不记得啦，没法整理，有需要的朋友，可以自己比较看看，如果不对，请指正，3162289690@qq.com




















