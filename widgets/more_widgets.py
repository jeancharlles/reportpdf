from reportlab.graphics.shapes import Drawing
from reportlab.graphics.widgets import signsandsymbols
from reportlab.graphics import renderPDF


d = Drawing(width=230, height=230)

ne = signsandsymbols.NoEntry()
ds = signsandsymbols.DangerSign()
fd = signsandsymbols.FloppyDisk()
ns = signsandsymbols.NoSmoking()

ne.x, ne.y = 10, 10
ds.x, ds.y = 120, 10
fd.x, fd.y = 10, 120
ns.x, ns.y = 120, 120

d.add(node=ne)
d.add(node=ds)
d.add(node=fd)
d.add(node=ns)

renderPDF.drawToFile(d=d, fn="more_widgets.pdf", msg="More Widgets")
