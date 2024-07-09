import pyproj

def wgs84_to_utm(lat, lon):

    utm_zone = int((lon + 180) // 6) + 1
    epsg_code = f"326{utm_zone:02d}" if lat >= 0 else f"327{utm_zone:02d}"
    transformer = pyproj.Transformer.from_crs("epsg:4326", f"epsg:{epsg_code}", always_xy=True)

    easting, northing = transformer.transform(lon, lat)

    utm_band = 'north' if lat >= 0 else 'south'

    return easting, northing, utm_zone, utm_band


if __name__ == '__main__':

    latitude = 32.84073613
    longitude = -117.24969349

    easting, northing, zone, band = wgs84_to_utm(latitude, longitude)
    print(f"Easting: {easting}, Northing: {northing}, Zone: {zone}, Hemisphere: {band}")
