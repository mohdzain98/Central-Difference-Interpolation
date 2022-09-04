# Central-Difference-Interpolation
Also known as Gauss Forward Central Difference Interpolation 
THis is case 1 when we take odd number of points.
THe given values are a list of x values and a list of y values where y[i]=f[i]
fi=Pn(xi)=a0+a1(xi-x0)+a2(xi-x0)(xi-x1)+a3(xi-x0)(xi-x1)(xi-x(-1))+a4(xi-x0)(xi-x1)(xi-x(-1))(xi-x4)........
where an=(Δ^nf(-i))/n!h^n
and Δf(i)=f(i+1)-f(i)
f0=a0
a0=f0
a1=(f1-f0)/h=Δf0/h
pn(x-1)=a0+a1(x(-1)-x0)+a2(x(-1)-x0)(x(-1)-x1)
f(-1)=f0+Δf0/h(-h)+a2(-h)(-2h)
2h^2a2=f(-1)-f0+Δf0
       -Δf(-1)+Δf0 = Δf0-Δf(-1)
       ΔΔf(-1)
2h^2a2=Δ^2f(-1)
    a2=Δ^2f(-1)/2!h^2
