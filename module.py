from ipyleaflet import Map, GeoJSON
from ipywidgets import widgets
from IPython.display import display
import json
import os
import requests
import bqplot as bq
import os
import imageio
import ipywidgets as wd
import matplotlib.pyplot as plt
from IPython.display import HTML
from IPython.display import Video
import numpy as np

def show_location_on_map(location):
    m = Map(center=(40.7205,-73.9060), zoom=12)
    geo_json = GeoJSON(data=location)
    m.add_layer(geo_json)
    return m
    
def select_within_boundingbox(df, BB):
    return (df.pickup_longitude >= BB[0]) & (df.pickup_longitude <= BB[1]) & \
           (df.pickup_latitude >= BB[2]) & (df.pickup_latitude <= BB[3]) & \
           (df.dropoff_longitude >= BB[0]) & (df.dropoff_longitude <= BB[1]) & \
           (df.dropoff_latitude >= BB[2]) & (df.dropoff_latitude <= BB[3])

def check_p1q1(lon, lat):
    if (lon == -73.99484672999999) and (lat == 40.75085565):
        response = "Correct!"
    else: response = "False. Try Again."
    print(response)


def check_p1q2(input_array):
    if  input_array == [[-73.78882321212122, 40.64573275757575, 57.33],
                        [-73.78640196969697, 40.641566999999995, 57.33],
                        [-73.78155948484849, 40.64573275757575, 57.33]]:
        response = "Correct!"
    else: response = "False. Try Again."
    print(response)

def check_p2q1(l):
    if l == [1919595929, 42440330, 3891963915]:
        response = "Correct!"
    else:
        response = "Incorrect. Try Again!"
    return response

def check_p2q2(l):
    if [370924957, 371188750, 371188756] == l:
        response = "Correct!"
    else:
        response = "Incorrect. Try Again!"
    return response
    
def check_p3(answer):
    if answer[0] == 6.0 and answer[1] == [(0, 1), (1, 2), (2, 0)]:
        response = "Correct!"
    else:
        response = "Incorrect. Try Again!"
    return response

def check_p4q1(you, v1, v2, v3, fn):
    if (not fn(you, v1) and not fn(you, v2) and fn(you, v3) and not fn(v1, v2) and not fn(v1, v3) and not fn(v2, v3)):
        response = "Correct!"
        os.makedirs("data", exist_ok=True)
        l = np.arange(0.0, 0.1, 0.0025)
        for i, t in enumerate(l):
            plot_object_positions([you, v1, v2, v3], t, i)
        make_video(image_folder='data', l=l, collision=1)
        print(response)
        return wd.interact(showvideo(1)) 
        
    else: 
        response = "Incorrect. Try Again!"
    return response

def check_p4q2(you, v1, v2, v3, fn):
    if (fn(you, v1) and not fn(you, v2) and fn(you, v3) and not fn(v1, v2) and not fn(v1, v3) and not fn(v2, v3)):
        response = "Correct!"
        os.makedirs("data", exist_ok=True)
        l = np.arange(0.0, 0.1, 0.0025)
        for i, t in enumerate(l):
            plot_object_positions([you, v1, v2, v3], t, i, with_radius=True)
        make_video(image_folder='data', l=l, collision=2)
        print(response)
        return wd.interact(showvideo(2)) 
    else: 
        response = "Incorrect. Try Again!"
    return response
    
def show_locations_on_map(locations):
    m = Map(center=(40.7205,-73.9060), zoom=11)
    for locs in locations:
        parse_loc = {
              "type": "FeatureCollection",
              "features": [
                {
                  "type": "Feature",
                  "properties": {},
                  "geometry": {
                    "type": "Point",
                    "coordinates": [
                      locs[0],
                      locs[1] 
                    ]
                  }
                }
              ]
            }
        geo_json = GeoJSON(data=parse_loc)
        m.add_layer(geo_json)
    return m


def show_location_on_map(location):
    m = Map(center=(40.7205,-73.9060), zoom=12)
    geo_json = GeoJSON(data=location)
    m.add_layer(geo_json)
    return m
    
def select_within_boundingbox(df, BB):
    return (df.pickup_longitude >= BB[0]) & (df.pickup_longitude <= BB[1]) & \
           (df.pickup_latitude >= BB[2]) & (df.pickup_latitude <= BB[3]) & \
           (df.dropoff_longitude >= BB[0]) & (df.dropoff_longitude <= BB[1]) & \
           (df.dropoff_latitude >= BB[2]) & (df.dropoff_latitude <= BB[3])

def generate_json(hist, arg_hotspot_func):
    location = {
              "type": "FeatureCollection",
              "features": [
                {
                  "type": "Feature",
                  "properties": {},
                  "geometry": {
                    "type": "Point",
                    "coordinates": [
                      hist[1][arg_hotspot_func(hist[0])[0]],
                      hist[2][arg_hotspot_func(hist[0])[1]] 
                    ]
                  }
                }
              ]
            }
    return location

#Plotting in Q4
def plot_object_positions(vehicles, t, i, with_radius=False):
    x = []
    y = []
    colors=["#000000","#0000FF", "#00FF00", "#FF0066"]
    if not with_radius:
        s = [20, 20, 20, 20]
        collision=1
    else:
        s = [30, 240, 30, 60]
        collision=2
    
    for vehicle in vehicles:
        u = round(vehicle.velocity * np.cos(vehicle.theta), 2)
        v = round(vehicle.velocity * np.sin(vehicle.theta), 2)
        x += [vehicle.pos[0] + u*t]
        y += [vehicle.pos[1] + v*t]
    plt.scatter(x, y, color=colors, s=s)
    plt.xlim(-2, 2)
    plt.ylim(0, 10)
    plt.savefig(f'data/collision{collision}_' + str(i) + '.png')
    plt.close()

def make_video(image_folder, l, collision=1):
    video_name = f'video{collision}.mp4'
    images = []
    for i in range(len(l)):
        images += ['data' + f'/collision{collision}_' + str(i) + '.png']
            

    writer = imageio.get_writer(video_name, fps=20)

    for im in images:
        writer.append_data(imageio.imread(im))
    writer.close()


def showvideo(collision):
    display(HTML(f"""<video width="500" height="500" controls><source src="video{collision}.mp4" type="video/mp4"></video>"""))