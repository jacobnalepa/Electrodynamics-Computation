%Sets the field point to the center of the cube
x = 0.5;
y = 0.5;
z = 0.5;

%Defines the electric potential function
fun = @(x_prime,y_prime,z_prime) 1./sqrt((x-x_prime).^2+(y-y_prime).^2+(z-z_prime).^2);
%Calculates the potential at the center of the cube
Phi_0 = integral3(fun,0,1,0,1,0,1);

%Sets the field point to the corner of the cube
x = 0;
y = 0;
z = 0;

%Defines the electric potential function
fun = @(x_prime,y_prime,z_prime) 1./sqrt((x-x_prime).^2+(y-y_prime).^2+(z-z_prime).^2);
%Calculates the potential at the corner of the cube
Phi_c = integral3(fun,0,1,0,1,0,1);

%Calculates the ratio of the potential at the corner of the cube to the
%potential at the center of the cube.
Corner = Phi_c / Phi_0;

%Sets the field point to the center of a cube face
x = 0.5;
y = 0;
z = 0.5;

%Defines the electric potential function
fun = @(x_prime,y_prime,z_prime) 1./sqrt((x-x_prime).^2+(y-y_prime).^2+(z-z_prime).^2);
%Calculates the potential at the center of a cube face
Phi_f = integral3(fun,0,1,0,1,0,1);

%Calculates the ratio of the potential at the center of a cube face to the
%potential at the center of the cube.
Face = Phi_f / Phi_0;

fprintf(['The potential at the corner of the cube in terms of Phi0 is %.4f\n','The potential at the center of a cube face in terms of Phi0 is %.4f\n'], Corner, Face);

%Calculates the electric potential at every point on the plane at z=1 in
%terms of Phi_0
s = 31;
Phi_plane = zeros(s);
x = -1;
y = -1;
z = 1;

for r = 1:s
    for c = 1:s
        fun = @(x_prime,y_prime,z_prime) 1./sqrt((x-x_prime).^2+(y-y_prime).^2+(z-z_prime).^2);
        Phi = integral3(fun,0,1,0,1,0,1);
        Phi_plane(c,r) = Phi/Phi_0;
        y = y+.1;
    end
y = -1;
x = x+.1;
end

%Sets x and y data and creates a surface plot of the potential.
xrange = -1:.1:2;
yrange = -1:.1:2;
surf(xrange,yrange,Phi_plane);