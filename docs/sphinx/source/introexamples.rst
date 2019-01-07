.. _introexamples:

Intro Examples
==============

This page contains introductory examples of pvlib python usage.

.. _modeling-paradigms:

Modeling paradigms
------------------

The backbone of pvlib-python
is well-tested procedural code that implements PV system models.
pvlib-python also provides a collection of classes for users
that prefer object-oriented programming.
These classes can help users keep track of data in a more organized way,
provide some "smart" functions with more flexible inputs,
and simplify the modeling process for common situations.
The classes do not add any algorithms beyond what's available
in the procedural code, and most of the object methods
are simple wrappers around the corresponding procedural code.

Let's use each of these pvlib modeling paradigms
to calculate the yearly energy yield for a given hardware
configuration at a handful of sites listed below.

.. ipython:: python

    import pandas as pd
    import matplotlib.pyplot as plt

    naive_times = pd.DatetimeIndex(start='2015', end='2016', freq='1h')

    # very approximate
    # latitude, longitude, name, altitude, timezone
    coordinates = [(30, -110, 'Tucson', 700, 'Etc/GMT+7'),
                   (35, -105, 'Albuquerque', 1500, 'Etc/GMT+7'),
                   (40, -120, 'San Francisco', 10, 'Etc/GMT+8'),
                   (50, 10, 'Berlin', 34, 'Etc/GMT-1')]

    import pvlib

    # get the module and inverter specifications from SAM
    sandia_modules = pvlib.pvsystem.retrieve_sam('SandiaMod')
    sapm_inverters = pvlib.pvsystem.retrieve_sam('cecinverter')
    module = sandia_modules['Canadian_Solar_CS5P_220M___2009_']
    inverter = sapm_inverters['ABB__MICRO_0_25_I_OUTD_US_208_208V__CEC_2014_']

    # specify constant ambient air temp and wind for simplicity
    temp_air = 20
    wind_speed = 0


Procedural
^^^^^^^^^^

The straightforward procedural code can be used for all modeling
steps in pvlib-python.

The following code demonstrates how to use the procedural code
to accomplish our system modeling goal:

.. ipython:: python

    system = {'module': module, 'inverter': inverter,
              'surface_azimuth': 180}

    energies = {}

    for latitude, longitude, name, altitude, timezone in coordinates:
        times = naive_times.tz_localize(timezone)
        system['surface_tilt'] = latitude
        solpos = pvlib.solarposition.get_solarposition(times, latitude, longitude)
        dni_extra = pvlib.irradiance.get_extra_radiation(times)
        airmass = pvlib.atmosphere.get_relative_airmass(solpos['apparent_zenith'])
        pressure = pvlib.atmosphere.alt2pres(altitude)
        am_abs = pvlib.atmosphere.get_absolute_airmass(airmass, pressure)
        tl = pvlib.clearsky.lookup_linke_turbidity(times, latitude, longitude)
        cs = pvlib.clearsky.ineichen(solpos['apparent_zenith'], am_abs, tl,
                                     dni_extra=dni_extra, altitude=altitude)
        aoi = pvlib.irradiance.aoi(system['surface_tilt'], system['surface_azimuth'],
                                   solpos['apparent_zenith'], solpos['azimuth'])
        total_irrad = pvlib.irradiance.get_total_irradiance(system['surface_tilt'],
                                                            system['surface_azimuth'],
                                                            solpos['apparent_zenith'],
                                                            solpos['azimuth'],
                                                            cs['dni'], cs['ghi'], cs['dhi'],
                                                            dni_extra=dni_extra,
                                                            model='haydavies')
        temps = pvlib.pvsystem.sapm_celltemp(total_irrad['poa_global'],
                                             wind_speed, temp_air)
        effective_irradiance = pvlib.pvsystem.sapm_effective_irradiance(
            total_irrad['poa_direct'], total_irrad['poa_diffuse'],
            am_abs, aoi, module)
        dc = pvlib.pvsystem.sapm(effective_irradiance, temps['temp_cell'], module)
        ac = pvlib.pvsystem.snlinverter(dc['v_mp'], dc['p_mp'], inverter)
        annual_energy = ac.sum()
        energies[name] = annual_energy

    energies = pd.Series(energies)

    # based on the parameters specified above, these are in W*hrs
    print(energies.round(0))

    energies.plot(kind='bar', rot=0)
    @savefig proc-energies.png width=6in
    plt.ylabel('Yearly energy yield (W hr)')
    @suppress
    plt.close();


.. _object-oriented:

Object oriented (Location, PVSystem, ModelChain)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first object oriented paradigm uses a model where a
:py:class:`~pvlib.pvsystem.PVSystem` object represents an assembled
collection of modules, inverters, etc., a
:py:class:`~pvlib.location.Location` object represents a particular
place on the planet, and a :py:class:`~pvlib.modelchain.ModelChain`
object describes the modeling chain used to calculate PV output at that
Location. This can be a useful paradigm if you prefer to think about the
PV system and its location as separate concepts or if you develop your
own ModelChain subclasses. It can also be helpful if you make extensive
use of Location-specific methods for other calculations. pvlib-python
also includes a :py:class:`~pvlib.tracking.SingleAxisTracker` class that
is a subclass of :py:class:`~pvlib.pvsystem.PVSystem`.

The following code demonstrates how to use
:py:class:`~pvlib.location.Location`,
:py:class:`~pvlib.pvsystem.PVSystem`, and
:py:class:`~pvlib.modelchain.ModelChain` objects to accomplish our
system modeling goal. ModelChain objects provide convenience methods
that can provide default selections for models and can also fill
necessary input data with modeled data. In our example below, we use
convenience methods. For example, no irradiance data is provided as
input, so the ModelChain object substitutes irradiance from a clear-sky
model via the prepare_inputs method. Also, no irradiance transposition
model is specified (keyword argument `transposition` for ModelChain) so
the ModelChain defaults to the `haydavies` model. In this example,
ModelChain infers the DC power model from the module provided by
examining the parameters defined for module.

.. ipython:: python

    from pvlib.pvsystem import PVSystem
    from pvlib.location import Location
    from pvlib.modelchain import ModelChain

    system = PVSystem(module_parameters=module,
                      inverter_parameters=inverter)

    energies = {}
    for latitude, longitude, name, altitude, timezone in coordinates:
        times = naive_times.tz_localize(timezone)
        location = Location(latitude, longitude, name=name, altitude=altitude,
                            tz=timezone)
        # very experimental
        mc = ModelChain(system, location,
                        orientation_strategy='south_at_latitude_tilt')
        # model results (ac, dc) and intermediates (aoi, temps, etc.)
        # assigned as mc object attributes
        mc.run_model(times)
        annual_energy = mc.ac.sum()
        energies[name] = annual_energy

    energies = pd.Series(energies)

    # based on the parameters specified above, these are in W*hrs
    print(energies.round(0))

    energies.plot(kind='bar', rot=0)
    @savefig modelchain-energies.png width=6in
    plt.ylabel('Yearly energy yield (W hr)')
    @suppress
    plt.close();


Object oriented (LocalizedPVSystem)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The second object oriented paradigm uses a model where a
:py:class:`~pvlib.pvsystem.LocalizedPVSystem` represents a PV system at
a particular place on the planet. This can be a useful paradigm if
you're thinking about a power plant that already exists.

The :py:class:`~pvlib.pvsystem.LocalizedPVSystem` inherits from both
:py:class:`~pvlib.pvsystem.PVSystem` and
:py:class:`~pvlib.location.Location`, while the
:py:class:`~pvlib.tracking.LocalizedSingleAxisTracker` inherits from
:py:class:`~pvlib.tracking.SingleAxisTracker` (itself a subclass of
:py:class:`~pvlib.pvsystem.PVSystem`) and
:py:class:`~pvlib.location.Location`. The
:py:class:`~pvlib.pvsystem.LocalizedPVSystem` and
:py:class:`~pvlib.tracking.LocalizedSingleAxisTracker` classes may
contain bugs due to the relative difficulty of implementing multiple
inheritance. The :py:class:`~pvlib.pvsystem.LocalizedPVSystem` and
:py:class:`~pvlib.tracking.LocalizedSingleAxisTracker` may be deprecated
in a future release. We recommend that most modeling workflows implement
:py:class:`~pvlib.location.Location`,
:py:class:`~pvlib.pvsystem.PVSystem`, and
:py:class:`~pvlib.modelchain.ModelChain`.

The following code demonstrates how to use a
:py:class:`~pvlib.pvsystem.LocalizedPVSystem` object to accomplish our
modeling goal:

.. ipython:: python

    from pvlib.pvsystem import LocalizedPVSystem

    energies = {}
    for latitude, longitude, name, altitude, timezone in coordinates:
        localized_system = LocalizedPVSystem(module_parameters=module,
                                             inverter_parameters=inverter,
                                             surface_tilt=latitude,
                                             surface_azimuth=180,
                                             latitude=latitude,
                                             longitude=longitude,
                                             name=name,
                                             altitude=altitude,
                                             tz=timezone)
        times = naive_times.tz_localize(timezone)
        clearsky = localized_system.get_clearsky(times)
        solar_position = localized_system.get_solarposition(times)
        total_irrad = localized_system.get_irradiance(solar_position['apparent_zenith'],
                                                      solar_position['azimuth'],
                                                      clearsky['dni'],
                                                      clearsky['ghi'],
                                                      clearsky['dhi'])
        temps = localized_system.sapm_celltemp(total_irrad['poa_global'],
                                               wind_speed, temp_air)
        aoi = localized_system.get_aoi(solar_position['apparent_zenith'],
                                       solar_position['azimuth'])
        airmass = localized_system.get_airmass(solar_position=solar_position)
        effective_irradiance = localized_system.sapm_effective_irradiance(
            total_irrad['poa_direct'], total_irrad['poa_diffuse'],
            airmass['airmass_absolute'], aoi)
        dc = localized_system.sapm(effective_irradiance, temps['temp_cell'])
        ac = localized_system.snlinverter(dc['v_mp'], dc['p_mp'])
        annual_energy = ac.sum()
        energies[name] = annual_energy

    energies = pd.Series(energies)

    # based on the parameters specified above, these are in W*hrs
    print(energies.round(0))

    energies.plot(kind='bar', rot=0)
    @savefig localized-pvsystem-energies.png width=6in
    plt.ylabel('Yearly energy yield (W hr)')
    @suppress
    plt.close();
