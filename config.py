from datetime import datetime, timedelta


class Config(object):

    # Bucket configuration
    BUCKET = 's3://era5-atlantic-northeast/netcdf/pressure-levels-ensemble/day'
    CLIENT_KWARGS = {'endpoint_url': 'https://s3.us-east-2.wasabisys.com',
                     'region_name': 'us-east-2'}
    CONFIG_KWARGS = {'max_pool_connections': 30}
    PROFILE = 'default'

    STORAGE_OPTIONS = {'profile': PROFILE,
                       'client_kwargs': CLIENT_KWARGS,
                       'config_kwargs': CONFIG_KWARGS
                       }

    # Dataset
    START_DATE = "1979-01-01"
    END_DATE = (datetime.utcnow() - timedelta(days=5)).strftime('%Y-%m-%d')

    VARIABLES = {'relative_humidity': 'r',
                 'temperature': 't',
                 'u_component_of_wind': 'u',
                 'v_component_of_wind': 'v',
                 'geopotential': 'z',
                 'vorticity': 'vo',
                 'potential_vorticity': 'pv',
                 'divergence': 'd',
                 'fraction_of_cloud_cover': 'cc'}

    TIMES = [
            '00:00', '03:00', '06:00',
            '09:00', '12:00', '15:00',
            '18:00', '21:00',
        ]
    PRESSURE = ['1000', '850', '700', '500', '250']
