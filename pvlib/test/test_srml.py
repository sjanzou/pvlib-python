import inspect
import os

from numpy import isnan
import pandas as pd
from pandas.util.testing import network
import pytest

from pvlib.iotools import srml


test_dir = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))
srml_testfile = os.path.join(test_dir, '../data/SRML-day-EUPO1801.txt')


def test_read_srml():
    srml.read_srml(srml_testfile)


@network
def test_read_srml_remote():
    srml.read_srml('http://solardat.uoregon.edu/download/Archive/EUPO1801.txt')


def test_read_srml_columns_exist():
    data = srml.read_srml(srml_testfile)
    assert 'ghi_0' in data.columns
    assert 'ghi_0_flag' in data.columns
    assert 'dni_1' in data.columns
    assert 'dni_1_flag' in data.columns
    assert '7008' in data.columns
    assert '7008_flag' in data.columns


def test_read_srml_nans_exist():
    data = srml.read_srml(srml_testfile)
    assert isnan(data['dni_0'][1119])
    assert data['dni_0_flag'][1119] == 99


@pytest.mark.parametrize('url,year,month', [
    ('http://solardat.uoregon.edu/download/Archive/EUPO1801.txt',
     2018, 1),
    ('http://solardat.uoregon.edu/download/Archive/EUPO1612.txt',
     2016, 12),
])
def test_read_srml_dt_index(url, year, month):
    data = srml.read_srml(url)
    start = pd.Timestamp('{:04d}{:02d}01 00:00'.format(year, month))
    start = start.tz_localize('Etc/GMT+8')
    end = pd.Timestamp('{:04d}{:02d}31 23:59'.format(year, month))
    end = end.tz_localize('Etc/GMT+8')
    assert data.index[0] == start
    assert data.index[-1] == end
    assert (data.index[59::60].minute == 59).all()
    assert str(year) not in data.columns


@pytest.mark.parametrize('column,expected', [
    ('1001', 'ghi_1'),
    ('7324', '7324'),
    ('2001', '2001'),
    ('2017', 'dni_7')
])
def test_map_columns(column, expected):
    assert srml.map_columns(column) == expected


@network
def test_read_srml_month_from_solardat():
    url = 'http://solardat.uoregon.edu/download/Archive/EUPO1801.txt'
    file_data = srml.read_srml(url)
    requested = srml.read_srml_month_from_solardat('EU', 2018, 1)
    assert file_data.equals(requested)
