# Central-Difference-Interpolation
Also known as Gauss Forward Central Difference Interpolation <br/>
THis is case 1 when we take odd number of points.<br/>
THe given values are a list of x values and a list of y values where y[i]=f[i]<br/>
fi=Pn(xi)=a0+a1(xi-x0)+a2(xi-x0)(xi-x1)+a3(xi-x0)(xi-x1)(xi-x(-1))+a4(xi-x0)(xi-x1)(xi-x(-1))(xi-x4)........<br/>
where an=(Δ^nf(-i))/n!h^n<br/>
and Δf(i)=f(i+1)-f(i)<br/>
f0=a0<br/>
a0=f0<br/>
a1=(f1-f0)/h=Δf0/h<br/>
pn(x-1)=a0+a1(x(-1)-x0)+a2(x(-1)-x0)(x(-1)-x1)<br/>
f(-1)=f0+Δf0/h(-h)+a2(-h)(-2h)<br/>
2h^2a2= f(-1)-f0+Δf0<br/>
2h^2a2= -Δf(-1)+Δf0 = Δf0-Δf(-1)<br/>
2h^2a2= ΔΔf(-1)<br/>
2h^2a2=Δ^2f(-1)<br/>
    a2=Δ^2f(-1)/2!h^2<br/>
