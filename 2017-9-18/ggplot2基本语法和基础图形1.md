# ggplot2基本语法和基础图形2
加载新的数据：
```R
> uspopage
> us <- uspopage
> ggplot(us) + geom_line(aes(x=Year, y=Thousands))
```
查看一下数据：
![](0261.png)

结果展示：

![](026.png)

按年龄段：
```R
> ggplot(us) + geom_line(aes(x=Year, y=Thousands, color=AgeGroup))
```
![](027.png)

区域图：
```R
> ggplot(us) + geom_area(aes(x=Year, y=Thousands, color=AgeGroup))
```
结果展示：

![](028.png)

换种形式：
```R
> ggplot(us) + geom_area(aes(x=Year, y=Thousands, fill=AgeGroup))
```

show:

![](029.png)

一图多画：
```R
> ggplot(us) + geom_area(aes(x=Year, y=Thousands)) + facet_wrap(~AgeGroup)
```

result show:

![](031.png)