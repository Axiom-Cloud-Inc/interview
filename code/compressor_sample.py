def isentropic_efficiency(**kwargs):
    """
    Given 3 of the 4 variables in the isentropic efficiency equation for a
    compressor, solve for the value of the missing one.

    :param float efficiency: Compressor isentropic efficiency, between 0 and 1.
    :param float inlet_enthalpy: Enthalpy of inlet gas.
    :param float outlet_enthalpy_real: Enthalpy of outlet gas.
    :param float outlet_enthalpy_ideal: Enthalpy of outlet gas in the
        isentropic case.
    :return: Value of the missing input.
    :rtype: float
    """
    keys = (
        "efficiency",
        "inlet_enthalpy",
        "outlet_enthalpy_real",
        "outlet_enthalpy_ideal")
    kwargs = {**{k: None for k in keys}, **kwargs}
    num_missing = len([v for v in kwargs.values() if v is None])
    efficiency = kwargs["efficiency"]
    inlet_enthalpy = kwargs["inlet_enthalpy"]
    outlet_enthalpy_real = kwargs["outlet_enthalpy_real"]
    outlet_enthalpy_ideal = kwargs["outlet_enthalpy_ideal"]

    assert num_missing <= 1, \
        "All but one of the inputs must be specified."
    if outlet_enthalpy_real is None:
        return \
            ((outlet_enthalpy_ideal - inlet_enthalpy) / efficiency +
             inlet_enthalpy)
    elif efficiency is None:
        return \
            ((outlet_enthalpy_ideal - inlet_enthalpy) /
             (outlet_enthalpy_real - inlet_enthalpy))
    elif outlet_enthalpy_ideal is None:
        return \
            (outlet_enthalpy_real - inlet_enthalpy) * efficiency + \
            inlet_enthalpy
    elif inlet_enthalpy is None:
        return \
            (outlet_enthalpy_ideal - efficiency * outlet_enthalpy_real) /\
            (1 - efficiency)
