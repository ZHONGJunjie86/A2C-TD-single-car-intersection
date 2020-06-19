# A2C-TD-single-car-intersection

When I found the A2C-MC was inefficient, I turned to use the A2C-TD which the paper used. MC method can't learn every stuation preciously.
To see model's details from [my previous work](https://github.com/ZHONGJunjie86/A3C-single-car-intersection).

# tips
   Let him slow down a little bit first, and then learn to speed up; once he learns faster, he can't slow down, because he can reduce the points caused by the number of rounds. Each round's reduction in time should be reduced more for slower chances
The higher the speed, the more speeding is possible. Don't use minus (one minus is a multiple), use ratio to measure.
The high-speed and low-speed rewards should be similar. Speed up a little bit harder, because defining the domain width will slow him down
The values of the incoming vectors should not differ by too many orders of magnitude, otherwise it will not converge, it is not easy to learn, and the graph will fluctuate greatly, which is not good-looking
