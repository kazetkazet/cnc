def code() -> str:
    """
    Example G-code module, a drawing of a house.

    Please simulate first, before milling.
    """
    return """
        G91
        G0 X10 Y15
        G0 X-10 Y-15
        G0 X10 Y-15
        G0 X-10 Y15
        G0 X10 Y-15
        G0 X0 Y30
        G0 X0 Y-5
        G0 X20 Y0
        G0 X0 Y-10
        G0 X0 Y3
        G0 X-10 Y0
        G0 X0 Y-6
        G0 X10 Y0
        G0 X0 Y3
        G0 X0 Y-10
        G0 X-20 Y0
    """
