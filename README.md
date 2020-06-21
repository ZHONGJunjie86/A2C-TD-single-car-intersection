# A2C-TD-single-car-intersection

　When I found the A2C-MC was inefficient, I turned to use the A2C-TD algorithm which the paper used. MC method can't learn every stuation preciously and costs more time.
　This is a basic model describing a car runs to goal in limited time by using A2C algorithm to control its accelerate.
　To see model's details from [my previous work](https://github.com/ZHONGJunjie86/A3C-single-car-intersection).
# Reward shaping 
　
# tips
   Let him slow down a little bit first, and then learn to speed up; once he learns faster, he can't slow down, because he can reduce the points caused by the number of rounds. Each round's reduction in time should be reduced more for slower chances
The higher the speed, the more speeding is possible. Don't use minus (one minus is a multiple), use ratio to measure.
The high-speed and low-speed rewards should be similar. Speed up a little bit harder, because defining the domain width will slow him down
The values of the incoming vectors should not differ by too many orders of magnitude, otherwise it will not converge, it is not easy to learn, and the graph will fluctuate greatly, which is not good-looking

![image](https://github.com/ZHONGJunjie86/A2C-TD-single-car-intersection/blob/master/illustrate/loss_curve_TD_21.png)
 ![image](https://github.com/ZHONGJunjie86/A3C-single-car-intersection/blob/master/illustrate/illustrate.gif )   
  ![image](https://github.com/ZHONGJunjie86/A3C-single-car-intersection/blob/master/illustrate/A2C-Architecture.JPG) 
![image](https://github.com/ZHONGJunjie86/A2C-TD-single-car-intersection/blob/master/illustrate/loss_curve_TD_20_%E5%AD%A6%E4%B9%A0%E7%8E%870-001%E7%A8%B3%E5%AE%9A%E4%B8%8D%E6%94%B6%E6%95%9B.png)
![image](https://github.com/ZHONGJunjie86/A2C-TD-single-car-intersection/blob/master/illustrate/loss_curve_TD_19_lr%E5%87%8F%E5%BE%97%E5%A4%AA%E6%85%A2%EF%BC%9F.png)
