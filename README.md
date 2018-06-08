# Google Street View Loader Demo

## Prerequisites
```
pip3 install -r requirements.txt
```

## How it works

## Step 1: Convert geojson polygon to points/coordinates

<p align="center">
<img src="doc/GeoJSON.png" width="850"  style="display: block;  margin: 0 auto;"/>
</p>


### Step 2: Extract coordinates along roads/streets cooresponding to the subdistrict

<p align="center">
<img src="doc/overpass_api.png" width="900"  style="display: block;  margin: 0 auto;"/>
</p>

### Step 3: Send the coordinates to the street view api to retrieve static images

<p align="center">
<img src="doc/gsv.png" width="870"  style="display: block;  margin: 0 auto;"/>
</p>
