import psycopg2
from sqlalchemy.engine import URL, make_url


class SQLDeviceAPI:
    def __init__(self, dsn: str):
        self.connection = psycopg2.connect(**self.dsn_parse(dsn))

    @staticmethod
    def dsn_parse(dsn: str) -> dict[str, str]:
        pg_address = make_url(dsn)
        assert isinstance(pg_address, URL)

        pg_connection_dict = {
            "dbname": pg_address.database,
            "user": pg_address.username,
            "password": pg_address.password,
            "port": pg_address.port,
            "host": pg_address.host,
        }

        return pg_connection_dict
