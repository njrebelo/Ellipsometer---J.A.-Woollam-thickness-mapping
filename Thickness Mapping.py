from imports import *

file_location="C:\\Users\\rebelo\\Desktop\\Elipsometer Scripts\\Data\\DataHfO2_8cm.txt"
wavelength=300
z_z=3 #Thinckness s always the 8th collumn
z_n=8 #Refractive Indexes is always the 8th collumn
z_ot=9 #Optical Thickness is always the 9th collumn
z_mse=2 #MSE is always the 9th collumn

z_zlabel="Thickness [nm]"
z_nlabel="Refractive Index"
z_otlabel="Optical Thickness [nm]"
z_mselabel="MSE [a.u]"
x_label="X Position [cm]"
y_label="Y Position [cm]"

title="Thickness Variation for HfO2 on Si"
ntitle="Refractive Index Variation for HfO2 on Si"
ottitle="Optical Thickness Variation for HfO2 on Si"
msetitle="MSE Variation for HfO2 on Si"

data=UploadData(file_location)
data=CalculateN(data,wavelength)
data=OpticalThickness(data)
data=MSETolerance(data,15)

plot_maps(data,x_label,y_label,z_z,z_zlabel,title)
plot_maps(data,x_label,y_label,z_n,z_nlabel,ntitle)
plot_maps(data,x_label,y_label,z_ot,z_otlabel,ottitle)
plot_maps(data,x_label,y_label,z_mse,z_mselabel,msetitle)