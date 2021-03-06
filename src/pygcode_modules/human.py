def code() -> str:
    """
    Example G-code module, a drawing of a human.

    Please simulate first, before milling.
    """
    return """
        G91
        G17
        G3 X8 Y-8 I8 J0
        G3 X-8 Y8 I0 J8
        G3 X16 Y0 I8 J0
        G0 X12 Y0
        G0 X10 Y10
        G0 X-10 Y-10
        G0 X10 Y-10
        G0 X-10 Y10
        G0 X20 Y0
        G0 X10 Y10
        G0 X-10 Y-10
        G0 X10 Y-10
        G0 X-10 Y10
    """
