import cdsapi
c = cdsapi.Client()
do="/home/lunet/gytm3/Teaching/GYP043/2021/ERA5/"

for y in range(2021,2022):
    
    for m in range(8,10): 
        
        ofile=do+"year-%.0f_month-%.0f.nc"%(y,m)
        
        c.retrieve(
        
            'reanalysis-era5-single-levels',
            {
                'product_type': 'reanalysis',
                'variable': [
                    '10m_u_component_of_wind', '10m_v_component_of_wind', 
                    '2m_dewpoint_temperature',
                    '2m_temperature', 'surface_solar_radiation_downwards', 
                    'surface_thermal_radiation_downwards',
                    'total_cloud_cover',
                ],
                'year': '%.0f'%y,
                'month': '%.0f'%m,
                'day': [
                    '01', '02', '03',
                    '04', '05', '06',
                    '07', '08', '09',
                    '10', '11', '12',
                    '13', '14', '15',
                    '16', '17', '18',
                    '19', '20', '21',
                    '22', '23', '24',
                    '25', '26', '27',
                    '28', '29', '30',
                    '31',
                ],
                'time': [
                    '00:00', '01:00', '02:00',
                    '03:00', '04:00', '05:00',
                    '06:00', '07:00', '08:00',
                    '09:00', '10:00', '11:00',
                    '12:00', '13:00', '14:00',
                    '15:00', '16:00', '17:00',
                    '18:00', '19:00', '20:00',
                    '21:00', '22:00', '23:00',
                ],
                'area': [
                    34.5, 77, 33,
                    78,
                ],
                'format': 'netcdf',
            },
            ofile)
