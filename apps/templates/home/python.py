import pyproj

# Definir una proyección UTM
utm = pyproj.Proj(proj='utm',zone=33,datum='WGS84')

# Definir una proyección latitud/longitud
latlng = pyproj.Proj(proj='latlong',datum='WGS84')

# Convertir coordenadas UTM a latitud/longitud
x, y = (449251.795, 4597820.171)
lon, lat = pyproj.transform(utm, latlng, x, y)
print(lat, lon)