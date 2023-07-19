import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import os
import time

"""
Created on Thu Mar  9 13:46:57 2023
This code will be used to plot maps of the elipsometer
@author: rebelo
"""

def remove_line(fileName,lineToSkip):
    """ Removes a given line from a file """
    with open(fileName,'r') as read_file:
        lines = read_file.readlines()

    currentLine = 1
    with open(fileName,'w') as write_file:
        for line in lines:
            if currentLine == lineToSkip:
                pass
            else:
                write_file.write(line)
	
            currentLine += 1

def UploadData(file_directory):

    with open(file_directory, 'r') as file :
      filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('(', '')
    filedata = filedata.replace(')', '')
    filedata = filedata.replace(',', '\t')

    # Write the file out again
    temp_file=file_directory[:-4]+"_temp.txt"
    with open(temp_file, 'w') as file:
      file.write(filedata)
      
    for i in range(6):
        remove_line(temp_file,1)
        time.sleep(0.5)
      
    data=np.loadtxt(temp_file)
    
    os.remove(temp_file)
    return data

def MSETolerance(data,maximun):
    lines=data.shape[0]
    to_delete=[]
    for i in range(lines):
        if data[i,2]>maximun:
            to_delete.append(i)
    data=np.delete(data,to_delete,0)
    return data
             
    
        
def CalculateN(data,wavelength):
    numberOfElements=data.shape[0]
    n_matrix=np.zeros(numberOfElements)
    for i in range(numberOfElements):
        n=data[i,4]+(data[i,5]/(wavelength*wavelength))+(data[i,6]/wavelength*wavelength*wavelength)
        n_matrix[i]=n
    data=np.column_stack((data,n_matrix))
    return data
    
def plot_maps(data,x_label,y_label,z,z_label,title):
    x=data[:,0]
    y=data[:,1]
    z=data[:,z]
    
    xi = np.linspace(x.min(), x.max(), 1000)
    yi = np.linspace(y.min(), y.max(), 1000)

    # Interpolate for plotting
    zi = griddata((x, y), z, (xi[None,:], yi[:,None]), method='linear')

    # I control the range of my colorbar by removing data 
    # outside of my range of interest
    zmin = np.amin(z)
    zmax = round(np.amax(z),3)
    zi[(zi<zmin) | (zi>zmax)] = None

    # Create the contour plot
    CS = plt.contourf(xi, yi, zi, 15, cmap=plt.cm.rainbow,
                      vmax=zmax, vmin=zmin)
    plt.colorbar(label=z_label)
    plt.title(title)
    #plt.xlim((-5,-3))
    #plt.ylim((-1,1))
    plt.xlabel(x_label,size=10)
    plt.ylabel(y_label,size=10)
    plt.show()
    
def OpticalThickness(data):
    ot=data[:,4]*data[:,8]
    data=np.column_stack((data,ot))
    return data